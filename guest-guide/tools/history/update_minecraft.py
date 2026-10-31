from pathlib import Path
p=Path('/workspace/brochure-draft/build_guide.py')
s=p.read_text()
a=s.index('# Minecraft has no brochure address')
z=s.index("svc('notes'",a)
s=s[:a]+'''# Connection details are explicitly authorized by Michael's follow-up.
k,t,c=services[-1]
c=c.replace('<a class="button" href="#accounts">Address · find your personal link</a>'+fill('personal Minecraft link; do not publish a guessed address'),'<a class="button" href="#minecraft-connection">Address · Minecraft connection details</a>')
c=c.replace(fill('supply Minecraft join-guide link; keep connection details in that guide'),'<div id="minecraft-connection" class="callout"><h3>Your connection details</h3>'+p('<strong>Java edition</strong><br>Server address: minecraft.ledgerbook.vip<br>Port: 25565')+p('<strong>Bedrock edition</strong><br>Server address: minecraft.ledgerbook.vip<br>Port: 19132')+p('Use these details only after Michael has added your exact Java name or Xbox gamertag. Don’t forward them.')+'</div>')
old=p('Use the separate join guide for Switch, Xbox, PlayStation or PC. The '+sign+' apply to Ledgerbook web pages, rather than joining the game.')
new=p('The '+sign+' apply to Ledgerbook web pages, rather than joining the game.')+'<aside class="callout"><h4>Bedrock: set up each Wi-Fi network</h4>'+p('Enter the required DNS settings for each different Wi-Fi network you use. Setting them at home does not set them for a friend’s Wi-Fi or a different hotspot. Check the settings again when you change networks.')+'</aside>'+fill('approved primary and secondary DNS values from the existing Minecraft brochure; confirm any differences by device')+'<h4>Nintendo Switch</h4>'+steps(['Connect to the Wi-Fi network you plan to use.','[[FILL: verified Switch menu steps and DNS values from the Minecraft brochure]]','[[FILL: verified steps to open the server list and enter minecraft.ledgerbook.vip with Bedrock port 19132]]'])+'<h4>Xbox</h4>'+steps(['Connect to the Wi-Fi network you plan to use.','[[FILL: verified Xbox DNS steps and values from the Minecraft brochure]]','[[FILL: verified steps to join using minecraft.ledgerbook.vip with Bedrock port 19132]]'])+'<h4>PlayStation</h4>'+fill('verified PlayStation DNS and joining steps from the Minecraft brochure')+'<h4>Phone or tablet</h4>'+fill('confirm iPhone/iPad and Android joining steps, including whether DNS changes are needed on either platform')+'<h4>PC</h4>'+p('Use the address and port above for your edition of Minecraft.')+fill('verified Java and Bedrock PC menu steps')+p('The separate Minecraft join guide has the full device instructions: [[FILL: Minecraft join-guide link]].')
c=c.replace(old,new)
c=c.replace('Can’t connect? Check the steps for your device in the join guide.','Can’t connect? Check your edition’s address and port. For Bedrock DNS setup, check the settings for the Wi-Fi network you’re using now.')
services[-1]=(k,t,c)
''' + s[z:]
s=s.replace('@media print{.skip,.back', '@media print{body{font-size:10pt;line-height:1.45}h3{margin-top:14px}p{margin-bottom:10px}li{margin:5px 0}.task{margin:14px 0}.callout{padding:12px 16px;margin:16px 0}.skip,.back')
p.write_text(s)
# Update test notes to reflect user-approved scope.
p=Path('/workspace/brochure-draft/check_guide.py');s=p.read_text().replace('Minecraft connection details and map address are omitted; the supplied join-guide link is still needed.','Minecraft hostname and Java/Bedrock ports are included per Michael’s correction. Exact DNS values, device steps and the earlier join guide are still needed; no map address is included.').replace('no IP patterns, ports or prohibited tool names','no IP patterns or prohibited tool names; Minecraft ports are included as requested')
p.write_text(s)
