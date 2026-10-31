from pathlib import Path
import re,json,hashlib,zipfile
root=Path(__file__).resolve().parents[1]; out=root/'argon-packages'
source=(root/'gemini-argon-prompts.md').read_text()
prompts=re.findall(r'## (\d)\. ([^\n]+)\n\n```text\n(.*?)\n```',source,re.S)
assert len(prompts)==3
context='''# Current project context

The included guide.html is the current working baseline. Keep the established Ledgerbook paper-and-ink theme. This is a private guest handbook, primarily read on phones, with an offline self-contained HTML deliverable and US-letter print support.

Latest user decisions supersede older briefs:
- Direct service discovery to the all-services directory, not to a support request when a guest cannot open something. The home page should show only a guest's enabled tiles.
- Keep the full directory visible independently of enabled-service instructions. Radarr is explicitly approved as a name/description-only directory entry labeled “Behind the scenes - admin only.” Do not invent additional installed services.
- Include minecraft.ledgerbook.vip, Java port 25565, and Bedrock port 19132 inside the personalized Minecraft section. Explain that required Bedrock DNS settings must be entered for each distinct Wi-Fi network.
- Exact DNS values, device-specific steps, and the earlier Minecraft brochure are not available in this package. Retain placeholders. Authentic device screenshots were requested, but none have been supplied or verified. The included phone preview is a render of this brochure, NOT a device setup screenshot.
- Concierge email is the single contact: concierge@ledgerbook.vip. Do not include credential values.

Asset roles:
- guide.html: editable baseline and source of factual copy, links and personalization hooks.
- references/phone-preview.png: baseline first-screen phone render, not a full-page review or an aspirational design.
- references/guide-print-check.pdf: baseline print render, not a polished final PDF. Its full-source version is 22 pages; improve awkward pagination where possible without cutting content.
- references/review-notes.md: unresolved placeholders and current limitations.
- references/checks.json: checks run on the included baseline. These results do not validate any subsequent revision. Browser checks measured geometry, palette contrast, print content, and personalization; they were not a complete visual or assistive-technology audit.

Do not treat historical checks as new evidence. Do not fill unresolved facts from guesses. Prefer a newer user-approved guide or design supplied in the conversation over this baseline when continuing stages 2 or 3. Keep the original baseline recoverable.
'''
shared={
 'guide.html':(root/'guide.html').read_bytes(),
 'references/phone-preview.png':(root/'phone-preview.png').read_bytes(),
 'references/guide-print-check.pdf':(root/'guide-print-check.pdf').read_bytes(),
 'references/review-notes.md':(root/'review-notes.md').read_bytes(),
 'references/checks.json':(root/'checks.json').read_bytes(),
 'PROJECT-CONTEXT.md':context.encode(),
}
names=['01-art-direction','02-design-and-icons','03-final-audit']
for (number,title,prompt),name in zip(prompts,names):
 preface='''First read PROJECT-CONTEXT.md and inspect guide.html and the relevant files in references/. Treat the reference renders as the current baseline to improve, not an approved final design. Write outputs as new files so the baseline remains recoverable. Do not deploy or publish anything.

'''
 if number=='2':
  preface+='If the conversation contains an approved stage-1 design or a newer guide, apply that. If this ZIP is your only context, refine the included theme as the approved starting point; do not claim to have seen or followed a separate stage-1 approval.\n\n'
 if number=='3':
  preface+='Audit the latest revised guide supplied in this conversation, if any; otherwise audit guide.html from this ZIP. State which version you actually checked. Do not assume a stage-2 revision exists.\n\n'
 files=dict(shared)
 files['PROMPT.md']=('# Stage '+number+': '+title+'\n\n'+preface+prompt+'\n').encode()
 files['START-HERE.txt']=('Ledgerbook / Argon / Stage '+number+'\n\nUpload this ZIP and say:\n\nRead PROMPT.md inside the ZIP, then follow it using the included guide.html and reference assets.\n\nAll paths are relative to this ZIP. Each stage is self-contained and includes the same current baseline.\nUse stage 1 first, approve its direction, then use stage 2 and stage 3 in the same conversation to preserve approved revisions.\nIf you start a fresh conversation for a later stage, also provide the approved design or revised HTML from the previous stage.\nA ZIP made now cannot contain outputs that have not been created yet.\n').encode()
 files['MANIFEST.json']=json.dumps({'package':name,'files':[{ 'path':k,'bytes':len(v),'sha256':hashlib.sha256(v).hexdigest()} for k,v in sorted(files.items())]},indent=2).encode()
 path=out/('ledgerbook-argon-'+name+'.zip')
 with zipfile.ZipFile(path,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for k,v in sorted(files.items()):z.writestr(k,v)
 with zipfile.ZipFile(path) as z:
  assert z.testzip() is None
  manifest=json.loads(z.read('MANIFEST.json'))
  for f in manifest['files']:
   assert hashlib.sha256(z.read(f['path'])).hexdigest()==f['sha256']
  assert z.read('guide.html')==(root/'guide.html').read_bytes()
  assert all(not n.startswith('/') and '..' not in Path(n).parts for n in z.namelist())
 print(path.name, path.stat().st_size, 'bytes; integrity verified;',len(files),'files')
