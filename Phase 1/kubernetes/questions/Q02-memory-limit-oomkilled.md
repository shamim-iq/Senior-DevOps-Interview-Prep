# Question 02 — OOMKilled Despite Free Node Memory

## 🎯 Scenario

An EKS API container repeatedly restarts during peak traffic. Its last termination reason is OOMKilled, its memory request is 256Mi, and its memory limit is 512Mi. Historical metrics show memory rising toward 512Mi before each restart, while the node has several GiB of available memory and no MemoryPressure condition. A teammate proposes moving the workload to a larger node. How would you assess that proposal and choose, validate, and follow up on a safe production fix?

## ✅ Interview-Ready Answer

> Moving to a larger node leaves the container's 512Mi limit unchanged. I would confirm the termination reason and memory trend, then distinguish legitimate peak demand from a leak or regression. For immediate recovery, I would make a controlled, evidence-based limit increase only after checking capacity, or roll back a faulty release. I would review the request separately, apply the change through GitOps, and validate stable memory, no new OOM kills and restored customer performance under representative peak load.

## 🔄 Diagram

```text
OOMKilled + usage near 512Mi + node has headroom
                         |
             Container limit is the constraint
                         |
          Legitimate demand or application growth?
              /                        \
     Demand tracks load          Leak / regression suspected
             |                           |
  Bounded limit increase;       Roll back if safe; investigate
  check capacity first          allocation / cache / concurrency
              \                        /
           Controlled rollout -> peak-load validation
```

## 🔍 Troubleshooting / Reasoning Flow

### ① Confirm with the essential commands

Replace placeholders; add `-c <container>` to logs if needed. Examples only; no cluster commands were executed.

```sh
kubectl describe pod <pod> -n <ns>
kubectl logs <pod> -n <ns> --previous
kubectl top pod <pod> -n <ns> --containers
```

| Command | Why / evidence |
| --- | --- |
| `describe pod` | Check the failing container's Last State, OOMKilled reason, restarts, request and limit. Do not inspect only Events. |
| `logs --previous` | Look for application errors or workload changes before the kill. An abrupt OOM kill may leave no useful final log. |
| `top pod --containers` | Check current per-container usage. Requires a working resource Metrics API, usually Metrics Server; it can miss the pre-crash peak. |

Use historical monitoring to compare memory with traffic, concurrency and release timing. Increasing memory even at steady load suggests investigating a leak, growing cache or backlog; the pattern alone is not proof.

### ② Mitigate without moving the problem to the node

- **Limit increase:** select a bounded value from representative measurements plus headroom, not an arbitrary doubling. A history capped by repeated OOM kills does not reveal the true peak requirement.
- **Capacity check:** account for other workloads, all replicas and temporary rollout replicas. If needed, `kubectl describe node <node>` shows allocatable resources and allocated requests; combine this with usage monitoring.
- **Request review:** 256Mi is used for scheduling; it is not the kill threshold. Set a realistic request separately so the scheduler does not overpack nodes. Larger requests may leave replacements Pending.
- **Alternative:** safely roll back a recent regression, or reduce concurrency / add replicas if the workload can distribute load. These are conditional mitigations, not cures for every leak.
- Apply the reviewed Deployment/Helm change through GitOps. Keep a finite limit and a rollback plan; avoid masking unbounded growth with repeated increases.

### ③ Validate and follow up

```sh
kubectl rollout status deployment/<deployment> -n <ns>
```

**Why:** confirm the updated Deployment completes its rollout. Then verify no new OOM kills/restarts, stable memory with headroom, healthy nodes, and recovered error rate and latency through representative peak traffic and a sufficient observation window.

Follow up with a load/soak test, application memory investigation if growth continues, and alerts for OOM kills and memory approaching limits. Communicate the next update time rather than inventing a recovery ETA.

## 🧠 Key Points

| Concept | Remember |
| --- | --- |
| Request: 256Mi | Scheduling input; exceeding it does not itself trigger a kill. |
| Limit: 512Mi | Container memory boundary; free node RAM does not remove it. |
| OOMKilled | Termination reason; repeated restarts can lead to CrashLoopBackOff. It does not prove the YAML is wrong. |
| `exec ... top` | Optional and often unavailable in minimal images; a restarting container may not stay up long enough. Historical metrics are more useful here. |

## 📌 Senior-Level Takeaway

**Fix the immediate constraint, prove the workload is stable, and investigate why memory demand grew.** Raising a limit is a mitigation until the cause and capacity impact are understood.

## Attempt Record — 2026-10-03

Candidate response summary (paraphrased): Start with observability, incidents and stakeholder communication including a mitigation ETA; suspect incorrectly configured requests/limits, explain peak usage and repeated OOM/restarts, reject moving to larger nodes, measure peak usage and raise the limit. Proposed node/pod inspection, previous/current logs, kubectl top with Metrics Server, and exec into the container to run top.

Score: 6.5/10. Interview Acceptance Probability: 62% (subjective answer-specific estimate).

## References

- [Kubernetes resource requests and limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [Resource metrics pipeline](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/)
