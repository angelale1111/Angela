import base64

def font_b64(name):
    with open(f"/home/claude/fonts_b64/{name}.b64") as f:
        return f.read()

def photo_b64(name):
    with open(f"/home/claude/photos/{name}.jpg.b64") as f:
        return f.read()

# Angela's actual uploaded photo for the Writing banner (striped sweater, mug).
placeholder_photo = photo_b64("angela-writing-real")

FONT_FACES = f"""
@font-face {{ font-family: 'Lora'; font-style: normal; font-weight: 400; src: url(data:font/woff2;base64,{font_b64('lora-400')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Playfair Display'; font-style: normal; font-weight: 400; src: url(data:font/woff2;base64,{font_b64('playfair-400')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Playfair Display'; font-style: normal; font-weight: 500; src: url(data:font/woff2;base64,{font_b64('playfair-500')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Cormorant Garamond'; font-style: italic; font-weight: 300; src: url(data:font/woff2;base64,{font_b64('cormorant-300-italic')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Cormorant Garamond'; font-style: normal; font-weight: 300; src: url(data:font/woff2;base64,{font_b64('cormorant-300-normal')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Inter'; font-style: normal; font-weight: 300; src: url(data:font/woff2;base64,{font_b64('inter-300')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Inter'; font-style: normal; font-weight: 500; src: url(data:font/woff2;base64,{font_b64('inter-500')}) format('woff2'); font-display: swap; }}
"""

def build():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Writing — Dr. Angela Le</title>
<style>
{FONT_FACES}
  :root {{
    --dark: #2C2A31;
    --light: #EFEFED;
    --ink: #4B4B52;
    --gold: #ADA79C;
    --gold-light: #CFCAC0;
    --gold-dark: #8C877C;
  }}
  * {{ box-sizing: border-box; }}
  a {{ text-decoration: none; color: inherit; }}
  body {{ margin: 0; font-family: 'Lora', serif; color: var(--ink); background: var(--light); line-height: 1.9; }}

  .label {{ font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.2em; color: var(--gold-dark); }}

  .gold-rule {{ width: 40px; height: 1px; background: var(--gold); opacity: 0.6; margin: 0 auto; }}

  /* HEADER */
  .site-header {{ background: var(--dark); padding: 1.4rem 0; }}
  .site-header-inner {{ display: flex; align-items: center; justify-content: space-between; padding: 0 2.5rem; }}
  .site-header .logo {{ font-family: 'Playfair Display', serif; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.18em; color: rgba(255,255,255,0.9); }}
  .site-header nav {{ display: flex; gap: 1.75rem; }}
  .site-header nav a {{ font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.14em; color: rgba(255,255,255,0.6); }}
  .site-header nav a.active {{ color: var(--gold); }}

  /* WRITING SECTION — Option 3: centered, stacked, photo above the line.
     Reuses the exact structure and sizing of the homepage's own "The Writing"
     section (build_home.py: .sub-wrap / .sub-text / .script-line), so this
     page matches it exactly instead of approximating it. */
  .writing-section {{ background: var(--light); padding: 5rem 2.5rem; }}
  .sub-wrap {{ max-width: 480px; margin: 0 auto; text-align: center; }}
  .writing-photo {{ display: block; width: 260px; height: 325px; margin: 0 auto 2.5rem; object-fit: cover; object-position: 50% 0%; background: #D8D5CE; }}
  .sub-text .label {{ letter-spacing: 0.2em; color: var(--gold-dark); margin-bottom: 1rem; }}
  .script-line {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; margin: 0 0 0.9rem; }}
  .script-line.big {{ font-size: 1.875rem; color: var(--ink); line-height: 1.45; letter-spacing: 0.01em; }}

  .btn {{ display: inline-flex; align-items: center; justify-content: center; border: 1px solid; padding: 1rem 2rem; font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.12em; transition: background 0.2s, color 0.2s; }}
  .btn-secondary {{ border-color: var(--dark); background: var(--dark); color: var(--light); }}
  .substack-link {{ display: inline-block; padding: 0.9rem 2rem; border: 1px solid var(--gold-dark); font-family: 'Inter', sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.14em; font-size: 0.688rem; color: var(--gold-dark); transition: background 0.2s, color 0.2s; }}

  /* FOOTER — dark, since the section above it here is light */
  .site-footer {{ background: var(--dark); border-top: 1px solid rgba(255,255,255,0.08); padding: 2.5rem 1.5rem; text-align: center; }}
  .site-footer .footer-nav {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 1.5rem 1.5rem; }}
  .site-footer .footer-nav a {{ font-family: 'Inter', sans-serif; font-weight: 300; text-transform: uppercase; letter-spacing: 0.18em; font-size: 0.688rem; color: #ffffff; }}
  .site-footer .copyright {{ margin-top: 2rem; font-size: 0.75rem; color: #ffffff; }}
  .site-footer .legal-row {{ margin-top: 0.75rem; display: flex; justify-content: center; gap: 0.5rem; font-size: 0.75rem; color: #ffffff; }}
</style>
</head>
<body>

<header class="site-header">
  <div class="site-header-inner">
    <a href="index.html" class="logo" style="text-decoration:none;">Dr. Angela Le</a>
    <nav>
      <a href="about.html">About</a>
      <a href="offerings.html">Offerings</a>
      <a href="kind-words.html">Kind Words</a>
      <a href="writing.html" class="active">Writing</a>
      <a href="connect.html">Connect</a>
    </nav>
  </div>
</header>

<section class="writing-section">
  <div class="sub-wrap">
    <img class="writing-photo" src="data:image/jpeg;base64,{placeholder_photo}" alt="Dr. Angela Le">
    <div class="sub-text">
      <p class="label">The Writing</p>
      <p class="script-line big">Each piece is a doorway back to yourself.</p>
      <a href="#" class="substack-link">Subscribe on Substack &rarr;</a>
    </div>
  </div>
</section>

<footer class="site-footer">
  <nav class="footer-nav">
    <a href="about.html">About</a>
    <a href="offerings.html">Offerings</a>
    <a href="kind-words.html">Kind Words</a>
    <a href="writing.html">Writing</a>
    <a href="connect.html">Connect</a>
  </nav>
  <p class="copyright">&copy; 2026 Dr. Angela Le</p>
  <div class="legal-row">
    <a href="#">Privacy Policy</a>
    <span>&middot;</span>
    <a href="#">Terms &amp; Conditions</a>
    <span>&middot;</span>
    <a href="#">Accessibility</a>
  </div>
</footer>

</body>
</html>
"""

with open("/home/claude/writing-redesign.html", "w") as f:
    f.write(build())

print("done")
