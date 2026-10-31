# Ledgerbook theming standard

Approved by Michael on 2026-10-20.

Ledgerbook Full (Full): default for all applications associated with this project where supported. Use the approved LB mark, dark leather texture, brass borders and actions, vellum fields, serif headings, and matching Ledgerbook wording. This is the approved existing direction; no new design choice is needed for faithful adaptations.

Ledgerbook Classic (Classic): fallback where Full is not supported. Retain the LB mark and brown/brass/ivory palette within the application's supported branding controls.

Use supported persistent theme mechanisms. Keep native authentication, accessibility, error states and authorization intact. Capability or account entitlement restrictions justify Classic; do not invent replacement authentication forms. Apply this standard when configuring or updating project applications. Deploy each stack separately with its changelog entry, commit, backup and health checks.

Cloudflare Access currently uses Classic because full custom-page validation returned 403 / 12133 on 2026-10-20. Do not expand access policies as part of theming.
