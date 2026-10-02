# Question 01 — Deployment CrashLoopBackOff

## 🎯 Scenario

An EKS production API has just received a new application release through Argo CD. The Deployment has six replicas: three pods are Ready and three are in CrashLoopBackOff. Customers are seeing intermittent HTTP 502 errors, and the error rate is rising. You are the on-call engineer. How would you investigate and handle this incident, from your first actions through recovery and follow-up?

## ✅ Interview-Ready Answer

- Confirm customer impact, error rate and rollout timing; declare severity and communicate an update cadence without promising an unverified recovery time.
- Compare healthy and failing pods: ReplicaSet, image, configuration and node placement. Capture termination reasons, events and previous-container logs quickly.
- Because errors followed a release, restore a known-good, compatible revision early while investigation continues. Prefer reverting the desired version in Git and syncing Argo CD. Check database/config compatibility first. Argo CD application rollback requires automated sync to be disabled; reconcile Git before restoring automation.
- Diagnose from evidence: application exceptions, OOM kills, probe failures, configuration errors or failed dependencies. Do not assume a node upgrade fixes the crash.
- Trace 502s through the ingress/load balancer, Service and EndpointSlices. Check readiness and surviving capacity; three Ready pods do not prove the user request path works.
- Validate rollout health, restart counts, successful requests, error rate and latency over an observation window. Test the fix before controlled redeployment; add regression tests, meaningful probes, alerts and a rollback runbook.

## 🔍 Troubleshooting / Reasoning Flow

Replace placeholders with actual names; these are diagnostic examples, not commands executed against a cluster.

```sh
kubectl get pods -n <namespace> -o wide
kubectl get deploy,rs -n <namespace>
kubectl describe pod <pod-name> -n <namespace>
kubectl logs <pod-name> -n <namespace> -c <container-name> --previous
kubectl logs <pod-name> -n <namespace> -c <container-name>
kubectl get events -n <namespace> --sort-by=.metadata.creationTimestamp
kubectl get deployment <deployment> -n <namespace> -o yaml
kubectl get svc,ingress -n <namespace>
kubectl get endpointslices -n <namespace> -l kubernetes.io/service-name=<service>
kubectl rollout status deployment/<deployment> -n <namespace>
```

1. Confirm impact and the recent change; communicate and mitigate in parallel.
2. Compare old/new ReplicaSets rather than assuming all six pods run identical revisions.
3. Inspect container Last State, reason, exit code, restart count and probes. Exit 137 alone does not prove a memory-limit violation.
4. Use previous logs and historical metrics; current usage may miss a pre-crash spike. Check centralized logs if the old pod is gone.
5. Separate container limits from node pressure. A larger node does not change a container's memory limit.
6. Inspect configuration references without exposing secrets. Native ConfigMaps/Secrets do not require IRSA; AWS-backed secret retrieval may require IAM permissions.
7. Investigate routing, readiness transitions, upstream resets and remaining capacity to explain the 502s.
8. Restore service, verify with real requests and metrics, then complete RCA and prevention.

## 🧠 Key Points

- CrashLoopBackOff describes restart backoff for a repeatedly failing container, not a root cause or necessarily repeated creation of pods.
- Use `kubectl logs <pod-name>` or `kubectl logs pod/<pod-name>`; `kubectl logs pod <pod-name>` is not the intended syntax.
- `-o wide` belongs with `kubectl get pods`, not `kubectl describe pod`.
- IRSA exchanges a projected service-account token for AWS STS credentials. A bad IAM trust policy can block that exchange; it does not generally stop Kubernetes from issuing the service-account token.
- Readiness controls normal endpoint eligibility; startup/liveness failures can cause restarts. Inspect the actual routing implementation and health checks.

## 🔄 Diagram

```text
Impact + release correlation
            |
Quick evidence + safe mitigation
            |
Compare healthy/failing pods
            |
Logs / termination / probes / config / metrics
            |
Explain 502 request path -> verify recovery -> prevent recurrence
```

## 📌 Senior-Level Takeaway

- Restore service without waiting for complete RCA; keep incident coordination parallel to mitigation.
- Test hypotheses before changing infrastructure, and keep emergency recovery consistent with GitOps.
- Recovery means successful customer requests and stable metrics, not simply Running pods.

## Attempt Record — 2026-10-02

Candidate response summary (paraphrased): Start with dashboards and identify affected workloads; communicate impact and recovery timing, create prioritized incidents, inspect pods/logs/events, explain increasing restart backoff, consider resource constraints and larger nodes, check ConfigMaps/Secrets and OIDC trust, roll back in Argo CD before deep RCA, then fix and redeploy.

Score: 6/10. Interview Acceptance Probability: 55% (subjective answer-specific estimate).

## References

- [Kubernetes logs command](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/)
- [Kubernetes memory resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/)
- [Argo CD automated sync and rollback](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/)
- [EKS IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html)
