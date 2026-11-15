#!/usr/bin/env python3
"""Generador ligero de landing HTML autocontenida para GoHighLevel."""
import argparse
import html
import json
from pathlib import Path
from urllib.parse import urlparse

THEMES = {
    "institutional_ink": ("#152332", "#F8F7F4", "#FFFFFF", "#AFC0CD"),
    "tech_modern": ("#10213D", "#EDF5FC", "#FFFFFF", "#93C9EB"),
    "warm_editorial": ("#41362D", "#F8F2E8", "#FFFFFF", "#B99E80"),
}
def esc(v):
    return html.escape(str(v or ""), quote=True)
def build(config):
    ink, paper, white, accent = THEMES.get(config.get("theme"), THEMES["institutional_ink"])
    brand,headline = esc(config.get("brand","Consultoría")),esc(config.get("headline","Resolvemos problemas reales."))
    email=esc(config.get("email",""))
    desc=esc(config.get("description",""))
    services="".join(f'<article class="ghlw-card"><h3>{esc(s.get("title"))}</h3><p>{esc(s.get("description"))}</p></article>' for s in config.get("services",[]))
    calendar=config.get("calendar_url","")
    parsed=urlparse(calendar)
    if calendar and (parsed.scheme!="https" or not parsed.hostname):
        raise ValueError("calendar_url debe ser una URL HTTPS válida")
    embedded=(f'<iframe title="Reservar reunión" src="{esc(calendar)}" style="width:100%;height:740px;border:0;display:block" loading="eager" scrolling="no"></iframe><p><a href="{esc(calendar)}" target="_blank" rel="noopener">Abrir calendario en otra pestaña</a></p>' if calendar else '<p>Configura la URL permanente del calendario de GoHighLevel.</p>')
    return f'''<div id="ghlw-site">
<style>
#ghlw-site{{--ink:{ink};--paper:{paper};--accent:{accent};font-family:Inter,Arial,sans-serif;color:var(--ink);width:100%;}}
#ghlw-site *{{box-sizing:border-box}}#ghlw-site a{{color:inherit}}
#ghlw-site .ghlw-wrap{{width:min(1160px,calc(100% - 40px));margin:auto}}
#ghlw-site .ghlw-hero{{background:var(--ink);color:{white};min-height:100svh;display:flex;flex-direction:column}}
#ghlw-site header{{padding:25px 0;display:flex;justify-content:space-between;align-items:center;gap:20px}}
#ghlw-site header strong{{font-family:Georgia,serif;font-size:27px}}
#ghlw-site .ghlw-hero-body{{flex:1;display:flex;flex-direction:column;justify-content:center;padding:80px 0}}
#ghlw-site h1{{font-family:Georgia,serif;font-weight:400;font-size:clamp(42px,6vw,88px);line-height:1.06;max-width:980px;margin:20px 0}}
#ghlw-site h2{{font-family:Georgia,serif;font-size:clamp(32px,4vw,56px);font-weight:400}}
#ghlw-site .ghlw-hero p{{max-width:690px;color:#D5DEE5;font-size:19px;line-height:1.6}}
#ghlw-site .ghlw-btn{{display:inline-block;padding:15px 24px;background:{paper};color:{ink};text-decoration:none;font-weight:650;border-radius:3px;margin-top:24px}}
#ghlw-site section{{padding:90px 0;background:var(--paper)}}
#ghlw-site .ghlw-grid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}}
#ghlw-site .ghlw-card{{border:1px solid #CAD1D6;padding:28px;min-width:0;background:#FFF}}
#ghlw-site .ghlw-card p{{line-height:1.6}}
#ghlw-site .ghlw-agenda{{background:{white}}}
#ghlw-site iframe{{max-width:100%}}
@media(max-width:680px){{#ghlw-site .ghlw-grid{{grid-template-columns:1fr}}#ghlw-site section{{padding:60px 0}}#ghlw-site header{{align-items:flex-start}}}}
</style>
<div class="ghlw-hero"><div class="ghlw-wrap"><header><strong>{brand}</strong><a href="#ghlw-agenda">Agenda una reunión</a></header></div><div class="ghlw-wrap ghlw-hero-body"><div>{esc(config.get("tagline",""))}</div><h1>{headline}</h1><p>{desc}</p><div><a class="ghlw-btn" href="#ghlw-agenda">Agendar diagnóstico →</a></div></div></div>
<section><div class="ghlw-wrap"><h2>Qué hacemos</h2><div class="ghlw-grid">{services}</div></div></section>
<section class="ghlw-agenda" id="ghlw-agenda"><div class="ghlw-wrap"><h2>Hablemos de tu proyecto</h2>{embedded}<p>Contacto: <a href="mailto:{email}">{email}</a></p></div></section>
</div>'''
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--config",required=True)
    p.add_argument("--out",default="outputs")
    a=p.parse_args()
    cfg=json.loads(Path(a.config).read_text(encoding="utf-8"))
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    slug="".join(ch.lower() if ch.isalnum() else "-" for ch in cfg.get("brand","site")).strip("-")
    fragment=build(cfg)
    (out/f"{slug}-ghl.html").write_text(fragment,encoding="utf-8")
    (out/f"{slug}-preview.html").write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(cfg.get("brand","Site"))}</title></head><body style="margin:0">{fragment}</body></html>',encoding="utf-8")
    print("Generated:",out/f"{slug}-ghl.html",out/f"{slug}-preview.html")
if __name__=="__main__":main()
