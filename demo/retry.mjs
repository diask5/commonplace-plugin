// Standalone Commonplace review fixture; not imported by the plugin.
// attempts is the maximum total number of calls, including the first call.
export async function retry(operation, attempts = 3) {
  for (let attempt = 0; attempt <= attempts; attempt++) {
    try {
      return await operation();
    } catch (error) {
      if (attempt === attempts) throw error;
    }
  }
}
