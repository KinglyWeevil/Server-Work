# Codex kickoff: Ledger Pocket, planning and deployment design (no app code yet)

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
