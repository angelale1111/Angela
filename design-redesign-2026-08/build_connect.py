import base64

def font_b64(name):
    with open(f"/home/claude/fonts_b64/{name}.b64") as f:
        return f.read()

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
<title>Connect — Dr. Angela Le</title>
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

  .label {{ font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.2em; }}
  .label.gold-dark {{ color: var(--gold-dark); }}

  .gold-rule {{ width: 40px; height: 1px; background: var(--gold); opacity: 0.6; margin: 0 auto; }}
  .hairline {{ width: 40px; height: 1px; background: var(--gold); opacity: 0.6; margin: 0 auto; }}

  /* SITE HEADER */
  .site-header {{ background: var(--dark); padding: 1.4rem 0; }}
  .site-header-inner {{ display: flex; align-items: center; justify-content: space-between; padding: 0 2.5rem; }}
  .site-header .logo {{ font-family: 'Playfair Display', serif; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.18em; color: rgba(255,255,255,0.9); }}
  .site-header nav {{ display: flex; gap: 1.75rem; }}
  .site-header nav a {{ font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.14em; color: rgba(255,255,255,0.6); }}
  .site-header nav a.active {{ color: var(--gold); }}

  /* MAIN — light. Heading lives here directly (no separate dark hero band),
     the same simplification already used on the About page. */
  .connect-main {{ background: var(--light); padding: 4.5rem 1.5rem 4rem; text-align: center; }}
  .connect-main-wrap {{ max-width: 480px; margin: 0 auto; }}
  .connect-main-wrap h1 {{ font-family: 'Playfair Display', serif; font-weight: 400; font-size: 2rem; letter-spacing: 0.04em; text-transform: uppercase; color: var(--dark); margin: 1rem 0 1.4rem; }}

  .connect-block {{ margin-top: 3rem; }}
  .connect-block p.body {{ font-size: 1.0625rem; margin: 1rem 0 1.6rem; }}

  .btn {{ display: inline-flex; align-items: center; justify-content: center; border: 1px solid; padding: 1rem 2rem; font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.12em; transition: background 0.2s, color 0.2s; }}
  .btn-secondary {{ border-color: var(--dark); background: var(--dark); color: var(--light); }}
  .btn-primary {{ border-color: var(--gold-light); background: var(--gold-light); color: var(--dark); }}
  .btn-ghost {{ border-color: rgba(255,255,255,0.35); background: transparent; color: rgba(255,255,255,0.6); }}

  .connect-location {{ margin-top: 3rem; padding-top: 2rem; border-top: 1px solid rgba(173,167,156,0.3); font-family: 'Inter', sans-serif; font-size: 0.62rem; text-transform: uppercase; letter-spacing: 0.18em; color: var(--gold-dark); opacity: 0.85; }}

  /* BEGIN WITH THE WRITING — dark, matches the Offerings page's closing CTA */
  .writing-cta {{ background: var(--dark); padding: 4.5rem 1.5rem; text-align: center; }}
  .writing-cta-inner {{ max-width: 560px; margin: 0 auto; }}
  .writing-cta h2 {{ font-family: 'Playfair Display', serif; font-weight: 400; font-size: 1.1rem; letter-spacing: 0.04em; text-transform: uppercase; color: rgba(255,255,255,0.9); margin: 0 0 1.6rem; }}

  /* FOOTER — light, since the section above it here is dark (matches Offerings) */
  .site-footer {{ background: var(--light); border-top: 1px solid rgba(75,75,82,0.12); padding: 2.5rem 1.5rem; text-align: center; }}
  .site-footer .footer-nav {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 1.5rem 1.5rem; }}
  .site-footer .footer-nav a {{ font-family: 'Inter', sans-serif; font-weight: 300; text-transform: uppercase; letter-spacing: 0.18em; font-size: 0.688rem; color: var(--ink); }}
  .site-footer .copyright {{ margin-top: 2rem; font-size: 0.75rem; color: var(--ink); }}
  .site-footer .legal-row {{ margin-top: 0.75rem; display: flex; justify-content: center; gap: 0.5rem; font-size: 0.75rem; color: var(--ink); }}
</style>
</head>
<body>

<header class="site-header">
  <div class="site-header-inner">
    <a href="index.html" class="logo" style="text-decoration:none;">Dr. Angela Le</a>
    <nav>
      <a href="about.html">About</a>
      <a href="offerings.html">Offerings</a>
      <a href="#">Kind Words</a>
      <a href="writing.html">Writing</a>
      <a href="connect.html" class="active">Connect</a>
    </nav>
  </div>
</header>

<section class="connect-main">
  <div class="connect-main-wrap">
    <p class="label gold-dark">Connect</p>
    <h1>Contact</h1>
    <div class="hairline"></div>

    <div class="connect-block">
      <p class="label gold-dark">Consultation</p>
      <p class="body">Reproductive health consultations happen through my clinical practice in New York City.</p>
      <a href="https://fafwellness.com" target="_blank" class="btn btn-secondary">Visit Fifth Avenue Fertility Wellness</a>
    </div>

    <div class="connect-block">
      <p class="label gold-dark">Mentorship</p>
      <p class="body">Mentorship is a private relationship over six to nine months, with support between sessions and priority scheduling. It begins with an application.</p>
      <a href="mailto:info@angelale.com?subject=Mentorship%20Application" class="btn btn-primary">Submit a Mentorship Application &rarr;</a>
    </div>

    <p class="connect-location">In Person in New York City &middot; Virtual Everywhere</p>
  </div>
</section>

<section class="writing-cta">
  <div class="writing-cta-inner">
    <h2>Begin With the Writing</h2>
    <a href="https://substack.com/@drangelale" class="btn btn-ghost">Subscribe on Substack &rarr;</a>
  </div>
</section>

<footer class="site-footer">
  <nav class="footer-nav">
    <a href="about.html">About</a>
    <a href="offerings.html">Offerings</a>
    <a href="#">Kind Words</a>
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

with open("/home/claude/connect-redesign.html", "w") as f:
    f.write(build())

print("done")
