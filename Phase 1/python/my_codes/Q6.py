# Q06: Failed deployment summary
# Implement failed_deployments(records). Return a dictionary mapping each service
# to its number of failed deployment records. Only status == "failed" counts.
# Ignore other statuses. Return {} for an empty list. Input is a list of
# dictionaries with valid string service and status fields; do not mutate it.
# Add your own checks: mixed statuses, repeated failures, and empty input.

import json

def failed_deployments(records):
	try:
		res = json.loads(records)
	except json.JSONDecodeError:
		return {}
	
	result = {}
	for record in res:
		if record.get("status") == "failed":
			service = record.get("service")
			if service:
				result[service] = result.get(service, 0) + 1
	return result