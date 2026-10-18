import asyncio, os
from playwright.async_api import async_playwright
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build.py')).read().split("pieces = {}")[0]
exec(src)

# Semana 3 (19-25 oct 2026): foto completa de oficina, telefono, antes/ahora, burbuja-mascara, asientos, sticker, bento
X = """
.outl{-webkit-text-stroke:3px rgba(245,241,232,.55);color:transparent}
.photo{position:absolute;inset:0;z-index:0;background:url('hero2.webp') no-repeat;background-size:1400px auto;background-position:-300px 0}
.photo.s{background-size:1560px auto;background-position:-330px -40px}
.shade{position:absolute;inset:0;z-index:1;background:linear-gradient(180deg,rgba(15,33,68,.50) 0%,rgba(15,33,68,.10) 32%,rgba(15,33,68,.55) 60%,rgba(15,33,68,.97) 86%)}
.duo{position:absolute;inset:0;z-index:1;background:#152C57;mix-blend-mode:color;opacity:.55}
.phone{position:absolute;z-index:7;width:470px;height:900px;border-radius:70px;background:#0b1730;border:12px solid #0b1730;box-shadow:0 0 0 3px rgba(242,181,68,.6),0 40px 90px rgba(0,0,0,.6),0 0 90px rgba(224,138,46,.35);overflow:hidden}
.phone .top{height:110px;background:var(--navy);display:flex;align-items:center;gap:16px;padding:0 26px;border-bottom:2px solid rgba(255,255,255,.08)}
.phone .av{width:62px;height:62px;border-radius:50%;background:var(--or);display:flex;align-items:center;justify-content:center;font-weight:800;color:var(--navy2);font-size:34px}
.phone .nm{font-weight:700;font-size:30px;line-height:1.05}.phone .nm small{display:block;font-size:20px;color:#9CB7F0;font-weight:500}
.phone .body{padding:26px 22px;background:linear-gradient(180deg,#1a3566,#0F2144);height:100%}
.phone .bub{font-size:27px;padding:20px 24px;margin-bottom:22px;border-radius:26px;line-height:1.25}
.doc{position:absolute;width:300px;height:390px;background:#d9d6cd;border-radius:10px;box-shadow:0 14px 30px rgba(0,0,0,.35);padding:30px 26px}
.doc i{display:block;height:10px;background:#9a978e;border-radius:5px;margin-bottom:18px}
.sticker{position:absolute;z-index:9;background:var(--cream);color:var(--navy2);border-radius:34px;padding:28px 34px;box-shadow:0 24px 60px rgba(0,0,0,.5)}
.tile{position:absolute;border-radius:36px;overflow:hidden}
"""
CSS3 = CSS + X
def page3(inner, kind, bg=None):
    st = f' style="background:{bg}"' if bg else ''
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS3}</style></head><body><div class='c {kind}'{st}>{inner}</div></body></html>"

P = {}

# 1 LUN post - HIPOTESIS A: foto completa de oficina (credibilidad) a pantalla completa
P['1-lunes-sin-inventar'] = ('post', None, """
<div class="photo"></div><div class="duo"></div><div class="shade"></div>
<div class="abs" style="right:56px;top:70px"><span class="tag">Lexa · para abogados</span></div>
<h1 class="abs" style="left:56px;top:620px;font-size:196px;letter-spacing:-6px;z-index:8;line-height:.9">SIN<br><span class="or">INVENTAR.</span></h1>
<div class="abs" style="left:60px;top:1030px;z-index:8;font-size:48px;font-weight:700">Solo lo que dice la ley.</div>
<div class="abs" style="left:56px;top:1105px;z-index:8"><span class="btn" style="font-size:34px;display:block">Escribe <b>LEXA</b> al 0961228420</span></div>
""" + band())

# 2 MAR post - HIPOTESIS B: recorte de Edu sobre fondo de marca + telefono gigante inclinado
P['2-martes-bolsillo'] = ('post', None, fx(1080,1350,22,760,520,50) + """
<div class="glow" style="width:760px;height:760px;right:-120px;top:230px"></div>
<h1 class="abs" style="left:56px;top:70px;font-size:88px;width:640px;z-index:8;letter-spacing:-3px">Tu biblioteca<br>legal <span class="or">en tu<br>bolsillo.</span></h1>
<div class="phone" style="right:46px;top:300px;transform:rotate(7deg)">
  <div class="top"><div class="av">L</div><div class="nm">Lexa<small>asistente legal</small></div></div>
  <div class="body">
    <div class="bub q" style="width:88%;margin-left:12%">¿Qué dice el Código Civil sobre el contrato?</div>
    <div class="bub a" style="width:92%">Te respondo con el artículo. <br><span class="chip" style="font-size:22px;margin-top:10px">Cita su ley</span></div>
    <div class="bub a" style="width:78%;font-size:24px">Apoyo de consulta: la decisión es tuya.</div>
  </div></div>
<img class="edu" src="edu-cut.webp" style="left:-40px;bottom:150px;height:530px;z-index:9">
<div class="abs" style="left:56px;top:420px;z-index:8;font-size:40px;font-weight:700;line-height:1.2;width:440px">En <span class="or">Telegram.</span></div>
<div class="abs" style="left:56px;top:490px;z-index:8"><span class="btn" style="font-size:30px;display:block;width:400px">Escribe <b>LEXA</b><br>0961228420</span></div>
""" + band())

# 3 MIE story - antes / ahora (pantalla dividida)
docs = ''.join(f'<div class="doc" style="left:{x}px;top:{y}px;transform:rotate({r}deg);z-index:{z}"><i style="width:80%"></i><i></i><i style="width:90%"></i><i></i><i style="width:60%"></i><i></i><i style="width:85%"></i><i></i></div>'
               for x,y,r,z in [(60,250,-9,2),(300,210,6,3),(560,270,-4,2),(760,230,10,3),(180,420,3,4)])
P['3-miercoles-story-antes-ahora'] = ('story', '#0F2144', f"""
<div class="abs" style="left:0;top:0;right:0;height:900px;background:#2a3550;z-index:0;filter:saturate(.2)"></div>
{docs}
<div class="abs" style="left:56px;top:90px;z-index:9;font-size:60px;font-weight:700;letter-spacing:6px;color:#aab1c4">ANTES</div>
<div class="abs" style="left:56px;top:710px;z-index:9;font-size:84px;font-weight:800;line-height:1;color:#e7e9f1;text-shadow:0 8px 30px rgba(0,0,0,.6)">Horas entre<br>códigos y PDF.</div>
<div class="abs" style="left:0;right:0;top:900px;height:1020px;background:radial-gradient(900px 700px at 70% 70%,#24427f,#152C57 55%,#0F2144);z-index:0"></div>
<div class="abs" style="left:0;right:0;top:896px;height:10px;background:var(--or);z-index:10"></div>
<div class="abs" style="left:56px;top:960px;z-index:9;font-size:60px;font-weight:700;letter-spacing:6px;color:var(--or)">AHORA</div>
<h1 class="abs" style="left:56px;top:1050px;font-size:124px;z-index:9;line-height:.95">Pregunta.<br><span class="or">Lexa busca.</span></h1>
<img class="edu" src="edu-cut.webp" style="right:-40px;bottom:210px;height:600px;z-index:6">
<div class="abs" style="left:56px;top:1470px;z-index:9"><span class="btn" style="font-size:38px;display:block">Escribe <b>LEXA</b></span></div>
""" + band(210))

# 4 JUE post - Star Studio bots de WhatsApp: foto dentro de burbuja de chat
P['4-jueves-burbuja-bot'] = ('post', None, fx(1080,1350,44,540,560,50) + """
<div class="glow" style="width:820px;height:820px;left:140px;top:280px"></div>
<div class="abs" style="left:120px;top:858px;width:90px;height:70px;background:var(--or);clip-path:polygon(0 0,100% 0,0 100%);z-index:5"></div>
<div class="abs" style="left:70px;top:60px;z-index:9"><span class="tag">Bots de WhatsApp</span></div>
<div style="position:absolute;z-index:6;left:120px;top:160px;width:860px;height:700px;border-radius:120px 120px 120px 30px;border:16px solid var(--or);background:linear-gradient(180deg,#35599f,#1b3566);overflow:hidden;box-shadow:0 30px 90px rgba(0,0,0,.5),0 0 90px rgba(224,138,46,.35)">
  <img src="edu-cut.webp" style="position:absolute;left:110px;top:20px;width:600px"></div>
<div class="abs" style="left:56px;top:900px;z-index:8;font-size:100px;font-weight:800;letter-spacing:-3px;line-height:.98">Tu negocio<br><span class="or">responde.</span></div>
<div class="abs" style="left:60px;top:1112px;z-index:8;font-size:38px;font-weight:700">Tú atiendes lo importante.</div>
""" + band())

# 5 VIE post - 5 asientos fundadores
seats = ''.join(f'<div style="width:150px;height:150px;border-radius:50%;border:8px solid var(--or);background:radial-gradient(circle,#35599f,#1b3566);display:flex;align-items:center;justify-content:center;box-shadow:0 0 40px rgba(224,138,46,.35)"><img src="logo-star-icon.png" style="width:92px"></div>' for _ in range(5))
P['5-viernes-5-cupos'] = ('post', None, fx(1080,1350,55,540,330,50) + f"""
<div class="abs" style="left:0;right:0;top:80px;display:flex;gap:26px;justify-content:center;z-index:8">{seats}</div>
<div class="abs" style="left:0;right:0;top:270px;text-align:center;z-index:8"><span class="tag">Abogados fundadores</span></div>
<h1 class="abs" style="left:56px;top:350px;font-size:180px;z-index:8;line-height:.9;letter-spacing:-6px">5 CUPOS.<br><span class="or" style="font-size:128px">7 DÍAS GRATIS.</span></h1>
<div class="glow" style="width:700px;height:700px;right:-190px;top:600px"></div>
<img class="edu" src="edu-cut.webp" style="right:-70px;bottom:150px;height:530px;z-index:6">
<div class="abs" style="left:60px;top:760px;z-index:8;font-size:46px;font-weight:700;line-height:1.2;width:560px">Pruébala <span class="or">antes de pagar.</span></div>
<div class="abs" style="left:56px;top:1010px;z-index:9"><span class="btn" style="font-size:36px;display:block;width:520px">Escribe <b>LEXA</b><br>al 0961228420</span></div>
""" + band())

# 6 SAB story - sticker de pregunta sobre foto completa
P['6-sabado-story-pregunta'] = ('story', None, """
<div class="photo s" style="background-position:-330px 0"></div><div class="duo"></div>
<div class="shade" style="background:linear-gradient(180deg,rgba(15,33,68,.55) 0%,rgba(15,33,68,0) 30%,rgba(15,33,68,.25) 55%,rgba(15,33,68,.96) 82%)"></div>
<div class="abs" style="left:56px;top:120px;z-index:8"><span class="tag">Preguntas</span></div>
<div class="sticker" style="left:80px;top:1010px;width:920px;transform:rotate(-3deg)">
  <div style="font-size:30px;font-weight:700;letter-spacing:3px;color:#b86a17">PREGÚNTAME SOBRE LEXA</div>
  <div style="font-size:64px;font-weight:800;line-height:1.05;margin-top:14px;letter-spacing:-1px">¿Qué ley quieres<br>consultar primero?</div>
  <div style="margin-top:26px;height:84px;border-radius:42px;background:rgba(21,44,87,.10);display:flex;align-items:center;padding:0 34px;font-size:32px;color:#59627a;font-weight:600">Escribe tu respuesta…</div>
</div>
<div class="abs" style="left:56px;top:1470px;z-index:9"><span class="btn" style="font-size:38px;display:block">Escribe <b>LEXA</b> al 0961228420</span></div>
""" + band(210))

# 7 DOM post - bento editorial, voz personal
P['7-domingo-planea'] = ('post', '#0F2144', """
<div class="tile" style="left:40px;top:40px;width:560px;height:760px;background:url('hero2.webp') no-repeat;background-size:1100px auto;background-position:-250px -20px;border:6px solid var(--or)"></div>
<div class="tile" style="left:620px;top:40px;width:420px;height:370px;background:var(--or);color:var(--navy2);padding:34px">
  <div style="font-size:30px;font-weight:700;letter-spacing:3px">DOMINGO</div>
  <div style="font-size:96px;font-weight:800;line-height:.95;margin-top:14px;letter-spacing:-3px">Planea.</div></div>
<div class="tile" style="left:620px;top:430px;width:420px;height:370px;background:var(--cream);color:var(--navy2);padding:34px">
  <div style="font-size:30px;font-weight:700;letter-spacing:3px;color:#b86a17">LUNES</div>
  <div style="font-size:92px;font-weight:800;line-height:.95;margin-top:14px;letter-spacing:-3px">Ejecuta.</div></div>
<div class="tile" style="left:40px;top:830px;width:1000px;height:350px;background:linear-gradient(135deg,#1b3566,#152C57);border:2px solid rgba(242,181,68,.45);padding:44px 52px">
  <div style="font-size:86px;font-weight:800;line-height:1;letter-spacing:-3px">Una semana nueva.<br><span class="or">Una idea a la vez.</span></div>
  <div style="font-size:30px;font-weight:600;margin-top:22px;color:#cdd7f0">Edu Estrella · escríbeme y conversamos</div></div>
""" + band())

async def main():
    out = os.path.join(BASE, 'out3'); os.makedirs(out, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium' if os.path.exists('/opt/pw-browsers/chromium') else None)
        for name,(kind,bg,inner) in P.items():
            h = 1350 if kind=='post' else 1920
            path = os.path.join(BASE, f'{name}.html'); open(path,'w').write(page3(inner,kind,bg))
            pg = await b.new_page(viewport={'width':1080,'height':h}); await pg.goto('file://'+path)
            await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(400)
            await pg.screenshot(path=os.path.join(out,f'{name}.png')); await pg.close()
        await b.close()
asyncio.run(main())
