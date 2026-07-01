# Experience 026: SVG Border Draw on Hover

## Classification
Feedback

## Emotion
Delight → Polish

## Difficulty
★★★☆☆

## Performance Impact
Low

## Libraries
GSAP

---

## Description

An animated SVG border that draws itself around an element when hovered. Using SVG's `stroke-dasharray` and `stroke-dashoffset` properties, the border appears to be drawn by an invisible pen, creating a handcrafted, premium feel.

Use on feature cards, service panels, pricing tiers, or any bordered container where you want to emphasize selection with a refined motion cue.

---

## Interaction

User hovers over a `.border-draw-card`. An SVG `<rect>` or `<path>` surrounds the element with a transparent stroke. GSAP animates `stroke-dashoffset` from the total dash length down to 0, making the border appear to draw clockwise. On `mouseleave`, the animation reverses, undrawing the border. Multiple border colors work well for branding.

---

## Psychology

- **Handcrafted Implication:** Drawing animations subconsciously signal craftsmanship and attention to detail.
- **Completion Reward:** Watching the border complete its circuit provides micro-satisfaction.
- **Spatial Confirmation:** The animated border reinforces the element's boundaries, improving visual hierarchy.

---

## Implementation

```html
<div class="border-draw-card" style="position: relative; padding: 2rem; border-radius: 16px; cursor: pointer; background: #1a1a2e; display: inline-block;">
  <svg class="border-draw-svg" style="position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none;" viewBox="0 0 100 100" preserveAspectRatio="none">
    <rect class="border-draw-rect" x="2" y="2" width="96" height="96" rx="14" ry="14"
      fill="none" stroke="#a29bfe" stroke-width="2"
      stroke-dasharray="280" stroke-dashoffset="280"
      vector-effect="non-scaling-stroke" />
  </svg>
  <div style="color: white; font-family: system-ui; position: relative; z-index: 1;">
    <h3 style="margin: 0 0 0.5rem;">Premium Feature</h3>
    <p style="margin: 0; opacity: 0.7;">Hover to see the border draw.</p>
  </div>
</div>
```

```javascript
document.querySelectorAll('.border-draw-card').forEach(card => {
  const rect = card.querySelector('.border-draw-rect');

  card.addEventListener('mouseenter', () => {
    gsap.to(rect, {
      strokeDashoffset: 0,
      duration: 0.8,
      ease: 'power2.inOut'
    });
  });

  card.addEventListener('mouseleave', () => {
    gsap.to(rect, {
      strokeDashoffset: 280,
      duration: 0.6,
      ease: 'power2.inOut'
    });
  });
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| SaaS | ★★★★★ | Pricing tier cards, feature highlights |
| Luxury | ★★★★☆ | Premium service panels |
| Creative Agency | ★★★★☆ | Portfolio items, service listing |
| Finance | ★★★☆☆ | Professional accent for selection |
| Real Estate | ★★★☆☆ | Property highlight cards |

---

## Accessibility Notes

- SVG borders are purely decorative — no semantic impact
- Reduced motion: show static border (stroke-dashoffset 0) without animation
- Ensure sufficient contrast between stroke color and card background
- Animation duration should not exceed 1s to avoid perceived delay

---

## Performance Notes

- SVG stroke animation uses GPU-composited rendering
- No DOM layout changes — only SVG attribute animation
- For large grids, use CSS `will-change: stroke-dashoffset` on the rect

---

## Variants

### Variant A: Gradient Border Draw
Use an SVG `<linearGradient>` as the stroke color for a multicolor draw effect.

### Variant B: Corner Draw Only
Only corners draw in (small L-shaped paths at each corner) — minimal and elegant.

### Variant C: Double Border
Two concentric rects with staggered draw timing for a layered effect.

---

## Anti-Patterns

- Using on elements that change size dynamically (SVG viewBox mismatch)
- Stroke dasharray value too small — rect draws too quickly with no visible animation
- No `preserveAspectRatio="none"` on fluid-width containers — causes SVG distortion
- Applying to every card in a grid simultaneously — too busy

---

## Checklist

- [ ] `stroke-dasharray` equals total path length (use `getTotalLength()` if uncertain)
- [ ] `preserveAspectRatio="none"` for fluid containers
- [ ] `vector-effect="non-scaling-stroke"` to keep stroke-width consistent
- [ ] Reduced motion: show filled border
- [ ] `pointer-events: none` on SVG
