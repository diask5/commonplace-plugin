"""Deterministic self-test for grade.py.

Builds Claude-format transcripts from the REAL tool payloads captured by
protocol-check.mjs and checks that the grader accepts a clean read-backed
answer and rejects snippet-only, changed/restart and error-backed answers.

This exercises the grader. It is NOT a model case and produces no model result.
"""
import json, os, pathlib, subprocess, sys, tempfile, uuid

root = pathlib.Path(os.environ.get('BENCH_ROOT') or pathlib.Path(__file__).resolve().parent.parent).resolve()
plan = json.loads((root / 'harness/plan.json').read_text())
steps = json.loads((root / 'evidence/protocol-steps.private.json').read_text())
case = next(c for c in plan['cases'] if c['id'] == 'claude-correction')
PREFIX = 'mcp__meet-proxy__'


def payload(step):
    text = (((step.get('value') or {}).get('result') or {}).get('content') or [{}])[0].get('text')
    if not isinstance(text, str):
        return None
    try:
        return json.loads(text)
    except ValueError:
        return None


def find(tool, predicate=lambda value: True):
    for step in steps:
        params = step.get('params') or {}
        if params.get('name') == tool:
            value = payload(step)
            if value is not None and predicate(value):
                return value
    raise SystemExit('No captured ' + tool + ' payload matched')


search = find('archive_search', lambda v: any(case['project'] in (r.get('title', '') + r.get('text', '')) for r in v.get('results', [])))
reads = [find('archive_read', lambda v, d=d: v.get('documentId') == d and v.get('text'))
         for d in [r['documentId'] for r in search['results']][:2]]
changed = find('archive_read', lambda v: v.get('restart'))


def block(name, payload_value, is_error=False):
    identifier = 'toolu_' + uuid.uuid4().hex[:16]
    return (
        {'type': 'assistant', 'message': {'role': 'assistant', 'content': [
            {'type': 'tool_use', 'id': identifier, 'name': PREFIX + name, 'input': {}}]}},
        {'type': 'user', 'message': {'role': 'user', 'content': [
            {'type': 'tool_result', 'tool_use_id': identifier, 'is_error': is_error,
             'content': [{'type': 'text', 'text': json.dumps(payload_value)}]}]}},
    )


def transcript(calls, final):
    events = []
    for name, value, is_error in calls:
        events.extend(block(name, value, is_error))
    events.append({'type': 'result', 'session_id': 'selftest-' + uuid.uuid4().hex[:8],
                   'result': final, 'permission_denials': []})
    return '\n'.join(json.dumps(e) for e in events) + '\n'


good_answer = (
    f"The {case['project']} pilot now launches {case['date']}, 2026, and {case['owner']} still owns it. "
    f"The 2026-10-25 decision update moved it because {case['reason']}. "
    f"Sources: {reads[0]['citations'][0]}, {reads[1]['citations'][0]}. "
    "Neither note sets a start time or timezone."
)
snippet_answer = (
    f"The {case['project']} pilot now launches {case['date']}, 2026, and {case['owner']} owns it. "
    f"Source: {search['results'][1]['citation']}."
)
changed_answer = (
    f"The {case['project']} pilot now launches {case['date']}, 2026, and {case['owner']} owns it. "
    f"Source: {reads[1]['citations'][0]}."
)

scenarios = {
    'accepts-read-backed-answer': (
        [('archive_search', search, False), ('archive_read', reads[0], False), ('archive_read', reads[1], False)],
        good_answer,
        {'state': 'passed'},
    ),
    'rejects-snippet-only-answer': (
        [('archive_search', search, False)],
        snippet_answer,
        {'state': 'failed', 'mustFail': ['readSupportingContext', 'citationsMatchSuccessfulReads']},
    ),
    'rejects-changed-read-answer': (
        [('archive_search', search, False), ('archive_read', changed, False)],
        changed_answer,
        {'state': 'failed', 'mustFail': ['readSupportingContext', 'citationsMatchSuccessfulReads']},
    ),
    'rejects-error-read-answer': (
        [('archive_search', search, False), ('archive_read', {'error': 'Conversation is not in this account archive.'}, True)],
        changed_answer,
        {'state': 'failed', 'mustFail': ['readSupportingContext', 'citationsMatchSuccessfulReads']},
    ),
}

results, ok = {}, True
with tempfile.TemporaryDirectory() as workdir:
    for name, (calls, final, expectation) in scenarios.items():
        stream = pathlib.Path(workdir) / (name + '.jsonl')
        stream.write_text(transcript(calls, final))
        completed = subprocess.run(
            [sys.executable, str(root / 'harness/grade.py'), '--plan', str(root / 'harness/plan.json'),
             '--case', case['id'], '--host', 'claude', '--stream', str(stream)],
            capture_output=True, text=True, check=True)
        graded = json.loads(completed.stdout)
        passed = graded['state'] == expectation['state'] and all(
            check in graded['failedChecks'] for check in expectation.get('mustFail', []))
        ok = ok and passed
        results[name] = {'expected': expectation, 'state': graded['state'],
                         'failedChecks': graded['failedChecks'],
                         'successfulReads': len(graded['successfulReads']),
                         'rejectedReads': graded['rejectedReads'],
                         'unsupportedCitations': graded['unsupportedCitations'],
                         'selfTestPassed': passed}

out = {'kind': 'grader self-test on real captured tool payloads; not a model case',
       'allScenariosPassed': ok, 'scenarios': results}
(root / 'evidence/grader-selftest.json').write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
sys.exit(0 if ok else 1)
