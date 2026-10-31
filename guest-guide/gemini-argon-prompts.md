# Ledgerbook: prompts for Gemini Argon

Attach the current `guide.html` with each prompt. Use these in order, carrying the approved output forward. Include the existing Minecraft brochure and any genuine device screenshots if you want that section polished too. The unresolved `[[FILL: ...]]` items are content questions, not invitations to guess.

## 1. Art direction — review before implementation

```text
You are the art director for Ledgerbook, a private guest guide for Michael’s family and friends. Study the attached guide.html before proposing changes. Evolve its existing identity into a carefully crafted editorial design: warm paper, dark ink, restrained forest green, serif display headings, system sans-serif instructions, fine ledger rules, and generous but purposeful spacing. Preserve its familiar, welcoming character.

The audience is nontechnical and reads primarily on phones. The aesthetic should feel like an exceptionally well-typeset personal handbook. Aim for quiet confidence, precise alignment, balanced typography, and clear information hierarchy. Avoid dashboard styling, oversized empty hero areas, gradients, glass effects, excessive cards, decorative animations, and visual clutter. Decoration must earn its place.

Show ONE recommended direction and one restrained alternative. For each, provide a compact art-direction board with specific color tokens, system font stacks, type scale, spacing scale, line weights, button treatment, section markers, and icon style. Demonstrate the cover, contents, one service heading, one step list, a help callout, and a directory entry. Describe the corresponding dark and print treatments.

Treat the current copy and service inventory as authoritative. Preserve the distinction between a guest’s enabled services and the all-services directory. Radarr is a directory-only entry labeled “Behind the scenes - admin only,” without an address or action button. Do not add other products or claim they are installed.

Keep this stage to a reviewable design proposal. Do not rewrite the full file yet. Explicitly identify the decisions you want me to approve before implementation. State any tool limitations; do not imply you rendered mockups if you only described them.
```

## 2. Implement the approved design and bespoke icon system

```text
Apply the approved Ledgerbook art direction to the attached guide.html. Return a complete, self-contained guide.html and a brief explanation of the visual changes. Preserve its factual copy, useful instructions, existing URLs, placeholder text, service order, and personalization hooks. Improve visual execution through typography, composition, spacing, iconography, and interaction details.

Craft a coherent family of small inline SVG icons for home, movies/shows, requests, audiobooks/podcasts, ebooks/comics, ebook shelves, Minecraft, private notes, and the directory. Use one consistent grid (such as 24 × 24), stroke weight, corner treatment, optical weight, and alignment. Make each silhouette recognizable at 20–24 CSS pixels. Use currentColor, no external assets, and appropriate decorative accessibility attributes when a text label already supplies the meaning. Avoid brand logos and avoid mixing emoji, Unicode symbols, filled icons, and outline icons. Let Radarr’s directory entry use the same restrained visual language with a clear text label indicating its admin-only role. Retain readable labels; icons must never carry meaning alone.

Refine heading measure, line height, paragraph rhythm, numbered steps, callout padding, divider placement, focus rings, tap targets, disclosure indicators, and URL wrapping. Keep the guide easy to scan at 360px and comfortable at 768px and 1280px. Use a single reading column. Keep navigation convenient without a tall sticky element obscuring content. Keep the service directory legible as a compact editorial list; do not make unavailable services look like launch buttons. All services must remain findable from the contents.

Non-negotiable implementation constraints:
- One HTML file, inline CSS and inline SVG, no build step, no fetched fonts, CSS, scripts, images, analytics, or libraries. All styling and icons must render offline.
- System font stacks only. Light/dark mode via prefers-color-scheme. At least 4.5:1 contrast for normal text, visible keyboard focus, semantic heading order, lang="en", and comfortable tap targets.
- Preserve each <section class="svc" data-service="KEY" data-summary="..."> and its ID. Keys: home, plex, requests, audio, books, library, minecraft, notes. Preserve corresponding data-service attributes on personalized contents entries.
- Preserve the empty <section id="other-services"></section> immediately after the service sections. Keep the populated #service-directory separate. Its entries must remain visible when enabled-service sections and their contents links are removed. Do not give directory entries data-service attributes, link them to potentially removed sections, or add client-side permission logic.
- Admin-only tools get names, brief descriptions, and their admin-only labels in the directory; no addresses, credentials, configuration instructions, or access buttons. Radarr is the only admin-only tool currently confirmed for this directory.
- US-letter print: hide contents and buttons, show useful addresses as text, reveal every disclosure’s contents even if closed on screen, start each enabled service on a fresh page, and avoid stranded headings or wasteful near-empty pages. Make visual rules work in grayscale. Do not shrink body text below a comfortable print size to force pagination.
- No JavaScript unless strictly necessary for expanding/collapsing disclosures, and then fewer than 30 lines. Never implement personalization in the page.
- All contact links go to mailto:concierge@ledgerbook.vip. Never insert credentials or invent missing facts.
- The Minecraft section must retain minecraft.ledgerbook.vip, Java port 25565, Bedrock port 19132, and the reminder that required DNS settings must be entered for every different Wi-Fi network. Keep its unknown DNS values and device steps as placeholders. Never fabricate device screenshots or present generated pictures as actual console UI.

Do not silently resolve content placeholders, remove useful troubleshooting steps, or claim live services were tested. Finish with a short list of preserved constraints, remaining placeholders, and any limitations you actually encountered.
```

## 3. Final visual and accessibility audit

```text
Audit the attached Ledgerbook guide.html as an exacting editorial designer, accessibility reviewer, and print production specialist. Make the final visual corrections needed to achieve the approved direction while preserving its content and personalization contract. Return the corrected standalone guide.html, a concise defect/change list, and actual validation evidence.

If browser tools are available, render at 360px, 768px, and 1280px in light and dark modes. Inspect screenshots, not just DOM dimensions. Look for horizontal scrolling, awkward line breaks, missing glyphs, cramped contact links, inconsistent icon weight, weak hierarchy, oversized gaps, and misaligned controls. Test keyboard navigation and visible focus. Measure contrast for text, icons that convey meaning, and controls in their actual contexts.

Simulate a guest with only home and books by removing the other .svc sections and their corresponding personalized contents entries from a temporary test copy. Confirm the directory remains complete, the remaining navigation works, and no directory entries become broken links. Keep that simulation out of the delivered file. In the full source, preserve the empty #other-services hook and the separate #service-directory.

Render a US-letter PDF with all screen disclosures initially closed. Verify their content still prints, URLs are visible, navigation and buttons are hidden, service starts honor page breaks, headings remain with text, and the output contains no accidental blank pages. Inspect every PDF page for awkward spillover. Report the page count and any unresolved pagination tradeoff.

Run an HTML validator and check every fragment target. Verify there are no external resource fetches and that external links remain limited to the original approved addresses and concierge email. Confirm the admin-only directory entry has no address or launch action. Check the approved Minecraft ports and per-Wi-Fi reminder remain in its personalized section. List every unresolved [[FILL: ...]] item without replacing it with invented information.

If any requested check cannot be run, explicitly mark it unrun. Do not describe a visual inspection, contrast check, accessibility check, or service test as passed without doing it. Preserve the Ledgerbook character throughout; finish by correcting concrete defects rather than introducing another redesign.
```
