# Quality Assurance

## Version 1.0

---

## Philosophy
Quality is not a final step. It is embedded in every stage of the process. Every line of code, every design decision, every interaction is tested before it reaches the client.

---

## QA Stages

### Stage 1: Development QA (Build-Time)
```
As each section is built:
  □ HTML validates
  □ Semantic elements used (nav, main, section, article)
  □ ARIA attributes correct
  □ Tailwind classes consistent with design system
  □ Images have alt text / aria-hidden="true" if decorative
  □ No console errors
  □ GSAP animations work without errors
  □ prefers-reduced-motion respected
```

### Stage 2: Visual QA (Design vs Code)
```
  □ All sections present and in correct order
  □ Colors match the palette (hex verified)
  □ Typography matches spec (font, size, weight)
  □ Spacing follows 8px grid
  □ Border radius consistent
  □ Shadows subtle, not heavy
  □ Glassmorphism effects render correctly
```

### Stage 3: Responsive QA
```
  □ Tested at 375px, 768px, 1024px, 1280px, 1536px
  □ No horizontal scroll
  □ All elements visible at all breakpoints
  □ Navigation usable on mobile (thumb reach)
  □ Forms usable on mobile keyboard
  □ Images responsive (not stretched/cropped)
```

### Stage 4: Functional QA
```
  □ All links work (internal + external + anchor)
  □ Contact form submits (tested end-to-end)
  □ WhatsApp button opens correct number
  □ Phone links work on mobile
  □ Google Maps embed loads
  □ Social media links open in new tab
  □ Page scrolls smoothly (Lenis)
  □ Mobile menu opens/closes correctly
```

### Stage 5: Performance QA
```
  □ Lighthouse Performance ≥ 90
  □ Lighthouse Accessibility ≥ 90
  □ Lighthouse Best Practices ≥ 90
  □ Lighthouse SEO ≥ 90
  □ Page weight < 2MB
  □ No render-blocking resources
  □ Images lazy-loaded with dimensions
  □ Fonts display with swap
  □ Core Web Vitals pass
```

### Stage 6: Accessibility QA
```
  □ Tab through entire page (all elements reachable)
  □ Focus indicators visible
  □ Screen reader test (NVDA or VoiceOver)
  □ Color contrast verified (4.5:1 text minimum)
  □ prefers-reduced-motion respected
  □ All form inputs have labels
  □ Error messages associated with inputs
```

### Stage 7: Content QA
```
  □ No placeholder text remaining
  □ All images are real (not placeholder/unsplash in production)
  □ Spelling and grammar checked
  □ Phone numbers, addresses, emails correct
  □ Business hours accurate
  □ Pricing (if shown) accurate
  □ Team names and titles correct
```

---

## Pre-Delivery Sign-Off

Before marking a project as complete, run this final checklist:

```
VISUAL
  □ Design matches approved mockup
  □ Animations work smoothly (60fps)
  □ No visual glitches, artifacts, or flickering
  □ Favicon present

FUNCTIONAL
  □ All forms working with validation
  □ All links verified
  □ No 404 pages
  □ SSL certificate valid
  □ Custom domain working (if applicable)

CONTENT
  □ All placeholder text replaced
  □ Images optimized and not placeholders
  □ Meta titles/descriptions set per page
  □ Open Graph tags set
  □ Structured data (JSON-LD) present

BUSINESS
  □ Analytics installed and events firing
  □ Google Search Console submitted
  □ Google Business Profile updated (if applicable)
  □ Sitemap submitted
  □ Client login/access provided
  □ Handoff documentation provided
```

---

## QA Anti-Patterns

| Anti-Pattern | Why |
|---|---|
| Skipping mobile testing | 60%+ of traffic is mobile |
| Testing only in Chrome | Safari, Firefox have rendering differences |
| Not testing forms end-to-end | Broken contact form = lost leads |
| Assuming reduced motion works | Must be explicitly tested |
| Not testing on real devices | Emulators miss touch/performance issues |
| Delaying QA to the end | Bugs found late are expensive to fix |
