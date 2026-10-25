# Q05 — Decide whether a CI/CD pipeline can deploy
#
# Write can_deploy(report_json). Input is a JSON string containing a jobs list.
# Each job has string fields name and status. Required jobs: build, test, scan.
# Return True only when each required job appears exactly once and its status
# is exactly "success". Return False if a required job is missing, duplicated,
# or has any other status. Ignore jobs with other names.
# An empty jobs list returns False. Invalid JSON must raise ValueError or a
# subclass. Assume the structure/field types are valid when JSON parses.
# Use only the standard library; do not modify files or trigger deployments.
#
# Example:
# {"jobs": [{"name": "build", "status": "success"}, {"name": "test", "status": "success"}, {"name": "scan", "status": "success"}]}
# Expected: True
#
# Add checks under the main guard for all-success, failed job, missing job,
# duplicate required job and invalid JSON. Include an extra unrelated job to
# verify it does not affect the decision. No solution supplied.

import json

def can_deploy(report_json):
    valid_jobs = []
    try:
        report = json.loads(report_json)
        if len(report["jobs"]) == 0:
            return False
        for job in report["jobs"]:
            if job["name"] not in ["build", "test", "scan"]:
                continue
            else:
                if job["status"] == "success":
                    if job in valid_jobs:
                        return False
                    valid_jobs.append(job)
                else:
                    return False

    except json.JSONDecodeError:
        raise ValueError

if __name__ == "__main__":
    # Example usage
    report_json = '{"jobs": [{"name": "build", "status": "success"}, {"name": "test", "status": "success"}, {"name": "scan", "status": "success"}]}'
    print(can_deploy(report_json))  # Expected: True