# Codex kickoff: PRISM, recommendations toward its own independent visualizer graphics

## Context
PRISM is Michael's music visualizer project (Windows; desktop is the only source and git writer at `C:\Users\Michael\Ledger\projects\PRISM`). W05 ("musical states with restrained transitions") was reviewed and the time-base and loudness fixes are done. Michael's goal now: PRISM creates **independent visualizer graphics of its own**. He wants recommendations, not code.

## Read first (all of it, then summarize what you learned in 10 bullets at the top of your report)
- Vault `Projects/PRISM/`: `README.md`, `Status.md`, `Decisions.md` (especially the 2026-11-07 decisions on independent scenes, Chrysalis and Thornstorm, and the shareable-licenses-only rule for external libraries), the newest `Log/` entries, `Files/` (including `W05 adversarial review - Claude 2026-10-31.md` and whatever records the fixes), and `Files/Handoff Prompts/`.
- The repo: the window plan docs (W05 to W26, especially the camera, palette and geometry windows W07/W08), the current renderer and how musical states drive it, and any existing scene code for Chrysalis or Thornstorm.

## Deliverable: `RECOMMENDATIONS.md` in this folder
1. **Where PRISM is today:** what draws the pixels now, what it depends on, and what "independent" would change. Confirm or correct the reading in `README.md`.
2. **Target architecture for native scenes:** a scene interface (inputs: musical state, features, beat/onset events, time; outputs: draw calls), scene lifecycle and transitions driven by the director, a parameter and palette system, and how presets are stored. One Mermaid diagram.
3. **Rendering technology options** with a recommendation: e.g. Direct3D 11/12, Vulkan, OpenGL, WebGPU (wgpu/Dawn), or staying with whatever the repo already uses. Compare on Windows support, shader tooling, performance at 120 fps and 4K, team familiarity (Codex-written code), debugging, and license (shareable licenses only; list each candidate library's license).
4. **Feature-to-visual mapping:** how the existing features (loudness with adaptive floor, spectral bands, onsets, tempo, stereo width, musical states) should drive geometry, motion, color and camera, with the W05 lessons (don't map raw loudness straight to intensity; states must change the picture, not just a label).
5. **Chrysalis and Thornstorm as first native scenes:** what each needs, a minimal first version, and what makes it "done".
6. **Quality and testing:** golden-frame tests, deterministic rendering from recorded feature streams, performance budgets per frame at 60/120 fps, fixture music (including mastered-loud tracks), and how to review visuals without watching hours of output.
7. **Roadmap:** proposed windows (or changes to the existing W06+ plan) with exit criteria and rough effort; call out anything in the current plan that's ordered wrong.
8. **Risks and open questions** for Michael, as multiple choice with your recommendation marked.

## Constraints
- **Read-only:** no commits, branches or file changes in the PRISM repo. If a 1-hour spike would settle a technology question, describe it precisely and ask; don't run it.
- Every claim about the codebase cites file paths and line numbers; every claim about a library cites its docs and license.

## Acceptance
- Michael can pick a rendering direction and the first native scene from the report's questions in one sitting.
- The roadmap fits into the existing window plan, or says exactly what to change.

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
