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

import subprocess

def run_check(command, timeout_seconds=5):
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout_seconds
        )
        # Nonzero exit codes (e.g. invalid arguments) are results, not exceptions.
        return {
            "success": result.returncode == 0,
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }
    # The command did not finish within timeout_seconds.
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "returncode": None,
            "stdout": "",
            "stderr": "timeout"
        }
    # The executable could not be found (e.g. a misspelled command name/path).
    # Invalid arguments to an existing executable do not trigger this handler.
    except FileNotFoundError:
        return {
            "success": False,
            "returncode": None,
            "stdout": "",
            "stderr": "command not found"
        }

# Other exceptions, such as PermissionError, propagate to the caller.

if __name__ == "__main__":
    import sys

    run_check([sys.executable, "-c", "print('healthy')"], 5)