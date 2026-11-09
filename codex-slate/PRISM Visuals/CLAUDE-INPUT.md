# Claude's input: how PRISM gets visuals of its own

Written 2026-11-09 for Michael, at his request, and as input for the Codex recommendations report. It's based on a read-only pass over the PRISM repo (branch `codex/graphics-math-modules` @ 4017ff4) and vault `Projects/PRISM` (Decisions #40, #58-#78, the Status of 2026-11-07, and the W05-W06 reviews).

## Short answer
The problem isn't the shader math or the graphics API. It's that scenes barely hear the music, and nothing in them develops over time. Fix the **music-to-picture contract** first, add a **feedback pass** and one **evolving simulation layer**, and build scenes from **seeded building blocks** that the director chooses by musical structure. Keep WebGL2 until that looks right; WebGPU (W13-W15) is a later speed-up, not the cure.

## What the code says today (Confirmed, repo read 2026-11-09)
- Every pixel is drawn in the browser (plain JS + WebGL2). Butterchurn (MilkDrop) is the default renderer and a **hard startup requirement** (`app.js:150`). PRISM's own presets are MilkDrop scripts.
- PRISM's own host (`visualizers/shared/graphics.js`, contract v1) already exists: a WebGL2 context per scene, a fixed 120 Hz step, and a fullscreen-triangle shader. It has four original scenes (Chrysalis, Thornstorm, quasicrystal, Gray-Scott ink), about 570 lines in total including the director.
- **A scene receives only** `dt, time, low, mid, high, attack`, each multiplied by `gentle = 0.25`, plus a few director channels (`width, brightness, rotation, camera, surface, intensity, travel, morph`). `palette` and `geometry` are **null** (unbound until W07/W08).
- Your rejection (#70) and quality bar (#72): visible musical reaction, visual complexity, intriguing development worth revisiting. Hidden mathematical complexity doesn't count.

## Recommendations, in order

### 1. Make scenes hear structure, not just loudness (biggest win)
- **Events, not levels.** People see sync in *events*: onsets, downbeats, section changes, drops, motif returns. Give scenes an event stream with typed **gestures** (pulse, burst, fold, cut, recall), each with its own envelope (fast attack, springy decay). Continuous band levels should only shade things.
- **Land on the beat, not after it.** Use the tempo phase the director already tracks to start motion slightly early, so it peaks *on* the beat. Measure the audio→WebSocket→frame latency once and subtract it. Visuals that trail by 60-100 ms read as "not connected" even when they technically react.
- **Three timescales, every parameter assigned to exactly one:**

| Timescale | Length | Drives |
|---|---|---|
| Beat | under 0.5 s | pulses, spikes, flashes, particle bursts |
| Phrase | 4-16 bars | camera paths, morph targets, feedback zoom/rotation |
| Section | 30-90 s | palette, geometry family, simulation regime |

  This is what turns "small changes of brightness, scale, rotation" into a journey.
- **Revisit `gentle = 0.25`.** Scaling every input to a quarter is a likely reason reactions look timid (**Presumed**; check it with the test in step 5). Prefer per-gesture gain with headroom over a blanket damping factor.
- **Bind palette and geometry now** (pull W07/W08 forward), keyed to sections and motifs, so a chorus coming back returns to a remembered form and colour.

### 2. Add a feedback pass (PRISM's own, no license questions)
Much of why Butterchurn looks rich and the originals look thin ("thin wire loops, sparse blobs") is MilkDrop's **frame feedback**: each frame warps, zooms, rotates and fades the previous one, so marks smear into trails, tunnels and blooms. Write PRISM's own version: a ping-pong framebuffer, a warp field driven by the director (zoom and rotation on the phrase timescale, warp intensity on the beat), and decay tied to section energy. It's a few hundred lines, multiplies the visual complexity of every scene, and is the single cleanest step toward retiring Butterchurn.

### 3. Add one evolving simulation layer (this is the "development worth revisiting")
Static formulas react, but they don't *develop*. Simulations do. Each runs on the GPU in WebGL2 and is written from a published method, so the license is clean (#40):
- **Physarum / slime-mould agents** (Jones, 2010): millions of agents leaving trails. Music sets sensor angle, speed and deposit, and sections change the regime. Striking, organic, and never the same twice. **My first pick.**
- **Curl-noise particle fields** (Bridson et al., 2007): fluid-looking motion. Attacks inject energy; the palette follows the section.
- **Lenia** (Chan, 2019; already #61): continuous cellular life. Better as a slow section-scale layer than a beat layer.
- **Gray-Scott** (already living-ink): good as a texture fed through the feedback pass rather than a scene on its own.
- **Spectre tiling** (Smith et al., 2023; #61): beautiful as geometry for a "family", not as motion.

### 4. Generate scenes from seeded building blocks
Scene = **form** (shells, spikes, attractor, tiling) × **field** (Julia, domain warp, simulation) × **palette** × **motion grammar** (which gestures on which timescale), all from one seed (W07). The director picks and morphs between combinations by musical event: a section change brings a new form family, and a motif return recalls its seed. That's endless "graphics of its own" without hand-authoring each idea. Polish **Chrysalis first** to excellence (you already called it better), then make it the first family in this system.

### 5. Test the music-to-picture link, not just stills
Today there are stills and frozen-morphology checks, but no measure of musical connection. Render offline from **recorded feature streams** (deterministic replay already exists) and measure:
- change energy (frame difference) correlated with onset strength (it should be high);
- visual distance across section boundaries (it should jump), and calm on calm passages (low motion);
- a complexity proxy, e.g. spatial-frequency entropy or PNG compression ratio, to catch "sparse blobs".

Then review as **side-by-side 30-second clips** of five fixed excerpts against the current best reference, instead of watching live for hours.

### 6. Retire Butterchurn as a requirement
Make it an optional "Classic" module, removable like LYGIA, with the original host as the default. Do this after step 2, so the default still looks rich on day one.

## Choice: what to build first

| Option | Musical connection | Richness | Effort | License risk |
|---|---|---|---|---|
| **A. Contract (1) + feedback (2) on Chrysalis, then physarum (3)** (recommended) | High | High | Medium | None (own code) |
| B. More hand-written scenes | Low until (1) is done | Medium | Medium per scene | Low |
| C. WebGPU first (W13 early) | Unchanged | Unchanged until art changes | High | Low |
| D. Lean on ISF/Shadertoy ports | Low | High | Low | **High**: many Shadertoy shaders are CC BY-NC-SA or unlicensed |

A beats B because B repeats the rejected pattern (#70), and it beats C because the API isn't the bottleneck. D conflicts with #40 and #58.

## Radical alternative (worth knowing, not recommended now)
**A real-time diffusion layer.** On the 4090, few-step image models (SD-Turbo class via StreamDiffusion) can repaint a low-resolution feedback frame tens of times per second, steered by the palette and a prompt per section. The look is genuinely new. Costs: latency, frame-to-frame flicker, a Python sidecar beside the browser app, and model-weight licenses that are often non-commercial (fine for personal use under the #63-style rule, but check again before any release). It's a later experiment, after A.

## Labels
Repository facts above are **Confirmed** from the read-only pass (file paths cited). The `gentle = 0.25` cause is **Presumed**. Paper references are to the original publications; implementations must be written from the methods, not copied.
