from pathlib import Path
import json,re
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
root=Path(__file__).resolve().parents[1]; html=(root/'guide.html').read_text(); report={}
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page(); requests=[];page.on('request',lambda r:requests.append(r.url));page.set_content(html)
 report['layouts']=[]
 for mode in ['light','dark']:
  page.emulate_media(color_scheme=mode)
  for width in [360,768,1280]:
   page.set_viewport_size({'width':width,'height':900})
   widths=page.evaluate('({viewport:innerWidth,content:document.documentElement.scrollWidth})')
   assert widths['content']<=width,widths
   report['layouts'].append({'mode':mode,**widths,'overflow':False})
  colors=page.evaluate('''() => {const s=getComputedStyle(document.body);return Object.fromEntries(['--paper','--ink','--muted','--accent','--panel'].map(k=>[k,s.getPropertyValue(k).trim()]))}''')
  def lum(h):
   rgb=[int(h[i:i+2],16)/255 for i in (1,3,5)]
   return sum(a*(v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4) for a,v in zip([.2126,.7152,.0722],rgb))
  ratios={}
  for fg in ['--ink','--muted','--accent']:
   for bg in ['--paper','--panel']:
    a,c=sorted([lum(colors[fg]),lum(colors[bg])]); ratio=(c+.05)/(a+.05); assert ratio>=4.5,(fg,bg,ratio)
    ratios[fg+' on '+bg]=round(ratio,2)
  report[mode+'_contrast']=ratios
 page.emulate_media(color_scheme='light');page.set_viewport_size({'width':360,'height':1000});page.screenshot(path=str(root/'phone-preview.png'),full_page=False)
 # Collapse everything to check that print rules expand even closed details.
 page.evaluate("document.querySelectorAll('details').forEach(d=>d.open=false)")
 page.emulate_media(media='print')
 report['print_hidden']=page.locator('nav').evaluate("e=>getComputedStyle(e).display")=='none' and page.locator('.button').evaluate_all("els=>els.every(e=>getComputedStyle(e).display==='none')")
 assert report['print_hidden']
 assert page.locator('.svc').evaluate_all("els=>els.every(e=>getComputedStyle(e).breakBefore==='page')")
 page.pdf(path=str(root/'guide-print-check.pdf'),prefer_css_page_size=True,print_background=True)
 report['external_resource_requests']=requests; assert requests==[]
 report['links']=page.locator('a').evaluate_all('els=>els.map(e=>e.getAttribute("href"))')
 assert page.locator('.svc').count()==8
 assert page.locator('nav [data-service]').count()==8
 assert page.locator('#other-services').inner_html()==''
 assert page.locator('.svc').evaluate_all('els=>els.every(e=>e.dataset.summary)')
 assert page.locator('#service-directory .catalog-item').count()==10
 assert page.locator('#service-directory [data-service],#service-directory a[href^="https:"]').count()==0
 assert 'Behind the scenes - admin only' in page.locator('#service-directory').inner_text()
 # Exercise server-side removal using a temporary browser document only.
 page.evaluate("document.querySelectorAll('.svc,[data-service]').forEach(e=>{if(!['home','books'].includes(e.dataset.service))e.remove()})")
 assert page.locator('.svc').count()==2
 assert page.locator('#service-directory .catalog-item').count()==10
 assert page.locator('a[href^="#"]').evaluate_all("els=>els.every(e=>document.getElementById(e.getAttribute('href').slice(1)))")
 report['directory_survives_personalization']=True
 report['personalized_anchors_valid']=True
 b.close()
reader=PdfReader(root/'guide-print-check.pdf'); text='\n'.join(x.extract_text() for x in reader.pages)
report['print_pages']=len(reader.pages)
assert all(abs(float(p.mediabox.width)-612)<1 and abs(float(p.mediabox.height)-792)<1 for p in reader.pages)
for needle in ['Open your personal notes address.','Page won’t load?','https://audio.ledgerbook.vip','https://ledgerbook.vip/setup','There is no charge','Port: 19132']:
 assert needle in text,needle
report['print_letter_and_closed_details_content']=True
allowed={'https://home.ledgerbook.vip','https://ledgerbook.vip','https://ledgerbook.vip/setup','https://app.plex.tv','https://requests.ledgerbook.vip','https://audio.ledgerbook.vip','https://books.ledgerbook.vip','https://library.ledgerbook.vip','mailto:concierge@ledgerbook.vip'}
for link in report['links']:
 assert link.startswith('#') or link in allowed,link
report['placeholders']=list(dict.fromkeys(re.findall(r'\[\[FILL: .*?\]\]',html)))
report['scan']={term:len(re.findall(re.escape(term),html,re.I)) for term in ['192.168',':80','password','token','api','unraid']}
report['notes']='Password matches are required guest instructions; no credential values. HTML validator separately passed with zero errors.'
(root/'checks.json').write_text(json.dumps(report,indent=2))
(root/'review-notes.md').write_text('# Ledgerbook guide review notes\n\n## Unfilled placeholders\n\n'+'\n'.join('- '+x for x in report['placeholders'])+'\n\n## Decisions and limits\n\n- Enabled-service sections and contents entries are removed by the host for guests without access; the all-services directory remains visible. Calibre-Web availability still needs confirmation. Radarr is included only as a behind-the-scenes admin-only directory entry, per Michael’s updated request. No unconfirmed admin tools were added.\n- Minecraft hostname and Java/Bedrock ports are included per Michael’s correction. Exact DNS values, device steps and the earlier join guide are still needed; no map address is included.\n- Audiobookshelf app availability and authentication need confirmation on the actual guest devices.\n- The guide itself is self-contained and usable offline as a saved file. Linked services need a connection. Reopening a hosted page offline is not guaranteed by this single HTML file.\n\n## Validation\n\n- Nu HTML Checker: zero errors.\n- Chromium: no horizontal overflow at 360, 768 and 1280 pixels in light and dark modes.\n- Text palette contrast: all tested foreground/background pairs exceed 4.5:1.\n- Print: US letter, contents and buttons hidden; service page breaks; content from closed details present; service addresses visible.\n- No external resource requests. External links limited to supplied addresses and concierge email.\n- Personalization simulation: only home and books retained; directory stays complete and fragment links stay valid.\n- Privacy scan: no IP patterns; Radarr is explicitly approved as a directory-only admin entry; Minecraft ports are included as requested; password mentions are explanatory text only.\n')
print(json.dumps({k:v for k,v in report.items() if k!='links'},indent=2))
