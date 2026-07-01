# Metrics — The Lumary Score

## Why

"Good website" is subjective.

The Lumary Score replaces opinion with measurement. Every project receives a score across 8 dimensions — not to grade, but to guide improvement.

---

## The Lumary Score

### Curiosity Score (0-100)
How likely is the user to explore further?
- Scroll depth (% of page reached)
- Interaction rate (clicks / hovers / scrolls per session)
- Time-to-next-section
- **Target: 80+**

### Memory Score (0-100)
What does the user remember after 24 hours?
- WOW moment recall (did they remember the animation?)
- CTA recall (did they remember what to do?)
- Brand recall (did they remember the name?)
- **Target: 75+**

### Interaction Density (0-100)
How alive does the interface feel?
- Number of interactive elements per viewport
- Response time for hover/click feedback
- Variety of interaction types (hover, scroll, click, drag)
- **Target: 60-80** (too low = dead, too high = overwhelming)

### Motion Density (0-100)
How much purposeful movement exists?
- Number of animated elements per section
- Duration distribution (100ms micro-interactions to 2s reveals)
- Transition quality (easing appropriateness, no jarring movements)
- **Target: 50-70**

### Cognitive Load (0-100, inverted)
How easy is it to process the page?
- Information density (elements per section)
- Reading time vs. actual content
- Distraction count (flashing, auto-playing, pop-ups)
- **Target: 80+** (lower = better, inverted score)

### Conversion Readiness (0-100)
How optimized is the page for its primary goal?
- CTA visibility (above fold, contrast, whitespace)
- Friction count (form fields, steps, clicks to convert)
- Trust signals (badges, testimonials, security indicators)
- **Target: 85+**

### Performance Budget (0-100)
How fast does it feel?
- Lighthouse Performance score
- Largest Contentful Paint (LCP) under 2.5s
- First Input Delay (FID) under 100ms
- Cumulative Layout Shift (CLS) under 0.1
- **Target: 90+**

### Accessibility Score (0-100)
How inclusive is the experience?
- WCAG AA compliance (minimum)
- Keyboard navigation completeness
- Screen reader compatibility
- Color contrast ratio (4.5:1 minimum)
- `prefers-reduced-motion` support
- **Target: 90+**

---

## Calculating the Lumary Score

```text
Lumary Score = (Curiosity + Memory + InteractionDensity + MotionDensity
                + CognitiveLoad + ConversionReadiness + Performance + Accessibility) / 8
```

| Score | Rating |
|-------|--------|
| 95-100 | World-class |
| 85-94 | Excellent |
| 70-84 | Good |
| 50-69 | Needs work |
| <50 | Poor |

---

## How to Measure

| Metric | Tool / Method |
|--------|--------------|
| Scroll depth | `IntersectionObserver` logging |
| Interaction rate | Custom event tracking |
| WOW recall | User surveys after 24h |
| Response time | Chrome DevTools Performance |
| Lighthouse | Chrome Lighthouse / PageSpeed Insights |
| Contrast | WebAIM Contrast Checker |
| Keyboard nav | Manual tab-through + axe DevTools |
| Screen reader | VoiceOver / NVDA manual test |

---

## Related Documents

- `docs/12-performance.md` — Performance budget guidelines
- `docs/11-accessibility.md` — Accessibility standards
- `docs/23-quality-assurance.md` — QA pipeline and checklist
