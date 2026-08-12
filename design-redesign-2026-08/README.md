# Angela Le Coaching — Design Redesign (August 2026)

Static, self-contained HTML previews of the four redesigned pages. Each `.html` file has its fonts and photos embedded directly (base64), so you can open any of them straight in a browser with no server or build step, and no other files needed.

- `home.html` — Homepage
- `about.html` — About page
- `offerings.html` — Offerings page
- `writing.html` — Writing page (current version: centered layout, photo above the headline, "Each piece is a doorway back to yourself.", headline sized to match the homepage's own Writing section)

The matching `build_*.py` files are the Python scripts that generated each HTML file. They're included for reference and reproducibility, but they pull font and photo files from local paths on the machine that generated them, so they won't run as-is outside that environment. The `.html` files are the actual deliverable — they don't depend on the scripts at all.

These are design mockups, not the production site. The live site is built in Lovable.
