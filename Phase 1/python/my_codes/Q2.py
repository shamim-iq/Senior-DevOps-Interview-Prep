# Q02 — Count server errors from a log file
#
# Write count_server_errors(path). Read a UTF-8 text file whose nonblank lines
# contain two whitespace-separated fields: SERVICE STATUS_CODE.
# Return a dictionary counting 500–599 responses per service. Include only
# services with at least one such response. Ignore blank lines, malformed lines
# (wrong field count, non-integer code or code outside 100–599), and non-5xx codes.
# An empty file returns {}. A missing file must raise FileNotFoundError rather
# than returning an empty result. Use standard library only and process the file
# line by line without loading the entire file at once.
#
# Example contents:
# api 200
# api 500
# worker 503
# api 502
# bad-line
# worker unknown
#
# Expected: {"api": 2, "worker": 1}
# Share or save your code here, plus any test output. No solution supplied.

from pathlib import Path

def count_server_errors(path):
    file_path = Path(path)

    services = {}

    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip().split()
                if len(line) == 2:
                    service, status_code = line
                    try:
                        status_code = int(status_code)
                        if 500 <= status_code < 600:
                            if service not in services:
                                services[service] = 0
                            services[service] += 1
                    except ValueError:
                        continue
    else:
        raise FileNotFoundError(f"The file {file_path} does not exist.")


    return services

if __name__ == "__main__":
    # Example usage
    log_file_path = "log.txt"  # Replace with your log file path
    try:
        result = count_server_errors(log_file_path)
        print(result)
    except FileNotFoundError as e:
        print(e)