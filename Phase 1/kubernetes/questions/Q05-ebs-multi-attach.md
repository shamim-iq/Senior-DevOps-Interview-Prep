# Question 05 — EBS Multi-Attach After Node Failure

## 🎯 Scenario

An EKS StatefulSet uses an EBS-backed PV. After a node failure, its replacement pod is scheduled elsewhere but stays ContainerCreating. The PVC is Bound and events report Multi-Attach. The application stores customer data. Investigate, recover safely and reduce recurrence.

## ✅ Interview-Ready Answer

> I would verify whether the volume is still attached to the old instance and whether that instance can still write. Bound only confirms the PVC/PV relationship, not a successful mount. I would ensure the old writer is stopped or fenced, let normal CSI detachment complete, and recover on an eligible node in the volume's AZ. I would validate the attachment, application recovery and data integrity. Force detachment or changing storage systems is not the first step.

## 🔄 Diagram

```text
Multi-Attach -> Identify old attachment + verify old instance
                                  |
                      Can the old node still write?
                       /                       \
                    Yes/unknown                 No
                        |                        |
              Stop/fence old writer      Normal CSI detach
                        \                       /
                    Confirm old attachment released
                                  |
                   Attach on eligible same-AZ node
                                  |
                    Validate data + application health
```

## 🔍 Troubleshooting / Reasoning Flow

### ① Confirm attachment and topology separately

```sh
kubectl describe pod <pod> -n <ns>
kubectl describe pvc <pvc> -n <ns>
kubectl get pv <pv> -o yaml
kubectl get volumeattachment
```

**Why:** pod events identify the failure; PVC identifies the PV; PV YAML shows the CSI volume handle, access mode and node affinity; VolumeAttachment shows the intended node and attachment status. For the affected entry, use `kubectl describe volumeattachment <name>` if errors need detail. These are illustrative read-only checks, not executed commands.

Use the EBS console to verify the actual volume attachment, instance ID and AZ. Compare with the old instance's state and the replacement node's AZ. Kubernetes records alone may be stale.

| Finding | Meaning |
| --- | --- |
| Volume still attached to old node | Can cause Multi-Attach even if both nodes are in the same AZ. |
| Replacement node in another AZ | Separate topology problem: EBS cannot attach across AZs. Correct PV node affinity normally prevents such scheduling. |
| PVC Bound | Claim is bound to storage; it does not prove attachment or mount success. |

### ② Recover without allowing two writers

- **Do not equate NotReady with powered off.** A partitioned old node may still run the application and write to the volume. Stop/fence it at the infrastructure layer when required and verify it cannot resume writes; cordoning alone does not stop an existing writer.
- Prefer normal unmount/detach and CSI reconciliation. If attachment remains stuck after the old writer is confirmed stopped, inspect CSI controller errors and EBS state; use the established recovery procedure.
- Do not blindly delete VolumeAttachment objects, force-delete StatefulSet pods, or force-detach a live volume. Force detachment is a last-resort recovery action with filesystem/data-corruption risk, not a guaranteed lossless fix.
- Ensure eligible capacity exists in the volume's AZ, then allow reattachment. Do not delete the PVC/PV to clear the error; reclaim policy may delete the underlying data.

### ③ Validate and prevent

- Confirm the volume is attached to the intended instance, the pod is Ready, and application recovery/data-integrity checks pass. Test representative reads/writes and monitor errors.
- Use topology-aware provisioning (`WaitForFirstConsumer`) for new volumes and preserve PV node affinity. This does not move an existing EBS volume between AZs or solve stale attachments.
- Maintain same-AZ failover capacity, healthy CSI components and tested node-failure/fencing procedures.
- For AZ-wide failure, plan application replication or snapshot restore to a new volume in another AZ with explicit recovery-time/data-loss objectives. Test backups and restores.

## 🧠 Key Points

**EFS is an architecture/migration choice, not an attachment repair.** Regional EFS offers multi-AZ file storage; EFS One Zone also exists. A new EFS StorageClass/PVC does not contain the old EBS data. Moving requires application-compatible storage semantics, controlled data migration, validation and cutover. Changing a StorageClass provisioner does not convert a bound EBS volume into EFS.

**Same AZ is necessary, not sufficient:** the old attachment/writer must be safely resolved before a normal single-node EBS attachment can move.

## 📌 Senior-Level Takeaway

**Separate attachment conflicts from AZ constraints, and prove the old writer is fenced before recovery. No storage change automatically guarantees zero data loss.**

## Attempt Record — 2026-10-03

Candidate response summary (paraphrased): Correctly stated EBS is AZ-specific and recognized the old attachment. Assumed the replacement node was in another AZ, said same-AZ reattachment would have no issue, and proposed switching the StorageClass provisioner to EFS CSI for cross-AZ persistence with no data loss. Linked the Multi-Attach/detachment issue to the different AZ.

Score: 4.5/10. Interview Acceptance Probability: 35% (subjective answer-specific estimate).

## References

- [EBS attachment and volume lifecycle](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-lifecycle.html)
- [EBS detachment and force-detach risks](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-detaching-volume.html)
- [Kubernetes StorageClasses](https://kubernetes.io/docs/concepts/storage/storage-classes/)
