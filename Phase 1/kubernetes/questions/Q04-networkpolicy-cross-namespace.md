# Question 04 — Cross-Namespace NetworkPolicy Failure

## 🎯 Scenario

In AKS, frontend pods in `web` cannot call the `orders` API in `backend` after a NetworkPolicy change. Orders pods and Service endpoints are Ready. Requests time out using both the Service DNS name and ClusterIP; other callers still succeed. Isolate the cause and restore intended access without removing isolation.

## ✅ Interview-Ready Answer

> I would compare the policy change and inspect both frontend egress and orders ingress. Ready endpoints do not prove traffic is allowed; ClusterIP failure also means DNS alone cannot explain the incident. I would reproduce from the affected frontend, verify policy selectors and ports, and apply a narrow allow rule through GitOps. Then I would confirm frontend access succeeds while unauthorized callers remain blocked.

## 🔄 Diagram

```text
Frontend pod (web)
       |
       +-- Egress allows destination + port?
                         |
       +-- Orders ingress allows source + port?
                         |
                  Orders pod (backend)

Both directions must allow the connection when isolated.
```

## 🔍 Troubleshooting / Reasoning Flow

### ① Inspect both ends

```sh
kubectl get networkpolicy -n web -o yaml
kubectl get networkpolicy -n backend -o yaml
```

**Why:** inspect policies selecting the frontend and orders pods, including default-deny rules, peer selectors, ports and `policyTypes`. A plain `get networkpolicy` lists policies but does not show their full rules. Compare selectors against actual pod/namespace labels and review the recent Git diff.

### ② Reproduce from the affected source

```sh
kubectl exec -n web <frontend-pod> -- curl -v --connect-timeout 3 --max-time 5 http://<orders-cluster-ip>:<service-port>/<safe-path>
```

**Why:** test the same source identity and destination as the application. Use the real protocol/port and a harmless endpoint; repeat with the Service DNS name after fixing access. If curl is absent, use an approved debug container in the affected pod rather than assuming a separate debug pod receives identical policy treatment. These are study examples, not executed commands.

### ③ Apply a narrow fix

| Check | Intended configuration |
| --- | --- |
| Orders ingress | Select orders pods in `backend`; allow frontend pods from `web` on the actual application TCP port. |
| Frontend egress | If egress-isolated, allow orders pods in `backend` on that port too. |
| Selector logic | Put namespaceSelector and podSelector in the same peer entry to require both; separate entries mean alternatives. |
| DNS | ClusterIP failure rules out a DNS-only cause. Preserve necessary DNS egress if frontend egress is restricted. |

Use namespace labels such as `kubernetes.io/metadata.name: web` with the intended frontend pod labels. Native NetworkPolicy allows are additive: another applicable policy can allow traffic; a missing rule in one policy does not alone prove denial. Namespace separation by itself does not block traffic.

Update only the affected policy through the normal GitOps path, or revert the specific bad change if the previous policy preserves required isolation. Avoid deleting all policies or adding allow-all rules. If rules appear correct, check the configured AKS policy enforcement engine and its drop evidence rather than assuming all AKS clusters have identical networking.

### ④ Verify both access and isolation

- Affected frontend reaches orders by Service name and ClusterIP.
- Other legitimate callers continue to work; a caller intended to remain denied still cannot connect.
- Application timeouts/errors and latency recover. Add these positive and negative connectivity tests to policy-change validation.

## 🧠 Key Points

- Ready means the workload passed readiness conditions, not that every source can reach it.
- Source egress and destination ingress are independent checks.
- A policy timeout is a strong hypothesis here, not proof; test from the affected source.

## 📌 Senior-Level Takeaway

**Restore the smallest intended connection, then test both what should work and what must remain blocked.**

## Attempt Record — 2026-10-03

Candidate response summary (paraphrased): Suspected missing ingress permission from web to orders; proposed updating NetworkPolicy, checking reachability with kubectl exec and listing policies. Correctly explained that Ready endpoints may still be unreachable because of policy.

Score: 6.5/10. Interview Acceptance Probability: 60% (subjective answer-specific estimate).

## References

- [Kubernetes NetworkPolicy semantics](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
