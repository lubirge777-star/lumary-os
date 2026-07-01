# Experience 046: Image Zoom on Hover

## Classification
Feedback

## Emotion
Discovery → Delight

## Difficulty
★★☆☆☆

## Performance Impact
Low

## Libraries
GSAP

---

## Description

An image zooms in smoothly when hovered, revealing finer details. The zoom can be center-focused or cursor-tracking (lens effect). GSAP provides the smooth easing that distinguishes a premium feel from a basic CSS `scale` transition.

Use for product images, portfolio thumbnails, team photos, or any grid where revealing detail on hover adds value.

---

## Interaction

User hovers over an image container. GSAP scales the image from 1 to a defined max (e.g., 1.3x) with a power ease for smooth acceleration. For cursor-tracking variants, the `transform-origin` updates based on cursor position within the container. On `mouseleave`, the image smoothly scales back to 1.

---

## Psychology

- **Detail Discovery:** Zoom invites exploration — users feel like they are inspecting a physical object.
- **Reward for Interaction:** Smooth, responsive zoom reinforces that the interface is high-quality and polished.
- **FOMO Avoidance:** The promise of seeing more detail on hover encourages users to hover over all images in a grid.

---

## Implementation

```html
<div class="zoom-container" style="width: 400px; height: 400px; overflow: hidden; border-radius: 16px; cursor: crosshair; position: relative;">
  <img class="zoom-image" src="https://picsum.photos/800/800?random=zoom" alt="Zoom example"
    style="width: 100%; height: 100%; object-fit: cover; will-change: transform;" />
</div>
```

```javascript
document.querySelectorAll('.zoom-container').forEach(container => {
  const img = container.querySelector('.zoom-image');
  const scale = 1.4;

  container.addEventListener('mouseenter', () => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    gsap.to(img, {
      scale: scale,
      duration: 0.6,
      ease: 'power3.out'
    });
  });

  container.addEventListener('mousemove', (e) => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const rect = container.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * 100;
    const y = ((e.clientY - rect.top) / rect.height) * 100;

    gsap.to(img, {
      transformOrigin: `${x}% ${y}%`,
      duration: 0.3,
      ease: 'power1.out'
    });
  });

  container.addEventListener('mouseleave', () => {
    gsap.to(img, {
      scale: 1,
      transformOrigin: '50% 50%',
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
| E-commerce | ★★★★★ | Product image zoom |
| Creative | ★★★★★ | Portfolio artwork detail |
| Real Estate | ★★★★☆ | Property photo detail |
| Art / Museum | ★★★★★ | High-res artwork inspection |
| Technology | ★★★☆☆ | Device screenshots |

---

## Accessibility Notes

- Image must have descriptive `alt` text — zoom is decorative enhancement
- `prefers-reduced-motion: reduce` — no zoom, image stays at native scale
- Ensure the full image is visible without hover (no critical detail hidden at 1x)
- Cursor tracking zoom must not obscure the view for keyboard users

---

## Performance Notes

- `scale` transform is GPU composited — no layout cost
- `will-change: transform` on image for layer promotion
- `transform-origin` changes are cheap (no repaint in modern browsers)
- Max scale 1.5x — beyond that reveals pixelation and causes jank

---

## Variants

### Variant A: Center Zoom (No Cursor Tracking)
Simple center-scale without cursor tracking — cleaner, less expensive, works well for grids.

### Variant B: Lens Zoom
A circular magnifier follows the cursor, showing a zoomed portion of the image underneath.

### Variant C: Window Zoom
A separate zoom window appears showing a magnified region of the image — classic e-commerce pattern.

---

## Anti-Patterns

- Scale > 1.5x — reveals low-res pixelation; use higher resolution source image
- No `overflow: hidden` — image spills outside container
- Cursor zoom on small images (< 150px) — no room for meaningful zoom
- Zoom without easing — feels abrupt and cheap
- Applying to images with text — text becomes unreadable at 1.4x

---

## Checklist

- [ ] Max scale ≤ 1.5x
- [ ] Container has `overflow: hidden`
- [ ] High-resolution source image (2x display density)
- [ ] Reduced motion: no zoom
- [ ] `alt` text provided
- [ ] Touch device fallback (tap to zoom)
