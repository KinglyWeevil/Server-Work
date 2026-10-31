# Ledger evidence — 2026-10-30

Confirmed: read-only inventory from Ledger via the approved `rx ledger` route. `containers.json` contains all 36 observed containers, image references and state. Image tags are not independently measured product versions; notably the Minecraft container tag does not identify Paper/Geyser/BlueMap versions. No live configuration was changed.

## Authoritative branding

Michael confirmed on 2026-10-30: use existing **leather, brass and vellum** branding only. The paper/green guide is an outdated content draft, not approved art direction. Use the existing LB mark, textures, portal CSS and SVG paths. Do not create a replacement identity. `assets/edge/THEMING.md` describes Full and Classic. Preserve semantic warnings, focus, syntax and terminal colors. Workbench uses Classic.

`asset-manifest.json` records original server paths, sizes and SHA-256 hashes. Files were copied from the clerk's shared stacks mount; inventory was queried from Ledger. Existing frontend HTML/CSS, book-model code and icon definitions are included; backend/auth code, frontend account/setup code, member identities, configuration, notes, media and credentials are deliberately excluded. These are private design references, not a new license grant. Existing embedded image data is part of the CSS. Source presence is confirmed; this collection did not test every live customization or authenticated screen.

## Reconciled targets and customization evidence

| Package target | Observed container / image reference | Existing surface inspected | Limit |
|---|---|---|---|
| Website | ledgerbook-portal / node | Custom portal public HTML/CSS, textures, icons, book model | Node tag unpinned; backend excluded; preserve server authorization |
| Requests | jellyseerr / ghcr.io/seerr-team/seerr:v3.5.0 | No theme implementation collected | Container name is legacy; product is Seerr; supported theme surface unverified |
| Audiobookshelf | audiobookshelf / 2.37.1 | Server README describes exported HTML routes with embedded CSS | Version-specific template overrides; not evidence of native theme support |
| Kavita | kavita / v0.9.1.4-ls128 | Existing bg-ledgerbook-full CSS; README describes native theme upload | Authenticated theme only; native upload not exercised here |
| Calibre-Web | calibre-web / 0.6.27-ls406 | README describes LinuxServer custom-init/theme.park adapter | Guest provisioning and delivery remain unverified |
| Jellyfin | jellyfin / 12.2ubu2604-ls54 | Existing CSS; README describes native Branding CustomCss | Native/TV clients differ; image tag is not app version |
| Radarr | radarr / 6.4.4.10685-ls319 | Existing custom-init CSS adapter | Admin only; no guest action or address |
| Private notes | obsidian and obsidian-zilthai / v1.14.4-ls149 | Native Obsidian CSS snippet; README inspected | Separate private instances, never include note contents; guest setup still unverified |
| Minecraft companion | minecraft / 2026.10.0-java25 | BlueMap Full CSS and README describing native styles registration | Companion web guide, not game-client reskin; map guest access unverified |
| Plex companion | plex / 1.43.4 | Own-account companion only | No verified supported Plex UI customization |

Other observed UI products are recorded in the inventory, not automatically offered to guests: n8n, Uptime Kuma, Bazarr, Sonarr, UpSnap, Workbench, Syncthing, Clerk portal, Tdarr, LazyLibrarian, Chaptarr, Prowlarr, Lidarr, Calibre, Homepage, Guacamole, SillyTavern and qBittorrent. Infrastructure containers are not individual design targets. Do not expand guest visibility from this inventory. Immich is absent from the observed container list; prepared files alone do not establish deployment.

## Minecraft and remaining gaps

The inspected Minecraft README confirms console custom-server limitations and mentions BedrockConnect/phone LAN broadcast. No earlier join brochure, authenticated device screenshots, or approved per-device DNS values were found in the inspected project sources. Do not replace placeholders with guesses. The public game hostname/ports remain as specified in the handoff. BlueMap exists, but that does not establish guest access. No new external product/version recommendations are made by this snapshot.

No browser, accessibility, guest login, native client, DNS or live integration acceptance test was performed during collection. Historical brochure checks validate the old draft only. Every generated archive is checked separately for CRC, safe paths and manifest hashes.
