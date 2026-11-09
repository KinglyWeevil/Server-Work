# Codex kickoff: ledger disaster-recovery drill + security review (combined) · Model: gpt-6.1-sol · Effort: xhigh

> **Start Codex with:** model `gpt-6.1-sol`, reasoning effort `xhigh` (touches the live server, so the lead runs every ledger command itself). Agents use the models in the roster below.

## Context
ledger is Michael's home server (Dell T330, Unraid 7.3.4, 192.168.1.100). Docker Compose stacks live in `/mnt/user/appdata/stacks` (git repo `KinglyWeevil/ledger-stacks`); `/boot/config` is backed up to `KinglyWeevil/ledger-config`. Run this from **Codex on Michael's desktop** using `ssh ledger "<command>"` (key auth as root). Every command you run on ledger is shown before you run it.

## Read first
- ledger-stacks `docs/HOW-LEDGER-WORKS.md` (branch `claude/project-thread-ljw1uc` until PR #3 merges): every service, network, port, sign-in and backup path, with evidence labels and a "Discrepancies" table.
- This folder's `README.md` (facts as of 2026-11-09), the stacks `README.md`, `scripts/proton-backup.sh`, the Appdata Backup plugin config, `edge/` (tunnel and Access audit scripts: GET only).
- Vault `Projects/Ledger/Status.md`, `To-do.md`, the newest `Log/` entry.

## Part 1: disaster-recovery drill (scratch only)
**Scratch area:** `/mnt/user/data/_staging/dr-drill-2026-11/`. Throwaway containers get names starting `drdrill-`, no published ports, no shared networks with live stacks, and are stopped (not removed) at the end. Nothing outside the scratch area changes. Ask Michael before removing scratch.

For each item, record: source file and age, command, wall time, result, and gaps.
1. **Authentik DB:** restore the newest nightly pg_dump into a fresh `postgres:16.10-alpine` (`drdrill-authentik-pg`); count users, flows, applications and providers; compare the counts with the live DB using read-only queries.
2. **Appdata:** if the 2026-11-10 05:00 Aegis run succeeded (folder not ending in `-failed`), use it; otherwise use the newest set in `/mnt/user/backups/appdata` and say so. Extract 5 apps (Radarr, Sonarr, Seerr, Audiobookshelf, Uptime Kuma) into scratch; prove each config opens (SQLite `PRAGMA integrity_check`, row counts of a key table, or start the app read-only in a `drdrill-` container with no ports and check its health endpoint from inside).
3. **Flash/config:** compare the newest flash backup with the `ledger-config` repo (file list and diff summary; never print secrets).
4. **Offsite:** `rclone lsf` and `rclone check --one-way` on a small sample (one tier 0 file set, one tier 1, one from tier 6) against local; download 3 files into scratch and verify checksums. Read the newest `proton-upload.log` and identify the file behind "Errors: 1".
5. **Home Assistant:** confirm the newest backup exists, its size and age, and that the archive header lists its contents (it's encrypted; the key is Michael's, so stop there and note it).
6. **VMs:** confirm VM XML backups exist for homeassistant and the clerk VMs and that disk images are covered (or say they aren't).
7. **Recovery-time estimate:** from the measured times, estimate a full rebuild onto a new Unraid flash plus restore, in order, with the manual steps Michael would do.

## Part 2: security review (report only, no changes)
Check and rank:
- Every published port: bound to `192.168.1.100` or justified (Authentik `0.0.0.0:9443`, Syncthing, Plex 32400, Minecraft).
- Every tunnel hostname has an Access app and the right policy; `auth.ledgerbook.vip` admin paths return 404; the catch-all is 404 (use the GET-only audit scripts).
- Image tags pinned; for each pinned version, known CVEs or advisories with links (GHSA, vendor advisories, NVD). Say which you couldn't check.
- Containers with `docker.sock`, SSH keys, `/boot` or broad `/mnt/user` mounts, `privileged`, `cap_add`, host networking.
- The clerk-to-root path: who can write which files that root executes (cron jobs, user scripts, stacks scripts). Propose the smallest fix.
- `.env` handling (permissions, git ignore, gitleaks config and a gitleaks run on both repos' history), SSH configuration (keys, allowed users, LAN-only), Unraid UI exposure, Tailscale ACLs and key expiry, Cloudflare account hygiene (API token scopes from the audit files; never print token values).
- Unused things worth removing (e.g. `wg0`), with the exact command for Michael.

## Deliverables
- `DR-DRILL.md` (per-item table with times and results, plus gaps).
- `SECURITY-REVIEW.md` ranked Critical / High / Medium / Low; each item has evidence, a concrete fix, effort (minutes), and risk if left alone.
- Vault note `Projects/Ledger/Files/DR drill and security review 2026-11.md` combining both halves: summary, top 10 fixes in order, what was not tested and why.
- `REPORT.md` and the vault log entry.

## Acceptance
- Every drill item has a measured time and a pass/fail with evidence, or a clear reason it couldn't run.
- No live container, config or share changed (show `git status` of the stacks repo before and after, and `docker ps` before and after).
- Each security finding cites where you saw it (file, command output, or advisory link).

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

**Roster for this project** (lead: `gpt-6.1-sol` · `xhigh`)

| Wave | task_name | Job | Model | Effort | Output |
|---|---|---|---|---|---|
| 1 | `cve-research` | For each pinned image version in the stacks, find advisories (GHSA, vendor, NVD) with links; no ledger access | gpt-6.1-sol | medium | `work/cve-research/cves.md` |
| 1 | `config-review` | Read the stacks repo (compose files, scripts, cron, edge audit JSON) for exposure, mounts, privileges, the clerk-to-root path and .env handling; repo files only | gpt-6.1-sol | high | `work/config-review/findings.md` |
| 1 | `secrets-scan` | Run gitleaks on both repos' history from a local clone; report finding types and locations, never values | gpt-6-luna | medium | `work/secrets-scan/` |
| — (lead) | `drill` | DR drill items 1-7, run sequentially on ledger by the lead only, inside the scratch dir | (lead) | (lead) | `DR-DRILL.md` |
| 2 | `redteam` | Read the drill results and findings; argue what an attacker or a disk failure would actually exploit first; re-rank | gpt-6-astra | high | `work/redteam/` |
| 3 | `review` | Independent review: every finding cited, no live change made (compare the before/after git status and docker ps) | gpt-6-astra | high | `work/review/review.md` |

**No agent gets SSH or runs commands on ledger.** Agents work from repo clones, files the lead copied into `work/`, and the web.

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
