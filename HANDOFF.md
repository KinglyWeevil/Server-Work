# Continue here

## Current state

The user approved the guest guide’s general Ledgerbook theme: warm paper, dark ink, muted forest green, serif headings, fine ledger rules, and practical phone-first instructions. The current working output is `guest-guide/guide.html`. It is still a draft with visible `[[FILL: ...]]` placeholders.

All available work is saved under `guest-guide/`: the current and initial sample HTML, both uploaded Markdown briefs, reference PDF and phone render, validation evidence, review notes, prompt documents, reusable asset references, individual ZIP handoffs, combined ZIP, and generation/checking scripts. Runtime caches and installed third-party validator/browser dependencies are not project artifacts and are not included.

## Next task — use the actual Ledger inventory and assets

The latest user requirement is to base website and individual-container Argon packages on **the container list and assets available on Ledger**. This was not completed: the cloud workspace had no configured connection or mounted assets for Ledger. The repository started empty. Do not mistake the existing ZIP target list for an inventory discovered on the server.

From an application with authorized access to Ledger:

1. Read any applicable repository/server agent instructions and determine the supported read-only access route.
2. Inspect actual container names, product versions, website source, existing branding/icons, supported theme surfaces, and any prior Minecraft brochure or genuine device screenshots.
3. Do not dump environment variables, credential files, cookies, full container inspection output, or unfiltered configuration into the repository or ZIPs. Gather only the nonsecret inventory and design assets needed for the work; review them before committing or packaging. Preserve original assets and record provenance/usage limits.
4. Reconcile the current service list with the real inventory. Do not invent containers, assume customization support, or add guest access to admin tools.
5. Replace provisional asset references where actual Ledger assets exist, update the target-specific prompts, rebuild the standalone ZIPs and combined suite, and verify each archive.
6. Return the resulting packages for upload to Gemini Argon. Do not deploy design changes to Ledger as part of packaging.

No actual Ledger host/alias, credentials, SSH configuration, container definitions or website source was provided in this conversation. Resolve access from the next application's existing authorized configuration before asking for new access details. Never ask for secret values in chat.

## Decisions that override the uploaded briefs

The briefs are historical references, not the full current specification. Later user instructions take precedence:

- Do not tell guests to request access merely because something does not work. Their home page should show only enabled tiles. Point service discovery to the all-services directory, which contains short descriptions and stays visible independently of guest personalization.
- Radarr may appear in that directory, labeled **“Behind the scenes - admin only”**, with a brief description and no admin address or action button. Other admin products must come from actual inventory, not guesses. Existing packages distinguish guest brochure exposure from a separate, explicitly admin-only design task.
- Minecraft users should get `minecraft.ledgerbook.vip`, **Java port 25565** and **Bedrock port 19132** in their personalized instructions. Include the required Bedrock DNS setup and explain that it must be entered for each unique Wi-Fi network. Exact DNS values and device-specific steps are still unknown. Do not substitute public DNS defaults or fake screenshots.
- The user requested actual Switch/Xbox/phone/etc. setup screenshots if available. BedrockConnect’s README was consulted and contained console video walkthroughs, but no suitable still screenshots were sourced. No setup screenshots are included. The existing phone preview shows the brochure only.
- All guest contact goes to `mailto:concierge@ledgerbook.vip`.
- Starter credentials are never embedded in brochure or design assets. `https://ledgerbook.vip/setup` is the personal setup page. Seerr and Audiobookshelf use starter credentials followed by a change in app settings; Kavita uses an emailed setup link and user-chosen password; Plex uses the guest’s own account.

## Personalization and delivery contract

- Keep the brochure as a standalone HTML file with inline CSS, no build requirement or remote resources, light/dark modes and letter-size print support.
- Preserve `.svc` sections with `data-service` and `data-summary` attributes. Keys: `home`, `plex`, `requests`, `audio`, `books`, `library`, `minecraft`, `notes`.
- Corresponding personalized table-of-contents links carry `data-service`.
- Preserve the empty `#other-services` section after the service sections, for the hosting server's existing hook.
- Preserve the separate populated `#service-directory` catalog. Catalog entries intentionally do not use `data-service` and do not link to personalized sections that may be removed. Server-side filtering must leave the directory intact. No client-side permission logic.
- Do not introduce credentials, unapproved endpoints, unknown infrastructure details, external fonts/trackers or hosting instructions into the guest brochure.

## Packages and asset provenance

`guest-guide/argon-packages/` contains three brochure stages plus website/shared-assets packages and nine service/companion targets. The combined suite expands all task folders into one ZIP, with a root `START-HERE.md`. Each individual ZIP has `PROMPT.md` and its own context/manifest.

For the combined suite, tell Argon: **“Read START-HERE.md inside the ZIP, then follow the selected task’s PROMPT.md using its included assets.”**

For an individual ZIP: **“Read PROMPT.md inside the ZIP and complete it using the included assets.”**

The website/service packages include extracted brochure CSS/tokens and newly authored SVG starter pictograms. These are not existing deployed Ledger assets or approved final art. The reference PDF is a baseline, not an ideal pagination standard. The user wanted the exact container list and real assets, so inspect Ledger before treating the extra packages as final. Keep later approved Argon outputs in the same conversation or carry them forward explicitly.

## Validation evidence and limits

`guest-guide/checks.json` records the checks run on the current brochure before this handoff:

- No horizontal overflow at 360, 768, and 1280px in light and dark modes.
- Tested normal-text palette pairings exceeded 4.5:1 contrast.
- Nu HTML Checker reported zero errors.
- US-letter print output hides navigation/buttons, includes URLs and text from closed disclosure blocks, and starts services on new pages.
- The full source PDF is **22 pages**. Typography/pagination can be refined further; do not mistake programmatic checks for a complete visual or assistive-technology audit.
- No external resource requests during local rendering.
- A temporary personalization simulation retained only Home and Books: the complete directory remained and fragment links were valid.
- ZIP CRC and SHA-256 manifest checks passed.

These checks do not verify live services, native apps, existing account flows, actual Ledger containers, DNS values or screenshot accuracy. Existing placeholders remain listed in `review-notes.md`. Recheck any revised output rather than reusing old results.

## Working with the tools

Scripts in `guest-guide/tools/` now resolve the guest-guide directory relative to themselves:

- `python guest-guide/tools/build_guide.py` rebuilds `guide.html` from the initial sample’s CSS and current content generator. If editing the generated HTML, update the generator too or do not rerun it.
- `python guest-guide/tools/check_guide.py` regenerates browser/print/check artifacts and review notes. It requires Python packages `playwright` and `pypdf`, Chromium at `/usr/bin/chromium`, and a runtime capable of launching it. It does **not** itself run Nu HTML Checker; that was run separately. The saved review-note validator statement must be reconfirmed if changing HTML.
- A Nu validator invocation used was `java -jar <path-to-vnu.jar> --errors-only guest-guide/guide.html`; the temporary installed JAR is not committed.
- `python guest-guide/tools/package_argon.py` rebuilds the three brochure ZIPs.
- `python guest-guide/tools/package_web_and_services.py` rebuilds the provisional shared assets, website/service ZIPs, package index and complete suite. It currently writes the extracted/new starter assets; revise it before substituting real Ledger assets so they are not overwritten.
- Rebuild brochure packages first, then website/service packages (which gather them into the complete suite).
- `tools/history/` preserves one-off edits for provenance. They already ran and must not be reapplied.

No app/container behavior, authentication, website hosting, or live server configuration was changed during this work.
