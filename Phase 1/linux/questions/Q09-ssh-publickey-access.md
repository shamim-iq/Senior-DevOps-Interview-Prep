# Q09 — SSH Permission Denied (publickey)

## 🎯 Scenario

TCP 22 is reachable, but an engineer gets Permission denied (publickey). An administrator has an existing session. Restore access without enabling root password login or locking out the administrator.

## ✅ Interview-Ready Answer

> Keep the administrator's session open. The error means SSH reached authentication, so first check the requested user, offered key and server rejection logs. Verify the target account's authorized_keys file and ownership/permissions. Correct the demonstrated problem; if a new key is needed, generate it on the engineer's trusted client and install only its public key. Validate any SSH configuration changes before reloading, and prove a fresh login works before closing the recovery session.

## 🔄 Flow

```text
Keep admin session → client debug + matching server logs
                              ↓
Correct user/key? → authorized_keys + permissions + access rules
                              ↓
Minimal fix → validate configuration if changed → fresh login test
```

## 🛠️ Essential Checks

Examples only; not executed. Use the actual username, key and host. The service is commonly ssh on Ubuntu and sshd on other distributions.

| Command | Purpose |
| --- | --- |
| `ssh -vvv -o IdentitiesOnly=yes -i <private-key> <user>@<host>` | On the client, see which key is offered and where authentication fails. Do not assume the username is ubuntu. |
| `sudo journalctl -u <ssh-unit> --since "15 minutes ago"` | On the server, correlate the rejected login with ownership, account or policy errors. Some systems use /var/log/auth.log or /var/log/secure. |
| `sudo namei -l /home/<user>/.ssh/authorized_keys` | Inspect ownership and permissions along the actual home/key path. authorized_keys is a file, usually containing one public key per line. |
| `sudo sshd -t` | Validate SSH configuration and host-key sanity before reloading configuration. This does not prove the user's authentication will succeed. |

Inspect the configured AuthorizedKeysFile location and relevant user/group restrictions or Match rules if logs point there. Typical user-owned permissions are 700 for .ssh and 600 for authorized_keys; the home/key path must not be writable by unauthorized users. Correct only the demonstrated issue; do not disable StrictModes or overwrite other valid keys.

## 🔑 Key Recovery

- If only the server public-key entry is missing, restore the matching public key from the user's trusted client. A new pair is not automatically necessary.
- If the private key is lost or compromised, the user generates a replacement **on their trusted client** (for example `ssh-keygen -t ed25519` where policy permits). Choose a new filename to avoid overwriting other keys; protect it with a passphrase.
- The administrator verifies and installs **only the public key** in the intended account's authorized_keys, preserving other valid entries. Keep the private key on the client; do not generate it on the server and distribute it as the default recovery workflow. Revoke the lost/compromised key as appropriate.
- OpenSSH does not directly use PuTTY's .ppk format; export it to an OpenSSH-compatible format or use PuTTY. A .pem filename alone does not guarantee a usable key.

## ✅ Validate Safely

An authorized_keys edit normally needs no daemon reload. If daemon configuration changes, first pass `sudo sshd -t`, then use `sudo systemctl reload <ssh-unit>` where supported. Preserve the old session and configuration rollback path.

Open a separate fresh session from the engineer's client, confirm the correct account and expected access, and confirm the administrator can still establish a new session. Keep root/password restrictions intact. An existing session alone does not prove new authentication works.

## Attempt — 2026-10-10

Candidate rejected root password access, preserved the administrator session, used client verbose output and service/log checks, and considered resource/key failures. Proposed generating a key pair, installing the public key in an authorized-keys directory and sharing the private key with the user. Missing explicit user/key/permission checks and fresh-login verification.

**Score: 6.5/10 — four-year baseline.** Subjective answer-specific acceptance estimate: 60%, not hiring probability.

Credit: useful debug command, log-first approach and lockout prevention. Deductions: 1.5 key-custody/recovery workflow; 1 omitted account/key-file ownership and permission checks; 0.75 missing configuration-change/fresh-login validation; 0.25 diagnostic focus and path/format precision. journalcrl is treated as a minor typo, not a separate deduction. sshd is a daemon often managed by systemd, not a special type of systemd process; resource investigation should follow evidence.

## References

- [OpenSSH authentication files and configuration testing](https://man.openbsd.org/sshd.8)
- [OpenSSH key generation](https://man.openbsd.net/ssh-keygen.1)
- [OpenSSH client authentication](https://man.openbsd.com/ssh.1)
