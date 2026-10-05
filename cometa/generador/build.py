import asyncio, os
from playwright.async_api import async_playwright

BASE = os.path.dirname(os.path.abspath(__file__))

CSS = """
@font-face{font-family:'Poppins';font-weight:400;src:url('fonts/poppins-latin-400-normal.woff2')}
@font-face{font-family:'Poppins';font-weight:600;src:url('fonts/poppins-latin-600-normal.woff2')}
@font-face{font-family:'Poppins';font-weight:700;src:url('fonts/poppins-latin-700-normal.woff2')}
@font-face{font-family:'Poppins';font-weight:800;src:url('fonts/poppins-latin-800-normal.woff2')}
*{box-sizing:border-box;margin:0;padding:0}
:root{--navy:#152C57;--navy2:#0F2144;--or:#E08A2E;--gold:#F2B544;--cream:#F5F1E8}
body{width:1080px;font-family:'Poppins',sans-serif;color:var(--cream)}
.c{position:relative;width:1080px;overflow:hidden;
  background:radial-gradient(900px 700px at 78% 62%,#24427f 0%,var(--navy) 45%,var(--navy2) 100%)}
.post{height:1350px}.story{height:1920px}
.band{position:absolute;left:0;right:0;height:150px;background:var(--navy2);border-top:6px solid var(--or);
  display:flex;align-items:center;justify-content:space-between;padding:0 48px;z-index:20}
.band img{height:76px}
.band .ct{text-align:right;line-height:1.15}
.band .wa{font-weight:700;font-size:36px;color:var(--cream);letter-spacing:.5px}
.band .ig{font-weight:600;font-size:30px;color:var(--or)}
.edu{position:absolute;z-index:5;filter:drop-shadow(0 18px 40px rgba(0,0,0,.45))}
.ring{position:absolute;border-radius:50%;border:16px solid var(--or);
  background:radial-gradient(circle at 50% 35%,#35599f,#1b3566 70%)}
.wm{position:absolute;opacity:.07;z-index:1}
.tag{display:inline-block;background:var(--or);color:var(--navy2);font-weight:800;font-size:28px;letter-spacing:2px;
  padding:12px 26px;border-radius:999px;text-transform:uppercase}
.or{color:var(--or);text-shadow:0 0 34px rgba(224,138,46,.55)}.gold{color:var(--gold)}
.glass{position:absolute;z-index:9;border-radius:22px;padding:16px 28px;font-weight:700;font-size:36px;line-height:1.15;color:var(--cream);
  background:linear-gradient(135deg,rgba(255,255,255,.20),rgba(255,255,255,.05));border:1.5px solid rgba(255,255,255,.30);
  backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);box-shadow:0 14px 44px rgba(0,0,0,.40),0 0 34px rgba(224,138,46,.28)}
.glass small{display:block;font-size:22px;font-weight:600;letter-spacing:2px;color:var(--gold);text-transform:uppercase}
.glass b{color:var(--or)}
.glow{position:absolute;z-index:3;border-radius:50%;filter:blur(40px);background:radial-gradient(circle,rgba(224,138,46,.75) 0%,rgba(224,138,46,.28) 45%,transparent 70%)}
.orbit{position:absolute;z-index:4;border-radius:50%;border:2px solid rgba(242,181,68,.55);box-shadow:0 0 22px rgba(242,181,68,.35)}
.vig{position:absolute;inset:0;z-index:2;background:radial-gradient(ellipse at 50% 45%,transparent 45%,rgba(6,14,34,.65) 100%)}
.edu{filter:drop-shadow(0 0 38px rgba(224,138,46,.38)) drop-shadow(0 22px 40px rgba(0,0,0,.5)) !important}

h1,h2{font-weight:800;line-height:.98;letter-spacing:-2px}
.abs{position:absolute;z-index:8}
.btn{display:inline-block;background:var(--or);color:var(--navy2);font-weight:800;border-radius:22px;padding:22px 38px}
.bub{border-radius:34px;padding:30px 36px;font-size:38px;line-height:1.3;font-weight:600}
.q{background:var(--cream);color:var(--navy2);border-bottom-right-radius:8px}
.a{background:var(--navy2);color:var(--cream);border:3px solid rgba(224,138,46,.55);border-bottom-left-radius:8px}
.chip{display:inline-block;margin-top:18px;background:var(--or);color:var(--navy2);font-weight:800;font-size:30px;padding:8px 22px;border-radius:12px}
"""

def band(bottom=0):
    return f"""<div class="band" style="bottom:{bottom}px"><img src="logo-star.webp"><div class="ct">
    <div class="wa">WhatsApp 0961228420</div><div class="ig">@eduustaar</div></div></div>"""

def wm(x, y, s):
    return f'<img class="wm" src="logo-star-icon.png" style="left:{x}px;top:{y}px;width:{s}px">'

def page(inner, kind):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div class='c {kind}'>{inner}</div></body></html>"

import random, math
def fx(w, h, seed, fx_, fy_, n=70):
    r = random.Random(seed)
    pts = [(r.uniform(0, w), r.uniform(0, h - 160), r.random()) for _ in range(n)]
    out = [f'<svg class="abs" style="left:0;top:0;z-index:1" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs>'
           '<filter id="g" x="-200%" y="-200%" width="500%" height="500%"><feGaussianBlur stdDeviation="3.5"/></filter></defs>']
    for i, (x1, y1, _) in enumerate(pts):
        for (x2, y2, _) in pts[i + 1:]:
            d = math.hypot(x1 - x2, y1 - y2)
            if d < 250:
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                near = max(0.0, 1 - math.hypot(mx - fx_, my - fy_) / 650)
                op = (0.10 + 0.55 * near) * (1 - d / 250)
                out.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#F2B544" stroke-opacity="{op:.2f}" stroke-width="1.6"/>')
    for (x, y, k) in pts:
        near = max(0.0, 1 - math.hypot(x - fx_, y - fy_) / 650)
        rad = 2 + 4.5 * k * (0.4 + near)
        col = '#F2B544' if k > .45 else '#9CB7F0'
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rad*2.6:.1f}" fill="{col}" fill-opacity="{.30 + .4*near:.2f}" filter="url(#g)"/>')
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rad:.1f}" fill="{col}" fill-opacity="{.65 + .3*near:.2f}"/>')
    out.append('</svg><div class="vig"></div>')
    return ''.join(out)

def glass(style, small, main):
    return f'<div class="glass" style="{style}"><small>{small}</small>{main}</div>'

SHIELD = '<svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="#F2B544" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" style="flex:none"><path d="M12 2.8 4.5 5.6v5.6c0 4.7 3.1 8.2 7.5 10 4.4-1.8 7.5-5.3 7.5-10V5.6z" fill="#F2B544" fill-opacity=".16"/><path d="m8.6 12.2 2.4 2.4 4.5-4.8"/></svg>'
def seal(style, text):
    return f'<div class="glass" style="display:flex;align-items:center;gap:16px;font-size:34px;{style}">{SHIELD}<span>{text}</span></div>'

pieces = {}

# 1 LUNES — lanzamiento
pieces['1-lunes-lanzamiento'] = ('post', wm(520, 120, 760) + f"""
<div class="abs" style="left:64px;top:84px"><span class="tag">Nuevo · para abogados</span></div>
<h1 class="abs" style="left:56px;top:170px;font-size:240px;color:var(--cream)">LEXA</h1>
<div class="abs" style="left:64px;top:430px;font-size:50px;font-weight:700;line-height:1.15;width:520px">Tu asistente legal <span class="or">en Telegram</span></div>
<div class="abs" style="left:64px;top:1010px;font-size:36px;font-weight:600;width:470px;line-height:1.25;color:var(--cream)">Sin inventar.<br><span class="or">Solo lo que dice la ley.</span></div>
<img class="edu" src="edu-cut.webp" style="right:-30px;bottom:150px;height:940px">
""" + band())

# 2 MARTES — gancho en pregunta
pieces['2-martes-pregunta'] = ('post', wm(-120, 700, 760) + f"""
<div class="ring" style="width:640px;height:640px;right:-90px;top:430px;z-index:2"></div>
<h1 class="abs" style="left:60px;top:80px;font-size:90px;width:600px">¿Cuánto tiempo pierdes buscando <span class="or">un artículo?</span></h1>
<img class="edu" src="edu-cut.webp" style="right:-70px;bottom:150px;height:880px">
<div class="abs" style="left:60px;top:1070px"><span class="btn" style="font-size:42px">Pregúntale a Lexa</span></div>
""" + band())

# 3 MIÉRCOLES — story, demostración
pieces['3-miercoles-story-demo'] = ('story', wm(380, 160, 900) + f"""
<h1 class="abs" style="left:64px;top:230px;font-size:132px;width:960px">Pregunta.<br><span class="or">Con artículo.</span></h1>
<div class="abs" style="left:64px;top:610px;width:760px"><div class="bub q">¿Cuánto dura el período de prueba en un contrato indefinido?</div></div>
<div class="abs" style="left:150px;top:830px;width:830px"><div class="bub a">Máximo noventa días, si el contrato se celebra por primera vez.<br><span class="chip">Código del Trabajo, Art. 15</span></div></div>
<img class="edu" src="edu-cut.webp" style="right:-40px;bottom:210px;height:640px;z-index:4">
""" + band(210))

# 4 JUEVES — secreto profesional
lock = """<svg width="150" height="150" viewBox="0 0 24 24" fill="none" stroke="#E08A2E" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4.5" y="10.5" width="15" height="10" rx="2.2" fill="#E08A2E" fill-opacity=".18"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/><circle cx="12" cy="15.5" r="1.4" fill="#E08A2E"/></svg>"""
pieces['4-jueves-secreto'] = ('post', wm(480, 80, 720) + f"""
<div class="ring" style="width:600px;height:600px;left:-110px;top:500px;z-index:2"></div>
<img class="edu" src="edu-cut.webp" style="left:-40px;bottom:150px;height:930px">
<div class="abs" style="right:64px;top:90px;text-align:right"><span class="tag">Secreto profesional</span></div>
<h1 class="abs" style="right:64px;top:190px;font-size:128px;text-align:right;width:600px">Tu caso es <span class="or">tuyo.</span></h1>
<div class="abs" style="right:64px;top:720px;text-align:right;width:520px;font-size:46px;font-weight:700;line-height:1.2">Lexa <span class="or">no guarda</span> tus consultas.</div>
<div class="abs" style="right:64px;top:850px">""" + lock + """</div>
""" + band())

# 5 VIERNES — oferta
pieces['5-viernes-oferta'] = ('post', wm(500, 40, 800) + f"""
<div class="abs" style="left:64px;top:84px"><span class="tag">Prueba sin riesgo</span></div>
<h1 class="abs" style="left:56px;top:170px;font-size:170px;line-height:.92">7 DÍAS<br><span class="or">GRATIS</span></h1>
<div class="abs" style="left:64px;top:560px;font-size:46px;font-weight:700;width:520px;line-height:1.2">Solo <span class="gold">5 cupos</span> fundadores</div>
<div class="abs" style="left:64px;top:930px"><span class="btn" style="font-size:40px;line-height:1.2;display:block;width:560px">Escribe <b>LEXA</b><br>al 0961228420</span></div>
<img class="edu" src="edu-cut.webp" style="right:-90px;bottom:150px;height:900px">
""" + band())

# 6 SÁBADO — story, leyes
laws = ["CONSTITUCIÓN", "COIP", "COGEP", "CÓDIGO CIVIL", "TRABAJO", "NIÑEZ", "COFJ", "LOGJCC"]
wall = "".join(f'<div style="font-weight:800;font-size:{84 if len(l)<9 else 70}px;letter-spacing:-1px;line-height:1.08;color:{"var(--or)" if i%3==0 else "var(--cream)"};opacity:{1 if i%3==0 else .92}">{l}</div>' for i, l in enumerate(laws))
pieces['6-sabado-story-leyes'] = ('story', wm(300, 300, 1000) + f"""
<h1 class="abs" style="left:64px;top:230px;font-size:150px">8 leyes.<br><span class="or">Un solo chat.</span></h1>
<div class="abs" style="left:64px;top:720px;width:560px">{wall}</div>
<img class="edu" src="edu-cut.webp" style="right:-40px;bottom:210px;height:880px">
""" + band(210))

# 7 DOMINGO — marca personal
pieces['7-domingo-hecho-en-cayambe'] = ('post', wm(-60, 760, 700) + f"""
<h1 class="abs" style="left:64px;top:84px;font-size:134px;width:900px">Hecho en <span class="or">Cayambe.</span></h1>
<div class="abs" style="left:64px;top:420px;font-size:54px;font-weight:700;width:760px;line-height:1.15">Para abogados <br>de todo Ecuador.</div>
<div class="ring" style="width:520px;height:520px;right:56px;top:560px;z-index:2;overflow:hidden"></div>
<div class="abs" style="right:56px;top:470px;width:520px;height:610px;overflow:hidden;z-index:6;border-radius:0 0 260px 260px"><img src="edu-cut.webp" style="position:absolute;left:-10px;top:50px;width:540px"></div>
<div class="abs" style="left:64px;top:1010px;font-size:40px;font-weight:700;line-height:1.2">Edu Estrella<br><span class="or" style="font-weight:600;font-size:32px">Star IA Solutions</span></div>
""" + band())

EX = {
 '1-lunes-lanzamiento': ((800,560), '<div class="glow" style="width:760px;height:760px;right:-170px;top:300px"></div><div class="orbit" style="width:620px;height:230px;right:-60px;top:900px;transform:rotate(-14deg)"></div>',
    glass('left:340px;top:620px','COIP','Art. 186') + glass('right:26px;top:900px','Código Civil','Art. 1561') + glass('left:64px;top:790px;font-size:38px','Base legal','<b>5.800+</b> artículos')),
 '2-martes-pregunta': ((780,650), '<div class="glow" style="width:700px;height:700px;right:-140px;top:380px"></div><div class="orbit" style="width:700px;height:240px;right:-120px;top:930px;transform:rotate(12deg)"></div>',
    seal('left:60px;top:790px;width:500px','Si no está en la ley, <b>te lo dice</b>') + glass('left:330px;top:930px','COGEP','Art. 142')),
 '3-miercoles-story-demo': ((780,1250), '<div class="glow" style="width:620px;height:620px;right:-150px;top:1080px"></div>',
    glass('left:64px;top:1230px','Búsqueda en','<b>8</b> leyes') + seal('left:64px;top:1400px;width:660px','Si no lo encuentra, <b>te lo dice</b>')),
 '4-jueves-secreto': ((300,640), '<div class="glow" style="width:700px;height:700px;left:-200px;top:400px"></div><div class="orbit" style="width:600px;height:220px;left:-60px;top:980px;transform:rotate(10deg)"></div>',
    glass('right:64px;top:1030px;font-size:32px','Solo se guarda','<b>cuántas</b> consultas') + seal('right:64px;top:500px;width:560px','Apoyo de consulta: <b>la decisión es tuya</b>')),
 '5-viernes-oferta': ((820,640), '<div class="glow" style="width:760px;height:760px;right:-190px;top:340px"></div><div class="orbit" style="width:640px;height:230px;right:-90px;top:930px;transform:rotate(-12deg)"></div>',
    seal('left:64px;top:690px;width:540px','Pruébalo <b>antes de pagar</b>')),
 '6-sabado-story-leyes': ((820,1450), '<div class="glow" style="width:700px;height:700px;right:-170px;top:1000px"></div><div class="orbit" style="width:640px;height:230px;right:-90px;top:1500px;transform:rotate(-12deg)"></div>',
    seal('left:64px;top:1440px;width:690px;font-size:32px','Cada respuesta <b>cita su artículo</b>')+glass('right:50px;top:760px','LOGJCC','Art. 1')+glass('left:560px;top:880px;font-size:28px','COFJ','Art. 1')),
 '7-domingo-hecho-en-cayambe': ((800,780), '<div class="glow" style="width:640px;height:640px;right:-10px;top:520px"></div><div class="orbit" style="width:700px;height:700px;right:-40px;top:470px;border-width:2px"></div>',
    seal('left:64px;top:620px;width:480px','Apoyo de consulta: <b>tu criterio manda</b>')),
}
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium' if os.path.exists('/opt/pw-browsers/chromium') else None)
        for name, (kind, inner) in pieces.items():
            h = 1350 if kind == 'post' else 1920
            path = os.path.join(BASE, f'{name}.html')
            ex = EX[name]
            inner = fx(1080, h, hash(name) % 1000, ex[0][0], ex[0][1]) + ex[1] + inner + ex[2]
            open(path, 'w').write(page(inner, kind))
            pg = await b.new_page(viewport={'width': 1080, 'height': h})
            await pg.goto('file://' + path)
            await pg.evaluate('document.fonts.ready')
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=os.path.join(BASE, 'out', f'{name}.png'))
            await pg.close()
        await b.close()
asyncio.run(main())
