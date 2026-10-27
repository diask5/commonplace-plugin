"""Read only the release/account metadata needed to resume owner-approved diagnostics."""
import json
import pathlib
import shutil
import subprocess

home = pathlib.Path.home()

def read_json(relative):
    try:
        return json.loads((home / relative).read_text())
    except (OSError, ValueError):
        return {}

runtime = read_json('.commonplace/runtime.json')
account = read_json('.commonplace/account-client.json').get('session', {})
human = account.get('humanAccount') or account.get('account') or {}
registry = read_json('.claude/plugins/installed_plugins.json').get('plugins', {})
installed = {}
for alias in ('meet-proxy', 'commonplace'):
    rows = registry.get(alias + '@commonplace', [])
    installed[alias] = [row.get('version') for row in rows if isinstance(row, dict)] if isinstance(rows, list) else []
gcloud = shutil.which('gcloud')
if not gcloud:
    gcloud = next((str(p) for p in [home / 'google-cloud-sdk/bin/gcloud', pathlib.Path('/opt/homebrew/share/google-cloud-sdk/bin/gcloud')] if p.is_file()), None)
active_accounts = []
gcloud_status = 'not_found'
if gcloud:
    try:
        result = subprocess.run([gcloud, 'auth', 'list', '--filter=status:ACTIVE', '--format=value(account)'], capture_output=True, text=True, timeout=15)
        gcloud_status = 'cached_account_list_only' if result.returncode == 0 else 'account_list_failed'
        if result.returncode == 0:
            active_accounts = [line for line in result.stdout.splitlines() if '@' in line]
    except subprocess.TimeoutExpired:
        gcloud_status = 'account_list_timeout'
processes = subprocess.run(['ps', '-axo', 'command='], capture_output=True, text=True, timeout=5).stdout
login_present = any('gcloud' in line and 'auth login' in line for line in processes.splitlines())
print(json.dumps({
    'runtimeRevision': runtime.get('revision'),
    'installedAliases': installed,
    'cachedMeetProxyEmail': human.get('email'),
    'expectedMeetProxyAccountMatches': human.get('email') == 'diaskyle10@gmail.com',
    'gcloudStatus': gcloud_status,
    'cachedGcloudActiveAccounts': active_accounts,
    'existingGcloudLoginProcess': login_present,
    'liveAuthenticationVerified': False,
    'mutations': False,
}))
