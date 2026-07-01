# Experience 027: Multi-Depth Parallax Scrolling

## Classification
Narrative

## Emotion
Wonder → Immersion

## Difficulty
★★★☆☆

## Performance Impact
Medium

## Libraries
GSAP, ScrollTrigger

---

## Description

A multi-layer parallax system where foreground, midground, and background elements scroll at different speeds, creating an illusion of 3D depth. The user feels as though they are moving through a dimensional space rather than a flat page.

Use on hero sections, landing pages, or storytelling layouts where spatial depth reinforces the narrative.

---

## Timeline

| Moment | Time | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0ms | Background layer | Parallax at 0.2x scroll speed | viewport-dependent | Linear |
| 2 | 0ms | Midground layer | Parallax at 0.5x scroll speed | viewport-dependent | Linear |
| 3 | 0ms | Foreground layer | Parallax at 0.8x scroll speed | viewport-dependent | Linear |
| 4 | scroll-end | All layers | Settle at final positions | 300ms | Power2.out |

---

## Psychology

- **Depth Perception:** Relative motion between layers triggers innate depth processing, making the scene feel three-dimensional.
- **Motion Parallax Cue:** The brain interprets speed differential as distance — a core visual cue from real-world movement.
- **Immersion:** Scrolling that responds with layered motion feels more like exploring a world than reading a page.

---

## Implementation

```html
<section class="parallax-depth" style="height: 200vh; position: relative; overflow: hidden;">
  <div class="parallax-layer parallax-bg" style="position: fixed; top: -20%; left: -10%; width: 120%; height: 120%; z-index: 1;">
    <img src="https://picsum.photos/1920/1080?random=bg" alt="" style="width: 100%; height: 100%; object-fit: cover;" />
  </div>
  <div class="parallax-layer parallax-mid" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 2; display: flex; align-items: center; justify-content: center;">
    <h2 style="color: white; font-family: system-ui; font-size: 5rem; text-shadow: 0 4px 20px rgba(0,0,0,0.5);">Depth</h2>
  </div>
  <div class="parallax-layer parallax-fg" style="position: absolute; bottom: -10%; left: 10%; width: 300px; height: 300px; z-index: 3;">
    <img src="https://picsum.photos/300/300?random=fg" alt="" style="width: 100%; height: 100%; object-fit: cover; border-radius: 24px;" />
  </div>
</section>
```

```javascript
gsap.registerPlugin(ScrollTrigger);

const tl = gsap.timeline({
  scrollTrigger: {
    trigger: '.parallax-depth',
    start: 'top top',
    end: 'bottom top',
    scrub: true
  }
});

tl
  .to('.parallax-bg', { y: '10%', scale: 1.1, duration: 1 }, 0)
  .to('.parallax-mid', { y: '5%', duration: 1 }, 0)
  .to('.parallax-fg', { y: '-15%', scale: 0.9, duration: 1 }, 0);
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Creative Agency | ★★★★★ | Portfolio storytelling |
| Travel | ★★★★★ | Destination depth scenes |
| Real Estate | ★★★★☆ | Property hero depth |
| Technology | ★★★★☆ | Product launch pages |
| E-commerce | ★★★☆☆ | Only for flagship brand pages |
| Healthcare | ★★☆☆☆ | Not suitable for clinical contexts |

---

## Accessibility Notes

- Content must be fully readable without parallax motion
- Disable parallax under `prefers-reduced-motion: reduce` — show layers stacked normally
- Fixed-position layers can cause issues with screen reader virtual cursors
- Text must have sufficient contrast against all background layers

---

## Performance Notes

- `position: fixed` layers are compositor-only, no layout cost
- Large background images must be optimized (WebP, < 500KB per layer)
- Use `will-change: transform` on each parallax layer
- Max 3 layers — more than 4 causes jank on mid-range devices

---

## Variants

### Variant A: Subtle Depth (1.5 layers)
Only background and foreground — less performance cost, suitable for SaaS pages.

### Variant B: Parallax Hero
Full-viewport hero where only the background moves. Mid and foreground are static.

### Variant C: Depth Stack
Elements at different z-depths within a single container (CSS `translateZ`) with scroll-linked translateY offsets.

---

## Anti-Patterns

- More than 4 parallax layers — performance degrades significantly
- Moving elements that overlap interactive content (buttons, links) — breaks click targets
- Parallax on every section — causes motion fatigue
- Ignoring mobile — fixed positioning behaves differently on mobile browsers

---

## Checklist

- [ ] Max 3 parallax layers
- [ ] Images optimized and preloaded
- [ ] Reduced motion respected
- [ ] Tested on mobile (disable or reduce)
- [ ] No interactive elements inside parallax layers
