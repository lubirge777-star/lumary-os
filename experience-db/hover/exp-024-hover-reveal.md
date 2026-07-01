# Experience 024: Hover Reveal

## Classification
Feedback

## Emotion
Curiosity → Discovery

## Difficulty
★★☆☆☆

## Performance Impact
Low

## Libraries
GSAP

---

## Description

A content swap effect triggered on hover where one piece of content (e.g., an image) transitions into another (e.g., text) with a smooth animation. Common use cases include image-to-text reveals, label-to-description swaps, and before/after previews.

The effect works by crossfading or translating two stacked layers, creating a clean information hierarchy that rewards exploration.

---

## Interaction

User hovers over a `.reveal-card` container. The front layer (image) fades or translates out while the back layer (text description) fades or translates in. On `mouseleave`, the animation reverses. A subtle easing curve gives it a polished, non-jarring feel.

---

## Psychology

- **Curiosity Gap:** Hiding information until hover creates micro-rewards that encourage exploration.
- **Lazy Loading (Cognitive):** Users only retrieve detailed information when they signal interest, reducing cognitive load at rest.
- **Surprise & Delight:** The transformation from visual to textual (or vice versa) feels like a magic trick.

---

## Implementation

```html
<div class="reveal-card" style="width: 300px; height: 380px; position: relative; overflow: hidden; border-radius: 16px; cursor: pointer;">
  <div class="reveal-front" style="position: absolute; inset: 0;">
    <img src="https://picsum.photos/300/380?random=1" alt="Preview" style="width: 100%; height: 100%; object-fit: cover;" />
  </div>
  <div class="reveal-back" style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; padding: 2rem; background: #1a1a2e; color: white; font-family: system-ui; opacity: 0;">
    <div style="text-align: center;">
      <h3 style="margin: 0 0 0.5rem;">Lumary Suite</h3>
      <p style="margin: 0; font-size: 0.9rem; opacity: 0.8;">Design system experience platform for modern interfaces.</p>
    </div>
  </div>
</div>
```

```javascript
document.querySelectorAll('.reveal-card').forEach(card => {
  const front = card.querySelector('.reveal-front');
  const back = card.querySelector('.reveal-back');

  card.addEventListener('mouseenter', () => {
    gsap.to(front, {
      opacity: 0,
      scale: 1.05,
      duration: 0.4,
      ease: 'power2.out'
    });
    gsap.to(back, {
      opacity: 1,
      duration: 0.4,
      ease: 'power2.out',
      delay: 0.1
    });
  });

  card.addEventListener('mouseleave', () => {
    gsap.to(front, {
      opacity: 1,
      scale: 1,
      duration: 0.4,
      ease: 'power2.out'
    });
    gsap.to(back, {
      opacity: 0,
      duration: 0.3,
      ease: 'power2.in'
    });
  });
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| E-commerce | ★★★★★ | Product image to description swap |
| Portfolio | ★★★★★ | Thumbnail to project info |
| Real Estate | ★★★★☆ | Property photo to details |
| Team Pages | ★★★★☆ | Photo to bio reveal |
| Food / Hospitality | ★★★☆☆ | Dish image to ingredients |

---

## Accessibility Notes

- Front content must have descriptive `alt` text
- Back content should be available via keyboard focus (`:focus-visible` equivalent)
- Ensure sufficient color contrast on the back layer
- `prefers-reduced-motion: reduce` — show both layers statically side by side

---

## Performance Notes

- Only opacity and transform changes — GPU composited
- No layout triggers; safe for large grids
- Images on front layer should be preloaded

---

## Variants

### Variant A: Slide Reveal
Front slides up/left while back slides in from opposite direction.

### Variant B: Scale Reveal
Back layer scales from 0.8 to 1 while front scales from 1 to 1.1.

### Variant C: Blur Reveal
Front layer blurs out while back unblurs in — cinematic depth-of-field effect.

---

## Anti-Patterns

- Revealing critical information that should always be visible
- Using on touch-only devices without a tap fallback
- Animating `height` or `width` — causes layout reflow
- Different content lengths causing layout shift

---

## Checklist

- [ ] Front and back layers same dimensions
- [ ] Keyboard focus handling added
- [ ] Reduced motion: show both layers
- [ ] Images preloaded
- [ ] Tested on touch devices (tap to reveal)
