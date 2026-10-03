# Question 08 — Intermittent CoreDNS SERVFAIL

## 🎯 Scenario

Several EKS applications intermittently fail to resolve internal Service names. Requests by ClusterIP succeed. CoreDNS pods are Running, but DNS latency and SERVFAIL increase at traffic peaks. Isolate the cause and restore DNS with minimal disruption.

## ✅ Interview-Ready Answer

> ClusterIP success narrows the issue toward DNS; Running CoreDNS pods do not prove healthy resolution or overload. I would reproduce an exact failing query from an affected pod, correlate CoreDNS errors with resource/query metrics, and check recent configuration changes and Kubernetes API access. I would scale only if capacity evidence supports it, otherwise fix the identified configuration, permission or connectivity issue. I would verify DNS and application recovery across affected nodes through peak traffic.

## 🔄 Diagram

```text
Service IP works, name fails
             |
Reproduce query -> correlate DNS logs + metrics
             |
      Evidence of saturation?
       /                 \
     Yes                 No
      |                   |
Add DNS capacity     Inspect Corefile, API access,
and verify spread    resolver path / recent change
       \                 /
        Test DNS + application recovery
```

## 🔍 Troubleshooting / Reasoning Flow

### ① Reproduce from the affected source

```sh
kubectl exec <app-pod> -n <ns> -- nslookup <service>.<namespace>.svc.cluster.local
```

**Why:** check the actual query, responding resolver and error. Use the configured cluster domain; use approved debugging tooling if nslookup is absent. Compare affected and unaffected pods/nodes. Inspect `/etc/resolv.conf` when resolver/search configuration is suspect; test an absolute name ending in a dot to avoid search expansion.

### ② Check the DNS server, not just pod phase

```sh
kubectl logs -n kube-system <coredns-pod> --since=10m
kubectl top pods -n kube-system
kubectl get configmap coredns -n kube-system -o yaml
```

| Check | Purpose / evidence |
| --- | --- |
| CoreDNS logs | Compare replicas for API watch/RBAC failures, plugin errors or forwarder timeouts; lack of logged queries is not proof no traffic arrived. |
| Resource metrics | Look for saturation and uneven load; current top samples alone can miss peaks. Correlate historical CPU throttling, memory, query rate, response codes and latency. |
| Corefile | Compare recent changes, cluster zone, forwarding and caching with the working configuration. |

Examples only; no cluster commands were executed. `top` needs a working Metrics API. Avoid enabling high-volume query logging indiscriminately during overload.

**Choose the next action from evidence:**

- High query load plus saturation: add CoreDNS capacity and check replica placement and resource sizing.
- Internal cluster-zone failures plus API/RBAC errors: restore CoreDNS's required Kubernetes API connectivity or scoped list/watch permissions. Adding replicas does not repair shared broken permissions.
- Forwarder errors: identify the exact query and Corefile route. Normal internal Service records are served by the Kubernetes plugin; upstream DNS is not automatically the cause of internal-name failures.
- Node-specific timeouts: check that node's DNS path, policy/UDP and TCP 53 reachability, and NodeLocal DNS if deployed. A SERVFAIL response differs from receiving no response at all.

### ③ Mitigate and verify

Scale through the component's actual owner (EKS add-on autoscaling, GitOps or another configured controller). Check available capacity and avoid competing replica controllers. The EKS add-on autoscaler is cluster-size based; do not assume it directly follows query rate.

If a configuration regression caused the issue, restore the known-good change through the managed configuration path. Avoid restarting every DNS replica together or hardcoding Service IPs as the permanent fix.

**Recovery:** repeat name lookups and real application requests from affected nodes; verify SERVFAIL rate and p95/p99 DNS latency return to baseline during representative load. Follow up with tested scaling, sensible caching and alerts tied to DNS success/latency; consider NodeLocal DNS after validating workload/network fit.

## 🧠 Key Points

- Running is a pod phase, not proof that DNS queries succeed.
- SERVFAIL means the resolver could not complete the query; overload is one hypothesis, not a diagnosis.
- CoreDNS resolves names rather than forwarding application requests. It can also forward external DNS queries.
- ClusterIP traffic uses the configured Service dataplane: often kube-proxy rules, but potentially an eBPF implementation. IPv4 is an address family, not the name of the forwarding table.

## 📌 Senior-Level Takeaway

**Validate the bottleneck before scaling; a larger set of identically misconfigured DNS servers still fails.**

## Attempt Record — 2026-10-04

Candidate response summary (paraphrased): Compared CoreDNS to a DNS provider mapping Service names to IPs, inferred that Running/healthy pods implied high query demand, proposed scaling CoreDNS, and explained successful ClusterIP requests through kube-proxy-maintained IPv4 tables. No isolation checks or recovery validation were supplied.

Score: 5/10. Interview Acceptance Probability: 40% (subjective answer-specific estimate).

## References

- [Kubernetes DNS debugging](https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/)
- [EKS CoreDNS autoscaling](https://docs.aws.amazon.com/eks/latest/userguide/coredns-autoscaling.html)
