import asyncio, os
from playwright.async_api import async_playwright
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build.py')).read().split("pieces = {}")[0]
exec(src)

X = """
.outl{-webkit-text-stroke:3px rgba(245,241,232,.55);color:transparent}
.outl-or{-webkit-text-stroke:4px var(--or);color:transparent}
.ray{position:absolute;z-index:1;left:50%;top:50%;width:2600px;height:2600px;margin:-1300px 0 0 -1300px;
 background:repeating-conic-gradient(from 0deg,rgba(224,138,46,.20) 0 7deg,transparent 7deg 20deg);
 -webkit-mask:radial-gradient(circle,#000 0,transparent 55%);mask:radial-gradient(circle,#000 0,transparent 55%)}
.cream{background:var(--cream);color:var(--navy2)}
.nt{position:absolute;z-index:9;border-radius:28px;padding:26px 32px;background:rgba(245,241,232,.96);color:var(--navy2);box-shadow:0 20px 50px rgba(0,0,0,.45)}
"""
CSS2 = CSS + X
def page2(inner, kind, bg=None):
    st = f' style="background:{bg}"' if bg else ''
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS2}</style></head><body><div class='c {kind}'{st}>{inner}</div></body></html>"

P = {}
# 1 LUN post — texto DETRÁS de Edu + rayos de luz (efecto nuevo: profundidad)
P['1-lunes-8-leyes'] = ('post', None, fx(1080,1350,11,540,620,50) + '<div class="ray" style="top:620px"></div>' + f"""
<div class="abs" style="left:0;right:0;top:70px;text-align:center"><span class="tag">Lexa · asistente legal</span></div>
<h1 class="abs outl" style="left:40px;top:120px;font-size:640px;letter-spacing:-20px;z-index:3;line-height:1">8</h1>
<h1 class="abs" style="left:56px;top:700px;font-size:200px;z-index:3;color:var(--cream);letter-spacing:-6px">LEYES</h1>
<div class="glow" style="width:700px;height:700px;right:-160px;top:380px"></div>
<img class="edu" src="edu-cut.webp" style="right:-120px;bottom:150px;height:1010px;z-index:6">
<div class="abs" style="left:56px;top:960px;z-index:8;font-size:52px;font-weight:700;line-height:1.15">Un solo <span class="or">chat.</span></div>
<div class="abs" style="left:56px;top:1060px;z-index:8"><span class="btn" style="font-size:38px;display:block">Escribe <b>LEXA</b> al 0961228420</span></div>
""" + band())

# 2 MAR post — diagonal crema/marino (emocional)
P['2-martes-tiempo'] = ('post', None, f"""
<div class="abs" style="inset:0;z-index:1;background:var(--cream);clip-path:polygon(0 0,62% 0,38% 100%,0 100%)"></div>
<div class="glow" style="width:760px;height:760px;right:-180px;top:380px"></div>
<h1 class="abs" style="left:56px;top:84px;font-size:100px;color:var(--navy2);z-index:3;width:560px">Tu tiempo<br>vale más<br>que un <span style="color:var(--or)">PDF.</span></h1>
<div class="abs" style="left:56px;top:640px;z-index:3;font-size:44px;font-weight:700;color:var(--navy2);line-height:1.2;width:420px">Pregúntale a Lexa.<br>Ella busca el artículo.</div>
<img class="edu" src="edu-cut.webp" style="right:-120px;bottom:150px;height:960px;z-index:6">
<div class="abs" style="left:56px;top:1010px;z-index:8"><span class="btn" style="font-size:38px;display:block">Escribe <b>LEXA</b> al 0961228420</span></div>
""" + band())

# 3 MIÉ story — notificaciones antes de la audiencia (mock UI)
P['3-miercoles-story-audiencia'] = ('story', None, fx(1080,1920,33,540,900,60) + f"""
<div class="abs" style="left:64px;top:150px;z-index:8"><span class="tag">Antes de la audiencia</span></div>
<h1 class="abs" style="left:56px;top:240px;font-size:300px;letter-spacing:-12px;z-index:8;color:var(--cream)">7:40</h1>
<div class="abs" style="left:64px;top:560px;font-size:56px;font-weight:700;z-index:8;line-height:1.1">Audiencia a las <span class="or">9:00.</span></div>
<div class="nt" style="left:64px;top:700px;width:760px"><div style="font-size:24px;font-weight:700;letter-spacing:2px;color:#9a5a12">TÚ</div><div style="font-size:38px;font-weight:600;line-height:1.25;margin-top:6px">¿Qué artículo regula la prueba testimonial?</div></div>
<div class="nt" style="left:150px;top:880px;width:850px;background:var(--navy2);color:var(--cream);border:3px solid rgba(224,138,46,.6)"><div style="font-size:24px;font-weight:700;letter-spacing:2px;color:var(--or)">LEXA</div><div style="font-size:38px;font-weight:600;line-height:1.25;margin-top:6px">Te la encuentro con su artículo, en segundos.</div></div>
<div class="glow" style="width:700px;height:700px;right:-200px;top:1180px"></div>
<img class="edu" src="edu-cut.webp" style="right:-60px;bottom:210px;height:600px;z-index:5">
<div class="abs" style="left:64px;top:1420px;z-index:8"><span class="btn" style="font-size:38px;display:block">Escribe <b>LEXA</b></span></div>
""" + band(210))

# 4 JUE post — Star Studio bots: reloj nocturno gigante
P['4-jueves-bot-noche'] = ('post', None, fx(1080,1350,44,300,500,45) + f"""
<h1 class="abs outl" style="left:0;right:0;top:20px;text-align:center;font-size:330px;letter-spacing:-10px;z-index:3">11:48</h1>
<div class="abs" style="left:0;right:0;top:350px;text-align:center;z-index:8"><span class="tag">pm · tu negocio sigue abierto</span></div>
<div class="glow" style="width:640px;height:640px;left:80px;top:500px"></div>
<div style="position:absolute;z-index:6;left:70px;top:470px;width:400px;height:400px;border-radius:50%;border:14px solid var(--or);background:#1b3566;overflow:hidden"><img src="edu-cut.webp" style="position:absolute;left:-40px;top:20px;width:480px"></div>
<div class="abs" style="left:520px;top:470px;width:500px;z-index:8"><div class="bub q" style="font-size:36px">Hola, ¿tienen disponible para mañana?</div></div>
<div class="abs" style="left:520px;top:690px;width:500px;z-index:8"><div class="bub a" style="font-size:36px">¡Claro! Te ayudo ahora mismo.</div></div>
<h1 class="abs" style="left:56px;top:900px;font-size:78px;z-index:8;width:960px;line-height:1.02">Un bot de WhatsApp<br><span class="or">que atiende por ti.</span></h1>
<div class="abs" style="left:56px;top:1085px;z-index:8"><span class="btn" style="font-size:34px;display:block">Escribe <b>BOT</b> al 0961228420</span></div>
""" + band())

# 5 VIE post — pase fundador (boarding pass)
P['5-viernes-pase-fundador'] = ('post', None, f"""
<div class="glow" style="width:900px;height:900px;left:90px;top:0"></div>
<img class="edu" src="edu-cut.webp" style="left:50%;margin-left:-260px;top:50px;height:900px;z-index:4">
<div class="abs" style="left:-30px;right:-30px;top:690px;height:410px;z-index:8;transform:rotate(-5deg);background:var(--or);color:var(--navy2);border-radius:28px;box-shadow:0 30px 70px rgba(0,0,0,.55);display:flex;overflow:hidden">
  <div style="flex:1;padding:44px 40px 0 80px"><div style="font-size:28px;font-weight:800;letter-spacing:5px">PASE FUNDADOR · LEXA</div>
  <div style="font-size:190px;font-weight:800;letter-spacing:-8px;line-height:1;margin-top:6px">7 DÍAS</div>
  <div style="font-size:70px;font-weight:800;line-height:1;margin-top:4px">GRATIS</div></div>
  <div style="width:0;border-left:6px dashed var(--navy2);margin:24px 0"></div>
  <div style="width:290px;padding:44px 20px;text-align:center"><div style="font-size:30px;font-weight:700">SOLO</div><div style="font-size:190px;font-weight:800;line-height:.95">5</div><div style="font-size:30px;font-weight:700">CUPOS</div></div>
</div>
<div class="abs" style="left:0;right:0;top:1105px;text-align:center;z-index:9"><span style="font-size:42px;font-weight:700">Escribe <span class="or">LEXA</span> al WhatsApp</span></div>
""" + band())

# 6 SÁB story — 3 pasos
steps = [("1","Preguntas"),("2","Lexa cita el artículo"),("3","Tú decides")]
st = "".join(f'<div style="display:flex;align-items:center;gap:36px;margin-bottom:56px"><div style="font-size:230px;font-weight:800;line-height:.8;letter-spacing:-8px;color:transparent;-webkit-text-stroke:4px var(--or)">{n}</div><div style="font-size:64px;font-weight:800;line-height:1.05;width:420px">{t}</div></div>' for n,t in steps)
P['6-sabado-story-3-pasos'] = ('story', None, fx(1080,1920,66,300,1000,60) + f"""
<h1 class="abs" style="left:56px;top:170px;font-size:140px;z-index:8">Así de <span class="or">simple.</span></h1>
<div class="abs" style="left:64px;top:520px;z-index:8;width:600px">{st}</div>
<div class="glow" style="width:760px;height:760px;right:-240px;top:1000px"></div>
<img class="edu" src="edu-cut.webp" style="right:-120px;bottom:210px;height:820px;z-index:5">
<div class="abs" style="left:64px;top:1400px;z-index:9"><span class="btn" style="font-size:40px;display:block">Escribe <b>LEXA</b> al 0961228420</span></div>
""" + band(210))

# 7 DOM post — editorial crema, Edu en arco
P['7-domingo-criterio'] = ('post', 'var(--cream)', f"""
<div class="abs" style="right:40px;top:90px;width:430px;height:900px;border-radius:260px 260px 0 0;background:linear-gradient(180deg,#24427f,#0F2144);z-index:2;overflow:hidden;border:14px solid var(--or);border-bottom:0">
  <img src="edu-cut.webp" style="position:absolute;left:-90px;bottom:0;width:600px"></div>
<h1 class="abs" style="left:56px;top:110px;font-size:100px;color:var(--navy2);z-index:3;width:560px;letter-spacing:-3px">Tu<br>criterio.<br><span style="color:var(--or)">Mi IA.</span></h1>
<div class="abs" style="left:56px;top:690px;z-index:3;font-size:42px;font-weight:700;color:var(--navy2);line-height:1.2;width:420px">Desde Cayambe,<br>para toda la semana.</div>
<div class="abs" style="left:56px;top:880px;z-index:3;font-size:34px;font-weight:600;color:var(--navy);line-height:1.2">Edu Estrella<br><span style="color:#b86a17;font-weight:700">Star IA Solutions</span></div>
""" + band())

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium' if os.path.exists('/opt/pw-browsers/chromium') else None)
        for name,(kind,bg,inner) in P.items():
            h = 1350 if kind=='post' else 1920
            path = os.path.join(BASE, f'{name}.html'); open(path,'w').write(page2(inner,kind,bg))
            pg = await b.new_page(viewport={'width':1080,'height':h}); await pg.goto('file://'+path)
            await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(300)
            await pg.screenshot(path=os.path.join(BASE,'out2',f'{name}.png')); await pg.close()
        await b.close()
asyncio.run(main())
