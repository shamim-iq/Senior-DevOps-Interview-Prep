# 🐧 Linux Boot Process

**Booting = starting the machine, loading Linux and bringing up services.**
Typical flow for a modern server using systemd; details vary by setup.

## 🌈 From power-on to a running server

```mermaid
flowchart TD
    A["🔌 Power on"] --> B["🧭 BIOS / UEFI<br/>Check hardware and choose the boot device"]
    B --> C["🚀 Boot loader — usually GRUB<br/>Load the kernel and temporary startup files into RAM"]
    C --> D["🧠 Kernel<br/>Start managing CPU, memory and devices"]
    D --> E["🧰 initramfs<br/>Temporary tools prepare access to the main disk"]
    E --> F["💾 Main filesystem mounted at /<br/>Switch to the installed Linux system"]
    F --> G["⚙️ systemd — process 1<br/>Manage mounts and start required services"]
    G --> H["🌐 Server mode<br/>Networking, SSH and configured applications"]
    H --> I["✅ Check readiness<br/>Verify login, storage and application health"]
    classDef blue fill:#dbeafe,stroke:#2563eb,color:#172554;
    classDef purple fill:#ede9fe,stroke:#7c3aed,color:#2e1065;
    classDef amber fill:#fef3c7,stroke:#d97706,color:#451a03;
    classDef green fill:#dcfce7,stroke:#16a34a,color:#052e16;
    class A,B blue;
    class C,D purple;
    class E,F amber;
    class G,H,I green;
```

## 💡 Remember these points

- **Kernel** = Linux's core; **systemd** = the service manager. systemd may also run during the temporary startup stage.
- **`/`** = the main directory tree. Separate disks such as `/data` may mount later.
- **Services can start together** once their requirements are ready. Servers usually use `multi-user.target` — a group of services for normal server operation.
- **Boot completed ≠ application healthy.** Always verify the application itself.

## 🛠️ Quick checks

| Command | Purpose |
| --- | --- |
| `sudo journalctl -b` | Read current boot logs. |
| `sudo journalctl -k -b` | Check kernel startup messages. |
| `systemctl --failed` | Find failed services or mounts. |
| `systemd-analyze` | Check recorded boot duration. |

**Memory aid:** 🔌 Power → 🧭 Firmware → 🚀 Loader → 🧠 Kernel → 🧰 Temporary tools → 💾 Main disk → ⚙️ Services → ✅ Verify.

[Source: systemd boot-process documentation](https://man7.org/linux/man-pages/man7/bootup.7.html)
