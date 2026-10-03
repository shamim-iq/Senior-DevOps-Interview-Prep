# Question 06 — IRSA AccessDenied After Helm Release

## 🎯 Scenario

An EKS application uses IRSA for S3 reads. After a Helm release, pods are Running but SDK calls fail with AccessDenied on AssumeRoleWithWebIdentity. The role's S3 permission policy is unchanged. A teammate proposes cluster-admin for the ServiceAccount. Investigate and restore access with minimal permissions.

## ✅ Interview-Ready Answer

> I would reject cluster-admin because Kubernetes RBAC does not authorize AWS STS calls. The failure occurs while obtaining credentials, before the S3 request. I would verify the running pod's ServiceAccount, its role annotation and injected IRSA configuration, then compare them with the IAM role's trust policy and the Helm change. I would restore the intended identity or correct narrowly scoped trust, roll out replacement pods if required, and verify the assumed role plus an authorized S3 read.

## 🔄 Diagram

```text
Pod uses ServiceAccount
           |
Kubernetes projects a signed JWT
           |
SDK -> STS AssumeRoleWithWebIdentity
           |
IAM trust matches issuer + subject + audience?
       /                         \
      No                         Yes
 AccessDenied          Temporary AWS credentials
                                  |
                         S3 authorization check
```

## 🔍 Troubleshooting / Reasoning Flow

### ① Inspect the identity actually deployed

```sh
kubectl describe pod <pod> -n <ns>
kubectl describe sa <service-account> -n <ns>
aws iam get-role --role-name <role-name> --query 'Role.AssumeRolePolicyDocument'
```

| Command | Why / key evidence |
| --- | --- |
| `describe pod` | Verify actual ServiceAccount, AWS_ROLE_ARN, AWS_WEB_IDENTITY_TOKEN_FILE and projected token mount. Listing ServiceAccounts alone cannot prove which one the pod uses. |
| `describe sa` | Check `eks.amazonaws.com/role-arn`; compare with the intended role and pod configuration. |
| `iam get-role` | Inspect trust: correct IAM OIDC provider, action `sts:AssumeRoleWithWebIdentity`, subject and audience. Requires operator IAM read permission. |

Replace placeholders; examples only, not executed commands. Do not print or copy the token itself. Compare rendered Helm manifests/values with the last working release, focusing on namespace, ServiceAccount name and annotation.

### ② Match the trust precisely

| Trust element | Expected value |
| --- | --- |
| Federated principal | IAM OIDC provider corresponding to this EKS cluster's issuer |
| `sub` | `system:serviceaccount:<namespace>:<service-account>` |
| `aud` | `sts.amazonaws.com` |

An accidental ServiceAccount rename can fail trust even with the correct role ARN. A nonexistent ServiceAccount would generally prevent pod creation; Running pods suggest an existing but unintended identity or another trust/configuration mismatch.

**Precision:** EKS already has an OIDC issuer; IRSA setup associates an IAM OIDC provider. Kubernetes issues the projected token, and the SDK exchanges it for STS temporary credentials. Trust is configured ahead of time in IAM; the pod does not create it.

### ③ Fix narrowly and validate

- Correct the Helm values/annotation to restore the intended identity, or update exact trust conditions if the identity change was intentional. Do not wildcard all ServiceAccounts or grant cluster-admin.
- Apply through GitOps and perform a controlled rollout when pod identity/injected settings must change. Updating only a ServiceAccount annotation does not reinject existing pods.
- Verify the application's actual credential identity and an allowed S3 operation. If the container includes AWS CLI and uses the same credential configuration:

```sh
kubectl exec <pod> -n <ns> -- aws sts get-caller-identity
```

**Why:** confirm the intended assumed role, not a node role or unrelated credentials. CLI success alone does not prove the application's SDK uses the same credentials; verify the application's read too. Only investigate S3 permissions as the next stage if STS succeeds but the S3 operation fails.

## 🧠 Key Points

- Kubernetes RBAC controls Kubernetes API access; IAM trust controls who can assume the AWS role; AWS permission policies govern resource operations.
- A Running pod proves neither IRSA success nor S3 access.
- Add rendered-manifest identity checks and a scoped integration test to prevent Helm regressions.

## 📌 Senior-Level Takeaway

**Locate the failing authorization stage before changing permissions. Restore the intended identity rather than broadening access.**

## Attempt Record — 2026-10-04

Candidate response summary (paraphrased): Explained IRSA, OIDC, annotated ServiceAccounts and Deployment linkage; identified Helm values changing the ServiceAccount name as a likely regression; proposed listing/describing ServiceAccounts to check the role ARN; rejected cluster-admin. Described token issuance/trust loosely and did not explicitly inspect role trust conditions, the running pod's identity, or post-fix validation.

Score: 7/10. Interview Acceptance Probability: 65% (subjective answer-specific estimate).

## References

- [Assign IAM roles to ServiceAccounts](https://docs.aws.amazon.com/eks/latest/userguide/associate-service-account-role.html)
- [IRSA SDK credential exchange](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts-minimum-sdk.html)
