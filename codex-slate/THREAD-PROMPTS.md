# Thread prompts for the Codex slate projects

Paste one into a new thread in the Server Work project. Each one points the thread at its folder in `Ledger\projects` (desktop `C:\Users\Michael\Ledger\projects\...`, ledger `/mnt/ssd/projects/...`). In each thread, Codex does the build and Claude reviews it, handles anything that needs ledger or Cloudflare, and keeps the folder's README status current.

---

### 1. Ledgerbook Site (#1)
Work on the project in `Ledger\projects\Ledgerbook Site`. Read its README.md and CODEX-PROMPT.md first. Codex builds the public front page, privacy policy and request-access form from that prompt. Your job: review Codex's PLAN.md and output against the acceptance list, check the privacy policy against docs/HOW-LEDGER-WORKS.md, and turn DEPLOY.md into Cloudflare steps I approve one at a time. Recommend apex vs www before anything moves. Keep the README status current.

### 2. Garage (#2)
Work on the project in `Ledger\projects\Garage` (vault project Projects/Garage). Read its README.md and CODEX-PROMPT.md first. Templates only for now: vehicle profile with custom entries, diagnostic record, service and parts records, printable forms. No spec research or full build plan yet. Your job: review Codex's drafts and examples, try each template in my vault, and install them only after I say yes.

### 3a. Vault Inbox Filer (#3, tied)
Work on the project in `Ledger\projects\Vault Inbox Filer`. Read its README.md and CODEX-PROMPT.md first. Codex builds a plan, approve, then file tool on clerk-codex. obs moves stay guarded, so I approve by ticking a plan note. Your job: review RULES.md and the first real plan with me, check that apply never runs unticked rows, and give me the cron line to paste.

### 3b. Concierge Mailbox (#3, tied)
Work on the project in `Ledger\projects\Concierge Mailbox`. Read its README.md and CODEX-PROMPT.md first. Codex writes DESIGN.md first and stops. Walk me through the design and its prerequisites (assistant Proton account, Bridge, LLM provider and cost, approval host), then get my OK before the build phase. Prompt-injection safety and approval-before-send are non-negotiable.

### 4. DR and Security Review (#4)
Work on the project in `Ledger\projects\DR and Security Review`. Read its README.md and CODEX-PROMPT.md first. Before Codex starts, check whether the 2026-11-10 05:00 Appdata Backup to the Aegis succeeded, and tell Codex which set to restore. Your job: keep the drill in its scratch folder, review DR-DRILL.md and SECURITY-REVIEW.md, and turn the top fixes into a short list I approve one at a time.

### 5. Ledger Pocket (planning)
Work on the project in `Ledger\projects\Ledger Pocket`. Read its README.md and CODEX-PROMPT.md first. This phase is planning and deployment design only; no app code. Your job: review Codex's plan set, especially NETWORK-AND-AUTH.md, THREAT-MODEL.md and DEPLOYMENT.md. Then give me OPEN-QUESTIONS.md as a checkbox form so I can decide what Phase 0 looks like.

### 6. PRISM Visuals
Work on the project in `Ledger\projects\PRISM Visuals` (vault project Projects/PRISM). Read its README.md and CODEX-PROMPT.md first. The W05 fixes are done. This is a read-only recommendations report on PRISM rendering its own independent scenes (Chrysalis and Thornstorm first). Your job: check Codex's report against the vault decisions and the shareable-licenses rule, then give me its open questions as a pick form.

### Parked (don't start yet)
`Ledger\projects\Parked Ideas\` holds Guest Guide (soon), Immich, SillyTavern Assistant, HA Automations and Minecraft Winter Event, each with a README and a draft prompt. To start one later: "Work on `Ledger\projects\Parked Ideas\<name>`. Read its README, check that its unblock conditions are met, refresh the draft prompt against the current server, then show me the refreshed prompt before Codex runs it."
