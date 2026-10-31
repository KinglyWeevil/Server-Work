"""Shared authoritative evidence for every standalone package."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
NOTICE='''# Current instruction — existing Ledgerbook branding only

Use the existing leather, brass and vellum Ledgerbook Full branding and LB mark in ledger-evidence/. Paper/green colors in guide.html, starter assets, old prompts and reference renders are obsolete draft styling. Preserve the guide's content/personalization contract while adapting its appearance to the real branding. This instruction supersedes conflicting historical art-direction language in this package.

Read ledger-evidence/README.md, containers.json and asset-manifest.json before designing. Existing assets and theme examples are real source references, not proof that every application supports arbitrary CSS. Private Notes is Obsidian. Requests is Seerr in the container named jellyseerr. Image references are inventory evidence, not independent app-version measurements. Do not deploy, change auth, expand guest access, expose private notes or fabricate screenshots/DNS values. Treat unverified integration as a proposal.

'''
def evidence_files():
    return {'ledger-evidence/'+p.relative_to(ROOT/'ledger-evidence').as_posix():p.read_bytes() for p in (ROOT/'ledger-evidence').rglob('*') if p.is_file()}
