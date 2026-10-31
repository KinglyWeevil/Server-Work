# Brief for ChatGPT: "Ledgerbook" guest brochure

Paste everything below the line into ChatGPT. Fill in the `[[FILL: ...]]` placeholders first, or let ChatGPT leave them visible.

---

## Your task

Design, write, test and hand back a **guest brochure** for a small private home server called **Ledgerbook**. It's run by Michael for a handful of family and friends. Readers are **non-technical** and will mostly use a **phone**.

Deliver **one self-contained HTML file** (`guide.html`) with inline CSS and no build step. It must:
- read well on a phone,
- print cleanly to PDF (letter size), so Michael can hand someone a copy,
- work offline once loaded.

Michael's admin assistant will host it behind the existing login, so only invited people can see it.

## Hard rules (security and privacy)

1. **No secrets.** No passwords, codes, API keys, IP addresses, port numbers, server names other than the public web addresses listed below, or anything about how the server is built.
2. **Member services only.** Never mention the admin tools (download managers, Unraid, Sonarr/Radarr, terminals and so on), even in passing.
3. **No external resources.** No trackers, no analytics, no external fonts, scripts or images. System font stack only. Icons as inline SVG or emoji.
4. **No invented facts.** If something isn't in this brief, write `[[FILL: ...]]` instead of guessing.
5. The brochure will also never be public. Still, write as if a screenshot of it might leak. Tell people *how* to use things, not what the server is or where it lives.
6. **One contact point.** Wherever the brochure would say "contact Michael" or "ask Michael", it says "email concierge@ledgerbook.vip" instead, as a `mailto:` link. Never give Michael's personal email, phone or other channels. Tell readers never to send passwords by email.

## Audience and tone

- Family and friends, mixed comfort with tech. Write for a reading level around grade 6 to 8.
- Warm, short and practical. Use numbered steps with one action per step.
- Every service section should work on its own, so a reader who jumps straight to "Books" isn't lost.
- The second person ("you"). Michael is "Michael", not "the admin".

## Structure

### 1. Welcome (short)
- What Ledgerbook is in two sentences: Michael's home server that shares a few things with people he knows.
- "Which services do I have?": tell readers that Michael gives access per service, and that they should ask if a section here doesn't work for them.

### 2. Signing in (shared by every web service)
How the login works. Explain it once, here, and have each service link back to it.
- Open the service's address. A sign-in page appears.
- Enter **your email address**: the one Michael registered for you.
- A **one-time code** arrives by email. Type it in within a few minutes.
- You stay signed in for **about a day** on that device, then you'll get a new code.
- **Tips and gotchas** (put these in a callout box):
  - Open links in your **real browser** (Chrome, Safari, Firefox), not inside Messages, Discord or Facebook. In-app browsers lose the code page.
  - Keep the sign-in tab open while you fetch the code, then switch back to **the same tab**.
  - Sign-in only works from **inside the US**. A VPN set to another country will block you, so switch it to a US location or turn it off.
  - Didn't get a code? Check spam, wait a minute, then try again. Codes expire.
  - Each service may ask you to sign in separately the first time.

### 2b. Your starter passwords (your personal setup page)
Several services have their own account on top of the Ledgerbook sign-in: Requests, Audiobookshelf, and Kavita through a setup link. Michael creates these accounts with **starter passwords**. The brochure must say where to find them, but **never contain them**.
- After signing in at `https://ledgerbook.vip`, open **Your accounts** (`https://ledgerbook.vip/setup`). It lists your username and starter password for each service you have, and any setup links. Only you and Michael can see it.
- Per service: **Audiobookshelf and Requests (Seerr)**: use the username and starter password from Your accounts, then change the password in that app's account settings. **Kavita**: no starter password; open the setup link emailed to you and choose your own. **Plex**: no Ledgerbook password; accept Michael's invitation email and use your own Plex account. **Private notes**: username and password are on Your accounts, along with which vault folder to open.
- If a service is missing from the page, or a password doesn't work, contact Michael.
- Save the new passwords in a password manager (for example Proton Pass, Bitwarden, or the phone's built-in one). Don't write them in notes or texts.
- Forgot a password? Ask Michael to reset it. Don't make a new account.
- Each service section's **Set it up** steps should say "use the username and starter password from your setup page" where that applies.

### 3. One section per service
Use the **same template for every service**, so people learn the pattern:

| Heading | Content |
|---|---|
| **What it is** | One or two sentences, and the everyday app it's like (for example "like Netflix" or "like Kindle") |
| **Address** | The web address, as a big tappable button |
| **Set it up (first time)** | Numbered steps, including any app to install, where to tap and what to name things |
| **How to use it** | The 3 or 4 most common tasks, each as a short numbered list |
| **On your phone / on a computer / on a TV** | Only where they differ |
| **If something's wrong** | The 3 most likely problems and their fixes, then "still stuck? contact Michael" |
| **Please don't** | One or two house rules specific to that service |

Services to cover, in this order. Each one gets a small "Ask Michael for access" note, because not everyone has every service.

1. **Home page**: `https://home.ledgerbook.vip` (also `https://ledgerbook.vip`). Starting page with tiles for each service. Suggest adding it to the phone's home screen.
2. **Movies and shows (Plex)**: watched in the **Plex app** (phone, TV, Roku, Fire TV, web at app.plex.tv), not through a ledgerbook address. Setup: create a free Plex account, send Michael the email you used, accept the invite under Plex's settings or in the email, then pick Ledgerbook's libraries in the app. Mention that streaming quality depends on Michael's home upload speed, so choosing a lower quality fixes buffering. [[FILL: confirm Plex is offered to this guest]]
3. **Requests (Seerr)**: `https://requests.ledgerbook.vip`. Ask for a movie or show to be added. It has **its own login** on top of the Ledgerbook sign-in; Michael sends the details. Search, tap Request, and it usually shows up in Plex [[FILL: typical wait, e.g. "within a day"]]. Michael reviews requests, so they aren't automatic. Set expectations: not everything can be found, and Michael may say no.
4. **Audiobooks and podcasts (Audiobookshelf)**: `https://audio.ledgerbook.vip`. It has **its own login**. Recommend its phone app (the "Audiobookshelf" app on Android and iOS) with the server address set to that URL. You can stream, or download for offline listening, and your progress syncs across devices. Note: if the app can't sign in because of the login page, use the browser instead and tell Michael. [[FILL: confirm app works through the login]]
5. **Ebooks and comics (Kavita)**: `https://books.ledgerbook.vip`. Read in the browser or a compatible app, with progress kept. You create your account through a **setup link from Michael**.
6. **Ebook shelves (Calibre-Web)**: `https://library.ledgerbook.vip`. Browse shelves, read, and send books to an e-reader. [[FILL: do members get Calibre-Web accounts? If not, leave this section out (key `library`)]]
7. **Minecraft**: summarize, then link to the existing **Minecraft join guide** (Michael will supply it; it covers Switch, Xbox, PlayStation and PC). Java edition: `minecraft.ledgerbook.vip`, port 25565. Bedrock edition: same address, port 19132. Joining needs Michael to add your exact Java name or Xbox gamertag first. Live world map: [[FILL: whether members can see minecraft-map.ledgerbook.vip; it's admin-only today]]. Do not put this section in anything public.
7b. **Jellyfin**: one short paragraph only. It's another movie and show player that works **only on Michael's home network**, not over the internet. No section key; mention it under Plex.
8. **Private notes** (only for people Michael set this up for): a personal notes space in the browser at an address Michael gives them. Just explain what it is and that it's private to them and Michael. [[FILL: whether to include]]

### 4. Getting help and asking for things
- **Contact**: all questions, problems and requests go to **concierge@ledgerbook.vip** (show it as a `mailto:` button). [[FILL: usual reply time]]. Michael has a day job, so replies aren't instant.
- **Something is down**: first try again in 10 minutes, since the server sometimes restarts for updates at night. [[FILL: link to status page later]]. Then contact Michael, saying which service, what you saw (a screenshot helps) and which device.
- **Ask for access to another service**: a short template message they can copy, with their name, the service, and the email to use.
- **Request a new service** ("could you host X?"): the same idea, with a template that asks what it is, what it's for, and who else would use it.

### 5. House rules (short, friendly)
- Don't share links, codes or your sign-in with anyone. Access is per person.
- Don't forward the Minecraft address or this guide.
- Respect the bandwidth: download over Wi-Fi, and don't stream from five devices at once.
- Michael can see basic activity, such as requests, reading progress and who's signed in. Say this plainly, so nobody is surprised.

### 6. Small FAQ (5 or 6 items)
For example: "Why do I keep getting codes?", "Why does it say I'm blocked?" (VPN or country), "Can my partner use my login?" (no, ask Michael), "Is this safe?", "Does this cost anything?" (no).

## Personalisation hook (required)

The page will be shown per person: the server hides the services a reader doesn't have. Build for that:
- Wrap each service section in `<section class="svc" data-service="KEY">`, using these keys: `home`, `plex`, `requests`, `audio`, `books`, `library`, `minecraft`, `notes`.
- Each table-of-contents entry gets the same `data-service` attribute.
- Add one empty `<section id="other-services">` after the services. The server fills it with "Other services you can ask Michael about", listing the names and one-line descriptions of the services the reader doesn't have.
- Without the personalisation, the page must still work with everything showing. Put no logic in the page itself; the server removes the sections.
- Put the one-line description of each service in `data-summary="..."` on its section, so the server can reuse it.

## Design requirements

- Phone first: a single column, a big tappable table of contents at the top, and section headers that stay findable. Use `<details>` blocks for long sections on mobile, but print everything expanded.
- Light and dark mode via `prefers-color-scheme`. Neutral palette with one accent color. Readable 16-18px base text.
- Each service section starts with a small icon, its name, and an "Address" button.
- `@media print`: hide the table of contents and buttons, expand all `<details>`, show URLs as text, page-break before each service section.
- Accessible: real headings in order, sufficient contrast, link text that makes sense out of context, `lang="en"`.
- No JavaScript, unless it's under 30 lines and only expands and collapses sections.

## Testing (do this, then report it)

1. Check the layout at 360px, 768px and 1280px width, with no horizontal scrolling.
2. Check print preview: every section expanded, sensible page breaks, URLs visible.
3. Run an HTML validator pass (no errors) and a basic contrast check.
4. Use a link list to confirm that every ledgerbook URL in the file is one of the addresses in this brief and nothing else.
5. Grep the file for `192.168`, `:80`, `password`, `token`, `api` and `unraid`. There should be no hits other than ordinary words.
6. List every remaining `[[FILL: ...]]` placeholder for Michael.

## Hand-back

Return:
1. `guide.html`.
2. A short list of the placeholders still unfilled.
3. A short list of anything you weren't sure about.

Michael's admin assistant (Claude) will host the file behind the login at `home.ledgerbook.vip/guide`. Don't include hosting instructions in the brochure itself.
