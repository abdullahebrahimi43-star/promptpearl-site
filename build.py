"""Builds the PromptPearl website pages from src/*.html bodies. Run: python build.py"""
import pathlib, re
ROOT = pathlib.Path(__file__).parent
SUPPORT = "promptpearl.support@gmail.com"
COMPANY = "PrimeEdge Solutions LLC"
EFFECTIVE = "November 4, 2026"
NAV = [("privacy.html", "Privacy"), ("terms.html", "Terms"), ("content-policy.html", "Content Policy"),
       ("subscriptions.html", "Subscriptions & Refunds"), ("delete-account.html", "Delete account")]

def page(title, body, desc):
    nav = "".join(f'<a href="{href}">{label}</a>' for href, label in NAV)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · PromptPearl AI</title><meta name="description" content="{desc}">
<link rel="stylesheet" href="style.css"></head>
<body><header><div class="wrap"><nav><a class="brand" href="index.html">PromptPearl AI</a>{nav}</nav></div></header>
<main><div class="wrap">
{body}
</div></main>
<footer><div class="wrap">© 2026 {COMPANY} · Virginia, USA · <a href="mailto:{SUPPORT}">{SUPPORT}</a></div></footer>
</body></html>
"""

for src in sorted((ROOT / "src").glob("*.html")):
    text = src.read_text(encoding="utf-8")
    m = re.match(r"<!--\s*title:(.*?)\|\s*desc:(.*?)-->\s*", text, re.S)
    title, desc = m.group(1).strip(), m.group(2).strip()
    body = text[m.end():].replace("{{SUPPORT}}", SUPPORT).replace("{{COMPANY}}", COMPANY).replace("{{EFFECTIVE}}", EFFECTIVE)
    (ROOT / src.name).write_text(page(title, body, desc), encoding="utf-8")
    print("built", src.name)
