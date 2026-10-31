from pathlib import Path
p=Path('/workspace/brochure-draft/build_guide.py')
s=p.read_text()
s=s.replace("access=f'<p class=\"note\">For access, {contact}.</p>'", "directory_link='<a href=\"#service-directory\">all available services</a>'\naccess=f'<p class=\"note\">Explore {directory_link}.</p>'")
s=s.replace("'A service won’t open? '+contact+' to check your access.'", "'Looking for a service that isn’t on your home page? Browse '+directory_link+'.'")
s=s.replace("'Asked for an account you don’t have? '+contact+' to check access.'", "'Looking for a service you don’t have? Browse '+directory_link+'.'")
s=s.replace("'No notes entry on Your accounts? '+contact+' to check access.'", "'No notes entry on Your accounts? Browse '+directory_link+' to learn what is available.'")
s=s.replace('Michael gives you access to each service separately. If a section here doesn’t work for you, ', 'Michael gives you access to each service separately. If a section here doesn’t work for you, ') # targeted full replacement below
old="p('Michael gives you access to each service separately. If a section here doesn’t work for you, '+contact+' to check your access.')"
new="p('Your home page shows only the service tiles available to you. To see what else Ledgerbook offers, explore '+directory_link+'. The directory describes each service, including those used only behind the scenes.')"
assert old in s;s=s.replace(old,new)
s=s.replace("p('Missing a service, or a password won’t work? '+contact+'. Forgot a password? Request a reset by email; don’t make a new account.')", "p('Looking for a service you don’t have? Browse '+directory_link+'. If a password won’t work, '+contact+' for a reset; don’t make a new account.')")
s=s.replace("contents+='<a href=\"#help\">", "contents+='<a href=\"#service-directory\">All available services</a><a href=\"#help\">")
s=s.replace('<span class="num" aria-hidden="true">↳</span>', '<span class="num" aria-hidden="true">·</span>')
# Catalog deliberately has no access links, server addresses, or data-service attributes.
# Server filtering of member service sections must leave this catalog intact.
marker="html='<!doctype html>"
assert marker in s
catalog='''catalog_entries=[
('Your home page', 'Your starting page, with tiles for the services available to you.', 'Member service'),
('Movies &amp; shows · Plex', 'Watch shared movies and shows in the Plex app.', 'Member service'),
('Requests · Seerr', 'Suggest a movie or show for Michael to review and add.', 'Member service'),
('Audiobooks &amp; podcasts · Audiobookshelf', 'Listen, download for offline listening, and keep your place across devices.', 'Member service'),
('Ebooks &amp; comics · Kavita', 'Read ebooks and comics in a browser or compatible app, with your place kept.', 'Member service'),
('Ebook shelves · Calibre-Web', 'Browse ebook shelves, read, and send books to an e-reader.', 'Member service · availability to be confirmed'),
('Minecraft', 'Join the shared world using the instructions for your device.', 'Member service'),
('Jellyfin', 'Another movie and show player that works only on Michael’s home network.', 'Local use only'),
('Private notes', 'A personal browser notebook, private to you and Michael.', 'Member service · available when set up for you'),
('Radarr', 'Helps Michael manage the movie collection behind the scenes.', 'Behind the scenes - admin only'),
]
catalog='<section id="service-directory"><p class="eyebrow">The Ledgerbook directory</p><h2>All available services.</h2>'+p('Here’s what each service does. This directory is for browsing; it does not give you access. Open the services you have from your home page.')+'<dl class="catalog">'+''.join('<div class="catalog-item"><dt>'+title+'</dt><dd><span class="catalog-label">'+label+'</span>'+description+'</dd></div>' for title,description,label in catalog_entries)+'</dl>'+p('Behind-the-scenes tools are for Michael’s use only. You don’t need to open or set them up.')+p('Interested in a member service? Use the <a href="#request-access">service access message</a> below.')+'</section>'
'''
s=s.replace(marker,catalog+marker)
s=s.replace("+'<section id=\"other-services\"></section>'+helpsec", "+'<section id=\"other-services\"></section>'+catalog+helpsec")
s=s.replace('<h3>Ask for access to a service</h3>', '<h3 id="request-access">Ask for access to a service</h3>')
s=s.replace("+p('Copy this into an email:')", "+p('Choose a member service from '+directory_link+', then copy this into an email:')")
s=s.replace('.index-label{margin-top:24px}', '.index-label{margin-top:24px}.catalog{margin:24px 0}.catalog-item{padding:18px 0;border-top:1px solid var(--line);break-inside:avoid}.catalog-item:last-child{border-bottom:1px solid var(--line)}.catalog dt{font-weight:650}.catalog dd{margin:4px 0 0}.catalog-label{display:block;font-size:13px;color:var(--muted);margin-bottom:6px}')
p.write_text(s)
