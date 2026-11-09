# Codex slate, 2026-11-09

Michael's picks from the Codex Sprint Slate (https://claude.ai/artifact/KfeM6X1ePUPfJVwR9xctj7), turned into project folders. Each top-level folder here is copied into `Ledger\projects\` as its own project.

| Rank | Folder | Status | Codex prompt |
|---|---|---|---|
| 1 | Ledgerbook Site | Ready | Front page + privacy policy + request form; brand-swappable for Science-Man.com later |
| 2 | Garage | Ready | Templates and printable forms only |
| 3 (tie) | Vault Inbox Filer | Ready | Plan, approve, file (obs moves stay guarded) |
| 3 (tie) | Concierge Mailbox | Ready | Design first, stop, then build |
| 4 | DR and Security Review | Ready | DR drill (scratch only) + security review (report only) |
| unranked | Media Library Audit | Ready | Read-only report: mismatches, dupes, subs, HEVC savings |
| unranked | Ledger Pocket | Ready | Planning and deployment design only |
| unranked | PRISM Visuals | Ready | Read-only recommendations for native scenes |
| parked | Parked Ideas/* | Later | Draft prompts only |

Every Codex prompt carries the same standing rules: no secrets, no deletes (quarantine), live systems read-only unless the prompt names the change, claims labeled Confirmed/Presumed/Not confirmed/Discrepancy, a REPORT.md at the end, and a vault log entry.

Thread prompts: `THREAD-PROMPTS.md` (each heading names the Claude model/effort for the thread and the Codex model/effort for the work).

**Models used (checked on the desktop 2026-11-09, codex-cli 0.164.0):** `gpt-6-astra` (frontier: design, security, judgment), `gpt-6.1-sol` (workhorse: most leads), `gpt-6.1-terra` (Codex-tuned: code-heavy agents; its strengths are Presumed from its name), `gpt-6-luna` (fast and cheap: mechanical agents). Efforts run low, medium, high, xhigh, max, ultra; nothing here needs max or ultra. Every active Codex prompt has an "Agent work structure" section: the lead plus waves of `spawn_agent` workers, one level deep, with an independent reviewer last.
