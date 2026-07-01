# Experience 025: Magnetic Button / Link

## Classification
Feedback

## Emotion
Surprise → Delight

## Difficulty
★★★☆☆

## Performance Impact
Low

## Libraries
GSAP

---

## Description

A magnetic effect where buttons or links subtly track the cursor within their bounds, creating an attractive "pull" sensation. As the cursor approaches, the element shifts toward it, and on click it snaps back. This adds a tactile, playful quality to CTAs and interactive elements.

Use on primary action buttons, download links, or any element where you want to increase click intention.

---

## Interaction

User moves cursor near a `.magnetic-btn` container. JavaScript computes the cursor offset from center, and GSAP smoothly translates the inner element toward the cursor within a limited radius. On `mouseleave`, the element springs back to its original position with an overshoot ease for a playful bounce.

---

## Psychology

- **Controlled Surprise:** Elements reacting to proximity violates flat UI expectations in a delightful way.
- **Increased Click Intention:** The magnetic pull creates a subconscious "grab" impulse — users are more likely to click.
- **Anthropomorphism:** Giving buttons "behavior" makes the interface feel alive and responsive.

---

## Implementation

```html
<div class="magnetic-btn" style="display: inline-block; padding: 14px 36px; border-radius: 50px; cursor: pointer; position: relative;">
  <span class="magnetic-inner" style="display: inline-block; padding: 14px 36px; border-radius: 50px; background: linear-gradient(135deg, #6c5ce7, #a29bfe); color: white; font-family: system-ui; font-weight: 600; font-size: 1rem; border: none; pointer-events: none; white-space: nowrap;">
    Get Started
  </span>
</div>
```

```javascript
document.querySelectorAll('.magnetic-btn').forEach(btn => {
  const inner = btn.querySelector('.magnetic-inner');
  const strength = 0.3;

  btn.addEventListener('mousemove', (e) => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const rect = btn.getBoundingClientRect();
    const x = (e.clientX - rect.left - rect.width / 2) * strength;
    const y = (e.clientY - rect.top - rect.height / 2) * strength;

    gsap.to(inner, {
      x: x,
      y: y,
      duration: 0.6,
      ease: 'power2.out'
    });
  });

  btn.addEventListener('mouseleave', () => {
    gsap.to(inner, {
      x: 0,
      y: 0,
      duration: 0.8,
      ease: 'elastic.out(1, 0.4)'
    });
  });
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| SaaS | ★★★★★ | CTA buttons, signup links |
| Creative Agency | ★★★★★ | Portfolio CTAs |
| E-commerce | ★★★★☆ | Add to cart buttons |
| Education | ★★★☆☆ | Enrollment CTAs |
| Healthcare | ★★☆☆☆ | Too playful for serious contexts |

---

## Accessibility Notes

- The magnetic movement is decorative — buttons must work with keyboard navigation
- Disable under `prefers-reduced-motion: reduce`
- Ensure the interactive area (outer wrapper) is large enough for easy clicking
- Do not move the button so far that the user misses the click target

---

## Performance Notes

- Only `x`/`y` transforms — zero layout cost
- `elastic.out` ease causes no reflow
- Use `pointer-events: none` on inner element to avoid interference

---

## Variants

### Variant A: Repel (Negative Magnetic)
Element pushes away from the cursor — good for "cancel" or "delete" actions.

### Variant B: Scale Attract
Button scales up slightly (1.05x) while moving toward cursor, combining magnetic with hover scale.

### Variant C: Multi-Element Magnetic
A group of elements (e.g., nav links) that each react when cursor enters their container.

---

## Anti-Patterns

- Moving the button outside its parent bounds (causes layout or overflow hidden clipping)
- Too much strength (> 0.5) — button moves too far from origin
- Applying to small elements (< 40px) — precision issues
- Magnetic effect on touch devices — no cursor position available

---

## Checklist

- [ ] Strength factor ≤ 0.3 for subtle effect
- [ ] `pointer-events: none` on inner element
- [ ] Reduced motion respected
- [ ] Button works with keyboard + enter
- [ ] Overflow hidden on parent if needed
