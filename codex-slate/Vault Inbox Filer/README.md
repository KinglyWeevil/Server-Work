# Vault Inbox Filer

**Slate rank:** #3 (tied with Concierge Mailbox) · **Status:** ready for Codex · **Vault project:** Projects/Ledger (subproject) · **Started:** 2026-11-09

## Michael's note
Picked with no extra note; ranked #3.

## What this is
A tool that reads the vault's `Inbox/`, works out which project and section each note belongs in, and files it. Anything uncertain stays in `Inbox/` and gets a `[needs Michael]` tag.

## The constraint that shapes the design (checked 2026-11-09)
- **Confirmed:** the Obsidian wrapper `obs` guards `move`, `rename` and `delete`. They exit with code 10 until Michael approves (the `--approved` flag). So a filer can't silently move notes on its own.
- **Design:** two phases. The filer writes a **filing plan** note with one checkbox per move. Michael ticks what he agrees with. A second step moves only the ticked rows. The cron only ever builds plans.

## Files
- `CODEX-PROMPT.md`: paste into Codex (run it on clerk-codex, where `obs` and the vault are).
