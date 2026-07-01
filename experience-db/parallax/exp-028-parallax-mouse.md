# Experience 028: Mouse-Driven Parallax

## Classification
Feedback

## Emotion
Delight → Playfulness

## Difficulty
★★☆☆☆

## Performance Impact
Low

## Libraries
GSAP

---

## Description

Elements on the page shift position in response to mouse movement, creating a 3D depth effect where items appear to float at different distances from the viewer. Unlike scroll parallax, this responds to cursor position in real-time.

Use for hero images, floating UI elements, product showcases, or any visual where a premium, interactive feel is desired.

---

## Interaction

User moves their mouse across the viewport. JavaScript calculates cursor position normalized to -1 to 1 range. GSAP updates each element's `x` and `y` transform proportionally to its assigned depth factor, creating the illusion of a 3D space viewed through a moving window.

---

## Psychology

- **Kinesthetic Response:** Direct mouse-to-element mapping satisfies the brain's expectation that movement changes perspective.
- **Depth Layering:** Varying movement speeds between elements reinforces their perceived distance, strengthening visual hierarchy.
- **Engagement Loop:** Small, continuous motion rewards every cursor movement, keeping users exploring the page.

---

## Implementation

```html
<div class="mouse-parallax" style="position: relative; height: 600px; overflow: hidden; border-radius: 20px; cursor: crosshair;">
  <div class="mp-layer" data-depth="0.1" style="position: absolute; top: 10%; left: 15%; width: 200px;">
    <img src="https://picsum.photos/200/200?random=1" alt="" style="width: 100%; border-radius: 16px;" />
  </div>
  <div class="mp-layer" data-depth="0.3" style="position: absolute; top: 50%; right: 20%; width: 150px;">
    <img src="https://picsum.photos/150/150?random=2" alt="" style="width: 100%; border-radius: 50%;" />
  </div>
  <div class="mp-layer" data-depth="0.05" style="position: absolute; bottom: 15%; left: 40%; width: 120px;">
    <div style="width: 100%; height: 120px; background: linear-gradient(135deg, #6c5ce7, #a29bfe); border-radius: 20px;"></div>
  </div>
</div>
```

```javascript
const container = document.querySelector('.mouse-parallax');
const layers = container.querySelectorAll('.mp-layer');

container.addEventListener('mousemove', (e) => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const rect = container.getBoundingClientRect();
  const x = ((e.clientX - rect.left) / rect.width - 0.5) * 2;
  const y = ((e.clientY - rect.top) / rect.height - 0.5) * 2;

  layers.forEach(layer => {
    const depth = parseFloat(layer.dataset.depth);
    gsap.to(layer, {
      x: x * 40 * depth,
      y: y * 40 * depth,
      duration: 0.6,
      ease: 'power2.out'
    });
  });
});

container.addEventListener('mouseleave', () => {
  gsap.to(layers, {
    x: 0,
    y: 0,
    duration: 0.8,
    ease: 'power3.out'
  });
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Creative Agency | ★★★★★ | Portfolio hero showcases |
| E-commerce | ★★★★☆ | Product float display |
| Gaming | ★★★★★ | Character/asset showcases |
| Technology | ★★★★☆ | Device mockup presentation |
| Legal | ★☆☆☆☆ | Too playful for professional services |

---

## Accessibility Notes

- Content must be fully visible and readable without mouse movement
- Disable entirely under `prefers-reduced-motion: reduce`
- Touch devices: consider using device orientation or a gentle idle animation instead
- Do not move text elements — only images and decorative graphics

---

## Performance Notes

- Only `x`/`y` translate transforms — fully GPU composited
- Uses `requestAnimationFrame` under GSAP hood — battery efficient
- `mouseleave` handler resets positions to avoid stuck elements

---

## Variants

### Variant A: Tilt-Shift Parallax
Elements also rotate slightly based on cursor position for a diorama effect.

### Variant B: Blur Depth
Elements with higher depth values have higher baseline `blur()` that reduces as cursor brings them "into focus."

### Variant C: Container-Bound Parallax
Each element reacts only when cursor is within its own bounds (for independent cards).

---

## Anti-Patterns

- Moving text content — impairs readability
- Depth values above 0.5 — elements move too far, breaks the illusion
- No mouseleave reset — elements stay offset if cursor leaves quickly
- Applying to full layout — causes motion sickness

---

## Checklist

- [ ] Depth values between 0.02 and 0.4
- [ ] Reduced motion respected
- [ ] Text elements excluded from parallax
- [ ] `mouseleave` handler resets positions
- [ ] Tested on touch (falls back gracefully)
