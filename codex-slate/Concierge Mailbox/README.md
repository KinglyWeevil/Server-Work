# Concierge Mailbox

**Slate rank:** #3 (tied with Vault Inbox Filer) · **Status:** ready for Codex (design first, then build) · **Vault project:** Projects/Ledger (subproject) · **Started:** 2026-11-09

## Michael's note (2026-11-09)
> Should be tied for #3.

## What this is
An assistant for `concierge@ledgerbook.vip`. Mail comes in, gets sorted, and a reply is drafted. Michael approves, edits or rejects each draft, and nothing is sent without his approval.

## Facts (checked 2026-11-09)
- **Confirmed:** ledgerbook.vip mail is on Proton (MX, SPF, DKIM, DMARC quarantine).
- **Confirmed:** n8n 2.45.6 runs LAN-only at `192.168.1.100:5678` (no tunnel route, no DNS name).
- **Confirmed:** no ntfy container and no Proton Bridge exist yet.
- **Not confirmed:** whether `concierge@` exists yet, and on which Proton account. The plan is a separate assistant account, so Michael's own mailbox credentials never sit in n8n.

## Phases
1. **Design** (`DESIGN.md`), then stop for Michael's OK.
2. **Build and test** against a mock IMAP/SMTP server.
3. **Go-live steps** that Michael runs himself.
