# Experience 001: The Awakening

## Classification
Narrative

## Emotion
Curiosity → Excitement

## Difficulty
★★★★☆

## Performance Impact
Medium

## Libraries
GSAP, Lenis, SplitType (optional)

---

## Description

The Awakening is a cinematic arrival experience. When the page loads, the visitor is greeted not with static content, but with a choreographed sequence that builds anticipation before revealing the core message.

This is the most premium arrival pattern in our library. Use it when first impressions matter most.

---

## Timeline

| Moment | Time | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0ms | Background | Slow zoom in from 1.1x → 1x | 2000ms | Power4.out |
| 2 | 400ms | Overlay | Fade from black/dark to transparent | 800ms | Power2.out |
| 3 | 600ms | Heading words | Stagger in from y:40, opacity:0 | 1000ms total | Power3.out |
| 4 | 1200ms | Subheading | Fade in + translate up | 800ms | Power2.out |
| 5 | 1500ms | Decorative element | Scale up from 0 → 1 with rotation | 1000ms | Back.out(1.2) |
| 6 | 1800ms | Primary CTA | Fade in + translate up | 600ms | Power2.out |
| 7 | 2000ms | Scroll indicator | Fade in (loop pulse) | 400ms | Power1.out |

---

## Interaction

No user interaction required. The experience plays on page load.

For subsequent visits, consider shortening the timeline by 50% (repeat viewers do not need the full buildup).

---

## Psychology

- **Primacy Effect:** The first experience sets the tone for the entire visit. A cinematic arrival signals premium quality.
- **Curiosity Gap:** Staggered reveals create micro-moments of curiosity — *"What's next?"*
- **Peak-End:** The final element (CTA) enters last, creating a natural action point.

---

## Implementation

```html
<section class="hero" data-experience="awakening">
  <div class="hero-bg">
    <img src="hero.jpg" alt="" />
  </div>
  <div class="hero-content">
    <h1 class="hero-heading split-text">Build Beyond Boundaries</h1>
    <p class="hero-subtext">Premium construction services for ambitious projects.</p>
    <a href="/contact" class="hero-cta btn-primary">Start Your Project</a>
    <div class="scroll-indicator">Scroll</div>
  </div>
</section>
```

```javascript
// GSAP: The Awakening
const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });

// Background cinematic zoom
tl.fromTo('.hero-bg img', 
  { scale: 1.1, opacity: 0 },
  { scale: 1, opacity: 1, duration: 2, ease: 'power4.out' }
)
// Overlay fade
.fromTo('.hero-overlay',
  { opacity: 1 },
  { opacity: 0, duration: 0.8 },
  '-=1.2'
)
// Heading — word stagger via SplitType or manual spans
.fromTo('.hero-heading .word',
  { y: 40, opacity: 0 },
  { y: 0, opacity: 1, duration: 0.8, stagger: 0.1 },
  '-=0.4'
)
// Subtext
.fromTo('.hero-subtext',
  { y: 24, opacity: 0 },
  { y: 0, opacity: 1, duration: 0.7 },
  '-=0.3'
)
// Decorative element
.fromTo('.hero-decoration',
  { scale: 0, opacity: 0, rotation: -15 },
  { scale: 1, opacity: 0.6, rotation: 0, duration: 1, ease: 'back.out(1.2)' },
  '-=0.5'
)
// CTA
.fromTo('.hero-cta',
  { y: 16, opacity: 0 },
  { y: 0, opacity: 1, duration: 0.5 },
  '-=0.2'
)
// Scroll indicator
.fromTo('.scroll-indicator',
  { opacity: 0 },
  { opacity: 1, duration: 0.4 },
  '-=0.1'
);
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Construction | ★★★★★ | Cinematic project imagery, bold typography |
| Luxury Real Estate | ★★★★★ | Property showcase, aspirational feel |
| Creative Studio | ★★★★★ | Portfolio first impression |
| Hospitality | ★★★★☆ | Ambient video backgrounds |
| Technology | ★★★★☆ | Product launches |
| E-commerce | ★★★☆☆ | Only for premium/luxury brands |
| Healthcare | ★★☆☆☆ | Too slow for urgency-required contexts |
| SaaS | ★★☆☆☆ | Better for landing pages, not dashboards |

---

## Accessibility Notes

- Entire sequence disabled if `prefers-reduced-motion: reduce`
- Content must be fully visible and readable without animation
- No flashing or stroboscopic effects
- `aria-live="polite"` on hero content for screen readers

---

## Performance Notes

- Hero image must be optimized (WebP, < 300KB)
- Consider using `<video>` instead of `<img>` for cinematic effect (muted, autoplay, loop, < 1MB)
- Lenis smooth scroll should be initialized before this experience
- Preload hero image in `<head>`:

```html
<link rel="preload" as="image" href="hero.webp" />
```

---

## Variants

### Variant A: Light (For fast-loading expectations)
Remove the background zoom. Focus on text stagger only. Total timeline: ~1000ms.

### Variant B: Video (For maximum cinematic impact)
Replace background image with muted autoplay video. Add color overlay.

### Variant C: Minimal (For professional services)
Remove decorative elements. Clean fade-in only. Total timeline: ~800ms.

---

## Anti-Patterns

- **Too slow:** > 3s total timeline risks user impatience
- **No reduced-motion:** Excludes users with vestibular disorders
- **Everything at once:** Eliminates the curiosity gap
- **Skip intro button:** Not needed — users can scroll past. Do not add "Skip" — it undermines the experience
- **Repeating on every page:** Use only on landing/home page

---

## Checklist

- [ ] Total timeline ≤ 2500ms
- [ ] Background image/video optimized
- [ ] `prefers-reduced-motion` respected
- [ ] Text visible without animation (no opacity:0 in HTML)
- [ ] CTA is the final element to enter
- [ ] Tested on mobile (reduce total duration by 30% for mobile)
- [ ] Lighthouse Performance ≥ 90
