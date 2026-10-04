# Question 10 — AKS Pool Replacement Breaks Scheduling

## 🎯 Scenario

After replacing an AKS user pool, payments pods stay Pending despite spare resources. Events report node-affinity mismatch on some nodes and an untolerated dedicated=system:NoSchedule taint on others. Payments must run only on its user pool. A teammate suggests removing affinity and tolerating every taint. Restore scheduling while preserving isolation.

## ✅ Interview-Ready Answer

> I would reject blanket tolerations and removing required placement rules. The events point to labels/affinity and taints, so I would compare the replacement payments pool's actual labels and taints with the pod specification. I would restore intended pool labels or narrowly update stale required affinity, and add only the payments-specific toleration if needed. I would preserve system-node restrictions, apply changes through the pool's infrastructure configuration and workload GitOps, then verify payments runs only on its intended pool and becomes Ready.

## 🔄 Diagram

```text
Pending pod -> read scheduler events
                    |
     Payments pool labels match required affinity?
              No -> restore labels / correct stale rule
                    |
     Payments pool has an intended taint?
              Yes -> matching narrow toleration
                    |
     Verify placement + readiness + isolation
```

## 🔍 Troubleshooting / Reasoning Flow

### ① Compare intended and actual placement

```sh
kubectl describe pod <payments-pod> -n <ns>
kubectl describe node <payments-node>
kubectl get deployment <deployment> -n <ns> -o yaml
```

**Why:** inspect FailedScheduling details, node labels/taints, and the full affinity/nodeSelector/tolerations. Compare old and replacement pool configuration: a changed pool-name label or omitted custom label can invalidate an otherwise correct rule. These are examples only, not executed commands.

### ② Make the smallest persistent correction

| Control | Purpose / safe fix |
| --- | --- |
| Required affinity or nodeSelector | Keeps payments on intended nodes; restore the label or change the stale label value deliberately. Preferred affinity alone does not enforce payments-only placement. |
| Payments taint | Keeps ordinary non-tolerating workloads off payments nodes; retain it if intentional. Remove only a confirmed accidental taint through managed configuration. |
| Payments toleration | Permits access to that tainted pool; does not force placement there. Match key/value/effect rather than tolerate everything. |
| System taint | Leave it intact; the scenario's dedicated=system taint is not permission to move payments onto system nodes. |

For example, if payments nodes intentionally have label `workload=payments` and taint `dedicated=payments:NoSchedule`, use required placement matching that label plus a toleration for that exact taint. Do not assume those labels already exist.

Persist labels/taints in the AKS node-pool/Terraform configuration so replacement nodes inherit them; persist pod constraints in Helm/Git. Ad hoc changes to one node can disappear on replacement. Check allocatable resources afterward if scheduling still reports a resource shortage; the supplied errors do not establish one.

### ③ Validate the result

```sh
kubectl get pods -n <ns> -o wide
```

**Why:** verify payments pods schedule on the intended pool, become Ready and stop generating FailedScheduling events. Confirm system nodes remain excluded, ordinary non-payment workloads cannot enter the dedicated pool without permission, and application requests recover.

## 🧠 Key Points

- Toleration permits; required affinity restricts. Both may be needed for dedicated placement.
- Namespace boundaries and scheduling rules do not themselves block network traffic. Use NetworkPolicy for network isolation, RBAC for API authorization and resource controls for capacity governance.
- Dedicated nodes are a design choice, not mandatory for every workload. Taints alone are not a complete security boundary against users allowed to set broad tolerations.
- VM size/SKU determines CPU and memory; the machine image determines OS/runtime contents. Select compatible images, but do not confuse them with capacity.

## 📌 Senior-Level Takeaway

**Follow the scheduler's explicit rejection reason, restore the intended pool contract, and prove the workload stayed within its placement boundary.**

## Attempt Record — 2026-10-04

Candidate response summary (paraphrased): Favored dedicated payments nodes/namespaces, discussed requests and node capacity first, then proposed correcting affinity/tolerations or removing taints if needed. Rejected blanket rule removal as harmful to network/resource isolation. Described the machine image as determining available resources. Did not explicitly compare replacement labels, distinguish required affinity from toleration, or verify final placement.

Score: 6/10. Interview Acceptance Probability: 55% (subjective answer-specific estimate).

## References

- [Taints, tolerations and dedicated nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)
- [Assign pods to nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
- [AKS node-pool configuration](https://learn.microsoft.com/en-us/azure/aks/create-node-pools)
