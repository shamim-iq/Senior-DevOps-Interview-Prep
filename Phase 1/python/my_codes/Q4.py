# Q04 — Run a diagnostic command safely
#
# Write run_check(command, timeout_seconds=5). command is a nonempty list of
# strings, for example [sys.executable, "-c", "print('healthy')"].
# Use the standard library to run it without shell=True, capturing text output.
# Return a dictionary with exactly these keys: success, returncode, stdout,
# stderr. Strip leading/trailing whitespace from output strings.
# A zero exit code means success=True; a nonzero code means success=False
# and must still return the captured output and actual returncode.
# On timeout, return success=False, returncode=None, stdout="", stderr="timeout".
# If the executable does not exist, return success=False, returncode=None,
# stdout="", stderr="command not found".
# Assume valid argument types and a positive timeout. Do not swallow unrelated errors.
#
# Add checks under the main guard for success, nonzero exit, timeout and missing
# executable. Use harmless local Python commands (sys.executable) for testing;
# no production commands or network access. Share/save your code and any output.
# No implementation supplied.
