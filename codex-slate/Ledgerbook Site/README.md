# Ledgerbook Site

**Slate rank:** #1 · **Status:** ready for Codex · **Vault project:** Projects/Ledger (subproject) · **Started:** 2026-11-09

## Michael's note (2026-11-09)
> This but go ahead and do it for Ledgerbook, along with the privacy policy. We'll do the same later, I'm thinking Science-Man.com (inside joke).

## What this is
A public front page and privacy policy for Ledgerbook, served from Cloudflare Pages. The site is built so a second brand (Science-Man.com, later) is a config swap, not a rewrite.

## Why a privacy policy matters here
Besides being decent practice for a site that hands out accounts, Google, GitHub and Microsoft OAuth consent screens (Authentik's social sign-in sources) ask for a homepage URL and a privacy-policy URL on a domain you control.

## Facts the build depends on (live check 2026-11-09)
- **Confirmed:** `ledgerbook.vip` (apex) is a tunnel route to `ledgerbook-portal` and sits in Cloudflare Access app "Ledger apps". `home.ledgerbook.vip` serves the same portal.
- **Confirmed:** n8n runs LAN-only at `192.168.1.100:5678`; no tunnel route or DNS record exists for it.
- **Confirmed:** mail for ledgerbook.vip is on Proton (MX `mail.protonmail.ch`, SPF, DKIM, DMARC quarantine).
- **Known limit:** Xfinity Advanced Security flags `.vip` names, so some visitors on Xfinity may be blocked. That is the reason for the separate cover-domain plan.
- **Brand assets:** Server-Work repo `guest-guide/argon-packages/ledgerbook-argon-04-website-theme.zip` and `-05-shared-asset-kit.zip` (leather, brass, vellum).

## Recommended hosting (Michael approves the Cloudflare part)
Public site on the apex `ledgerbook.vip`; "Member login" goes to `home.ledgerbook.vip` (the portal, already live). Moving the apex off the tunnel and out of "Ledger apps" is a Cloudflare change that Michael applies from `DEPLOY.md`.

## Files
- `CODEX-PROMPT.md`: paste into Codex.
- `REPORT.md`: Codex writes this when it finishes or stops.
