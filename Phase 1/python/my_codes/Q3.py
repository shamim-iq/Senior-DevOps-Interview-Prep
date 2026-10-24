# Q03 — Find unhealthy services in JSON
#
# Write find_unhealthy_services(json_text). The input is a JSON string containing
# an object with a services list. Each entry is an object with a string name
# and a string status. Assume this structure is valid when the JSON parses.
# Return names whose status is not exactly "healthy", in input order.
# An empty services list returns []. Invalid JSON must raise ValueError
# (or a subclass), not silently return []. Use only the standard library.
# Do not read files, make network calls, or change the input.
#
# Example input:
# {"services": [{"name": "api", "status": "healthy"}, {"name": "worker", "status": "degraded"}, {"name": "scheduler", "status": "down"}]}
# Expected result: ["worker", "scheduler"]
#
# Write your function here. Add checks for the example, all-healthy services,
# an empty services list, and invalid JSON. Keep any demonstration under the
# main guard so importing the module does not run it. No solution supplied.

import json
def find_unhealthy_services(json_text):
    try:
        services = json.loads(json_text) #loads() is for json strings whereas load() is for json files/objects
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON input")

    unhealthy_services = [service["name"] for service in services["services"] if service["status"] != "healthy"]
    return unhealthy_services

if __name__ == "__main__":
    # Example usage
    json_input = '{"services": [{"name": "api", "status": "healthy"}, {"name": "worker", "status": "degraded"}, {"name": "scheduler", "status": "down"}]'
    print(find_unhealthy_services(json_input))