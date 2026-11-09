# Ledger Pocket

**Slate rank:** unranked, wanted ("Absolutely") · **Status:** planning only · **Vault project:** Projects/Ledger (subproject) · **Started:** 2026-11-09

## Michael's note (2026-11-09)
> Absolutely but this needs more detailed planning and deployment.

## What this is
An Android app to manage ledger, and later other parts of life. **This phase produces the plan and the deployment design only; no app code.** The build starts after Michael approves the plan.

## Facts that shape the plan (checked 2026-11-09)
- **Confirmed:** Michael's phone is a Galaxy S23 Ultra on Tailscale (100.101.9.35). Ledger's Tailscale has **no subnet routes**, and most apps bind to `192.168.1.100` only, so over Tailscale the phone reaches only what's served on ledger's Tailscale address (HA via Serve on tcp 8123, Authentik 9443).
- **Confirmed:** away from home, apps are reached through Cloudflare Access. The phone already can't do Access's email-code login inside an app (that's why HA uses Tailscale). Service tokens or a Tailscale route are the realistic paths.
- **Confirmed:** Uptime Kuma and n8n have no public hostname; UpSnap, qBittorrent, Radarr, Sonarr and Seerr do (behind Access).
- Brand: Ledgerbook leather, brass and vellum (Server-Work repo argon packages).
