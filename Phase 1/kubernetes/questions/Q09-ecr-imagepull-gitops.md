# Question 09 — ECR ImagePullBackOff After GitOps Release

## 🎯 Scenario

After a Helm image-tag change is synced by Argo CD to EKS, new API pods enter ImagePullBackOff while old replicas serve traffic. Argo CD is Synced but Degraded. The image is in private ECR and the build succeeded. Isolate the pull failure and restore the rollout without disrupting healthy replicas.

## ✅ Interview-Ready Answer

> I would preserve the serving replicas and inspect the failing pod's exact pull error and image URI. I would verify the image exists in the intended ECR account/region/repository, then check the actual pull identity or network path according to the error. I would correct the Helm reference or narrowly scoped pull permissions, or revert to a known-good image in Git. After sync, I would verify new pods pull, become Ready and serve requests before replacing healthy capacity.

## 🔄 Diagram

```text
Pod pull error -> inspect exact event
     |
     +-- Not found -> image URI / tag / digest / platform
     +-- Denied    -> actual pull identity + repository policy
     +-- Timeout   -> registry DNS / network / endpoints
                          |
                Correct or revert through Git
                          |
             New pods Ready + customer checks pass
```

## 🔍 Troubleshooting / Reasoning Flow

### ① Start with evidence

```sh
kubectl describe pod <failing-pod> -n <ns>
aws ecr describe-images --registry-id <account-id> --repository-name <repo> --image-ids imageTag=<tag> --region <region>
```

**Why:** pod events show the runtime error and exact image reference. ECR lookup verifies publication in the intended registry; build success alone does not prove push success. The AWS lookup uses operator credentials, so success does not prove the node can pull. An authorization error on the lookup does not prove the image is absent. Examples only; no cluster commands were executed.

| Evidence | Next check |
| --- | --- |
| Not found / manifest unknown | Compare rendered Helm image URI with the published tag/digest; verify account, region and repository. |
| Unauthorized / access denied | Identify the configured pull credentials, then check their ECR permissions and repository policy, especially cross-account. |
| Timeout / DNS error | Check node-to-ECR connectivity; private setups may need ECR API/DKR endpoints and S3 access for image layers. |
| No matching platform | Verify the image manifest supports the node architecture. |

### ② Check the correct identity

| Setup | Normal image-pull identity |
| --- | --- |
| EKS EC2 nodes | Node IAM role via kubelet's ECR credential provider |
| EKS Fargate | Fargate pod execution role |
| Explicit registry secret | Pod/ServiceAccount imagePullSecrets; inspect the secret reference without exposing credentials |

**IRSA runtime access is separate:** the application's `eks.amazonaws.com/role-arn` annotation alone does not grant ordinary kubelet pulls its permissions. Only investigate ServiceAccount-based pull roles if that credential-provider mechanism is configured. Newer supported EKS configurations can use a separate `eks.amazonaws.com/ecr-role-arn` annotation for per-pod image pulls; do not assume it is enabled or confuse it with runtime IRSA.

### ③ Recover while keeping healthy capacity

- Preserve old serving replicas; avoid deleting all pods or a recreate-style rollout. Review maxUnavailable/maxSurge and available capacity before continuing.
- Fix the reference or narrowly scoped pull permissions. If a quick safe correction is unavailable, revert Git to the known-good immutable image reference. Existing pods may run cached images even when new pulls are broken, so verify the recovery image remains pullable.
- Auto-sync acts only if enabled; otherwise sync explicitly after the reviewed change:

```sh
# State-changing: apply the corrected desired state
argocd app sync <app>
kubectl rollout status deployment/<deployment> -n <ns>
```

**Why:** sync applies manifests; rollout status checks Deployment progress. Also verify the new image/version, pod readiness, Argo CD health and customer errors/latency. Rollout completion alone is not a functional test.

## 🧠 Key Points

- **Synced:** desired manifests match live resources. **Healthy:** resources operate successfully. Synced does not imply the image can be pulled.
- kubelet/container runtime pulls the image; Argo CD applies the workload definition.
- Prevent recurrence with verified push/digest promotion, immutable image references and a rollout smoke test using the target environment's pull mechanism.

## 📌 Senior-Level Takeaway

**Trace the failure to the exact image, identity or network path; recover through Git without sacrificing existing serving capacity.**

## Attempt Record — 2026-10-04

Complete answer evaluated once, including the recovery paragraph supplied after the interrupted turn.

Candidate response summary (paraphrased): Identified incorrect Helm image tags and insufficient pull permissions; proposed checking the Deployment's ServiceAccount role annotation and IAM permissions. Recognized pipeline success does not guarantee image pulls or healthy workloads. Proposed correcting tag/permissions/ServiceAccount in Git and allowing auto-sync or using argocd app sync. Assumed the image was pushed and did not specify pod-event diagnosis or healthy-replica preservation/validation.

Score: 6.5/10. Interview Acceptance Probability: 60% (subjective answer-specific estimate).

## References

- [ECR image pulls on EKS](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_on_EKS.html)
- [Private registry troubleshooting](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/)
- [Optional per-pod ECR pull roles](https://aws.amazon.com/blogs/containers/implement-per-pod-image-pull-permissions-with-ecr-repository-policies-on-amazon-eks/)
