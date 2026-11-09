# Media Library Audit

**Slate rank:** unranked (picked, no note) · **Status:** ready for Codex · **Vault project:** Projects/Ledger (subproject) · **Started:** 2026-11-09

## What this is
A read-only report on the media library: mismatches, duplicates, missing subtitles, low-resolution files, HEVC conversion candidates and unmonitored items. It changes nothing.

## Facts (checked 2026-11-09)
- **Confirmed:** Radarr 6.4.4 (`192.168.1.100:7878`), Sonarr 4.0.20 (`:8989`), Bazarr 1.6.2 (`:6767`), Lidarr 3.1.0 (`:8686`), Plex 1.43.4 (`:32400`) and Tdarr 3.01 (`:8265`, transcodes with the desktop's 4090) are running on the default Docker bridge.
- **Confirmed:** Tdarr already keeps reports in stacks `tdarr/reports/` (e.g. a seeding-quarantine list), so the audit must not suggest converting files that are still seeding.
- Michael's library rules (English subs, quality targets, Plex Pass for Bunny and Caleb) are in vault notes for the media stack.
