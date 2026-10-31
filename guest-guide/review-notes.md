# Ledgerbook guide review notes

## Unfilled placeholders

- [[FILL: confirm iPhone and Android home-screen steps]]
- [[FILL: confirm Plex is offered to this guest]]
- [[FILL: typical wait for an approved request to appear in Plex]]
- [[FILL: confirm Audiobookshelf app availability and sign-in through the Ledgerbook login on Android and iOS]]
- [[FILL: confirmed compatible Kavita apps and their setup steps]]
- [[FILL: confirm members get Calibre-Web accounts; remove this section and its contents entry if not]]
- [[FILL: Calibre-Web account and first-time sign-in steps, if offered]]
- [[FILL: confirmed Calibre-Web reading action]]
- [[FILL: confirmed e-reader setup and send steps]]
- [[FILL: confirm whether guests may use the live world map; no map link included]]
- [[FILL: Minecraft join-guide link]]
- [[FILL: approved primary and secondary DNS values from the existing Minecraft brochure; confirm any differences by device]]
- [[FILL: verified Switch menu steps and DNS values from the Minecraft brochure]]
- [[FILL: verified steps to open the server list and enter minecraft.ledgerbook.vip with Bedrock port 19132]]
- [[FILL: verified Xbox DNS steps and values from the Minecraft brochure]]
- [[FILL: verified steps to join using minecraft.ledgerbook.vip with Bedrock port 19132]]
- [[FILL: verified PlayStation DNS and joining steps from the Minecraft brochure]]
- [[FILL: confirm iPhone/iPad and Android joining steps, including whether DNS changes are needed on either platform]]
- [[FILL: verified Java and Bedrock PC menu steps]]
- [[FILL: personal Private notes link; do not publish a guessed address]]
- [[FILL: confirm private notes should be included for this guest]]
- [[FILL: confirmed create-note and save steps]]
- [[FILL: usual reply time]]
- [[FILL: status-page link, when available]]

## Decisions and limits

- Enabled-service sections and contents entries are removed by the host for guests without access; the all-services directory remains visible. Calibre-Web availability still needs confirmation. Radarr is included only as a behind-the-scenes admin-only directory entry, per Michael’s updated request. No unconfirmed admin tools were added.
- Minecraft hostname and Java/Bedrock ports are included per Michael’s correction. Exact DNS values, device steps and the earlier join guide are still needed; no map address is included.
- Audiobookshelf app availability and authentication need confirmation on the actual guest devices.
- The guide itself is self-contained and usable offline as a saved file. Linked services need a connection. Reopening a hosted page offline is not guaranteed by this single HTML file.

## Validation

- Nu HTML Checker: zero errors.
- Chromium: no horizontal overflow at 360, 768 and 1280 pixels in light and dark modes.
- Text palette contrast: all tested foreground/background pairs exceed 4.5:1.
- Print: US letter, contents and buttons hidden; service page breaks; content from closed details present; service addresses visible.
- No external resource requests. External links limited to supplied addresses and concierge email.
- Personalization simulation: only home and books retained; directory stays complete and fragment links stay valid.
- Privacy scan: no IP patterns; Radarr is explicitly approved as a directory-only admin entry; Minecraft ports are included as requested; password mentions are explanatory text only.
