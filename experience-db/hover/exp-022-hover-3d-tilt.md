# Experience 022: 3D Tilt on Hover

## Classification
Feedback

## Emotion
Delight → Engagement

## Difficulty
★★★☆☆

## Performance Impact
Low

## Libraries
GSAP

---

## Description

A 3D perspective tilt that follows the cursor on hover, giving elements a physical, tactile feel. Ideal for cards, buttons, and product showcases where depth creates perceived quality.

The effect maps cursor position within an element to rotateX and rotateY transforms, creating the illusion of a surface floating in 3D space.

---

## Interaction

User hovers over a `.tilt-3d` element. JavaScript captures `mousemove` coordinates relative to the element bounds, normalizes them to a -0.5 to 0.5 range, and applies inverse rotation via GSAP. On `mouseleave`, the element springs back to neutral with a smooth ease.

---

## Psychology

- **Depth Perception:** 3D transforms trigger innate spatial awareness, making flat UI feel dimensional and premium.
- **Novelty Effect:** Unusual motion patterns increase dwell time and exploration.
- **Control Illusion:** Direct cursor-to-element mapping gives user a sense of influence over the interface.

---

## Implementation

```html
<div class="tilt-3d" style="width: 320px; height: 420px; perspective: 1000px; cursor: pointer;">
  <div class="tilt-3d-inner" style="width: 100%; height: 100%; border-radius: 16px; background: linear-gradient(135deg, #1a1a2e, #16213e); display: flex; align-items: center; justify-content: center; color: white; font-family: system-ui; font-size: 1.5rem; transform-style: preserve-3d;">
    <span style="transform: translateZ(40px);">Lumary OS</span>
  </div>
</div>
```

```javascript
document.querySelectorAll('.tilt-3d').forEach(card => {
  const inner = card.querySelector('.tilt-3d-inner');

  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width - 0.5;
    const y = (e.clientY - rect.top) / rect.height - 0.5;

    gsap.to(inner, {
      rotateX: y * -12,
      rotateY: x * 12,
      duration: 0.4,
      ease: 'power2.out'
    });
  });

  card.addEventListener('mouseleave', () => {
    gsap.to(inner, {
      rotateX: 0,
      rotateY: 0,
      duration: 0.6,
      ease: 'power3.out'
    });
  });
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| E-commerce | ★★★★★ | Product card showcase |
| Creative Agency | ★★★★★ | Portfolio grid items |
| SaaS | ★★★☆☆ | Feature cards |
| Real Estate | ★★★★☆ | Property listing cards |
| Education | ★★☆☆☆ | Distracting for learning content |

---

## Accessibility Notes

- Disable entirely when `prefers-reduced-motion: reduce` is set
- Focus states must remain visible — tilt should not break outline
- Touch devices get no tilt; ensure content is still readable

---

## Performance Notes

- Uses GPU-composited `rotateX`/`rotateY` — no layout thrashing
- Apply `will-change: transform` to tilt-3d elements
- Avoid on more than 12 elements per page to keep repaint cost low

---

## Variants

### Variant A: Subtle (2-3 degree max)
For professional/B2B contexts where minimal motion is preferred.

### Variant B: Glare Follow
Add a radial gradient overlay that tracks the cursor position for a shiny surface effect.

### Variant C: Depth Card
Add multiple inner elements at different `translateZ` values for a layered 3D scene.

---

## Anti-Patterns

- Applying tilt to full-page sections — causes motion sickness
- Mobile-only implementation — no cursor on touch devices
- Ignoring `perspective` — without it the rotate has no depth illusion
- Jitter from not debouncing `mousemove` — GSAP's `.to()` handles smoothing

---

## Checklist

- [ ] `perspective` set on parent container
- [ ] `transform-style: preserve-3d` on inner element
- [ ] Reduced motion respected
- [ ] Touch devices have static fallback
- [ ] Max rotation ≤ 15 degrees
