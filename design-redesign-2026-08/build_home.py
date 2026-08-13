import base64

def b64(name):
    with open(f"/home/claude/photos/{name}.jpg.b64") as f:
        return f.read()

angela_hero = b64("angela-hero")
angela_bio = b64("angela-bio")
interlude_a = b64("essay-photo")
two_ways = b64("two-ways-in")
substack_img = b64("substack")
closing = b64("closing-cta")
kind_words_img = b64("kind-words-photo")
aliveness_img = b64("aliveness-photo")
jump_img = b64("jump-photo")
laugh_flare_img = b64("laugh-flare-photo")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dr. Angela Le</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500&family=Cormorant+Garamond:ital,wght@1,300&family=Lora:wght@400&family=Inter:wght@300;500&display=swap" rel="stylesheet">
<style>
  :root {{
    --dark: #2C2A31;
    --light: #EFEFED;
    --alt-light: #F0F1F1;
    --ink: #4B4B52;
    --subtext: #8B8D8E;
    --gold: #ADA79C;
    --gold-light: #CFCAC0;
    --gold-dark: #8C877C;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Lora', serif; color: var(--ink); background: var(--light); }}
  .heading {{ font-family: 'Playfair Display', serif; text-transform: uppercase; letter-spacing: 0.06em; }}
  .script {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; }}
  .label {{ font-family: 'Inter', sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.22em; font-size: 0.688rem; }}
  .ui {{ font-family: 'Inter', sans-serif; }}
  a {{ text-decoration: none; }}

  /* NAV */
  header.nav {{
    position: sticky; top: 0; z-index: 50;
    background: var(--dark);
    padding: 1.1rem 2.5rem;
    display: flex; align-items: center; justify-content: space-between;
  }}
  .logo {{ font-family: 'Playfair Display', serif; font-weight: 400; text-transform: uppercase; letter-spacing: 0.18em; color: rgba(255,255,255,0.9); font-size: 0.875rem; }}
  nav.links {{ display: flex; gap: 2.2rem; }}
  nav.links a {{ font-family: 'Inter', sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.15em; font-size: 0.688rem; color: rgba(255,255,255,0.6); }}
  nav.links a:hover {{ color: var(--gold); }}

  /* HERO */
  .hero {{ display: flex; min-height: 92vh; background: var(--dark); }}
  .hero-photo {{ width: 40%; position: relative; overflow: hidden; }}
  .hero-photo img {{ width: 100%; height: 100%; object-fit: cover; object-position: 50% 25%; display: block; }}
  .hero-photo::after {{
    content: ''; position: absolute; inset: 0;
    background: linear-gradient(to right, transparent 60%, rgba(44,42,49,0.8));
  }}
  .hero-text {{ width: 60%; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 5rem 4rem; }}
  .hero-text-inner {{ max-width: 34rem; }}
  .hero-eyebrow {{ font-family: 'Inter', sans-serif; font-size: 0.8125rem; text-transform: uppercase; letter-spacing: 0.22em; color: rgba(255,255,255,0.75); margin-bottom: 2.2rem; }}
  .hero-h1 {{ font-family: 'Playfair Display', serif; font-weight: 400; font-size: 2.5rem; line-height: 1.3; letter-spacing: 0.06em; text-transform: uppercase; color: rgba(255,255,255,0.9); margin-bottom: 1.8rem; }}
  .hero-script {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; font-size: 2rem; line-height: 1.5; letter-spacing: 0.01em; color: var(--gold-light); margin-bottom: 1.8rem; }}
  .hero-sub {{ font-size: 0.95rem; line-height: 1.8; color: rgba(255,255,255,0.55); max-width: 26rem; margin: 0 auto 2rem; }}
  .hairline {{ width: 40px; height: 1px; background: var(--gold); opacity: 0.6; margin: 0 auto 2rem; }}
  .btn {{ display: inline-block; padding: 1rem 2rem; font-family: 'Inter', sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.688rem; border: 1px solid transparent; transition: all 0.2s; }}
  .btn-primary {{ background: var(--gold); color: var(--dark); }}
  .btn-primary:hover {{ background: transparent; color: var(--gold); border-color: var(--gold); }}
  .btn-secondary {{ background: var(--dark); color: var(--light); }}
  .btn-secondary:hover {{ background: transparent; color: var(--dark); border-color: var(--dark); }}

  /* PHOTO BREAK - sits directly in the essay flow, no color band */
  /* Portrait family: essay break photos share one tall rectangular frame */
  .photo-break, .photo-break-tall {{ width: 220px; height: 330px; overflow: hidden; margin: 3.5rem auto; }}
  .photo-break img, .photo-break-tall img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}

  /* Landscape family: Kind Words and Substack photos share one wide rectangular frame */
  .photo-landscape {{ width: 300px; height: 200px; overflow: hidden; margin: 0 auto 2.5rem; }}
  .photo-landscape img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}

  /* LIGHT SECTIONS */
  section.light {{ background: var(--light); padding: 4.5rem 1.5rem; }}
  .essay {{ max-width: 620px; margin: 0 auto; }}
  .essay p {{ font-size: 1.0625rem; line-height: 1.9; margin-bottom: 1.75rem; }}
  .essay .script-block {{ text-align: center; padding: 0.5rem 0 1.5rem; }}
  .essay .script-line {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; font-size: 2.25rem; line-height: 1.45; letter-spacing: 0.01em; }}
  .essay .repeats {{ margin-top: 1.5rem; list-style: none; }}
  .essay .repeats li {{ font-family: 'Inter', sans-serif; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.16em; color: var(--gold-dark); margin-bottom: 0.5rem; }}
  .essay p.mid-script {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; font-size: 1.75rem; line-height: 1.4; letter-spacing: 0.01em; text-align: center; padding: 0.5rem 0 1.75rem; margin-bottom: 0; }}
  .essay p.essay-heading {{ font-family: 'Playfair Display', serif; font-weight: 400; text-transform: uppercase; letter-spacing: 0.14em; line-height: 1.35; font-size: 1.5rem; text-align: center; padding: 0.5rem 0 1.75rem; margin-bottom: 0; }}
  .essay-link {{ text-align: center; padding-top: 1rem; }}
  .essay-link a {{ font-family: 'Inter', sans-serif; font-weight: 300; text-transform: uppercase; letter-spacing: 0.16em; font-size: 0.85rem; color: var(--gold-dark); }}

  /* MEET DR LE */
  section.dark {{ background: var(--dark); padding: 4.5rem 1.5rem; }}
  .meet {{ max-width: 720px; margin: 0 auto; display: flex; gap: 3.5rem; align-items: center; }}
  .meet img {{ width: 220px; flex-shrink: 0; display: block; }}
  .meet-text p.meet-label {{ font-size: 0.688rem; font-weight: 300; letter-spacing: 0.22em; color: var(--gold); margin-bottom: 1.2rem; }}
  .meet-text p {{ font-size: 0.92rem; line-height: 1.85; color: rgba(255,255,255,0.58); margin-bottom: 1rem; }}

  /* KIND WORDS */
  .kind-words {{ max-width: 620px; margin: 0 auto; text-align: center; }}
  .kind-words .label {{ color: var(--gold-dark); margin-bottom: 2rem; }}
  .kind-words .quote {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; font-size: 1.4rem; line-height: 1.6; margin-bottom: 1.2rem; }}
  .kind-words .name {{ font-family: 'Inter', sans-serif; font-weight: 300; text-transform: uppercase; letter-spacing: 0.18em; font-size: 0.6rem; color: var(--gold-dark); margin-bottom: 2rem; }}
  .kind-words .dots {{ display: flex; justify-content: center; gap: 0.6rem; }}
  .kind-words .dots span {{ width: 5px; height: 5px; border-radius: 50%; background: var(--gold); opacity: 0.3; }}
  .kind-words .dots span.active {{ opacity: 1; }}

  /* TWO WAYS IN */
  .tw-wrap {{ max-width: 660px; margin: 0 auto; }}
  .tw-label {{ text-align: center; color: rgba(255,255,255,0.35); margin-bottom: 2.5rem; }}
  .tw-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 0; }}
  .tw-col {{ padding: 1.5rem 2rem; }}
  .tw-col:first-child {{ border-right: 1px solid rgba(173,167,156,0.15); }}
  .tw-col h3 {{ font-family: 'Playfair Display', serif; font-weight: 400; text-transform: uppercase; line-height: 1.35; font-size: 1.1rem; letter-spacing: 0.05em; color: rgba(255,255,255,0.85); margin-bottom: 1rem; }}
  .tw-col p {{ font-size: 0.88rem; line-height: 1.8; color: rgba(255,255,255,0.45); margin-bottom: 1.4rem; }}
  .tw-col a {{ font-family: 'Inter', sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.13em; font-size: 0.62rem; color: var(--gold); border-bottom: 1px solid rgba(173,167,156,0.3); padding-bottom: 0.25rem; }}

  /* THE WRITING */
  section.writing {{ padding: 4rem 1.5rem; }}
  .sub-wrap {{ max-width: 480px; margin: 0 auto; text-align: center; }}
  .sub-text .label {{ letter-spacing: 0.2em; color: var(--gold-dark); margin-bottom: 1rem; }}
  .sub-text .script-line {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; font-size: 1.875rem; line-height: 1.45; letter-spacing: 0.01em; margin-bottom: 0.9rem; }}
  .sub-text .script-line.small {{ font-size: 1.5rem; line-height: 1.5; color: var(--gold-dark); margin-bottom: 1.5rem; }}

  /* CLOSING */
  .closing {{ background: var(--dark); text-align: center; padding: 6rem 1.5rem; }}
  .closing-script {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 300; font-size: 2.25rem; line-height: 1.5; letter-spacing: 0.01em; color: var(--gold-light); margin-bottom: 2.5rem; }}

  /* FOOTER */
  footer {{ background: var(--light); text-align: center; padding: 2.5rem 1.5rem; }}
  footer .flinks {{ display: flex; justify-content: center; gap: 1.6rem; margin-bottom: 1.2rem; }}
  footer .flinks a {{ font-family: 'Inter', sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.18em; font-size: 0.688rem; color: var(--ink); }}
  footer .fine {{ font-family: 'Lora', serif; font-size: 0.75rem; letter-spacing: 0.025em; color: var(--ink); opacity: 0.85; }}
</style>
</head>
<body>

<header class="nav">
  <a href="index.html" class="logo" style="text-decoration:none;">Dr. Angela Le</a>
  <nav class="links">
    <a href="about.html">About</a>
    <a href="offerings.html">Offerings</a>
    <a href="kind-words.html">Kind Words</a>
    <a href="writing.html">Writing</a>
    <a href="connect.html">Connect</a>
  </nav>
</header>

<!-- HERO -->
<section class="hero">
  <div class="hero-photo">
    <img src="data:image/jpeg;base64,{angela_hero}" alt="Dr. Angela Le">
  </div>
  <div class="hero-text">
    <div class="hero-text-inner">
      <p class="hero-eyebrow">Twenty-five years of clinical practice have taught me this</p>
      <h1 class="hero-h1">When You Listen to What Is Alive in You</h1>
      <p class="hero-script">your entire life reorganizes around what feels true.</p>
      <div class="hairline"></div>
      <a href="#" class="btn btn-primary">Begin a Conversation</a>
    </div>
  </div>
</section>

<!-- ESSAY PART 1 -->
<section class="light">
  <div class="essay">
    <p>Some part of you knows this already. You feel it in the way you brace when you finally sit down to rest. In the list that starts composing itself the moment stillness arrives. There is a distance between the life you are living and the life that is true. It has been calling to you for years.</p>
    <p>From the outside, you have it together. Most of it, anyway. But something has stopped being yours. And inside that something, you can look composed and be quietly falling apart. You have been tending it the way you tend everything. Capably. Privately. Alone.</p>
    <div class="script-block">
      <p class="script-line">An emotion that doesn&rsquo;t complete itself repeats.</p>
      <ul class="repeats">
        <li>The hurt you buried.</li>
        <li>The anger you softened.</li>
        <li>The no you swallowed.</li>
      </ul>
    </div>

    <div class="photo-break">
      <img src="data:image/jpeg;base64,{interlude_a}" alt="">
    </div>

    <p>Early on, your nervous system learned that the world was not safe. It built these patterns to protect you, and they have been running ever since. Stillness means danger. Producing means belonging. Slow down, and you will have to feel what you have been outrunning.</p>
    <p>So the strategy keeps running. You keep performing.</p>
    <p class="mid-script">Everyone around you calls it strength.</p>
    <p>And the cost compounds. It shows up in the digestion you have stopped trusting, the sleep that stops repairing you, the joy that dims. Much of what you have learned to call your personality is armoring. The over-functioning. The perfectionism. The way you apologize for taking up space. The way you keep yourself small.</p>
    <p>Over decades of practice, I&rsquo;ve watched this pattern. Your nervous system organized around the belief that your worth must be earned. And the pattern is a form of intelligence. You learned it early. Elegant strategies, still doing their job.</p>
    <p class="essay-heading">If any of this is you, you are in the right place.</p>
    <p>Here is what I have witnessed when the pattern is finally met. Given enough time, enough steadiness, and a witness, the response that froze decades ago completes itself.</p>
    <p>Somatic work reaches where nothing else does. And what returns is capacity. The energy that spent decades in protection becomes available again.</p>
    <p class="script-line" style="text-align:center; padding: 0.5rem 0 1rem;">Decisions clarify. Aliveness returns. There is a coming home, and from there, the life that is actually yours begins.</p>
    <div class="photo-break-tall">
      <img src="data:image/jpeg;base64,{jump_img}" alt="">
    </div>
    <div class="essay-link">
      <a href="#">See how the work unfolds &rarr;</a>
    </div>
  </div>
</section>

<!-- MEET DR LE -->
<section class="dark">
  <div class="meet">
    <img src="data:image/jpeg;base64,{angela_bio}" alt="Dr. Angela Le">
    <div class="meet-text">
      <p class="label meet-label">Meet Angela Le, DACM</p>
      <p>Dr. Le is a Doctor of Acupuncture and Chinese Medicine, in practice since 2001, and one of the country&rsquo;s first integrative fertility acupuncturists. In twenty-five years, she has guided thousands of women through health challenges and major reproductive life transitions.</p>
      <p>What emerged from decades of study, clinical practice, and her own healing is a way of working that belongs to no single tradition and draws on all of them.</p>
      <a href="#" class="btn btn-primary" style="margin-top:0.5rem;">Read Her Story</a>
    </div>
  </div>
</section>

<!-- KIND WORDS -->
<section class="light">
  <div class="kind-words">
    <div class="photo-landscape"><img src="data:image/jpeg;base64,{kind_words_img}" alt=""></div>
    <p class="label">Kind Words</p>
    <p class="quote">My business went from pre-revenue and fledgling to self-sustaining and thriving, not because I worked harder, but because I worked differently. Angela is an alchemist. She doesn&rsquo;t fix you; she reveals what was always there, waiting.</p>
    <p class="name">Susan</p>
    <div class="dots">
      <span class="active"></span><span></span><span></span><span></span><span></span>
    </div>
  </div>
</section>

<!-- TWO WAYS IN -->
<section class="dark">
  <div class="tw-wrap">
    <p class="label tw-label">Work With Dr. Le</p>
    <div class="tw-grid">
      <div class="tw-col">
        <h3>Consultation</h3>
        <p>One hour, in service of your question. You leave with insight, direction, and the sense of having been truly heard. A limited number of sessions are available each month.</p>
        <a href="#">Book a session &rarr;</a>
      </div>
      <div class="tw-col">
        <h3>Mentorship</h3>
        <p>Six to nine months, working together closely. Your health, your relationships, your sense of self, all of it welcomed. The deeper work becomes possible here. We begin where you are.</p>
        <a href="#">Apply &rarr;</a>
      </div>
    </div>
  </div>
</section>

<!-- THE WRITING -->
<section class="light writing">
  <div class="sub-wrap">
    <div class="photo-landscape" style="margin: 0 auto 2rem;">
      <img src="data:image/jpeg;base64,{substack_img}" alt="">
    </div>
    <div class="sub-text">
      <p class="label">The Writing</p>
      <p class="script-line">A way to stay connected.</p>
      <p class="script-line small">Practical and thoughtful reflections on what I am learning.</p>
      <a href="#" class="btn btn-secondary">Subscribe on Substack</a>
    </div>
  </div>
</section>

<!-- CLOSING -->
<section class="closing">
  <p class="closing-script">Something is ready to shift.</p>
  <a href="#" class="btn btn-primary">Begin a Conversation</a>
</section>

<footer>
  <div class="flinks">
    <a href="about.html">About</a><a href="offerings.html">Offerings</a><a href="kind-words.html">Kind Words</a><a href="writing.html">Writing</a><a href="connect.html">Connect</a>
  </div>
  <p class="fine">© 2026 Dr. Angela Le</p>
  <p class="fine" style="margin-top:0.75rem;">Privacy Policy &nbsp;·&nbsp; Terms &amp; Conditions &nbsp;·&nbsp; Accessibility</p>
</footer>

</body>
</html>
"""

with open("/home/claude/homepage-redesign-v1.html", "w") as f:
    f.write(html)

print("done", len(html))
