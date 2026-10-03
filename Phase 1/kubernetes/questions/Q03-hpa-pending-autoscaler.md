# Question 03 — HPA Scales, but Pods Stay Pending

## 🎯 Scenario

During peak traffic, an EKS API's CPU-based HPA raises desired replicas from 4 to 10. Four pods remain Running and six stay Pending. Pending-pod events report Insufficient cpu, although node dashboards show only about 35% CPU usage. Cluster Autoscaler is installed, but no new nodes appear and latency is rising. Explain the discrepancy, investigate the missing capacity and restore service safely.

## ✅ Interview-Ready Answer

> The scheduler fits CPU requests into each node's allocatable capacity after existing requests, not its current CPU usage. So 35% usage does not prove another pod fits. I would confirm the Pending reason, then inspect Cluster Autoscaler logs and the node group's limits and launch activity. Depending on the evidence, I would fix discovery/permissions, increase suitable capacity, or correct genuinely oversized requests. I would verify nodes become Ready, pods schedule and customer latency recovers.

## 🔄 Diagram

```text
HPA increases replicas -> Scheduler cannot fit requests
                                      |
                     Can a suitable node group grow?
                       /                       \
                     No                        Yes
                      |                         |
           Check max size / pod fit     Was a launch requested?
           / discovery / permissions      /              \
                                        No               Yes
                                         |                |
                                    CA logs         AWS activity,
                                    and health      launch / node join
```

## 🔍 Troubleshooting / Reasoning Flow

### ① Explain the apparent contradiction

**Example:** node allocatable CPU = 4 cores; existing requests = 3.5 cores; new pod requests 1 core. Only 0.5 cores remain available for scheduling, even if actual usage is 1.4 cores (35%).

The request need not be wrong. It must fit on an eligible individual node; spare fractions across multiple nodes cannot be combined. For CPU-utilization targets, HPA compares pod CPU usage with requests, so node-average usage is a different measurement.

### ② Use the key checks

Examples only; replace names/namespaces with actual values. No cluster commands were executed.

```sh
kubectl describe pod <pending-pod> -n <ns>
kubectl describe node <node>
kubectl logs -n kube-system deployment/cluster-autoscaler --since=15m
```

| Check | Why / what matters |
| --- | --- |
| Pending pod | Confirm CPU request, FailedScheduling events and any other constraints. |
| Node | Compare Allocatable with Allocated resources **requests**, not only Capacity or live usage. |
| Autoscaler logs | Find scale-up decisions, max-size/no-fit messages, permission errors or launch backoff. Deployment name/namespace may differ; if logs cannot be read, check the autoscaler workload's health. |

**No new nodes does not prove Autoscaler is broken.** Identify the blocked step:

| Evidence | Likely blocker → action |
| --- | --- |
| Node group at maximum | Raise its maximum within approved capacity/cost constraints. |
| No suitable expansion option | Pod cannot fit a fresh node, or taints/affinity exclude it → provide a suitable group or fix unintended constraints. |
| Group not discovered / access denied | Check configured ASG discovery tags and the autoscaler's AWS identity/permissions. |
| Desired capacity rose, instances did not launch | Check ASG Activity history for EC2 capacity, quotas or launch-template errors; resolve the reported failure. |
| Instances launched but no Ready nodes | Investigate node bootstrap/join and networking instead of repeatedly scaling. |

Use the EKS/EC2 Auto Scaling console to inspect group maximum, desired/current capacity and Activity history. Cluster Autoscaler scales for unschedulable pods when adding an eligible node would help; it does not simply react to node CPU percentage.

### ③ Restore and verify

- Add suitable capacity or fix the identified scaling blocker. Manual capacity changes are an incident fallback; reconcile them with Terraform/Autoscaler afterward.
- Lower requests only if measurements justify it. Blind reductions risk CPU contention and change the denominator of CPU-utilization-based HPA calculations.
- If capacity takes time, use existing load-shedding/rate-limiting mechanisms where appropriate to protect the running replicas.

```sh
kubectl get nodes
kubectl get pods -n <ns>
```

**Why:** verify new nodes are Ready and Pending pods become Running/Ready. Then confirm stable application latency/errors, enough capacity, and no repeated scaling failures. Follow up with realistic requests, capacity limits and unschedulable-pod/scaling-failure alerts.

## 🧠 Key Points

- **HPA:** changes replica count. **Scheduler:** finds a node that fits requests and constraints. **Cluster Autoscaler:** grows eligible node groups when that would help pending pods.
- “Request above average usage” does not mean “never schedulable.” The comparison is with remaining allocatable capacity based on requests.
- Limits are not the normal CPU scheduling fit criterion; an omitted request can be defaulted from a limit, so inspect the effective pod specification.

## 📌 Senior-Level Takeaway

**Find whether the failure is scheduling, scale-up selection, cloud provisioning or node readiness; fix that stage and verify customer recovery.**

## Attempt Record — 2026-10-03

Candidate response summary (paraphrased): HPA created six additional replicas, but requests prevented scheduling despite low usage; the scheduler considers requests rather than limits. Stated that requests above average would never schedule. Asked for an explanation of Autoscaler failure and referred generally to previous commands without identifying scaling checks or a concrete recovery plan.

Score: 5/10. Interview Acceptance Probability: 40% (subjective answer-specific estimate). Credit reflects the scheduling explanation; the requested teaching on Autoscaler is not counted as demonstrated knowledge.

## References

- [Cluster Autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)
- [EKS Cluster Autoscaler guidance](https://docs.aws.amazon.com/eks/latest/best-practices/cas.html)
