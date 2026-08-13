import base64

def b64(name):
    with open(f"/home/claude/photos/{name}.jpg.b64") as f:
        return f.read()

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

# Verbatim, from the live Lovable homepage quote carousel (src/components/site/HomeSections.tsx).
# Do not substitute other names or invent additional quotes.
TESTIMONIALS = [
    ("Susan", "My business went from pre-revenue and fledgling to self-sustaining and thriving, not because I worked harder, but because I worked differently. Angela is an alchemist. She doesn’t fix you; she reveals what was always there, waiting."),
    ("Darcy", "With Angela’s guidance I started to view life’s challenges differently, realizing my capacity for happiness and peace, which continues to grow daily. I am not the same person I was a year ago and that is largely due to my work with Angela."),
    ("Sally", "Working with Angela has been a transformative experience that has profoundly impacted my life. What I treasure most is the personal transformation she has facilitated — a journey towards becoming a more present, compassionate, and calmer individual."),
    ("Amy", "For years, sex felt routine and like just another task on our to-do list. Angela’s insight, particularly her powerful invitation for us to take full responsibility for our pleasure, struck a chord with my partner and I."),
    ("Laurie", "While working with Angela, I felt I was her only client. She is so much more than an acupuncturist. To me, she is a physical healer, spiritual teacher, and coach. Honestly, if I had one wish for the world, it would be that everyone finds their own Angela."),
]

kind_words_img = b64("kind-words-photo")

def build():
    testimonial_sections = ""
    for i, (name, quote) in enumerate(TESTIMONIALS):
        bg = "dark" if i % 2 == 0 else "light"
        testimonial_sections += f"""
<section class="kw-block {bg}">
  <div class="kw-block-inner">
    <p class="kw-quote">{quote}</p>
    <p class="kw-name">{name}</p>
  </div>
</section>
"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Kind Words — Dr. Angela Le</title>
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

  /* SITE HEADER */
  .site-header {{ background: var(--dark); padding: 1.4rem 0; }}
  .site-header-inner {{ display: flex; align-items: center; justify-content: space-between; padding: 0 2.5rem; }}
  .site-header .logo {{ font-family: 'Playfair Display', serif; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.18em; color: rgba(255,255,255,0.9); }}
  .site-header nav {{ display: flex; gap: 1.75rem; }}
  .site-header nav a {{ font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.14em; color: rgba(255,255,255,0.6); }}
  .site-header nav a.active {{ color: var(--gold); }}

  /* INTRO — light, matches the homepage carousel's visual language */
  .kw-intro {{ background: var(--light); padding: 5rem 1.5rem 4rem; text-align: center; }}
  .kw-intro-photo {{ display: block; width: 300px; height: 200px; margin: 0 auto 2.5rem; object-fit: cover; object-position: 50% 35%; }}
  .kw-intro .label {{ color: var(--gold-dark); margin-bottom: 1.2rem; }}
  .kw-intro p.sub {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; font-size: 1.5rem; color: var(--ink); max-width: 480px; margin: 0 auto; line-height: 1.5; }}

  /* TESTIMONIAL BLOCKS — alternating dark/light, matching site rhythm */
  .kw-block {{ padding: 4.5rem 1.5rem; text-align: center; }}
  .kw-block.dark {{ background: var(--dark); }}
  .kw-block.light {{ background: var(--light); }}
  .kw-block-inner {{ max-width: 560px; margin: 0 auto; }}
  .kw-quote {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; font-size: 1.4rem; line-height: 1.6; }}
  .kw-block.dark .kw-quote {{ color: rgba(255,255,255,0.85); }}
  .kw-block.light .kw-quote {{ color: var(--ink); }}
  .kw-name {{ margin-top: 1.2rem; font-family: 'Inter', sans-serif; font-weight: 300; text-transform: uppercase; letter-spacing: 0.18em; font-size: 0.6rem; }}
  .kw-block.dark .kw-name {{ color: var(--gold); }}
  .kw-block.light .kw-name {{ color: var(--gold-dark); }}

  /* FOOTER — light, since the last testimonial block above it is dark (Laurie) */
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
      <a href="kind-words.html" class="active">Kind Words</a>
      <a href="writing.html">Writing</a>
      <a href="connect.html">Connect</a>
    </nav>
  </div>
</header>

<section class="kw-intro">
  <img class="kw-intro-photo" src="data:image/jpeg;base64,{kind_words_img}" alt="">
  <p class="label">Kind Words</p>
  <p class="sub">Five stories from women who have walked this path.</p>
</section>
{testimonial_sections}
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

with open("/home/claude/kindwords-redesign.html", "w") as f:
    f.write(build())

print("done")
