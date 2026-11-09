# Garage

**Slate rank:** #2 · **Status:** ready for Codex (templates only) · **Vault project:** Projects/Garage (folder name maps automatically) · **Started:** 2026-11-09

## Michael's note (2026-11-09)
> Yes, and add custom entries, and diagnostic record keeping forms or form templates. Don't plan the full build yet, I want templates first.

## Scope now
Templates only: vehicle profile with custom entries, diagnostic record, service record, parts record, a generic custom entry, plus printable forms for the garage. **Not now:** spec research (fluids, torque tables, part numbers), Home Assistant reminders, or any full build plan.

## Facts (checked 2026-11-09)
- **Confirmed:** vault `Projects/Garage/` has `README.md`, `Civic.md`, `Status.md`. The YJ note is `Projects/Bunnys Jeep/Jeep YJ.md` (it is Bunny's Jeep).
- **Confirmed:** vault rule there: each fact gets a confidence label and a source.
- **Confirmed:** vault templates live in `_System/Templates/` (Project README/Status/Decisions, Thread Summary, Vault entry).
- **Units:** torque in ft-lb with N·m in parentheses; the YJ is SAE (inch sizes), the Civic metric.
- **Vehicles:** 2017 Honda Civic Si (1.5 L turbo L15B7, OBD-II); 1995 Jeep Wrangler YJ (2.5 L I4, AMC 150; pre-OBD-II, codes via key cycling: **Presumed**, verify).

## Files
- `CODEX-PROMPT.md`: paste into Codex.
- `templates/` and `forms/`: Codex drafts here first; they go into the vault only after Michael approves.
