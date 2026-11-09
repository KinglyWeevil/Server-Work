# Codex kickoff: media library auditor (read-only)

## Context
Michael's media stack on ledger: Radarr, Sonarr, Bazarr, Lidarr, Plex, qBittorrent behind gluetun, and Tdarr for HEVC conversion using the desktop's RTX 4090. He wants a report he can act on, not automatic changes.

## Read first
- ledger-stacks `docs/HOW-LEDGER-WORKS.md` (branch `claude/project-thread-ljw1uc` until PR #3 merges), stacks `media/`, `streaming/`, `tdarr/` (including `tdarr/reports/`), and the Recyclarr config for the quality profiles.
- Vault notes on the media stack decisions (`Projects/Ledger/Decisions.md` and any media notes it links).

## Goal
`scripts/library-audit.py` (Python 3, standard library + `requests` only; run it from a clerk or the desktop, since ledger has no python3) that calls **read-only** API endpoints and writes a vault note `Projects/Ledger/Files/Library audit YYYY-MM-DD.md`.

## Report sections (each a table, plus a count)
1. **Title/year vs folder name mismatches** (Radarr and Sonarr paths vs metadata).
2. **Duplicate movies** (same TMDB/IMDb id, or the same title and year in two paths).
3. **Missing English subtitles** (Bazarr wanted lists, plus files with no embedded or external English track).
4. **Below 1080p** files where a better release is likely available (profile cutoff not met).
5. **HEVC conversion candidates** (H.264 files above a size threshold), with estimated savings per file and total, **excluding** anything still seeding (check qBittorrent read-only and Tdarr's seeding-quarantine report).
6. **Unmonitored or missing items** (monitored but no file; files on disk not in Radarr/Sonarr).
7. **Plex vs arr drift** (in Plex but not in the arr apps, or the reverse; Plex library section counts).
8. **Short action list:** the top 10 actions, each with how Michael does it in the app's UI (exact labels or "label not verified").

## Constraints
- **GET requests only.** The script refuses to run any other HTTP method (enforce it in code and test it).
- API keys come from environment variables or a local untracked config file that Michael fills in; never print them, never commit them, never read them from the stacks `.env` files.
- Respect rate limits; cache responses in a scratch folder so a rerun doesn't hammer the apps.
- No file system writes on ledger; read file info through the APIs, not by walking `/mnt/user`.

## Deliverables
- `scripts/library-audit.py`, `config.example.toml`, `tests/` (fixture JSON for each API; tests for each section and for the GET-only guard).
- The first real report in the vault (after Michael fills in the keys), or a fixture-based sample report if keys aren't available yet.
- `README.md` usage section, `REPORT.md`, and the vault log entry.

## Acceptance
- Tests pass; the GET-only guard is tested.
- The report's counts match a manual spot-check of 5 items per section.
- No secrets anywhere in the folder.

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
