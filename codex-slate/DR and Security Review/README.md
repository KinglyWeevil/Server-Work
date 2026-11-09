# DR and Security Review

**Slate rank:** #4 · **Status:** ready for Codex · **Vault project:** Projects/Ledger (subproject) · **Started:** 2026-11-09

## Michael's notes (2026-11-09)
> dr: Add as #4. · audit: Combine with disaster recovery.

## What this is
One project, two halves:
1. **Disaster-recovery drill:** prove the backups actually restore, in a scratch area, and time each step.
2. **Security review:** a report on ledger's attack surface. Report only, no fixes.

Both end in one vault note with a ranked fix list.

## Facts the drill must account for (checked 2026-11-09)
- **Confirmed:** the Aegis (`/mnt/disks/Fortress_L3/ledger-backups/appdata`) holds only `ab_20261108_050004-failed`. An exclude fix went in at 09:45Z, and the 2026-11-10 05:00 run is the first real test. The older 181 GB set in `/mnt/user/backups/appdata` is **Presumed** to be the newest good local set.
- **Confirmed:** Authentik pg_dump runs nightly at 03:15 (keep 7); HA makes native encrypted backups at 04:30 (keep 7; the key is Michael's); Proton offsite copy runs at 01:00 (tiers 0, 1, 3, 4 monthly appdata, 5, and new tier 6 for HA backups and photos); configs go to GitHub at 03:50.
- **Confirmed:** Authentik publishes `0.0.0.0:9443` (all interfaces). An unused Docker network `wg0` exists. The Proton upload log shows "Errors: 1" on every tick of the 2026-11-09 run.
- **Flagged earlier:** clerks can write `/mnt/user/appdata/stacks`, which root cron jobs execute (a clerk-to-root path).
- **Pending elsewhere:** splitting the "Ledger admin" Access app (P1) waits on Michael's pick. Don't duplicate that work; note how it changes the findings.
