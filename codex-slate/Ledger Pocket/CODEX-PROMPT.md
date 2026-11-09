# Codex kickoff: Ledger Pocket, planning and deployment design (no app code yet) · Model: gpt-6-astra · Effort: high

> **Start Codex with:** model `gpt-6-astra`, reasoning effort `high` (architecture and planning judgment). Agents use the models in the roster below.

## Context
Michael wants an Android app, "Ledger Pocket", to manage his home server (ledger) and, later, other parts of his life. He asked for detailed planning and a deployment design before anything is built. Your job is the plan, not the app.

## Read first
- ledger-stacks `docs/HOW-LEDGER-WORKS.md` (branch `claude/project-thread-ljw1uc` until PR #3 merges): services, addresses, sign-in guards, the Tailscale and Cloudflare paths.
- This folder's `README.md` (network facts as of 2026-11-09).
- Server-Work repo `guest-guide/argon-packages/PACKAGE-INDEX.md` for the brand kit.
- Vault `Projects/Ledger/Status.md`, `To-do.md`, `Eventually.md`.

## Deliverables (Markdown in this folder; Mermaid for diagrams)
1. **`PLAN.md`:** the one-page summary: what v1 does, who it's for (Michael only at first; maybe Bunny later), what it never does, and the phase list.
2. **`FEATURES.md`:** candidate modules ranked by value and risk. Server: health (Uptime Kuma), wake PCs (UpSnap), downloads (qBittorrent, Radarr and Sonarr queues), requests (Seerr), Home Assistant scenes and a few entities, backup status (last Appdata Backup, Proton run, Authentik dump), Minecraft players. Life: quick capture into the vault Inbox, garage log entry (matching the Garage project templates), maybe notifications hub. Mark each **read-only** or **writes**, and keep v1 read-only.
3. **`API-INVENTORY.md`:** per service: endpoint, auth method, read vs write calls needed, how the phone reaches it at home and away, rate limits, and anything **Not confirmed**. Include each app's version from the doc.
4. **`NETWORK-AND-AUTH.md`:** compare the reachable paths with a recommendation:
   - (a) Tailscale subnet route for `192.168.1.100/32` only (ACL-restricted to Michael's phone);
   - (b) Tailscale Serve per service on ledger's tailnet name;
   - (c) Cloudflare Access service tokens on the existing hostnames (one token per device, revocable);
   - (d) a small "pocket API" gateway on ledger that aggregates read-only calls behind one auth.
   Cover how each behaves at home (Xfinity blocks `.vip` names for ledger itself; check whether it affects the phone on home Wi-Fi), away, and when one service is down. Where secrets live on the phone (Android Keystore, biometric gate), rotation, and what happens if the phone is lost.
5. **`ARCHITECTURE.md`:** Kotlin, Jetpack Compose, Material 3 with the Ledgerbook theme, single activity, MVVM, modules, offline cache, background refresh limits (WorkManager), notifications, testing approach (unit tests, fake servers, screenshot tests). One Mermaid diagram.
6. **`THREAT-MODEL.md`:** assets, attackers (lost phone, malicious app, network attacker, leaked token), mitigations, and the "kill switch" steps Michael takes to revoke everything in under 5 minutes.
7. **`DEPLOYMENT.md`:** how builds reach the phone: compare sideloading a signed APK via a private GitHub Release plus Obtainium, a private F-Droid repo on ledger, and Google Play internal testing ($25 one-time developer account). Signing-key custody and backup, versioning, CI (GitHub Actions build and test; no secrets in logs), update cadence, rollback. Recommend one.
8. **`ROADMAP.md`:** phases with exit criteria: 0 (spike: one read-only call over the chosen path), 1 (read-only dashboard), 2 (safe writes with confirm dialogs: wake, request, pause torrent), 3 (life modules). Effort per phase in Codex-sessions and in hours of Michael's time.
9. **`OPEN-QUESTIONS.md`:** every decision Michael must make, as multiple choice with your recommendation marked, so he can answer by ticking.

## Constraints
- No app code, no Android project scaffolding, no changes on ledger or Cloudflare. Read-only checks on ledger (e.g. `curl` to a health endpoint from ledger itself) are allowed only if you show the command first.
- Prefer options that add **no new public hostnames**.
- Every claim about an API or a platform rule is labeled and cited (official docs first).

## Acceptance
- Michael can read `PLAN.md` + `OPEN-QUESTIONS.md` in ten minutes and make every decision needed to start Phase 0.
- Each network option lists exact setup steps and the undo.

## Agent work structure (use agents wherever the work splits cleanly)

Codex's `multi_agent` feature is on by default (stable in codex-cli 0.164+). Use `spawn_agent`, `wait_agent`, `send_message` and `list_agents`. If they aren't available in your session, do the same tasks one after another and say so in `REPORT.md`.

**How it runs:**
1. **You are the lead.** You own the plan, every write to shared files and the final checks. Agents write only inside `work/<task_name>/` in this folder. You review and merge their output.
2. **Brief every agent fully.** Agents don't share your context. Give each one a `task_name`, a self-contained brief (goal, inputs with paths, constraints from the Standing rules, output file, done-when), and the `model` and `reasoning_effort` from the roster below.
3. **Run in waves.** Agents in the same wave run in parallel; wait for a whole wave before starting the next. Anything that touches ledger, a live service, or a file another agent writes runs **lead-only and sequential**.
4. **One level deep.** Agents don't spawn their own agents unless the roster says so. This keeps cost and behavior predictable.
5. **Agents return** a summary of five lines or fewer, plus their output paths and any open questions. Check each claim before you build on it, because an agent's report is input, not truth.
6. **Independent review last.** A fresh reviewer agent checks the deliverables against the Acceptance list and writes `work/review/review.md`. You fix what it finds, or explain why not.
7. **Record it.** `REPORT.md` lists each agent, its model and effort, what it produced and whether it was used.

**Roster for this project** (lead: `gpt-6-astra` · `high`)

| Wave | task_name | Job | Model | Effort | Output |
|---|---|---|---|---|---|
| 1 | `api-inventory` | Per-service API endpoints, auth, read/write calls and versions (official docs first) | gpt-6.1-sol | medium | `work/api-inventory/` |
| 1 | `network-auth` | Compare the four network/auth paths with exact setup steps and undo | gpt-6.1-sol | high | `work/network-auth/` |
| 1 | `deployment` | Distribution, signing, CI and update options with costs | gpt-6.1-sol | medium | `work/deployment/` |
| 2 | `threat-model` | Threat model and 5-minute kill switch, built on the wave-1 outputs | gpt-6-astra | high | `work/threat-model/` |
| 2 | `features-roadmap` | FEATURES.md ranking and ROADMAP.md phases with effort | gpt-6.1-sol | medium | `work/features-roadmap/` |
| 3 | `review` | Check that PLAN.md + OPEN-QUESTIONS.md are enough for Michael to decide Phase 0 in ten minutes | gpt-6-astra | high | `work/review/review.md` |

The lead writes PLAN.md, ARCHITECTURE.md and OPEN-QUESTIONS.md, and resolves conflicts between agents.

## Standing rules (apply to every step)

1. **Read first:** the shared agent rules (`AGENTS.md`), the vault project's `Status.md` and newest `Log/` entry, and this folder's `README.md`.
2. **Secrets:** never print, read or commit secret values (`.env` files, tokens, keys, passwords). Use placeholders such as `<WEBHOOK_SECRET>` and say exactly where Michael enters the real value.
3. **No deletes.** Move anything you would remove into a `_quarantine/` folder and list it in your report.
4. **Live systems are read-only** unless this prompt names the change. Cloudflare (DNS, tunnel, Access, Pages), the routers, Proton, and anything on ledger outside a scratch directory: write the exact steps into a doc for Michael and stop. Do not apply them.
5. **Commands on ledger:** show each command before running it. Never touch the array, parity, `/boot`, or containers you did not create.
6. **Label factual claims:** **Confirmed** (name the source), **Presumed** (give the reasoning), **Not confirmed**, or **Discrepancy** (show both sides).
7. **Small commits** with clear messages, one concern per commit, where the folder is a git repo.
8. **When you finish or stop,** write `REPORT.md` in this folder: what is done, what is not, what Michael must do (numbered steps, one command per code block), and open questions as multiple choice with your recommendation marked.
9. **Log it:** append a short entry to the vault project's `Log/` per `_System/Assistant Rules.md`.

**Paths (Syncthing keeps them in step; work on one machine at a time):** desktop `C:\Users\Michael\Ledger\projects\<this folder>`, ledger `/mnt/ssd/projects/<this folder>`, workbench and clerks `/workspace/projects/<this folder>`.
