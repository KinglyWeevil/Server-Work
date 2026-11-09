# Codex kickoff: Ledgerbook public site + privacy policy · Model: gpt-6.1-sol · Effort: high

> **Start Codex with:** model `gpt-6.1-sol`, reasoning effort `high` (Pages site + Function: mostly integration work with a careful writing piece). Agents use the models in the roster below.

## Context
Ledgerbook is Michael's private home-server service (ledger, a Dell T330 running Unraid in Santa Fe, NM). Friends and family get media, books, notes and a few other apps through Cloudflare Access sign-in. Right now there is no public page: `ledgerbook.vip` goes straight to the signed-in portal. Michael wants a public front page and a privacy policy, built for reuse so a second brand (Science-Man.com) can follow later.

## Goal
A static Cloudflare Pages site with:
1. **Front page:** understated, on-brand (leather, brass, vellum). A one-line description of what Ledgerbook is, a "Member login" button to `https://home.ledgerbook.vip`, and a "Request access" section. Do not list or advertise individual services, ports or Minecraft.
2. **Privacy policy** at `/privacy`: plain English, honest, specific to what this setup really collects.
3. **Request access form (phase 2):** name, email, which services (checkboxes), note. Cloudflare Turnstile. A Pages Function validates Turnstile server-side and forwards to an n8n webhook (details below).
4. **Brand config:** every name, color, font, logo, contact address and policy fact lives in one `brand/<brand>.json` (+ assets folder). Building with `BRAND=ledgerbook` or `BRAND=science-man` swaps the whole site. Ship only the Ledgerbook brand now, plus a stub `science-man.json` that builds with obvious placeholders.

## Read first
- This folder's `README.md` (live facts as of 2026-11-09).
- Server-Work repo (GitHub `KinglyWeevil/server-work`): `guest-guide/argon-packages/PACKAGE-INDEX.md`, then `ledgerbook-argon-04-website-theme.zip` and `ledgerbook-argon-05-shared-asset-kit.zip` for the brand; `guest-guide/ledger-evidence/README.md` for what really exists.
- ledger-stacks repo: `docs/HOW-LEDGER-WORKS.md` (every service, sign-in path and data flow; it is on branch `claude/project-thread-ljw1uc` until PR #3 merges). Use it as the source for the privacy policy's data inventory.

## Constraints
- **No framework.** Plain HTML, CSS and minimal JS; a tiny build script (Node, no dependencies beyond what `npx wrangler` needs) that renders templates from the brand JSON into `dist/`.
- **Fast and accessible:** under 100 KB per page before fonts, WCAG AA contrast, works without JS (form shows a mailto fallback), passes on a phone at 360 px wide, honors dark mode with the brand's dark palette.
- **No trackers, analytics or third-party fonts at runtime** (self-host fonts with their license files). If the brand fonts aren't freely licensed, choose close open-licensed substitutes and say so.
- **Security headers** via `_headers`: a strict CSP that allows Turnstile only, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy` minimal, HSTS.
- **Do not deploy.** Cloudflare changes are Michael's; you write `DEPLOY.md`.

## Privacy policy content (draft every item; mark anything you can't confirm with `[CHECK]`)
Write it for a small private service, not a company. Cover at least:
- Who runs it and how to reach them (placeholder `privacy@ledgerbook.vip` `[CHECK]`; mail is on Proton).
- **What is collected, by path:** Cloudflare (Access sign-in email, IP, country, device and browser data in Access and edge logs; Turnstile), Authentik (account, sign-in history; data received from Google, GitHub or Microsoft when those sign-ins are used), each app's own data (Seerr requests, Audiobookshelf and Kavita reading progress, notes in Obsidian/Syncthing, Minecraft username and IP in server logs, Plex: governed by Plex's own policy), the request-access form, and email.
- **Where it lives:** a home server in the United States; backups to local drives and encrypted offsite copies (Proton Drive). Name processors (Cloudflare, Proton, Plex, the OAuth providers) and link their policies.
- **Retention, access and deletion:** how a member asks for a copy or removal; realistic timelines; what can't be removed (e.g. Cloudflare's own logs).
- **Children, cookies (only the sign-in session cookies and Turnstile), changes to the policy, effective date.**
- A short "plain summary" box at the top.
- A note in `REPORT.md` (not on the page) that this is a draft and not legal advice, plus the items Michael should check.

## Request-access path (phase 2; design it, build it, do not wire live)
n8n is LAN-only. Recommended design, which `DEPLOY.md` explains step by step:
1. A new tunnel hostname, e.g. `hooks.ledgerbook.vip`, with an ingress rule that sends only `^/webhook/request-access$` to `http://192.168.1.100:5678` and everything else to `http_status:404`.
2. That hostname sits behind its own Cloudflare Access app whose only policy is **Service Auth** with one service token. The Pages Function sends `CF-Access-Client-Id` and `CF-Access-Client-Secret` (stored as encrypted Pages env vars), so nothing on the internet can reach n8n without that token.
3. The Pages Function verifies Turnstile (`siteverify`), rate-limits per IP (simple KV or a time-window header check), validates and length-limits fields, then POSTs JSON to the webhook. It returns a friendly result page.
4. Include an importable n8n workflow JSON (`n8n/request-access.json`): webhook → basic validation → notify Michael (email to an address placeholder) → append to a CSV or data table. No auto-replies to the requester in v1.
Note Xfinity's `.vip` filtering as a known limitation in `DEPLOY.md`.

## Hosting change (document for Michael; do not apply)
In `DEPLOY.md`, give two options with a recommendation:
- **Recommended:** public site on the apex `ledgerbook.vip` (Pages custom domain). Steps: remove the apex from Access app "Ledger apps", remove the apex tunnel ingress rule, attach the apex to Pages. `home.ledgerbook.vip` keeps the portal; update the portal's links if any point at the apex. Include the order of operations, a backup step (export the tunnel config and the Access app JSON first) and an undo.
- **Alternative:** public site on `www.ledgerbook.vip`, apex unchanged.
Also list the Authentik follow-up: put the homepage and `/privacy` URLs into the Google, GitHub and Microsoft OAuth app settings.

## Deliverables (all in this folder)
- `site/` source: `brand/ledgerbook.json`, `brand/science-man.json` (stub), `templates/`, `assets/`, `functions/api/request-access.js`, `_headers`, `build.mjs`, `wrangler.toml`.
- `dist/` built output for Ledgerbook (ignored by git if this becomes a repo; keep a copy for review).
- `n8n/request-access.json`.
- `DEPLOY.md`: exact steps, one command or one UI action per step, with the exact Cloudflare dashboard labels or "label not verified".
- `PREVIEW.md`: how to run it locally (`npx wrangler pages dev dist`).
- Screenshots at 1440 px and 390 px of `/` and `/privacy`, light and dark (`screenshots/`).
- `REPORT.md`.

## Steps
1. Read the sources above. Write `PLAN.md` (half a page): page list, brand tokens you extracted, font choice, open questions. Then continue without waiting unless a question blocks you.
2. Build the brand JSON and templates; build the front page and privacy page.
3. Write the privacy policy from the data inventory in `HOW-LEDGER-WORKS.md`, marking every uncertain line `[CHECK]`.
4. Build the Pages Function and n8n workflow with tests for the function (Turnstile failure, missing fields, oversize fields, happy path with a mocked fetch).
5. Accessibility and size check (axe or pa11y if available; otherwise a manual checklist) and screenshots.
6. Write `DEPLOY.md`, `PREVIEW.md`, `REPORT.md`, and the vault log entry.

## Acceptance
- `node build.mjs` with `BRAND=ledgerbook` and `BRAND=science-man` both succeed; no Ledgerbook strings appear in the Science-Man build.
- Pages render well at 360 px and 1440 px, light and dark; AA contrast passes.
- Function tests pass; no secret values anywhere in the folder.
- The privacy policy names every data path in the Facts section and links every processor's policy.
- `DEPLOY.md` can be followed by someone who has never used Pages.

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
| 1 | `brand-extract` | Unzip and read the Argon website-theme and asset-kit packages; extract color, type and spacing tokens and the logo files | gpt-6-luna | medium | `work/brand-extract/tokens.json`, notes |
| 1 | `data-inventory` | From HOW-LEDGER-WORKS.md, list every path where personal data is collected, stored, backed up or shared, with source lines | gpt-6.1-sol | medium | `work/data-inventory/inventory.md` |
| 1 | `turnstile-function` | Pages Function + tests for request-access (Turnstile verify, validation, rate limit, service-token forward), mocked fetch | gpt-6.1-terra | medium | `work/turnstile-function/` |
| 2 | `privacy-draft` | Write the privacy policy from the inventory, plain English, `[CHECK]` on every uncertain line, processor links | gpt-6-astra | high | `work/privacy-draft/privacy.md` |
| 2 | `n8n-workflow` | Importable n8n request-access workflow JSON with placeholder credentials | gpt-6-luna | medium | `work/n8n-workflow/request-access.json` |
| 3 | `a11y-check` | Build both brands, then run the accessibility, size, contrast and screenshot checks at 360/1440 px, light and dark | gpt-6-luna | medium | `work/a11y-check/` |
| 3 | `review` | Independent review against Acceptance; check that DEPLOY.md can be followed cold | gpt-6-astra | high | `work/review/review.md` |

The lead builds templates, `build.mjs` and `DEPLOY.md` itself, between waves 1 and 3.

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
