# Question 01 — Deployment CrashLoopBackOff

## 🎯 Scenario

An EKS production API has just received a new application release through Argo CD. The Deployment has six replicas: three pods are Ready and three are in CrashLoopBackOff. Customers are seeing intermittent HTTP 502 errors, and the error rate is rising. You are the on-call engineer. How would you investigate and handle this incident, from your first actions through recovery and follow-up?

## ✅ Interview-Ready Answer

> I would confirm customer impact and correlate failures with the release, then capture pod events and previous-container logs. If a known-good version is compatible, I would restore it through Git and Argo CD without waiting for complete RCA. I would compare healthy and failing replicas, investigate the crash and 502 request path, and verify recovery using successful requests, error rate, latency and stable pods. Finally, I would test the fix and add prevention based on the actual cause.

## 🔄 Diagram

```text
Confirm impact + capture quick evidence
                  |
       Safe known-good version?
         /                 \
       Yes                  No
        |                    |
 Revert Git + sync    Evidence-based fix
         \                 /
          Verify customer recovery
                     |
          RCA -> test -> prevent
```

📣 Communicate severity and the next update time while mitigating; avoid an unsupported recovery ETA.

## 🔍 Troubleshooting / Reasoning Flow

### ① Find the failing pods and the reason

Diagnostic examples: replace placeholders; add `-c <container>` to logs for a multi-container pod. These commands are study examples, not executed against a cluster.

```sh
kubectl get pods -n <ns> -o wide
kubectl describe pod <pod> -n <ns>
kubectl logs <pod> -n <ns> --previous
```

| Command | Why / what to inspect |
| --- | --- |
| `get pods` | Identify readiness, restarts and node placement. Compare healthy and failing pods. |
| `describe pod` | Inspect Last State, exit reason, image, owning ReplicaSet, resources, probes and events. |
| `logs --previous` | Read the crashed container's output. Omit `--previous` for the current instance. |

**Use evidence to choose the fix:**

| Finding | Next action |
| --- | --- |
| Only the new release fails | Compare image/config changes; prioritize safe rollback. |
| `OOMKilled` | Check historical memory against the container limit and node pressure. Larger nodes do not change that limit. |
| Probe failures | Check startup time, probe settings and application health before relaxing probes. |
| Missing configuration / access denied | Check ConfigMap/Secret references or AWS permissions, depending on the dependency. |

### ② Restore a safe version early

**Preferred:** revert the faulty deployment/Helm change in Git, then sync the application. Confirm compatibility with database migrations and configuration first.

```sh
# Changes the deployed application; use after the reviewed Git revert:
argocd app sync <app>
```

**Why:** apply the corrected desired state through GitOps, so reconciliation will not restore the faulty version.

**Emergency alternative:** Argo CD history rollback requires automated sync disabled. Reconcile Git before restoring automation. Avoid a blind `kubectl rollout undo` while Argo CD can reapply the faulty desired state. If rollback is unsafe, choose a targeted fix based on the evidence above.

### ③ Explain the 502s if they persist

```sh
kubectl describe service <service> -n <ns>
kubectl get endpointslices -n <ns>
```

**Why:** check Service ports/targetPort and backend pod addresses. If needed, inspect the relevant EndpointSlice with `-o yaml` for readiness conditions. Match it to the affected Service.

**Decision:** incorrect backend configuration needs a routing fix; correct backends require checking ingress/load-balancer errors, readiness changes and surviving capacity. For EKS with ALB, use ALB target health and access logs to identify where the 502 originated. Three Ready pods alone do not prove the customer request path works.

### ④ Verify recovery, then prevent recurrence

```sh
kubectl rollout status deployment/<deployment> -n <ns>
```

**Why:** confirm the Deployment rollout completed. Also check stable restart counts, representative successful requests, and 5xx/latency returning to normal over an observation window.

**Prevention:** reproduce and test the cause; improve probes or resource sizing where justified. Review rollout capacity (`maxSurge`/`maxUnavailable`) and use canary error/latency checks to limit future impact.

## 🧠 Key Points

- 🔁 **CrashLoopBackOff:** container restart backoff, not the root cause. Exit 137 alone does not prove a memory-limit violation.
- 🚦 **Probes:** readiness affects traffic eligibility; startup/liveness failures can restart containers.
- 🔐 **Identity:** native ConfigMaps/Secrets do not need IRSA. Broken IAM trust can block the service-account-token → AWS STS credentials exchange, not generally token issuance.
- 🛠️ **Syntax:** `-o wide` belongs with `get pods`, not `describe pod`; use `logs <pod>`, not `logs pod <pod>`.

## 📌 Senior-Level Takeaway

**Mitigate before complete RCA → change only what evidence supports → verify customer recovery, not just pod status.** Keep rollback compatible with GitOps and application dependencies.

## Attempt Record — 2026-10-02

Candidate response summary (paraphrased): Start with dashboards and identify affected workloads; communicate impact and recovery timing, create prioritized incidents, inspect pods/logs/events, explain increasing restart backoff, consider resource constraints and larger nodes, check ConfigMaps/Secrets and OIDC trust, roll back in Argo CD before deep RCA, then fix and redeploy.

Score: 6/10. Interview Acceptance Probability: 55% (subjective answer-specific estimate).

## References

- [Kubernetes logs command](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_logs/)
- [Kubernetes memory resources](https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/)
- [Argo CD automated sync and rollback](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/)
- [EKS IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html)
