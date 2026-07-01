# Lumary Pro Max — OpenCode Agent Skill

## Version 1.0

---

## Agent Name
lumary-pro-max

---

## Description
Builds premium, animated websites using **data-driven design systems** (ui-ux-pro-max) + **proven motion/experience language** (Lumary OS). Combines the world's largest UI/UX design database with a production-grade build pipeline. Output: beautiful, performant, accessible websites in one shot.

---

## Trigger Phrases
- "Build a premium website for [business]"
- "One-shot beautiful site for [industry]"
- "Data-driven Lumary site for [client]"
- "Pro Max build for [project]"
- "Full website with design system"

---

## Prerequisites

### Python + Dependencies
```bash
pip install rank-bm25
```

### ui-ux-pro-max Script
Located at: `skills/ui-ux-pro-max/scripts/search.py`
```bash
python skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system -p "Project Name"
```

Available domains for supplemental searches: product, style, color, typography, landing, chart, ux, prompt

Available stacks: html-tailwind, react, nextjs, vue, svelte, swiftui, react-native, flutter, shadcn, jetpack-compose

---

## Core Workflow

### Phase 1: Generate Design System (ui-ux-pro-max)

Run the design system generator with the project's industry and style keywords:

```bash
python <path>/search.py "<industry> <style-keywords>" --design-system -p "<Project Name>"
```

**Extract these values:**
| Value | Source | Used For |
|-------|--------|----------|
| Primary color | COLORS → Primary | Main brand color, hero backgrounds |
| Secondary color | COLORS → Secondary | Cards, sections, borders |
| CTA/accent color | COLORS → CTA | Buttons, highlights, links |
| Background color | COLORS → Background | Page/section backgrounds |
| Text color | COLORS → Text | Body text, headings |
| Heading font | TYPOGRAPHY → first font | All headings (h1-h6) |
| Body font | TYPOGRAPHY → second font | Paragraphs, navigation, buttons |
| Style pattern | PATTERN | Layout structure (Hero-Centric, Feature-Rich, etc.) |
| Style name | STYLE → Keywords | Visual treatment (Glassmorphism, Minimalism, etc.) |

**Supplement if needed** (for additional detail):
```bash
python <path>/search.py "<specific-keyword>" --domain <domain>
```

### Phase 2: Select Experience Profile (Lumary OS)

Map the design system's style to a Lumary OS Experience Profile:

| Style Pattern | Energy | Formality | Warmth | Depth | Tempo |
|---------------|--------|-----------|--------|-------|-------|
| Motion-Driven + Minimalism | High | Semi-Formal | Neutral | Elevated | Fast |
| Glassmorphism + Flat Design | Medium | Formal | Cold | Immersive | Moderate |
| Vibrant & Block-based | High | Informal | Warm | Flat | Fast |
| Minimalism + Accessible | Low | Formal | Neutral | Flat | Slow |
| Brutalism + Motion | High | Informal | Cold | Elevated | Fast |
| Liquid Glass + Premium | Low | Formal | Warm | Immersive | Slow |
| Dark Mode + OLED | Medium | Semi-Formal | Cold | Immersive | Moderate |
| Neumorphism + Soft | Low | Informal | Warm | Elevated | Slow |

**Select 3-5 WOW Moments** from the Experience Database (`experience-db/`):
1. **Hero text reveal** (The Awakening) — stagger-fade heading + subtext + CTA
2. **Scroll section reveals** (The Cascade) — GSAP ScrollTrigger fade-up on each section
3. **Counter animation** (The Counter) — animated stats/numbers on scroll
4. **Card hover lift** — translateY(-8px) + shadow on hover
5. **Parallax** — multi-layer scroll speed differential
6. **Image reveal** — clip-path or scale reveal on scroll
7. **Smooth scroll** — Lenis for butter-smooth scrolling
8. **Cursor effects** — custom cursor with magnetic hover on CTAs

### Phase 3: Build — Scaffold & Sections

#### CDN Setup
```html
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- GSAP -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

<!-- Lenis -->
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>

<!-- Lucide Icons -->
<script src="https://unpkg.com/lucide@latest"></script>
```

#### Tailwind Config
Configure Tailwind with the design system colors from Phase 1:
```html
<script>
tailwind.config = {
  theme: {
    extend: {
      colors: {
        primary:   '#<hex>',  // from ui-ux-pro-max COLORS → Primary
        secondary: '#<hex>',  // from ui-ux-pro-max COLORS → Secondary
        accent:    '#<hex>',  // from ui-ux-pro-max COLORS → CTA
        bg:        '#<hex>',  // from ui-ux-pro-max COLORS → Background
        text:      '#<hex>',  // from ui-ux-pro-max COLORS → Text
      },
      fontFamily: {
        heading: ['<Font Name>', 'serif'],  // from TYPOGRAPHY → first font
        body:    ['<Font Name>', 'sans-serif'],  // from TYPOGRAPHY → second font
      }
    }
  }
}
</script>
```

#### Section Order (Standard)
1. **Navigation** — floating, transparent → glassmorphism on scroll
2. **Hero** — Experience 001 (The Awakening): stagger text reveal + CTA
3. **Social Proof** — client logos or trust metrics
4. **Services/Features** — card grid with hover lift
5. **Portfolio/Gallery** — masonry or grid with scroll reveals
6. **Testimonials** — carousel or grid with quote cards
7. **CTA** — final conversion section with urgency
8. **Contact** — form + info
9. **Footer** — multi-column with links + social

#### Theme Toggle (Standard)
Use the Lumary OS standardized theme toggle pattern:
```javascript
(function() {
  const saved = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  if (saved === 'dark' || (!saved && prefersDark)) {
    document.documentElement.classList.add('dark');
  }
})();
```

### Phase 4: Quality Check

- [ ] Mobile responsive (375px, 768px, 1024px, 1440px)
- [ ] WCAG AA contrast on all text (use `--muted: #475569` minimum)
- [ ] `prefers-reduced-motion` respected (Lenis destroyed, animations skipped)
- [ ] All interactive elements have `cursor-pointer`
- [ ] No emojis used as icons (use Lucide SVG icons)
- [ ] All images have `alt` text + `loading="lazy"` (below fold)
- [ ] No placeholder domains (use working Unsplash photo IDs only)
- [ ] Theme toggle works in both directions (light ↔ dark)
- [ ] Hover states have smooth transitions (150-300ms)
- [ ] Floating nav doesn't overlap content
- [ ] `will-change` hints on animated elements for 60fps
- [ ] Keyboard navigable (focus rings visible)

---

## One-Shot Prompt Template

Use this when the user says "Build a website for [X]":

```
Generate a complete, production-ready HTML file for a [INDUSTRY] website called [NAME].

First, run ui-ux-pro-max to generate the design system.
Then apply the Lumary OS build pipeline with the standard section order and 3-5 WOW moments.

Design system: [INSERT --design-system OUTPUT]
Experience Profile: [Energy/Formality/Warmth/Depth/Tempo]
WOW Moments: [List 3-5 experiences]

Output: A single self-contained index.html file with all CSS and JS inline.
```

---

## Industry → Design System Quick Reference

| Industry | ui-ux-pro-max Query | Expected Style |
|----------|--------------------|----------------|
| Construction | `construction architecture building` | Minimalism + Grey/Orange |
| Restaurant | `restaurant fine dining food` | Warm + Vibrant block |
| Real Estate | `real estate luxury property` | Glassmorphism + Minimal |
| SaaS / Tech | `saas technology software` | Flat Design + Trust Blue |
| E-Commerce | `ecommerce luxury fashion` | Vibrant + Premium |
| Creative Agency | `creative agency portfolio` | Brutalism + Motion |
| Blog / Magazine | `editorial blog magazine` | Minimal + Typography |
| Wellness / Spa | `wellness spa health` | Neumorphism + Calm |
| Fintech | `fintech crypto banking` | Glassmorphism + Dark |
| Education | `education learning platform` | Claymorphism + Playful |

---

## References
- Lumary OS `docs/` — 26 documents covering design, motion, a11y, perf, SEO
- Lumary OS `experience-db/` — 54 cataloged WOW moments
- Lumary OS `patterns/` — 19 reusable HTML components
- Lumary OS `prompts/` — Prompt templates for build, add-section, Stitch handoff
- ui-ux-pro-max `skills/ui-ux-pro-max/` — Search engine + CSV databases
