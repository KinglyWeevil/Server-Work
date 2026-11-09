# Codex kickoff: Garage templates (templates first, no full build) · Model: gpt-6.1-sol · Effort: medium

> **Start Codex with:** model `gpt-6.1-sol`, reasoning effort `medium` (templates and forms: clear, mostly mechanical work). Agents use the models in the roster below.

## Context
Michael keeps vehicle notes in an Obsidian vault (Obsidian 1.14 desktop and phone, synced by Syncthing; core Templates plugin; check whether Templater is installed and don't depend on it unless it is). Two vehicles today:
- **2017 Honda Civic Si**, 1.5 L turbo L15B7, OBD-II (vault `Projects/Garage/Civic.md`).
- **1995 Jeep Wrangler YJ**, 2.5 L I4 (AMC 150), Bunny's Jeep, pre-OBD-II (vault `Projects/Bunnys Jeep/Jeep YJ.md`).
More vehicles may come, so nothing may hard-code these two.

Michael wants **templates first**: record-keeping and diagnostic forms he can start using this week. Do not research specs, build reminders, or plan a larger system.

## Read first
- Vault `_System/Assistant Rules.md`, `_System/Templates/` (match their style and frontmatter conventions), `Projects/Garage/README.md`, `Status.md`, `Civic.md`, and `Projects/Bunnys Jeep/Jeep YJ.md`.
- Note the vault's confidence-label rule: **Confirmed / Presumed / Not confirmed / Discrepancy**, each with a source.

## Deliverables (draft in this folder; install into the vault only after Michael says yes)

### A. Obsidian templates (`templates/`), each with YAML properties so they can be filtered and listed
1. **Vehicle profile:** properties `type: vehicle`, `vehicle` (short id, e.g. `civic-si`), year, make, model, trim, engine, transmission, drivetrain, VIN (last 8 only by default, with a note on why), plate (optional), purchase date, odometer + odometer date, owner/driver, tire size, oil spec placeholder. Then sections: Specs (empty table with columns Item | Value | Units | Confidence | Source), Known issues, Mods, Links, and **Custom entries**.
2. **Custom entries, done properly:** a documented pattern for adding any field Michael wants without editing the template: (a) a `custom:` property list of `key: value` pairs, and (b) a "Custom entries" table (Field | Value | Units | Date | Confidence | Source | Notes). Explain both in a short `templates/HOW-TO-CUSTOM-ENTRIES.md` and pick one as the default with a reason.
3. **Diagnostic record** (the most important one): properties `type: diagnostic`, `vehicle`, `date`, `odometer`, `status` (open / monitoring / fixed / abandoned), `system` (engine, cooling, fuel, ignition, charging, brakes, suspension, steering, driveline, electrical, HVAC, body, other), `severity`, `cost_total`. Sections:
   - Complaint (in the driver's own words), when it started, how often.
   - **Conditions:** cold/warm, ambient temperature, speed, load, gear, weather, and **altitude** (Santa Fe is about 7,000 ft; it matters for fuel trims and boost).
   - **Codes:** table Code | Status (pending/confirmed/permanent, or flash code for the YJ) | Description | Freeze-frame notes | Cleared? For the YJ, a short note on reading codes by key cycling, marked **Presumed** until verified from a source.
   - **Live data:** table PID/Measurement | Value | Units | Spec | Spec source | Conditions.
   - **Tests performed:** table Test | Tool | Result | Spec | Pass/Fail | Notes.
   - Hypotheses ranked (cause, evidence for, evidence against, next test).
   - Root cause, fix, parts used (link to parts records), labor time, verification drive, follow-up date, photos/attachments.
4. **Service record:** routine maintenance (oil, filters, fluids, tires, brakes): date, odometer, work done, parts and fluids (spec + brand + quantity), torque values used (ft-lb with N·m), who did it, cost, next due (miles/date).
5. **Parts record:** part name, OEM part number, aftermarket number, brand, store, price, pack size, warranty, date bought, installed on (link), substitute options.
6. **Fuel / trip log entry** (optional, small): date, odometer, gallons, price, station, notes.

### B. Views
- An Obsidian **Bases** file (`templates/Garage.base`, Obsidian 1.9+ core feature; confirm the installed version supports it) with views: Open diagnostics by vehicle; Service history by vehicle; Parts by vehicle. If Bases isn't available, provide an equivalent Dataview query only if Dataview is installed; otherwise skip and say so.

### C. Printable forms (`forms/`)
- One-page **Diagnostic worksheet** and **Service record** as HTML with print CSS (US Letter, 0.5 in margins, black ink, readable at arm's length, checkboxes and write-in lines), plus a blank **Codes and readings** sheet. Each prints cleanly to PDF from a browser; include the PDFs too.
- Keep the fields identical to the Obsidian templates so a paper sheet can be typed in later without guessing.

### D. Examples (`examples/`)
- One filled-in example per template, clearly marked **EXAMPLE, fictional values**, so Michael sees how it reads. Use plausible but obviously sample data. Do not put real specs in them.

### E. Install plan (`INSTALL.md`)
- Where each file goes in the vault (recommend `_System/Templates/Garage/` for templates, `Projects/Garage/Forms/` for printables, `Projects/Garage/Garage.base`), and how the YJ in `Projects/Bunnys Jeep/` is included in views (by `vehicle` property, not folder).
- How to add a new vehicle in under a minute.

## Constraints
- Templates must work with the **core Templates plugin** (`{{date}}`, `{{title}}`); do not rely on Templater syntax unless it is installed.
- Property names in lower_snake_case, consistent across all templates.
- Units: miles, gallons, °F, psi for the YJ and general use; torque ft-lb (N·m); metric fastener sizes on the Civic, SAE on the YJ. Each units choice appears as a property or column header so it is never ambiguous.
- No spec values are filled in anywhere except the fictional examples.
- Do not edit existing vault notes. Install only after Michael approves (ask in `REPORT.md`).

## Acceptance
- Creating a note from each template in Obsidian gives valid properties (no YAML errors) and readable sections.
- The Bases views list the examples correctly by vehicle.
- Printed forms fit on one page each and match the template fields.
- A new vehicle can be added without changing any template.

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

**Roster for this project** (lead: `gpt-6.1-sol` · `medium`)

| Wave | task_name | Job | Model | Effort | Output |
|---|---|---|---|---|---|
| 1 | `vault-conventions` | Read _System/Templates, Assistant Rules and the Garage/YJ notes; report the property conventions and whether Templater, Bases and Dataview are present | gpt-6-luna | low | `work/vault-conventions/conventions.md` |
| 2 | `md-templates` | Vehicle, diagnostic, service, parts, fuel and custom-entry templates plus HOW-TO-CUSTOM-ENTRIES.md | gpt-6-luna | medium | `work/md-templates/` |
| 2 | `print-forms` | Printable HTML + PDF diagnostic worksheet, service record and codes sheet, with fields identical to the templates | gpt-6-luna | medium | `work/print-forms/` |
| 3 | `views-examples` | Garage.base views and one fictional example per template | gpt-6-luna | medium | `work/views-examples/` |
| 3 | `review` | Check that template fields match the forms, that the YAML is valid, and that adding a new vehicle needs no template change | gpt-6.1-sol | high | `work/review/review.md` |

Wave 2 starts only after the lead fixes the shared property list from wave 1, so both wave-2 agents use the same field names.

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
