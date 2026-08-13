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

# Verbatim, supplied directly by Angela. "Rebirth" (the old program name) removed
# per her instruction to keep this content for Angela Le Coaching. Nothing else
# altered — full stories, not excerpts.
TESTIMONIALS = [
    ("Susan", [
        "Two years ago, I felt that my life looked pretty much the way I had planned it: I had a family that I adored, my technology startup was gaining traction, and I had a community of friends, colleagues, and funders I respected. Below the surface, however, I was stressed in ways I readily dismissed and even justified. I was in regular conflict with my co-founder to the point where a funder recommended that I hire an executive coach to “survive” the relationship. I resisted the idea at first.",
        "As a bootstrapped startup founder, I felt like executive coaching was an unaffordable luxury. More than that, I’d grown skeptical of coaches and consultants who parachuted in without truly knowing me, my industry, or the intimate dynamics of my work. I thought I was better off staying the course and resolving things on my own. Of course, “on my own” meant staying stuck in my same patterns.",
        "I started talking to her about my business on a purely social basis. As the warm and wise girlfriend that she is, she would listen patiently to my stories as they became increasingly focused on the conflict I experienced with my co-founder. Then two years ago, Angela told me she started an executive coaching practice. I had the good fortune of knowing Angela personally and witnessing her incredible success in the fertility field. I knew that Angela would re-create that same success in whatever field she focused on next, so I signed up. Two years later, I know it was the best professional decision I made.",
        "Over the past two years, my business went from pre-revenue and fledgling to self-sustaining and thriving—not because I worked harder, but because I worked differently. With Angela’s guidance, I learned to make hard and difficult decisions to get myself to a place of greater strength, agency, and clarity. Over time, entrenched conflicts started to dissipate, and decisions that were previously painful became straightforward. Before working with Angela, I was burning myself out, often expending energy in areas that did not move my business forward to any significant degree. Now my business energizes rather than depletes me, my relationships with colleagues and partners are harmonious, and my work moves forward in ways that are meaningful to me.",
        "Angela once told me that her goal for me was to achieve what I wanted to achieve, expending little to no effort. It is a reality that I never could have imagined possible, and yet, that is the reality I have been able to access and live.",
        "My hope for any reader considering engaging in the work Angela offers is that they make the leap and move forward. Angela is an alchemist. She doesn’t fix you; she reveals what was always there, waiting. Her coaching and guidance have made me a stronger, more effective businessperson, colleague, wife, and mother. As Angela says, who we are in our personal lives is who shows up in our professional lives. An unexpected byproduct of our work has been that moving toward strengthening my relationships with colleagues and business partners has strengthened my personal relationships with friends and especially my family. I have told Angela that my partnership with her is a life extension technology, and I am grateful for her every day.",
    ]),
    ("Laurie", [
        "I came to Angela at a moment when I knew something in my life needed to change. I had reached a crossroads and was searching for a different way forward, one that addressed not just a single issue, but the deeper patterns shaping my health, my relationships, and my sense of self.",
        "I was curious about holistic approaches and open to doing deeper work, but I could not have anticipated how profoundly this mentorship would impact my life.",
        "From the beginning, working with Angela felt deeply personal. In our sessions, I felt as though I was her only client. Her presence is unmistakable. She listens with full attention, without judgment, and asks questions that are both simple and penetrating. Those conversations alone had a calming effect on my nervous system and helped me clarify what truly mattered.",
        "Over the course of nearly a year, something fundamental shifted. I became a different person, not by reinventing myself, but by coming home to who I actually am. I know myself better than ever before. My relationship with my husband is the strongest it has been in over nine years of marriage. Life feels lighter now, and joy arises more naturally.",
        "I work in professional development, so I was surprised by how much I grew. I thought I already had the tools and the insight. What Angela offered went far beyond that. She helped me integrate what I knew into how I live. She gave me practical ways to align my choices with my values, not just intellectually, but in my body and in my daily life.",
        "As the year unfolded, my path took an unexpected turn. Some of the goals I once held no longer felt true, and I had to grieve and release them. Even so, I would not trade this year for anything. The clarity, self trust, and inner stability I gained have been life changing.",
        "Angela is so much more than a practitioner. To me, she is a guide, a teacher, and a steady presence through profound transition. If I had one wish for the world, it would be that everyone have access to this kind of support. This work was exactly that for me, a true initiation into a more honest, connected, and meaningful life.",
    ]),
    ("Bri", [
        "Something inside me told me I needed to work with Angela. I could not fully explain why, I just knew. I arrived carrying many concerns about my life and a long history of trying to fix what felt broken. I was focused on outcomes, convinced that if I just tried harder or did more, things would finally resolve. Angela helped me step back and see the bigger picture. In her loving, perceptive way, she showed me the subtle and not-so-subtle ways I was preventing my own healing.",
        "Our work addressed my body, yes, but it went much deeper. We explored my relationships, my choices, my patterns, and my unspoken fears. Slowly, I began to see how interconnected it all was.",
        "I still remember her words clearly, “You need to give birth to yourself.” She was right. And that is exactly what happened.",
        "Through the course of our time together, I came to understand just how unhappy and out of alignment my life had been. My path was different from the one I had been forcing myself to walk. That realization was both terrifying and exhilarating. For the first time in years, I felt alive after feeling numb for so long.",
        "After years of stuckness and stagnation, joy returned. I found meaning in my life again. I made changes that turned my life upside down in the best possible way. I began to speak my truth and live it. I discovered reserves of courage inside myself that I never knew existed. I made the choices I knew I had to make to live authentically, breaking old patterns and ancestral chains in the process.",
        "Today, I am living, loving, and thriving in a way I never imagined possible.",
        "When I reflect on who I was before working with Angela, I am awed by how much I have grown. Her guidance, wisdom, and compassion have made all the difference. Angela has an extraordinary ability to cut through noise and distraction to reach the true heart of the matter. Time and again, I left our sessions with profound clarity and insight.",
        "There was life before working with Angela and life after working with her.",
        "My life now is everything I never dared to believe I could have. My heart is full of gratitude for all that I have learned and all that continues to unfold. I wholeheartedly recommend working with Angela. Your life may never be the same.",
    ]),
    ("Beth", [
        "I was struggling with feeling stuck in my life. Even though I had accomplishments and moments of joy, there was a deep frustration and confusion I couldn’t shake. I didn’t fully recognize it at the time, but I also carried a quiet anger at how limited I felt by old patterns and beliefs.",
        "Angela saw the opportunities for my growth with such clarity and communicated them with love and insight. She helped me completely shift my perspective on life. I now welcome challenges and see them as opportunities for greater self-awareness, expansion, and growth. While our sessions provided a calm, reflective space for integration, the core of the changes I experienced came from our conversations, the guidance she offered, and the new ways of thinking she introduced.",
        "After working with Angela, I feel free to create the life I desire. I see life differently.",
        "From the day I began this journey to now, I have been reconnecting with my body, my intuition, and the value of embodiment in ways I had never fully experienced before. That connection continues to deepen.",
        "I came to this work seeking guidance and support, but instead, I ended up giving birth to myself. I realized that my life had been shaped by ideas, beliefs, and patterns that were not truly my own. Through this process, I developed a clear awareness of who I am, what I desire, and how I want to show up in the world. I shed the elements that no longer served me and built a new foundation for a life filled with joy, pleasure, and peace.",
        "Angela helps you become aware of and fall in love with your most authentic self. She guided me to see, understand, and experience life differently—with more clarity, peace, compassion, joy, and pleasure.",
        "I came away from this work with everything I had been seeking. For me, life and creativity are deeply intertwined, and this work with Angela marked the beginning of stepping fully into my own creative power, presence, and capacity.",
    ]),
    ("Kaitlin", [
        "Like many, my life has been driven by fear. Fear of failing, disappointing others, not growing enough, of growing too much, of loss, and in a strange way of success.",
        "Fear has essentially led the way under the guise of safety and logic. I assumed this was all part of who I was, an overly cautious, over-thinking, over-sensitive Italian-American girl who was born this way. “It’s in your blood” or “It’s who we are” were phrases I heard over and over growing up in response to questioning this paralyzing default setting I seemed to have.",
        "At the same time, there has been a part of me that has always challenged this fear-based life and has screamed out for attention. That voice is usually muffled but there are distinct moments in my life where she escaped her cage and was able to influence the trajectory of my life. I can count these moments on one hand, but they are the moments I felt most like me, whatever that meant at the time. There were moments when my actions maybe didn’t make the most “sense” but I did them anyway and they are the moments that have gotten me closest to life I want to live. My inner voice led me straight into Angela’s acupuncture office over two years ago in a desperate attempt to find answers during my struggle with infertility.",
        "I distinctly remember my first walk to her office, rehearsing in my head all the questions I had that would elicit an a-ha moment resulting in me being pregnant by the end of the week. Instead, when Angela asked me what I wanted out of our time together, I very calmly said, I just want this to be OK. Whatever ‘this’ is, I want it to be OK. This was not the answer I had planned, because this answer implied potentially not ever being pregnant, but it was the most truthful I had been in a long time.",
        "Knowing Angela now, I can look back on that moment and know being in her presence has a profound effect on the things that come out of your mouth. It makes perfect sense to me now that at that moment I had no choice but to surrender to how I was feeling. Being pregnant wasn’t what I wanted, it was all so much deeper than that. Angela and I then set out on a journey that would forever change my life. It’s cliche to say how hard it is to put into words what she has done for me, but it’s the truth. There’s a simplicity to it that is deceiving. The best way to describe the effect she’s had on me is simply to say she has introduced me to my truest self.",
        "Angela’s guidance has brought this version of myself to the surface in the most clear and powerful ways.",
        "This work doesn’t change you, it brings you to life and that distinction is important. This version of myself is someone I have always known and being reintroduced to her in these ways has been a sigh of relief and a sense of comfort. Make no mistake, this work is hard. It’s the most challenging work I have ever done and in some ways, I know the further I go the harder it will be. But the main lesson I have learned from this journey is that pain is where all the good stuff lives.",
        "We’ve all heard that pain and struggle are necessary, but I’ve never imagined that one day I’d find it beautiful. Never would I have imagined that I’d be grateful for my infertility journey, but I am because it made space for even more important work.",
        "I now can understand and appreciate that my body knows exactly what it’s doing for me. In any struggle, the key is to slow down and listen, not resist. I have spent so much of my life resisting that to let go and surrender to listening — whether it be as small as a stressful conversation at the office or as big as grappling with not having children — is nothing short of magic.",
        "The nuance in what Angela teaches is in the realization that your progress is directly related to your truest self. It’s access to that version of you that is leading the charge and Angela is here to be the guide. This means that beyond the tips and tools you gain from this work, you start to trust yourself in ways you could have never imagined. What a gift this is for the rest of your life.",
        "I am forever indebted to Angela and the time and energy she put into my journey. She has given and continues to give so much of herself for the sake of me that I continue to be amazed and inspired by her devotion to this work. I wish everyone I love could share in even just a few moments in her presence to experience what it’s like.",
        "I’ve learned to breathe, I’ve learned to listen, I’ve learned to slow down and be quiet. I’ve learned to daydream with intention. I’ve learned to live inside my body, not my mind. I’ve learned to take ownership of my life and to trust. I’ve learned to celebrate my shadow self and the fear-based life she led — she isn’t so bad after all and fear is here for an important reason. I’ve learned to not only embrace the unexpected nature of life but to look forward to it.",
        "I’ve learned to love my infertility and truly be so thankful for it. That is an insane sentence to type out but I couldn’t leave this testimonial without saying it loud and clear. I still have a ways to go on the journey, but this thought is exciting because I now understand it’s all self-discovery. All that I need, I have.",
        "Three months after writing this testimonial I finally became pregnant. I gave birth to my beautiful baby girl in August of 2023 on a very hot end-of-summer Wednesday. Raphaëlle is now just shy of her first birthday and as I get to know her and fall more deeply in love each minute, I can’t help but say the most cliche thing there is to say, which is I couldn’t imagine her being here without all that’s come before.",
    ]),
]

kind_words_img = b64("kind-words-photo")

def build():
    testimonial_sections = ""
    for i, (name, paragraphs) in enumerate(TESTIMONIALS):
        bg = "dark" if i % 2 == 0 else "light"
        paras_html = "\n".join(f'      <p class="kw-p">{p}</p>' for p in paragraphs)
        testimonial_sections += f"""
<section class="kw-block {bg}">
  <div class="kw-block-inner">
    <p class="kw-name">{name}</p>
{paras_html}
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

  /* STORY BLOCKS — alternating dark/light, full narrative body copy, matching
     the site's About/My Story treatment rather than short pull-quote styling. */
  .kw-block {{ padding: 4.5rem 1.5rem; }}
  .kw-block.dark {{ background: var(--dark); }}
  .kw-block.light {{ background: var(--light); }}
  .kw-block-inner {{ max-width: 640px; margin: 0 auto; }}
  .kw-name {{ font-family: 'Inter', sans-serif; font-weight: 500; text-transform: uppercase; letter-spacing: 0.22em; font-size: 0.688rem; margin-bottom: 2rem; text-align: center; }}
  .kw-block.dark .kw-name {{ color: var(--gold); }}
  .kw-block.light .kw-name {{ color: var(--gold-dark); }}
  .kw-p {{ font-size: 1rem; line-height: 1.9; margin-bottom: 1.6rem; }}
  .kw-p:last-child {{ margin-bottom: 0; }}
  .kw-block.dark .kw-p {{ color: rgba(255,255,255,0.72); }}
  .kw-block.light .kw-p {{ color: var(--ink); }}

  /* FOOTER — light, since the last story block above it is dark (Kaitlin) */
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
