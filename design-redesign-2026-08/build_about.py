import base64

def b64(name):
    with open(f"/home/claude/photos/{name}.jpg.b64") as f:
        return f.read()

def font_b64(name):
    with open(f"/home/claude/fonts_b64/{name}.b64") as f:
        return f.read()

# Real font files (Lora 400, Playfair Display 400/500, Cormorant Garamond 300
# italic/normal, Inter 300/500) embedded directly as base64 @font-face data
# URIs. This removes any dependency on fonts.googleapis.com loading at
# render time — whatever viewer opens this file (browser, Lovable's file
# preview panel, etc.) will render the exact same font every time, with no
# risk of a silent fallback to a system serif if the external stylesheet
# request is blocked or slow.
FONT_FACES = f"""
@font-face {{ font-family: 'Lora'; font-style: normal; font-weight: 400; src: url(data:font/woff2;base64,{font_b64('lora-400')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Playfair Display'; font-style: normal; font-weight: 400; src: url(data:font/woff2;base64,{font_b64('playfair-400')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Playfair Display'; font-style: normal; font-weight: 500; src: url(data:font/woff2;base64,{font_b64('playfair-500')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Cormorant Garamond'; font-style: italic; font-weight: 300; src: url(data:font/woff2;base64,{font_b64('cormorant-300-italic')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Cormorant Garamond'; font-style: normal; font-weight: 300; src: url(data:font/woff2;base64,{font_b64('cormorant-300-normal')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Inter'; font-style: normal; font-weight: 300; src: url(data:font/woff2;base64,{font_b64('inter-300')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Inter'; font-style: normal; font-weight: 500; src: url(data:font/woff2;base64,{font_b64('inter-500')}) format('woff2'); font-display: swap; }}
"""

# Bio photo — recommended candidate (soft, contained expression, sleeveless v-neck).
# The other candidate (about-candidate-smile, big open smile, zip-front top) is also
# available below for comparison but is not the recommended default.
bio_photo = b64("about-candidate-soft")
bio_photo_alt = b64("about-candidate-smile")
story_photo = b64("two-ways-in")

credentials = [
    "Doctor of Acupuncture and Chinese Medicine",
    "Somatic Experiencing Practitioner",
    "In practice since 2001 · New York City",
]

bio_paragraphs = [
    "Dr. Le is a Doctor of Acupuncture and Chinese Medicine and one of the country&rsquo;s first integrative fertility acupuncturists. In twenty-five years, she has guided thousands of women through health challenges and major reproductive life transitions.",
    "Her training began under Master Ni and his sons, heirs to a 74-generation Taoist lineage. From that foundation, she built an integrated practice that draws on Traditional Chinese Medicine, health optimization and longevity science, Somatic Experiencing with a focus on sexual and medical trauma, and somatic sex education. What emerged from decades of study, clinical practice, and her own healing is a way of working that belongs to no single tradition and draws on all of them.",
    "Dr. Le is the founder of Fifth Avenue Fertility Wellness in New York City. This website is where she offers private consultations and ongoing mentorship, work that reaches beyond a single condition and meets women in the wider questions of health, intimacy, and authorship.",
    "She is a community leader for nonduality teacher David Bingham and writes on Substack. She lives in New York City.",
]

credential_rows = [
    ("As Featured In", "Huffington Post &middot; Motherly &middot; Mind Body Green &middot; Cup of Jo &middot; EmpowerHER &middot; Beyond Bulletproof"),
]

story_part_one = [
    "Long before I was a clinician, I was a young woman searching for answers no one seemed to have.",
    "At sixteen, a misdiagnosis set off a cascade of medical interventions. What followed were years of struggling with my health, leaving me physically and emotionally unrecognizable to myself. I felt alone inside my experience, trying to piece together a life that no longer felt like mine.",
    "That period changed everything. I now recognize it as the turning point. It dismantled everything I thought I knew and set me on a path I could not yet see.",
    "At twenty-two, I felt an overwhelming pull to visit India, sensing that healing would find me there. A series of impossible coincidences led me to an acupuncturist who was at home in herself in a way I had never seen. In her presence I recognized what I had been searching for. A way of being, lived.",
    "Her medicine became my doorway. I returned home and devoted myself to Traditional Chinese Medicine, and I began applying the medicine to my own health. I rebuilt my lifestyle from the ground up, by sheer will and discipline. And I healed nearly a decade of illness.",
]

story_part_two = [
    "Then came the car accident, and chronic pain that would follow for over a decade. Fear of the pain returning became a constant in me. I organized every hour around it. My whole world revolved around managing it, and the more I tried, the smaller my life became.",
    "One night, I found myself in the dark on the bathroom floor. And I heard a whisper.",
]

story_part_three = [
    "Fixing was all I knew. It had saved me once. Around that time, a therapist told me I had complex trauma. I fired him. My parents had survived a war. Who was I to admit I had trauma? But his words lingered, quiet and patient, the way true things are.",
    "Slowly, I saw what he had seen. Underneath all my control was a nervous system that had learned, before I had words, that the world was not safe. It had been generating my experience my whole life. Every symptom, every reaction, every pattern I had been managing from the outside was being produced from the inside. Fixing could not reach that deep.",
    "So I stopped fixing and began allowing. I began to create the safety my nervous system had never been given. As the trauma resolved, the pain released with it. My nervous system, no longer bracing for threat, opened to the life it had been guarding me from. Pleasure. Joy. Connection. A softer way of being.",
    "Today I experience an abundance of health, in a life I did not know was possible.",
    "I have come to see suffering as a signal, pointing us home. What we long for most is self-love, and it can take years of peeling back the layers to touch our truest self. Once we touch it, we come to know ourselves as love. The fixing ends.",
    "Everything I teach, I have lived. What I once called my calling turned out to be a doorway. Chinese medicine was the healing language I learned first. Walking alongside women as they come home to themselves is the language I was born to speak.",
]

def p_tags(paragraphs, cls):
    return "\n".join(f'<p class="{cls}">{p}</p>' for p in paragraphs)

def build(variant, photo=None):
    photo = photo or bio_photo
    if variant == "a":
        bio_block = f"""
    <div class="bio-photo">
      <img src="data:image/jpeg;base64,{photo}" alt="Dr. Angela Le">
    </div>
    {p_tags(bio_paragraphs, "bio-p")}
"""
        wrap_class = "bio-wrap"
    else:
        # Full reference layout: photo column on the left, entire bio text
        # block on the right — matching the angelale1111 reference screenshots.
        bio_block = f"""
    <div class="bio-columns">
      <div class="bio-photo-col">
        <img src="data:image/jpeg;base64,{photo}" alt="Dr. Angela Le">
      </div>
      <div class="bio-text-col">
        {p_tags(bio_paragraphs, "bio-p")}
      </div>
    </div>
"""
        wrap_class = "page-container"
    return _template(bio_block, wrap_class)

def _template(bio_block, wrap_class="bio-wrap"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>About — Redesign Preview</title>
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
  body {{ margin: 0; font-family: 'Lora', serif; color: var(--ink); background: var(--light); }}
  .annot {{ background: #fffbe0; color: #6b5b00; font-family: 'Inter', sans-serif; font-size: 0.75rem; text-align: center; padding: 0.5rem; }}

  .label {{ font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.2em; }}

  /* PAGE CONTAINER — one shared grid, used by every section, so the header,
     bio, story, closing and footer all share the exact same left/right edge. */
  .page-container {{ max-width: 940px; margin: 0 auto; padding: 0 1.5rem; }}

  /* SITE HEADER — logo + nav, sits at the top of the banner. Full-width with
     its own edge padding, matching the header on the Offerings/Writing/Home
     pages, instead of being boxed into the narrower page-container. */
  .site-header {{ background: var(--dark); padding: 1.4rem 0; }}
  .site-header-inner {{ display: flex; align-items: center; justify-content: space-between; padding: 0 2.5rem; }}
  .site-header .logo {{ font-family: 'Playfair Display', serif; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.18em; color: rgba(255,255,255,0.9); }}
  .site-header nav {{ display: flex; gap: 1.75rem; }}
  .site-header nav a {{ font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.14em; color: rgba(255,255,255,0.6); }}
  .site-header nav a.active {{ color: var(--gold); }}

  /* HERO — text only, no photo. Thin banner beneath the header. */
  .about-hero {{ background: var(--dark); padding: 2.75rem 1.5rem 3rem; text-align: center; }}
  .about-hero .label {{ color: rgba(255,255,255,0.55); margin-bottom: 1rem; }}
  .about-hero h1 {{ font-family: 'Playfair Display', serif; font-weight: 400; font-size: 2.1rem; letter-spacing: 0.06em; text-transform: uppercase; color: rgba(255,255,255,0.9); margin: 0 0 1.2rem; }}
  .hairline {{ width: 40px; height: 1px; background: var(--gold); opacity: 0.6; margin: 0 auto 1.2rem; }}
  .about-hero .credentials {{ list-style: none; padding: 0; margin: 0; }}
  .about-hero .credentials li {{ font-family: 'Inter', sans-serif; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; color: rgba(255,255,255,0.68); margin-bottom: 0.4rem; }}

  /* BIO — photo now lives here. min-height + centering keeps this section
     filling the full first screen on load, so the dark My Story section
     below it doesn't peek into view until the person actually scrolls. */
  .bio-section {{ background: var(--light); padding: 4.5rem 0 3.5rem; min-height: calc(100vh - 74px); display: flex; flex-direction: column; justify-content: center; box-sizing: border-box; }}
  .bio-wrap {{ max-width: 620px; margin: 0 auto; padding: 0 1.5rem; }}
  .bio-photo {{ width: 240px; height: 320px; overflow: hidden; margin: 0 auto 2.5rem; }}
  .bio-photo img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 25%; display: block; }}
  .bio-wrap p.bio-p {{ font-size: 1rem; line-height: 1.85; margin-bottom: 1.6rem; }}

  /* BIO variant B — photo left, full bio text right. align-items: stretch
     makes the photo column match the full height of the bio text column,
     so the photo runs the length of the copy instead of stopping partway
     with empty space beneath it. Sits on .page-container, so the photo's
     left edge and the text's right edge match the header exactly. */
  .bio-columns {{ display: flex; gap: 3.5rem; align-items: stretch; margin-bottom: 1rem; }}
  .bio-photo-col {{ position: relative; width: 300px; overflow: hidden; flex-shrink: 0; }}
  .bio-photo-col img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 8%; display: block; }}
  .bio-text-col {{ flex: 1; }}
  .bio-text-col p.bio-p {{ font-size: 1rem; line-height: 1.85; margin-bottom: 1.6rem; }}
  .bio-text-col p.bio-p:last-child {{ margin-bottom: 0; }}
  @media (max-width: 760px) {{
    .bio-columns {{ flex-direction: column; align-items: center; gap: 2rem; }}
    .bio-photo-col {{ width: 240px; height: 320px; }}
  }}
  .credential-rows {{ margin-top: 3rem; }}
  .credential-rows .row {{ text-align: center; border-top: 1px solid rgba(173,167,156,0.3); padding: 2rem 0; }}
  .credential-rows dt {{ font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.2em; color: var(--gold-dark); margin-bottom: 0.5rem; }}
  .credential-rows dd {{ margin: 0; font-size: 1rem; line-height: 1.8; }}

  /* MY STORY */
  .story-section {{ background: var(--dark); padding: 5rem 1.5rem; }}
  .story-wrap {{ max-width: 620px; margin: 0 auto; }}
  .story-wrap .label {{ color: var(--gold); text-align: center; margin-bottom: 2rem; display: block; }}
  .story-wrap p.story-p {{ font-size: 1.0625rem; line-height: 1.9; color: rgba(255,255,255,0.62); margin-bottom: 1.75rem; }}
  .story-wrap .gold-rule {{ width: 40px; height: 1px; background: var(--gold); opacity: 0.6; margin: 1.5rem auto; }}
  .story-wrap .script-line {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; font-size: 2.6rem; color: var(--gold-light); text-align: center; padding: 2rem 0 1rem; margin: 0; }}
  .story-photo {{ width: 240px; height: 320px; overflow: hidden; margin: 1rem auto 2rem; }}
  .story-photo img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}

  /* CLOSING */
  .closing-section {{ background: var(--light); padding: 4rem 1.5rem; text-align: center; }}
  .closing-section .script-line {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; font-size: 1.875rem; margin-bottom: 2rem; }}
  .btn {{ display: inline-block; padding: 1rem 2rem; font-family: 'Inter', sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.688rem; background: var(--dark); color: var(--light); }}
  .closing-section .sub-line {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; font-size: 1.125rem; margin: 2rem 0 1rem; }}
  .closing-section a.substack-link {{ display: inline-block; padding: 0.9rem 2rem; border: 1px solid var(--gold-dark); font-family: 'Inter', sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.14em; font-size: 0.688rem; color: var(--gold-dark); transition: background 0.2s, color 0.2s; }}

  /* FOOTER — dark */
  .site-footer {{ background: var(--dark); border-top: 1px solid rgba(255,255,255,0.08); padding: 2.5rem 1.5rem; text-align: center; }}
  .site-footer .footer-nav {{ display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 0.6rem 1.5rem; max-width: 700px; margin: 0 auto; }}
  .site-footer .footer-nav a {{ font-family: 'Inter', sans-serif; font-weight: 300; text-transform: uppercase; letter-spacing: 0.18em; font-size: 0.688rem; color: rgba(255,255,255,0.68); }}
  .site-footer .copyright {{ margin: 2rem 0 0; font-size: 0.75rem; letter-spacing: 0.02em; color: rgba(255,255,255,0.55); }}
  .site-footer .legal-row {{ margin-top: 0.75rem; display: flex; align-items: center; justify-content: center; gap: 0.5rem; font-size: 0.75rem; letter-spacing: 0.02em; color: rgba(255,255,255,0.55); }}
</style>
</head>
<body>

<!-- SITE HEADER -->
<header class="site-header">
  <div class="site-header-inner">
    <a href="index.html" class="logo" style="text-decoration:none;">Dr. Angela Le</a>
    <nav>
      <a href="about.html" class="active">About</a>
      <a href="offerings.html">Offerings</a>
      <a href="#">Kind Words</a>
      <a href="writing.html">Writing</a>
      <a href="connect.html">Connect</a>
    </nav>
  </div>
</header>

<!-- Banner removed per Angela's request — just the dark header strip remains above the bio. -->

<!-- BIO: photo now lives here -->
<section class="bio-section">
  <div class="{wrap_class}">
    {bio_block}
    <dl class="credential-rows">
      {"".join(f'<div class="row"><dt>{label}</dt><dd>{value}</dd></div>' for label, value in credential_rows)}
    </dl>
  </div>
</section>

<!-- MY STORY -->
<section class="story-section">
  <div class="story-wrap">
    <span class="label">My Story</span>
    {p_tags(story_part_one, "story-p")}
    <div class="gold-rule"></div>
    {p_tags(story_part_two, "story-p")}
    <p class="script-line">Stop fixing.</p>
    <div class="story-photo">
      <img src="data:image/jpeg;base64,{story_photo}" alt="">
    </div>
    {p_tags(story_part_three, "story-p")}
  </div>
</section>

<!-- CLOSING -->
<section class="closing-section">
  <p class="script-line">Something is ready to shift.</p>
  <a href="connect.html" class="btn">Begin a Conversation</a>
  <p class="sub-line">Not ready yet? The writing is a place to start.</p>
  <a href="https://substack.com/@drangelale" class="substack-link">Subscribe on Substack &rarr;</a>
</section>

<!-- FOOTER -->
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

html_b_soft = build("b", photo=bio_photo)
html_b_smile = build("b", photo=bio_photo_alt)

with open("/home/claude/about-redesign-v2-soft.html", "w") as f:
    f.write(html_b_soft)
with open("/home/claude/about-redesign-v2-smile.html", "w") as f:
    f.write(html_b_smile)

print("done", len(html_b_soft), len(html_b_smile))
