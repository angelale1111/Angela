# Angela Le Coaching — Design Redesign (August 2026)

Static, self-contained HTML previews of the four redesigned pages. Each `.html` file has its fonts and photos embedded directly (base64), so you can open any of them straight in a browser with no server or build step, and no other files needed.

**Start here:** [`index.html`](./index.html) — this is the single entry point for the whole site. The nav bar and footer links on every page point to the real sibling files (`about.html`, `offerings.html`, `writing.html`), so once you're on `index.html` you can click through the entire site normally.

- `index.html` / `home.html` — Homepage (identical content, `index.html` is what loads automatically when you visit the folder)
- `about.html` — About page
- `offerings.html` — Offerings page
- `writing.html` — Writing page (current version: centered layout, photo above the headline, "Each piece is a doorway back to yourself.", headline sized to match the homepage's own Writing section)

"Kind Words" and "Connect" don't have pages built yet, so those two nav links are still placeholders (`#`).

The matching `build_*.py` files are the Python scripts that generated each HTML file. They're included for reference and reproducibility, but they pull font and photo files from local paths on the machine that generated them, so they won't run as-is outside that environment. The `.html` files are the actual deliverable — they don't depend on the scripts at all.

These are design mockups, not the production site. The live site is built in Lovable.
