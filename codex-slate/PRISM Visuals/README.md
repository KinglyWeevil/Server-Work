# PRISM Visuals

**Slate rank:** unranked · **Status:** ready for Codex (recommendations only) · **Vault project:** Projects/PRISM · **Started:** 2026-11-09

## Michael's note (2026-11-09)
> Already fixed, you can review the notes in the vault. You could probably make some recommendations toward my goal for it to create independent visualizer graphics of its own though.

## What this is
The W05 time-base and loudness fixes are already done, so that kickoff is retired. This project is a **recommendations report** on how PRISM gets to generating its own visualizer graphics, independent of anything it currently leans on. No code changes.

## Facts (checked 2026-11-09)
- **Confirmed:** the desktop is PRISM's only source and git writer (`C:\Users\Michael\Ledger\projects\PRISM`); builds and tests are Windows scripts.
- **Confirmed:** handoff prompts live in vault `Projects/PRISM/Files/Handoff Prompts/`. The 2026-11-07 decisions cover independent scenes (Chrysalis, Thornstorm) and a licensing rule for external libraries: shareable licenses only.
- **What "independent" means (Confirmed, vault thread summary 2026-10-30):** Michael asked about "creating visualizer graphics from independent mathematical ideas or post-early-2010s advances, and about libraries outside those already acquired". In practice that means PRISM drawing its own scenes instead of the default Butterchurn (MilkDrop) engine.
- **Confirmed:** Michael rejected the first original scenes for both appearance and their connection to the music (#70). The bar (#72) is visible musical reaction, visual complexity, and development worth revisiting.

## Files
- `CODEX-PROMPT.md`: paste into Codex.
- `CLAUDE-INPUT.md`: Claude's recommendations (2026-11-09), which Codex tests against the code.
