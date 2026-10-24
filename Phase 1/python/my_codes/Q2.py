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
