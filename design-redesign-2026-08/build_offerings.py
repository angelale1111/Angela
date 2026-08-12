import base64

def font_b64(name):
    with open(f"/home/claude/fonts_b64/{name}.b64") as f:
        return f.read()

def photo_b64(name):
    with open(f"/home/claude/photos/{name}.jpg.b64") as f:
        return f.read()

bio_photo = photo_b64("about-candidate-soft")

FONT_FACES = f"""
@font-face {{ font-family: 'Lora'; font-style: normal; font-weight: 400; src: url(data:font/woff2;base64,{font_b64('lora-400')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Playfair Display'; font-style: normal; font-weight: 400; src: url(data:font/woff2;base64,{font_b64('playfair-400')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Playfair Display'; font-style: normal; font-weight: 500; src: url(data:font/woff2;base64,{font_b64('playfair-500')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Cormorant Garamond'; font-style: italic; font-weight: 300; src: url(data:font/woff2;base64,{font_b64('cormorant-300-italic')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Cormorant Garamond'; font-style: normal; font-weight: 300; src: url(data:font/woff2;base64,{font_b64('cormorant-300-normal')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Inter'; font-style: normal; font-weight: 300; src: url(data:font/woff2;base64,{font_b64('inter-300')}) format('woff2'); font-display: swap; }}
@font-face {{ font-family: 'Inter'; font-style: normal; font-weight: 500; src: url(data:font/woff2;base64,{font_b64('inter-500')}) format('woff2'); font-display: swap; }}
"""

# ---- Copy -------------------------------------------------------------
# ASSUMPTIONS (flagged for Angela to confirm before this goes to Lovable):
#   1. Nav label "Work With Me" -> "Offerings" (renamed everywhere, not just
#      the page heading), since she said "let's call it offerings."
#   2. The Fifth Avenue Fertility Wellness link below is a placeholder —
#      using fafwellness.com, inferred from her own email domain
#      (angela@fafwellness.com). NEEDS CONFIRMATION before it goes live.
#   3. Mentorship section is left as-is (it was already the strongest,
#      most complete section) and is now positioned as the clear focus of
#      the page — Consultation is intentionally short, since it just
#      routes people to FAFW rather than describing a coaching offer.

mentorship_paragraphs = [
    "The work follows what is alive in you. There is no program, and it deepens in a way I have watched hundreds of times.",
    "It begins with what brought you in, a symptom, a decision, a situation that stopped responding to effort. As the ground steadies, the pattern beneath it comes into view, the strategy your system built long ago, still running your days. We meet it directly, at a pace your system can trust, until it no longer needs to run.",
    "What remains is space. The attention that spent years managing returns to you, and the questions change. What do you want now. What will you build. The final months belong to that.",
]

included = [
    "Two to three private sessions per month, in person or virtual",
    "Email support between sessions and priority scheduling",
    "Access to the therapeutic modalities that best serve you",
    "Curated resources drawn from decades of study",
    "Personalized practices and tools you can integrate into your daily life",
    "Clarification and alignment of your goals throughout our work together",
]

faqs = [
    ("How is this different from therapy?",
     "Many of my clients have a therapist, and the two work well together. Therapy tends to work with the story and the past. Our work centers what is present in you now. We work in real time, with the patterns as they are showing up."),
    ("What's the difference between a consultation and mentorship?",
     "A consultation is an acupuncture session through Fifth Avenue Fertility Wellness. Mentorship is a private relationship over six to nine months, with support between sessions and priority scheduling. It begins with an application."),
    ("Why does mentorship take months?",
     "The patterns we work with were built over decades. Real change comes through repetition, safety, and consistent attention. Months is what allows the change to integrate and last."),
    ("Are sessions in person or virtual?",
     "Both. I see clients in person in New York City and virtually. Most sessions happen virtually."),
    ("I am not in a crisis. Is this for me?",
     "Yes. The people who come here are functioning well by every external measure. They come because they are at a turning point, and they want to move through it with intention. You do not need to be in crisis to deserve this depth of care. If you are in a crisis, this work can hold that too. You do not need to have it together to begin."),
    ("I am not sure this is for me.",
     "Most people who come here have not worked at this depth before. The depth is not in what you are asked to do. It is in the quality of attention you receive. Sustained, private, and undivided. That is what makes change possible."),
    ("What is the investment?",
     "This work is a significant investment of time, money, and attention. The people who come here understand that sustained private work at this depth cannot be delivered any other way. We discuss the specifics during our first conversation."),
    ("Do I need to believe anything?",
     "No. Nothing here asks for belief. Your own experience is the evidence. If something in you has been calling you here, that is enough to begin."),
]

def build():
    faq_html = "\n".join(
        f'''<div class="faq-item">
          <button class="faq-q" type="button"><span>{q}</span><span class="faq-icon"></span></button>
          <div class="faq-a"><p>{a}</p></div>
        </div>''' for q, a in faqs
    )
    included_html = "\n".join(f'<li><span class="dot"></span><span>{item}</span></li>' for item in included)
    mentorship_html = "\n".join(f'<p class="mentor-p">{p}</p>' for p in mentorship_paragraphs)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Offerings — Redesign Preview</title>
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
  .label.gold-dark {{ color: var(--gold-dark); }}
  .label.gold {{ color: var(--gold); }}

  .page-container {{ max-width: 940px; margin: 0 auto; padding: 0 1.5rem; }}

  .gold-rule {{ width: 40px; height: 1px; background: var(--gold); opacity: 0.6; margin: 0 auto; }}

  /* HEADER */
  .site-header {{ background: var(--dark); padding: 1.4rem 0; }}
  .site-header-inner {{ display: flex; align-items: center; justify-content: space-between; padding: 0 2.5rem; }}
  .site-header .logo {{ font-family: 'Playfair Display', serif; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.18em; color: rgba(255,255,255,0.9); }}
  .site-header nav {{ display: flex; gap: 1.75rem; }}
  .site-header nav a {{ font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.14em; color: rgba(255,255,255,0.6); }}
  .site-header nav a.active {{ color: var(--gold); }}

  /* HERO */
  .hero {{ background: var(--dark); padding: 5rem 1.5rem 4rem; text-align: center; }}
  .hero-inner {{ max-width: 640px; margin: 0 auto; }}
  .hero .label {{ color: rgba(255,255,255,0.35); margin-bottom: 1.2rem; }}
  .hero h1 {{ font-family: 'Playfair Display', serif; font-weight: 400; font-size: 2rem; text-transform: uppercase; letter-spacing: 0.05em; color: rgba(255,255,255,0.9); margin: 0 0 1.4rem; }}

  /* CONSULTATION */
  .consultation {{ background: var(--light); padding: 4rem 1.5rem; text-align: center; }}
  .consultation-inner {{ max-width: 600px; margin: 0 auto; }}
  .consultation p.body {{ font-size: 1.0625rem; margin: 1.4rem 0 1.8rem; }}

  /* BUTTONS */
  .btn {{ display: inline-flex; align-items: center; justify-content: center; border: 1px solid; padding: 1rem 2rem; font-family: 'Inter', sans-serif; font-weight: 500; font-size: 0.688rem; text-transform: uppercase; letter-spacing: 0.12em; transition: background 0.2s, color 0.2s; }}
  .btn-secondary {{ border-color: var(--dark); background: var(--dark); color: var(--light); }}
  .btn-primary {{ border-color: var(--gold-light); background: var(--gold-light); color: var(--dark); }}

  /* MENTORSHIP */
  .mentorship {{ background: var(--dark); padding: 4.5rem 1.5rem; text-align: center; }}
  .mentorship-inner {{ max-width: 600px; margin: 0 auto; }}
  .mentorship .label {{ color: var(--gold); }}
  .mentorship p.body {{ font-size: 1.0625rem; color: rgba(255,255,255,0.65); margin: 1.4rem 0; }}
  .mentor-p {{ font-size: 1.0625rem; color: rgba(255,255,255,0.65); margin: 0 0 1.4rem; text-align: left; }}

  .quote {{ max-width: 420px; margin: 2.5rem auto; }}
  .quote blockquote {{ font-style: italic; font-size: 0.92rem; color: rgba(255,255,255,0.65); margin: 0; }}
  .quote figcaption {{ margin-top: 1rem; font-family: 'Inter', sans-serif; font-size: 0.625rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.2em; color: var(--gold-light); }}

  .mentorship .gold-rule {{ margin: 2rem auto; }}

  .included-label {{ font-family: 'Inter', sans-serif; font-size: 0.625rem; font-weight: 500; text-transform: uppercase; letter-spacing: 0.2em; color: var(--gold-light); margin-bottom: 1.5rem; }}
  .included-list {{ list-style: none; margin: 0; padding: 0; max-width: 560px; margin-left: auto; margin-right: auto; display: grid; grid-template-columns: 1fr 1fr; gap: 0.4rem 2.5rem; text-align: left; }}
  .included-list li {{ display: flex; align-items: flex-start; gap: 0.6rem; font-size: 0.9rem; line-height: 1.7; color: rgba(255,255,255,0.55); padding: 0.55rem 0; }}
  .included-list .dot {{ margin-top: 0.55rem; width: 6px; height: 6px; border-radius: 50%; background: var(--gold); flex-shrink: 0; }}

  .apply-line {{ font-style: italic; font-size: 1.0625rem; color: rgba(255,255,255,0.65); margin: 0 0 1.5rem; }}

  /* FAQ */
  .faq-section {{ background: var(--light); padding: 4.5rem 1.5rem; }}
  .faq-inner {{ max-width: 680px; margin: 0 auto; }}
  .faq-inner .label {{ color: var(--gold-dark); margin-bottom: 2.2rem; display: block; }}
  .faq-item {{ border-bottom: 1px solid rgba(75,75,82,0.15); }}
  .faq-item:first-child {{ border-top: 1px solid rgba(75,75,82,0.15); }}
  .faq-q {{ width: 100%; background: none; border: none; display: flex; align-items: center; justify-content: space-between; gap: 1.5rem; padding: 1.25rem 0; text-align: left; cursor: pointer; font-family: 'Playfair Display', serif; font-size: 0.95rem; color: var(--ink); }}
  .faq-icon {{ position: relative; width: 12px; height: 12px; flex-shrink: 0; color: var(--gold-dark); }}
  .faq-icon::before {{ content: ""; position: absolute; left: 0; top: 50%; width: 12px; height: 1px; background: currentColor; }}
  .faq-a p {{ padding: 0 2rem 1.5rem 0; font-size: 0.95rem; color: var(--ink); margin: 0; }}

  /* WRITING CTA */
  .writing-cta {{ background: var(--dark); padding: 4.5rem 1.5rem; text-align: center; }}
  .writing-cta-inner {{ max-width: 560px; margin: 0 auto; }}
  .writing-cta .label {{ color: rgba(255,255,255,0.35); margin-bottom: 1rem; }}
  .writing-cta h2 {{ font-family: 'Playfair Display', serif; font-weight: 400; font-size: 1.1rem; letter-spacing: 0.04em; text-transform: uppercase; color: rgba(255,255,255,0.9); margin: 0 0 1.2rem; }}
  .writing-cta .sub {{ font-style: italic; color: rgba(255,255,255,0.55); margin: 0 0 1.5rem; }}
  .writing-cta .banner-photo {{ display: block; margin: 0 auto 1.5rem; width: 220px; height: 110px; object-fit: cover; object-position: 50% 25%; }}
  .btn-ghost {{ border-color: rgba(255,255,255,0.35); background: transparent; color: rgba(255,255,255,0.6); }}

  /* FOOTER */
  .site-footer {{ background: var(--light); border-top: 1px solid rgba(75,75,82,0.12); padding: 2.5rem 1.5rem; text-align: center; }}
  .site-footer .footer-nav {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 1.5rem 1.5rem; }}
  .site-footer .footer-nav a {{ font-family: 'Inter', sans-serif; font-weight: 300; text-transform: uppercase; letter-spacing: 0.18em; font-size: 0.688rem; color: var(--ink); }}
  .site-footer .copyright {{ margin-top: 2rem; font-size: 0.75rem; color: var(--ink); }}
  .site-footer .legal-row {{ margin-top: 0.75rem; display: flex; justify-content: center; gap: 0.5rem; font-size: 0.75rem; color: var(--ink); }}
</style>
</head>
<body>

<div class="annot"><b>DRAFT — local preview only, nothing built into Lovable yet.</b>Two flags to confirm before this goes live: (1) nav label "Work With Me" renamed to "Offerings" everywhere, and (2) the Fifth Avenue Fertility Wellness link uses a placeholder URL (fafwellness.com, guessed from your email domain) — send the real link.</div>

<header class="site-header">
  <div class="site-header-inner">
    <span class="logo">Dr. Angela Le</span>
    <nav>
      <a href="#">About</a>
      <a href="#" class="active">Offerings</a>
      <a href="#">Kind Words</a>
      <a href="#">Writing</a>
      <a href="#">Connect</a>
    </nav>
  </div>
</header>

<section class="consultation">
  <div class="consultation-inner">
    <p class="label gold-dark">Consultation</p>
    <p class="body">Reproductive health consultations happen through my clinical practice in New York City.</p>
    <a href="https://fafwellness.com" target="_blank" class="btn btn-secondary">Visit Fifth Avenue Fertility Wellness</a>
  </div>
</section>

<section class="mentorship">
  <div class="mentorship-inner">
    <p class="label">Mentorship</p>
    <p class="body">Six to nine months, working together closely. Your health, your relationships, your sense of self, all of it welcomed. The deeper work becomes possible here. We begin where you are.</p>

    <figure class="quote">
      <blockquote>&ldquo;My business went from pre-revenue and fledgling to self-sustaining and thriving, not because I worked harder, but because I worked differently. Angela is an alchemist. She doesn&rsquo;t fix you; she reveals what was always there, waiting.&rdquo;</blockquote>
      <figcaption>— Susan</figcaption>
    </figure>

    <div class="gold-rule"></div>

    {mentorship_html}

    <div style="padding-top: 2rem;">
      <p class="included-label">What Is Included</p>
      <ul class="included-list">
        {included_html}
      </ul>
    </div>

    <div class="gold-rule"></div>

    <a href="#" class="btn btn-primary">Submit an Application</a>
  </div>
</section>

<section class="faq-section">
  <div class="faq-inner">
    <span class="label gold-dark">Q &amp; A</span>
    {faq_html}
  </div>
</section>

<section class="writing-cta">
  <div class="writing-cta-inner">
    <h2>Begin With the Writing</h2>
    <a href="#" class="btn btn-ghost">Subscribe on Substack &rarr;</a>
  </div>
</section>

<footer class="site-footer">
  <nav class="footer-nav">
    <a href="#">About</a>
    <a href="#">Offerings</a>
    <a href="#">Kind Words</a>
    <a href="#">Writing</a>
    <a href="#">Connect</a>
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

with open("/home/claude/offerings-redesign.html", "w") as f:
    f.write(build())

print("done")
