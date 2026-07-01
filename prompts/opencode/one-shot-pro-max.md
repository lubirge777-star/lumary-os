# Lumary Pro Max — One-Shot Website Prompt

## Usage
Replace placeholders in `[BRACKETS]` and give this prompt to the agent.

---

```
Build a complete, production-ready single-page HTML website for [BUSINESS NAME], a [INDUSTRY] company.

## Design System Generation
First, generate a data-driven design system using the ui-ux-pro-max search engine:
Run: python <ui-ux-pro-max-path>/search.py "[INDUSTRY KEYWORDS]" --design-system -p "[BUSINESS NAME]"
Extract the colors, fonts, style pattern, and recommended sections from the output.

## Experience Profile
Map the design system to this experience profile:
- Energy: [Low / Medium / High]
- Formality: [Formal / Semi-Formal / Informal]
- Warmth: [Cold / Neutral / Warm]
- Depth: [Flat / Elevated / Immersive]
- Tempo: [Slow / Moderate / Fast]

## WOW Moments (select 3-5)
- Hero text reveal (stagger-fade heading + subtext + CTA)
- Scroll section reveals (GSAP ScrollTrigger fade-up)
- Counter animation (animated stats on scroll)
- Card hover lift (translateY + shadow)
- Smooth scroll (Lenis)
- Image reveal (clip-path reveal on scroll)

## Section Order
1. Navigation — floating transparent → glassmorphism on scroll
2. Hero — full-screen with stagger reveal animation
3. Social Proof — client logos or metrics with counter animation
4. Services/Features — card grid with hover lift
5. Portfolio/Gallery — masonry or grid with scroll reveals
6. Testimonials — carousel or quote grid
7. CTA — final conversion section
8. Contact — form with name, email, message
9. Footer — multi-column with links + social

## Tech Stack
- HTML5 + Tailwind CSS (CDN)
- GSAP 3.12.5 + ScrollTrigger (CDN)
- Lenis 1.1.13 smooth scroll (CDN)
- Lucide icons (CDN)
- Google Fonts (from design system)

## Quality Requirements
- Single self-contained index.html file
- Mobile responsive (375px–1440px)
- WCAG AA contrast on all text
- `prefers-reduced-motion` respected
- All images from working Unsplash photo IDs
- Lucide SVG icons only (no emojis)
- Dark/light theme toggle
- `cursor-pointer` on all interactive elements
- Smooth transitions (150-300ms)
- Lighthouse Performance 90+

## Additional Context
- Target emotion: [TRUST / EXCITEMENT / CALM / DESIRE]
- Pages needed: [single-page / multi-page]
- Special features: [any specific requirements]
```

---

## Example: Construction Company

**Business:** Jenga Bora Builders
**Industry:** Construction / Architecture
**Keywords:** construction architecture building industrial
**Target emotion:** Trust + Confidence
**WOW Moments:** Hero reveal, scroll reveals, counter animation, card hover lift, smooth scroll

---

## Example: Luxury Restaurant

**Business:** The Spice Merchant
**Industry:** Restaurant / Fine Dining
**Keywords:** restaurant fine dining elegant warm
**Target emotion:** Desire + Warmth
**WOW Moments:** Hero reveal, image reveals, scroll reveals, card hover, smooth scroll
