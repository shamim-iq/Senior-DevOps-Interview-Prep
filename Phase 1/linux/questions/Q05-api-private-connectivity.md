# Question 05 — Local API Works / Remote Connection Fails

## 🎯 Scenario

localhost:8080/health responds on the Linux API host. A second server cannot reach its private IP on port 8080, but SSH works. A teammate proposes disabling the firewall. Locate the failure, restore minimal access and verify.

## ✅ Interview-Ready Answer

> I would first inspect the listening address, not just the port: a loopback-only listener cannot accept remote traffic. I would test the private-IP endpoint locally and from the client, then inspect the actual host firewall and cloud network controls/routes. I would correct a proven bind-address regression or allow only the authorized source to TCP 8080. Different private networks can communicate through configured private connectivity; public exposure is unnecessary. Finally I would test from the real client and verify unauthorized sources remain blocked.

## 🔄 Flow

```text
Inspect listener address → test private IP locally and remotely
                                  ↓
Loopback-only? Fix binding     Network failure? Check rules/routes
                                  ↓
             Narrow change → client works + isolation preserved
```

## 🔍 Essential Commands

Examples only; no production commands executed. Replace placeholders with real values.

| Command | Purpose |
| --- | --- |
| `sudo ss -ltnp 'sport = :8080'` | Inspect TCP listener and owner. `127.0.0.1:8080` is loopback-only; `<private-ip>:8080` binds that address; `0.0.0.0:8080` binds all IPv4 interfaces. Do not assume an IPv6 listener accepts IPv4. |
| `curl -v --connect-timeout 5 http://<private-ip>:8080/health` | Run on the host, then the actual client. Distinguish refusal, timeout and HTTP error; these guide investigation but do not prove a unique cause. |
| `sudo ufw status verbose` | Inspect policy if UFW manages this host. An inactive UFW does not prove all host/cloud filtering is absent. |
| `ip route get <private-ip>` | On the client, inspect the chosen route/source; also check the return path and cloud route tables if needed. |

`ps`, `netstat` and `lsof` can help, but repeating all three adds little once ss identifies the listener. SSH success proves access to its own port, not TCP 8080.

## 🛠️ Narrow Mitigation

- If the application is unintentionally bound only to loopback, update its listen configuration to the intended private interface and safely restart/reload as supported. Preserve an intentional reverse-proxy design rather than exposing a backend blindly. Binding is usually configuration, not a code rewrite.
- If UFW is proven to block authorized traffic, a **state-changing example** is:

```sh
sudo ufw allow proto tcp from <client-ip-or-cidr> to <api-private-ip> port 8080
```

- Review existing rules: adding a narrow rule does not cancel an already broad allow. Retain SSH access and change only the demonstrated blocker. Check cloud security groups/NSGs, ACLs and return traffic where applicable.
- Separate VPCs/VNets or on-premises clients can use peering, VPN or other approved private routing. They need suitable routes and access rules, not mandatory public IPs. In cloud NAT designs the public IP may not even be assigned to a host interface.

## ✅ Verify / Key Takeaway

Repeat the request from the original client; confirm expected HTTP response and application logs, authorized traffic only, and preserved SSH. Verify an unauthorized test source remains blocked where feasible. Persist the proven configuration in deployment/IaC so the next release retains it.

**Check address + port + route + policy; keep internal APIs private.**

## Attempt — 2026-10-06

Candidate rejected disabling the firewall; used ufw status, broad allow 8080/tcp, ps, ss/netstat and lsof. Mentioned correct IP binding generally, but did not explicitly interpret loopback versus private listeners. Claimed private clients must share a VPC/VNet and otherwise require public exposure. Did not specify end-to-end verification.

**Score: 6.5/10 — four-year baseline.** Subjective answer-specific acceptance estimate: 60%, not a hiring prediction.

Credit: right diagnostic areas, useful listener tools and intent to preserve filtering. Deductions: 1 for broad firewall permission, 1 for incorrect private-connectivity/public-exposure claim, 0.75 for missing explicit loopback/address interpretation and evidence before mutation, 0.75 for omitted client-side recovery verification. No penalty for omitted advanced packet-capture commands.

## References

- [Ubuntu firewall source-scoped rules](https://documentation.ubuntu.com/server/how-to/security/firewalls/index.html)
- [AWS private connectivity across VPCs](https://docs.aws.amazon.com/vpc/latest/peering/)
