# Question 07 — Node Drain Blocked by PDB

## 🎯 Scenario

During an EKS node-group upgrade, drain fails with: Cannot evict pod as it would violate the pod's disruption budget. The API Deployment desires three replicas; only two are Ready. Its PDB has minAvailable: 2. A teammate suggests deleting the PDB. Investigate and finish maintenance while protecting availability.

## ✅ Interview-Ready Answer

> With two healthy replicas and minAvailable 2, there is no budget to evict a healthy replica. I would inspect the PDB and identify why the third replica is unready, then restore it or safely add another Ready replica on eligible capacity. Once the budget permits an eviction, I would drain incrementally, waiting for replacement readiness and checking customer metrics. I would not weaken the PDB just because a maintenance window exists.

## 🔄 Diagram

```text
2 Ready - minimum 2 = 0 healthy-pod evictions allowed
                         |
          Investigate third replica + blocked pod
                         |
       Restore health / add capacity and Ready replica
                         |
             PDB reports disruptionsAllowed > 0
                         |
            Drain incrementally -> verify recovery
```

## 🔍 Troubleshooting / Reasoning Flow

### ① Check the actual budget and unhealthy replica

```sh
kubectl describe pdb <pdb> -n <ns>
kubectl get pods -n <ns> -o wide
kubectl describe pod <unready-pod> -n <ns>
```

| Command | Why / key evidence |
| --- | --- |
| `describe pdb` | Verify selector, Current Healthy, Desired Healthy and Allowed Disruptions; check that it covers the intended workload. |
| `get pods` | Identify the unready replica, its status and node; identify which pod drain is attempting to evict. |
| `describe pod` | Find readiness failures, Pending scheduling reasons, image errors or other startup problems; inspect logs if the events point to an application failure. |

Examples only; replace placeholders. No cluster commands were executed.

### ② Restore availability before continuing

- Fix the third replica's actual problem. If it is Pending, check suitable spare capacity and scheduling constraints; if Running but unready, investigate probes/application health.
- If more replicas can help, scale through the normal deployment/GitOps path with sufficient capacity. A higher desired count alone is not enough: wait for new replicas to become Ready, preferably away from the node being drained.
- New worker capacity is useful but does not create PDB headroom until workload replicas are healthy. Use a tested version compatible with the control plane and add-ons, not simply the latest release.

### ③ Drain with a recovery gate

```sh
# State-changing: only after workload health and budget checks
kubectl drain <node> --ignore-daemonsets
```

**Why:** cordon the node and request pod evictions through the Eviction API, respecting PDBs. A separate cordon can be an earlier preparation step. Other blockers must be inspected; do not add force/data-deletion flags blindly. For an EKS-managed update, resume/retry its managed process rather than concurrently running an independent drain.

Drain incrementally. Wait for replacement readiness and restored budget before another disruption; watch latency, errors and serving capacity. Pause maintenance if health deteriorates.

## 🧠 Key Points

| Point | Practical meaning |
| --- | --- |
| PDB scope | Limits voluntary eviction; it does not guarantee zero latency or prevent every failure/direct deletion. |
| Maintenance window | Coordinates risk and communication; it does not make reduced capacity harmless. |
| Temporary relaxation | An explicit, time-bounded availability trade-off after validating lower replica capacity, with monitoring and a restoration plan—not a default prerequisite. |
| Upgrade order | Check release-specific prerequisites and add-on compatibility; there is no universal reason to loosen PDBs for upgrades. |

**Unhealthy-pod nuance:** identify whether the blocked pod is healthy. `unhealthyPodEvictionPolicy` affects Running-but-unready pod eviction. `AlwaysAllow` can help drain such pods but does not permit evicting healthy pods below the budget. With default `IfHealthyBudget`, an unhealthy Running pod can be evicted when currentHealthy is at least desiredHealthy; inspect actual status before assuming every pod is blocked.

## 📌 Senior-Level Takeaway

**Treat the blocked eviction as evidence of insufficient healthy capacity. Restore that capacity first; any reduction in protection is an explicit risk decision.**

## Attempt Record — 2026-10-04

Candidate response summary (paraphrased): Explained PDBs for voluntary disruption, control-plane/add-on/worker upgrade sequencing, cordon/drain and preparing new worker nodes. Rejected deleting the PDB but proposed loosening it before maintenance, stating a communicated maintenance window and new workers would avoid impact/latency. Did not diagnose the unready third replica or calculate the zero eviction budget.

Score: 5.5/10. Interview Acceptance Probability: 45% (subjective answer-specific estimate).

## References

- [Configure a PDB](https://kubernetes.io/docs/tasks/run-application/configure-pdb/)
- [Kubernetes disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)
- [EKS upgrade guidance](https://docs.aws.amazon.com/eks/latest/best-practices/cluster-upgrades.html)
