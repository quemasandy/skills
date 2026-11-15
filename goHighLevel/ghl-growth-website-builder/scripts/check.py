#!/usr/bin/env python3
"""Validación estática básica del output generado por build.py."""
import argparse
from pathlib import Path
import json
p=argparse.ArgumentParser()
p.add_argument("--config",required=True)
p.add_argument("--out",default="outputs")
a=p.parse_args()
cfg=json.loads(Path(a.config).read_text(encoding="utf-8"))
slug="".join(ch.lower() if ch.isalnum() else "-" for ch in cfg.get("brand","site")).strip("-")
fragment=Path(a.out,f"{slug}-ghl.html").read_text(encoding="utf-8")
assert 'id="ghlw-site"' in fragment
assert 'id="ghlw-agenda"' in fragment
assert "max-width:100%" in fragment
assert "<!doctype" not in fragment.lower()
assert 'href="#ghlw-agenda"' in fragment
print("PASS: HTML de GHL y enlaces básicos")
