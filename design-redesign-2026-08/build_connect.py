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
  .annot {{ background: #fffbe0; color: #6b5b00; font-family: 'Inter', sans-serif; font-size: 0.75rem; text-align: center; padding: 0.6rem 1rem; line-height: 1.5; }}
  .annot b {{ display: block; margin-bottom: 0.3rem; }}

  .label {{ font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.2em; }}

  /* SITE HEADER */
  .site-header {{ background: var(--dark); padding: 1.4rem 0; }}
  .site-header-inner {{ display: flex; align-items: center; justify-content: space-between; padding: 0 2.5rem; }}
  .site-header .logo {{ font-family: 'Playfair Display', serif; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.18em; color: rgba(255,255,255,0.9); }}
  .site-header nav {{ display: flex; gap: 1.75rem; }}
  .site-header nav a {{ font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.14em; color: rgba(255,255,255,0.6); }}
  .site-header nav a.active {{ color: var(--gold); }}

  /* HERO */
  .connect-hero {{ background: var(--dark); padding: 5rem 1.5rem 3.5rem; text-align: center; }}
  .connect-hero .label {{ color: rgba(255,255,255,0.35); margin-bottom: 1.2rem; }}
  .connect-hero h1 {{ font-family: 'Playfair Display', serif; font-weight: 400; font-size: 2rem; letter-spacing: 0.04em; text-transform: uppercase; line-height: 1.3; color: rgba(255,255,255,0.9); margin: 0 0 1.4rem; }}
  .hairline {{ width: 40px; height: 1px; background: var(--gold); opacity: 0.6; margin: 0 auto; }}

  /* MAIN */
  .connect-main {{ background: var(--light); padding: 4rem 1.5rem 2.5rem; text-align: center; }}
  .connect-main-wrap {{ max-width: 460px; margin: 0 auto; }}
  .connect-main-wrap p.intro {{ font-size: 1.0625rem; line-height: 1.9; margin: 0 0 1.75rem; }}
  .connect-buttons {{ display: flex; flex-direction: column; align-items: center; gap: 1.25rem; }}
  .btn {{ display: inline-flex; align-items: center; justify-content: center; border: 1px solid; padding: 1rem 2rem; font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.12em; transition: background 0.2s, color 0.2s; }}
  .btn-secondary {{ border-color: var(--dark); background: var(--dark); color: var(--light); }}
  .btn-primary {{ border-color: var(--gold-light); background: var(--gold-light); color: var(--dark); }}
  .connect-location {{ margin-top: 0.4rem; padding-top: 0.25rem; font-family: 'Inter', sans-serif; font-size: 0.62rem; text-transform: uppercase; letter-spacing: 0.18em; color: var(--gold-dark); opacity: 0.85; }}

  /* START WITH THE WRITING */
  .connect-writing {{ background: var(--dark); padding: 4.5rem 1.5rem; text-align: center; }}
  .connect-writing-wrap {{ max-width: 560px; margin: 0 auto; }}
  .connect-writing .label {{ color: rgba(255,255,255,0.35); margin-bottom: 1rem; }}
  .connect-writing h2 {{ font-family: 'Playfair Display', serif; font-weight: 400; font-size: 1.5rem; letter-spacing: 0.04em; text-transform: uppercase; color: rgba(255,255,255,0.9); margin: 0 0 1.2rem; }}
  .connect-writing .sub-line {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; font-size: 1.125rem; color: rgba(255,255,255,0.55); margin: 0 0 1.75rem; }}
  .substack-link-dark {{ display: inline-block; padding: 0.9rem 2rem; border: 1px solid rgba(173,167,156,0.5); background: transparent; font-family: 'Inter', sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.14em; font-size: 0.688rem; color: var(--gold); transition: background 0.2s, color 0.2s; }}

  /* FOOTER */
  .site-footer {{ background: var(--dark); border-top: 1px solid rgba(255,255,255,0.08); padding: 2.5rem 1.5rem; text-align: center; }}
  .site-footer .footer-nav {{ display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 0.6rem 1.5rem; max-width: 700px; margin: 0 auto; }}
  .site-footer .footer-nav a {{ font-family: 'Inter', sans-serif; font-weight: 300; text-transform: uppercase; letter-spacing: 0.18em; font-size: 0.688rem; color: rgba(255,255,255,0.68); }}
  .site-footer .copyright {{ margin: 2rem 0 0; font-size: 0.75rem; letter-spacing: 0.02em; color: rgba(255,255,255,0.55); }}
  .site-footer .legal-row {{ margin-top: 0.75rem; display: flex; align-items: center; justify-content: center; gap: 0.5rem; font-size: 0.75rem; letter-spacing: 0.02em; color: rgba(255,255,255,0.55); }}
</style>
</head>
<body>

<div class="annot"><b>DRAFT — local preview only, nothing built into Lovable yet.</b>Copy is verbatim from the live Connect page source (already built in Lovable, just not linked here before).</div>

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

<section class="connect-hero">
  <p class="label">Connect</p>
  <h1>Contact</h1>
  <div class="hairline"></div>
</section>

<section class="connect-main">
  <div class="connect-main-wrap">
    <p class="intro">Reach out to schedule a consultation or begin a mentorship application.</p>
    <div class="connect-buttons">
      <a href="mailto:info@angelale.com?subject=Consultation%20Inquiry" class="btn btn-secondary">Email to Schedule a Consultation &rarr;</a>
      <a href="mailto:info@angelale.com?subject=Mentorship%20Application" class="btn btn-primary">Submit a Mentorship Application &rarr;</a>
    </div>
    <p class="connect-location">In Person in New York City &middot; Virtual Everywhere</p>
  </div>
</section>

<section class="connect-writing">
  <div class="connect-writing-wrap">
    <p class="label">Start With the Writing</p>
    <h2>Before You Begin</h2>
    <p class="sub-line">The writing is a place to start.</p>
    <a href="https://substack.com/@drangelale" class="substack-link-dark">Subscribe on Substack &rarr;</a>
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
