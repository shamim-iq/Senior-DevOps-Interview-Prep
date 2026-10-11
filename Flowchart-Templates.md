# Colorful Answer Flowchart Templates

Use these reusable Mermaid layouts for all topics. Copy a template, replace its labels and preserve the scenario's meaningful branches. View diagrams in a Mermaid-capable Markdown preview or on GitHub.

**Color key:** 🔵 starting point · 🟣 evidence · 🟡 decision · 🩵 action · 🟢 verified outcome · 🔴 risk/failure. Labels and shapes carry meaning even without color.

## 1. Linear steps

```mermaid
flowchart TD
    A["🔍 Symptom or input"]:::start --> B["Collect relevant evidence"]:::inspect
    B --> C["Apply the supported action"]:::action
    C --> D["✅ Verify the outcome"]:::success
    classDef start fill:#dbeafe,stroke:#2563eb,color:#172554;
    classDef inspect fill:#ede9fe,stroke:#7c3aed,color:#2e1065;
    classDef decision fill:#fef3c7,stroke:#d97706,color:#451a03;
    classDef action fill:#cffafe,stroke:#0891b2,color:#164e63;
    classDef success fill:#dcfce7,stroke:#16a34a,color:#052e16;
    classDef caution fill:#ffe4e6,stroke:#e11d48,color:#4c0519;
```

## 2. Troubleshooting branches

```mermaid
flowchart TD
    A["🔍 Capture evidence"]:::start --> B{"Condition confirmed?"}:::decision
    B -->|Yes| C["Targeted correction"]:::action
    B -->|No| D["Inspect alternative cause"]:::inspect
    D --> E["Evidence-supported correction"]:::action
    C --> F["✅ Verify recovery"]:::success
    E --> F
    classDef start fill:#dbeafe,stroke:#2563eb,color:#172554;
    classDef inspect fill:#ede9fe,stroke:#7c3aed,color:#2e1065;
    classDef decision fill:#fef3c7,stroke:#d97706,color:#451a03;
    classDef action fill:#cffafe,stroke:#0891b2,color:#164e63;
    classDef success fill:#dcfce7,stroke:#16a34a,color:#052e16;
    classDef caution fill:#ffe4e6,stroke:#e11d48,color:#4c0519;
```

## 3. Stored-data pipeline

```mermaid
flowchart TD
    A["📥 Source data"]:::start --> B["Process data"]:::action
    B --> C["Stored data"]:::inspect
    D["💬 Request"]:::start --> E["Retrieve relevant data"]:::action
    C -->|Search| E
    E --> F["Build response"]:::action
    F --> G["✅ Check response quality"]:::success
    classDef start fill:#dbeafe,stroke:#2563eb,color:#172554;
    classDef inspect fill:#ede9fe,stroke:#7c3aed,color:#2e1065;
    classDef decision fill:#fef3c7,stroke:#d97706,color:#451a03;
    classDef action fill:#cffafe,stroke:#0891b2,color:#164e63;
    classDef success fill:#dcfce7,stroke:#16a34a,color:#052e16;
    classDef caution fill:#ffe4e6,stroke:#e11d48,color:#4c0519;
```

Keep labels short and quote node text. Use a diamond for a real decision; preserve Yes/No and failure routes. Add a red failure node only where the scenario needs one. Do not turn command examples, terminal output or plain explanatory arrows into flowcharts.
