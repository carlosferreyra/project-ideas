"""Render the canonical README into the standalone reading view."""

import re
import html

def inline(s):
    s=html.escape(s)
    s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    return s

def render(s):
    parts=[]; listing=False; table=False
    for line in s.strip().splitlines():
        if line.startswith('- '):
            if not listing: parts.append('<ul>'); listing=True
            parts.append('<li>'+inline(line[2:])+'</li>'); continue
        if listing: parts.append('</ul>'); listing=False
        if line.startswith('|'):
            if re.match(r'\|[\s:|-]+\|$',line): continue
            if not table: parts.append('<table>'); table=True
            parts.append('<tr>'+''.join('<td>'+inline(c.strip())+'</td>' for c in line.strip('|').split('|'))+'</tr>'); continue
        if table: parts.append('</table>'); table=False
        if line.strip() and line!='---': parts.append('<p>'+inline(line)+'</p>')
    if listing: parts.append('</ul>')
    if table: parts.append('</table>')
    return ''.join(parts)

def render_html(source, review_date):
    sections=re.split(r'^## (\d+)\. (.+)\n',source,flags=re.M)
    intro=source.split('## How to use this list\n')[1].split('\n---')[0]
    cards=[]
    for i in range(1,len(sections),3):
        rank,name,body=sections[i:i+3]
        body=body.split('## Idea Graveyard')[0]
        statusline=re.search(r'\*\*Status:\*\* (.+)',body).group(1)
        status=re.search(r'`(idea|in-progress|done)`',re.sub(r'~~.*?~~','',statusline)).group(1)
        effort=re.search(r'\*\*Estimated effort:\*\* (\w)',body).group(1)
        stack=re.search(r'\*\*Stack:\*\* (.+)',body).group(1)
        desc=re.search(r'\*\*Description:\*\* (.+)',body).group(1)
        repo_link = re.search(r'\[.*?\]\((https://github.com/[^)]+)\)', statusline)
        detail=re.sub(r'^\*\*(Status|Stack|Description|Estimated effort):\*\* .+\n?','',body,flags=re.M)
        if repo_link:
            detail += '\n\n[Repository](' + repo_link.group(1) + ')\n'
        cards.append(f'<article data-status="{status}"><div class="eyebrow"><span>#{int(rank):02d}</span><span class="badge {status}">{status}</span><span class="effort">Effort {effort}</span></div><h2>{html.escape(name)}</h2><div class="stack">{html.escape(stack)}</div><p class="description">{inline(desc)}</p><details><summary>Career signal &amp; build details</summary>{render(detail)}</details></article>')
    grave=source.split('## Idea Graveyard\n')[1].split('## Resources')[0]
    resources=source.split('## Resources\n')[1]
    css='''
    :root{color-scheme:dark}*{box-sizing:border-box}body{margin:0;color:var(--foreground,#e7e9ef);font-family:var(--font-sans,system-ui);line-height:1.65}main{max-width:1000px;margin:auto}header{padding:24px 0 20px;border-bottom:1px solid var(--border,#303744)}.kicker{text-transform:uppercase;letter-spacing:.18em;font-size:11px;color:var(--primary,#a6baff)}h1{font-size:clamp(32px,6vw,54px);line-height:1.1;letter-spacing:-.045em;margin:12px 0}header p{color:var(--muted-foreground,#aab3c5);margin:10px 0}.toolbar{display:flex;flex-wrap:wrap;gap:10px;margin:22px 0}input,select,button{font:inherit;color:inherit;background:var(--card,#18202e);border:1px solid var(--border,#303744);border-radius:9px;padding:10px 12px}input{flex:1;min-width:170px}button,summary{cursor:pointer}button:hover{border-color:var(--primary,#a6baff)}#count{font-size:12px;color:var(--muted-foreground,#aab3c5);margin-bottom:16px}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}article{padding:20px;background:var(--card,#18202e);border:1px solid var(--border,#303744);border-radius:var(--radius,12px)}.eyebrow{display:flex;align-items:center;gap:10px;font-size:12px;color:var(--muted-foreground,#aab3c5)}.badge{padding:2px 8px;border-radius:20px;color:var(--info,#93baff);background:var(--secondary,#253149)}.in-progress{color:var(--warning,#f1ca7d)}.done{color:var(--success,#84d7ad)}.effort{margin-left:auto}h2{font-size:24px;line-height:1.2;letter-spacing:-.025em;margin:14px 0 8px;overflow-wrap:anywhere}.stack{font-size:12px;color:var(--primary,#a6baff)}.description{font-size:14px}details{font-size:13px}summary{color:var(--primary,#a6baff);padding:8px 0}details p,li{overflow-wrap:anywhere}a{color:var(--primary,#a6baff);text-underline-offset:3px}code{font-family:var(--font-mono,monospace);font-size:.9em;background:var(--code-background,#101724);padding:2px 4px;border-radius:4px}ul{padding-left:20px}section{margin:28px 0}table{width:100%;border-collapse:collapse;font-size:13px}td{padding:12px;border-bottom:1px solid var(--border,#303744);text-align:left}tr:first-child{font-weight:bold}#empty{padding:30px;text-align:center}[hidden]{display:none!important}@media(max-width:600px){.grid{grid-template-columns:1fr}article{padding:16px}}@media print{.toolbar{display:none}.grid{display:block}article{break-inside:avoid;margin:16px 0}details{display:block}}
    '''
    page='''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Project ideas — reading room</title><style>'''+css+'''</style></head><body><main><header><div class="kicker">Personal project backlog · reviewed {review_date}</div><h1>Ideas worth coming back to.</h1><p>A ranked backlog of project ideas to build, ordered by career impact.</p><details><summary>How this list works · ranking &amp; status definitions</summary>'''+render(intro)+'''</details></header><div class="toolbar"><input id="search" type="search" aria-label="Search project ideas" placeholder="Search ideas, stacks, or features…"><select id="status" aria-label="Filter by status"><option value="all">All statuses</option><option value="idea">Idea</option><option value="in-progress">In progress</option><option value="done">Done</option></select><button id="expand" type="button">Expand all details</button></div><div id="count" role="status">27 ideas · original ranking preserved</div><div class="grid">'''+''.join(cards)+'''</div><p id="empty" hidden>No ideas match. Try another search or status.</p><section><details><summary>Idea graveyard · considered &amp; deprioritized</summary>'''+render(grave)+'''</details></section><section><details><summary>Resources · inspiration &amp; signal</summary>'''+render(resources)+'''</details></section></main><script>
    const search=document.querySelector('#search'),status=document.querySelector('#status'),cards=[...document.querySelectorAll('article')];
    function filter(){let n=0;const q=search.value.toLowerCase().trim();cards.forEach(c=>{c.hidden=!(c.textContent.toLowerCase().includes(q)&&(status.value==='all'||c.dataset.status===status.value));if(!c.hidden)n++});document.querySelector('#count').textContent=n+' of '+cards.length+' ideas · original ranking preserved';document.querySelector('#empty').hidden=n!==0}
    search.addEventListener('input',filter);status.addEventListener('change',filter);document.querySelector('#expand').addEventListener('click',e=>{const open=e.target.textContent.startsWith('Expand');cards.forEach(c=>c.querySelector('details').open=open);e.target.textContent=open?'Collapse all details':'Expand all details'});
    </script></body></html>'''
    return page.replace('{review_date}', html.escape(review_date)).replace('27 ideas ·', f'{len(cards)} ideas ·')
