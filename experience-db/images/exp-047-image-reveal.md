# Experience 047: Image Reveal (Clip-Path / Scale)

## Classification
Narrative

## Emotion
Anticipation → Satisfaction

## Difficulty
★★★☆☆

## Performance Impact
Low

## Libraries
GSAP, ScrollTrigger

---

## Description

An image is initially hidden (masked or scaled down) and is revealed with a smooth animation triggered by scroll or hover. Common techniques include `clip-path` rectangle expansion, scale-up from center, or a diagonal wipe. The reveal creates a dramatic entrance for visual content.

Use for portfolio grids, gallery images, blog featured images, product showcases, or any scenario where images should appear deliberately rather than all at once.

---

## Timeline

| Moment | Time | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0ms | Image wrapper | Set initial clip-path (0% rectangle) or scale(0.8) | 0ms | — |
| 2 | scroll-in | Image wrapper | Expand clip-path to 100% or scale to 1 | 800ms | Power3.out |
| 3 | reveal-end | Image wrapper | Subtle overshoot settle | — | — |

---

## Psychology

- **Curiosity Gap:** A partially hidden image creates intrigue — the user must wait to see the full picture.
- **Reveal as Reward:** The act of revealing feels earned — whether by scroll progress or hover action.
- **Visual Weight:** Images that reveal with animation feel more important than those that simply appear.

---

## Implementation

```html
<div class="reveal-image-grid" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 2rem; max-width: 800px; margin: 0 auto;">
  <div class="reveal-image-wrap" style="overflow: hidden; border-radius: 16px; position: relative;">
    <img src="https://picsum.photos/400/500?random=rev1" alt="Reveal 1" style="width: 100%; display: block;" />
  </div>
  <div class="reveal-image-wrap" style="overflow: hidden; border-radius: 16px; position: relative;">
    <img src="https://picsum.photos/400/500?random=rev2" alt="Reveal 2" style="width: 100%; display: block;" />
  </div>
  <div class="reveal-image-wrap" style="overflow: hidden; border-radius: 16px; position: relative;">
    <img src="https://picsum.photos/400/500?random=rev3" alt="Reveal 3" style="width: 100%; display: block;" />
  </div>
  <div class="reveal-image-wrap" style="overflow: hidden; border-radius: 16px; position: relative;">
    <img src="https://picsum.photos/400/500?random=rev4" alt="Reveal 4" style="width: 100%; display: block;" />
  </div>
</div>
```

```javascript
gsap.registerPlugin(ScrollTrigger);

document.querySelectorAll('.reveal-image-wrap').forEach((wrap, i) => {
  // Set initial state
  gsap.set(wrap, {
    clipPath: 'inset(0 0 100% 0)',
    y: 30,
    opacity: 0
  });

  ScrollTrigger.create({
    trigger: wrap,
    start: 'top 85%',
    onEnter: () => {
      gsap.to(wrap, {
        clipPath: 'inset(0 0 0% 0)',
        y: 0,
        opacity: 1,
        duration: 0.8,
        delay: i * 0.15,
        ease: 'power3.out'
      });
    },
    once: true,
    // Reduced motion
    onRefresh: (self) => {
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        gsap.set(wrap, { clipPath: 'inset(0 0 0% 0)', y: 0, opacity: 1 });
        self.disable();
      }
    }
  });
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Creative Agency | ★★★★★ | Portfolio grid reveals |
| E-commerce | ★★★★☆ | Product gallery |
| Real Estate | ★★★★☆ | Property photo showcases |
| Travel | ★★★★★ | Destination galleries |
| Blog / Media | ★★★★☆ | Featured images |

---

## Accessibility Notes

- Images must have descriptive `alt` text — reveal is decorative
- `prefers-reduced-motion: reduce` — show all images immediately without animation
- Ensure images are fully visible to screen readers (not hidden via `aria-hidden`)
- No flashing or rapid reveals that could trigger vestibular disorders

---

## Performance Notes

- `clip-path` is a composited property in modern browsers (no paint)
- `opacity` and `y` transforms are GPU accelerated
- Stagger multiple reveals by 150ms each to avoid "all at once" visual noise
- For `clip-path` on older browsers, fall back to `opacity` + `scale` reveal

---

## Variants

### Variant A: Scale Reveal
Image scales from 0.8 to 1 with opacity fade — no clip-path, better browser support.

### Variant B: Diagonal Wipe
`clip-path: polygon(0 0, 0 0, 0 100%, 0 100%)` animating to `polygon(0 0, 100% 0, 100% 100%, 0 100%)` for a diagonal sweep.

### Variant C: Mask Reveal (Text Mask)
Image revealed through animated text or shape mask using CSS `mask-image`.

---

## Anti-Patterns

- Reveal direction mismatched with image content (e.g., top-down reveal on a landscape image)
- All images in grid revealing at the same time — overwhelming
- No `overflow: hidden` — clip-path edges visible
- Using `clip-path` on images that later need interaction within clipped area

---

## Checklist

- [ ] Initial state set with `gsap.set()` (no visible flash)
- [ ] Stagger delay between items (100-200ms)
- [ ] Reduced motion: show all immediately
- [ ] `alt` text on all images
- [ ] Fallback for browsers without `clip-path` support
- [ ] ScrollTrigger `once: true` to avoid re-triggering
