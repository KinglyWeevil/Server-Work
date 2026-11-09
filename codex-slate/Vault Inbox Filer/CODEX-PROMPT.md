# Codex kickoff: Vault Inbox filer (plan, approve, then file) · Model: gpt-6.1-sol · Effort: high

> **Start Codex with:** model `gpt-6.1-sol`, reasoning effort `high` (safety-critical file moves; correctness over speed). Agents use the models in the roster below.

## Context
Michael's Obsidian vault (`/mnt/user/data/notes/vault` on ledger, git-tracked, Syncthing to PCs and phone) has an `Inbox/` where chats and quick notes land, often as "Vault entry" blocks (project, thread, date, status, Summary, Decisions, Actions, Open items). Each project has `Projects/<P>/{README.md, Status.md, Decisions.md, Log/, Threads/, Files/}`. The rules are in `_System/Assistant Rules.md`.

Run on **clerk-codex** (`/workspace/...`), which has the `obs` wrapper. `obs` allows read, search, create and append; `move`, `rename`, `delete`, `overwrite` and `eval` exit 10 ("Not run. Ask Michael") unless called with `--approved`.

## Goal
1. `filer plan`: read every note in `Inbox/`, decide its destination, and write one **filing plan** note.
2. Michael ticks the rows he approves in that note.
3. `filer apply <plan>`: perform exactly the ticked rows, using `obs move --approved` (his ticks are the approval), append the Log entries, and mark the plan done.
4. A 30-minute cron on clerk-codex that runs **only `filer plan`** (never `apply`), and only writes a new plan when the Inbox changed.

## Read first
- `_System/Assistant Rules.md` (the filing rules are the spec), `_System/Templates/`, a sample of 5 notes from `Inbox/` and 3 projects' folders to learn the real shapes.
- The `obs` wrapper source and the guard (`_rules/hooks/guard.sh`, `_rules/bin/obs`) so you call it correctly. **Do not modify the guard or obs.**

## Decision rules (write them into `RULES.md` and follow them)
- Map to a project by: explicit `project:` field or "Vault entry" block → thread title match against `Projects/*/Threads/` → keywords from each project's README. If two projects score close, it's uncertain.
- Map to a section: Decisions (decision language, "picked", "chose"), `Log/` (dated work done), `Threads/` (thread summaries), `Files/` (reference material, long docs), otherwise uncertain.
- A note that contains several of these is **split**: create the pieces by append/create (allowed), and leave the original in Inbox for a ticked move to `Inbox/_filed/`.
- Uncertain: leave in place, append ` [needs Michael]` to the title line via `obs append` (no rename), and list it in the plan with your best guess.
- Never overwrite an existing note; on a name clash, append ` (2)` and flag it.

## Plan note format
`Inbox/_plans/Filing plan YYYY-MM-DD HHmm.md` with frontmatter `type: filing-plan`, `status: pending`, and a table or list per note: `- [ ] <note> → <destination> (confidence %, reason)`. Uncertain notes go in a separate "Needs Michael" list with no checkbox. Put a one-line summary at the top (N notes, N proposed moves, N uncertain).

## Apply step
- Re-read the plan; act only on `- [x]` rows; skip any row whose source changed since the plan (compare mtime or hash recorded in the plan).
- For each move: `obs move --approved`, then append a Log entry in the destination project (`Log/YYYY-MM-DD.md`, one line per note) per Assistant Rules.
- Mark the plan `status: applied` with a results section; commit the vault (`git add` only the touched paths; message `Inbox filer: apply <plan name>`).

## Deliverables
- `filer` (Python 3 or bash; clerk-codex has python3; ledger does not) with `plan`, `apply`, `--dry-run`, and `--inbox`/`--vault` flags for testing.
- `tests/` with a fixture vault (copy of the structure with fake notes) covering: clear match, split note, uncertain, name clash, changed-since-plan, unticked rows ignored.
- `RULES.md`, `INSTALL.md` (cron line for clerk-codex that Michael pastes, with `flock`, and log rotation), `REPORT.md`.

## Steps
1. Read the sources; write `RULES.md`.
2. Build `plan` against the fixture vault; then run it read-only against the real Inbox and show Michael the plan (do not apply).
3. Build `apply` and test it on the fixture vault only.
4. Write `INSTALL.md` with the cron line; do not install it yourself unless Michael says so in this session.

## Acceptance
- On the real vault, `plan` writes one plan note and changes nothing else.
- All fixture tests pass; `apply` never touches an unticked row; no `--approved` call happens outside `apply`.

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

**Roster for this project** (lead: `gpt-6.1-sol` · `high`)

| Wave | task_name | Job | Model | Effort | Output |
|---|---|---|---|---|---|
| 1 | `rules-spec` | Turn _System/Assistant Rules.md + 5 sample Inbox notes into RULES.md decision rules | gpt-6.1-sol | medium | `work/rules-spec/RULES.md` |
| 1 | `obs-contract` | Read the obs wrapper and guard; document exact calls, exit codes and what `--approved` permits | gpt-6-luna | medium | `work/obs-contract/obs.md` |
| 1 | `fixture-vault` | Build the fixture vault and the test cases (clear, split, uncertain, clash, changed-since-plan, unticked) | gpt-6.1-terra | medium | `work/fixture-vault/` |
| 2 | `adversary` | Try to make `apply` act on an unticked row, a changed note or a wrong path; write failing tests for anything it finds | gpt-6-astra | high | `work/adversary/` |
| 3 | `review` | Independent review against Acceptance | gpt-6.1-sol | high | `work/review/review.md` |

The lead writes `filer` itself. Only the lead runs it against the real vault, and only `plan`.

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
