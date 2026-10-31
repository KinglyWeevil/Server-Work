"""Read-only, allowlisted snapshot. Run on a clerk with rx and /workspace/stacks."""
from pathlib import Path
import subprocess,json,hashlib,re
root=Path(__file__).resolve().parents[1]
out=root/'ledger-evidence'; out.mkdir(exist_ok=True)
stacks=Path('/workspace/stacks')
raw=subprocess.check_output(['/workspace/agents/_rules/bin/rx','ledger',"docker ps -a --format '{{.Names}}|{{.Image}}|{{.State}}'"],text=True)
rows=[]
for line in raw.splitlines():
    name,image,state=line.split('|')
    rows.append(dict(container=name,image=image,state=state,version_evidence='Configured image reference; not an in-app version measurement'))
(out/'containers.json').write_text(json.dumps({'observed':'2026-10-30','source':'Ledger docker ps -a; allowlisted fields only','containers':rows},indent=2)+'\n')
paths=['edge/THEMING.md']
paths += ['edge/ledgerbook/public/'+x for x in ['index.html','style.css','finish.css','book-model.js']]
paths += ['edge/ledgerbook/public/assets/'+x for x in ['brass.png','lb-baroque.png','leather.png','vellum.png']]
paths += ['books/ledgerbook-theme/ledgerbook-full.css','streaming/ledgerbook-theme/jellyfin-full.css','media/ledgerbook-theme/radarr/hooks/full.css','notes/ledgerbook-theme/obsidian-zilthai/ledgerbook-full.css','minecraft/ledgerbook-theme/bluemap-full.css']
manifest=[]
for rel in paths:
    data=(stacks/rel).read_bytes(); target=out/'assets'/rel; target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(data)
    manifest.append(dict(path='assets/'+rel,source='/mnt/user/appdata/stacks/'+rel,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),usage='Private Ledgerbook design reference; no license grant or public redistribution rights inferred'))
app=(stacks/'edge/ledgerbook/public/app.js').read_text()
icons=re.search(r'const iconPaths=(\{.*?\n\});',app,re.S).group(1)
(out/'portal-icon-paths.js').write_text('/* Extracted existing portal icons, not starter art. */\nconst iconPaths='+icons+';\n')
(out/'asset-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'Collected {len(rows)} containers and {len(manifest)} allowlisted assets. No configs, identities or credentials copied.')
