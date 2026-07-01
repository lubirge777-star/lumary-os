# Experience 048: Enhanced 3D Tilt with Glow Follow

## Classification
Feedback

## Emotion
Delight → Premium

## Difficulty
★★★★☆

## Performance Impact
Medium

## Libraries
GSAP

---

## Description

An enhanced 3D tilt card where not only the card rotates following the cursor, but a dynamic glow/lighting effect follows as well. The combination of tilt and positional lighting creates a hyper-realistic material feel — as if the card is made of glass, metal, or pearlescent material.

Use for premium product cards, pricing tiers, membership cards, or any UI element where perceived material quality should be maximal.

---

## Interaction

User hovers over a 3D card. The card rotates in 3D space with `perspective` while a radial gradient overlay tracks the cursor position, simulating a light source. The glare shifts as the card tilts. A subtle `translateZ` on child elements creates internal depth layers. On `mouseleave`, everything resets with an elastic bounce.

---

## Psychology

- **Material Realism:** Combined tilt + lighting mimics real-world material behavior (light hitting a curved surface).
- **Perceived Value:** High-fidelity material rendering subconsciously signals premium quality and craftsmanship.
- **Tactile Affordance:** The realistic interaction invites touch/click, increasing conversion on CTAs.

---

## Implementation

```html
<div class="card-3d-enhanced" style="perspective: 1200px; width: 320px; height: 420px; cursor: pointer;">
  <div class="card-3d-inner" style="width: 100%; height: 100%; border-radius: 20px; background: linear-gradient(145deg, #1a1a2e, #16213e); position: relative; overflow: hidden; transform-style: preserve-3d; box-shadow: 0 20px 60px rgba(0,0,0,0.4);">
    <!-- Glare overlay -->
    <div class="card-glare" style="position: absolute; inset: 0; border-radius: 20px; background: radial-gradient(circle at 50% 50%, rgba(255,255,255,0.15) 0%, transparent 60%); pointer-events: none; z-index: 3;"></div>
    <!-- Border shine -->
    <div class="card-border" style="position: absolute; inset: -1px; border-radius: 21px; background: linear-gradient(135deg, #6c5ce7, #a29bfe, #6c5ce7); opacity: 0; z-index: 2; mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0); mask-composite: exclude; padding: 2px;"></div>
    <!-- Content -->
    <div class="card-content" style="position: relative; z-index: 2; padding: 2rem; color: white; font-family: system-ui; height: 100%; display: flex; flex-direction: column; justify-content: flex-end; transform: translateZ(30px);">
      <h3 style="margin: 0 0 0.5rem; font-size: 1.5rem;">Premium Plan</h3>
      <p style="margin: 0; opacity: 0.7; font-size: 0.9rem;">Everything you need, plus priority support.</p>
    </div>
  </div>
</div>
```

```javascript
document.querySelectorAll('.card-3d-enhanced').forEach(card => {
  const inner = card.querySelector('.card-3d-inner');
  const glare = card.querySelector('.card-glare');
  const border = card.querySelector('.card-border');

  card.addEventListener('mousemove', (e) => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const rect = card.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width;
    const y = (e.clientY - rect.top) / rect.height;

    const rotX = (y - 0.5) * -16;
    const rotY = (x - 0.5) * 16;

    gsap.to(inner, {
      rotateX: rotX,
      rotateY: rotY,
      duration: 0.5,
      ease: 'power2.out'
    });

    gsap.to(glare, {
      background: `radial-gradient(circle at ${x * 100}% ${y * 100}%, rgba(255,255,255,0.2) 0%, transparent 60%)`,
      duration: 0.3,
      ease: 'power1.out'
    });

    gsap.to(border, {
      opacity: Math.min(1, (Math.abs(x - 0.5) + Math.abs(y - 0.5)) * 2),
      duration: 0.3
    });
  });

  card.addEventListener('mouseleave', () => {
    gsap.to(inner, {
      rotateX: 0,
      rotateY: 0,
      duration: 0.8,
      ease: 'elastic.out(1, 0.4)'
    });
    gsap.to(glare, {
      background: 'radial-gradient(circle at 50% 50%, rgba(255,255,255,0.15) 0%, transparent 60%)',
      duration: 0.5
    });
    gsap.to(border, {
      opacity: 0,
      duration: 0.4
    });
  });
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| SaaS | ★★★★★ | Pricing cards |
| E-commerce | ★★★★★ | Premium product cards |
| Finance | ★★★★☆ | Premium account tiers |
| Luxury | ★★★★★ | Membership / loyalty cards |
| Technology | ★★★★☆ | Feature cards |

---

## Accessibility Notes

- All content must be readable without hover or tilt
- `prefers-reduced-motion: reduce` — static card, no tilt or glare movement
- Touch devices: no tilt; ensure CTAs work on tap
- Glare must not reduce text contrast — test at all cursor positions

---

## Performance Notes

- 3D transforms are GPU accelerated — `perspective`, `rotateX`, `rotateY`
- Glare uses `background` which is a paint property — keep updates throttled
- Glow border opacity change is cheap (compositor)
- For performance, cap at 6 enhanced cards per page

---

## Variants

### Variant A: Glass Morphism Tilt
Card uses `backdrop-filter: blur()` with reduced opacity for a glass material feel.

### Variant B: Gradient Shift Tilt
The card's background gradient angle shifts as the card tilts — no glare overlay needed.

### Variant C: Reflection Tilt
A pseudo-element with a linear gradient reflects below the card, simulating a shiny surface reflection.

---

## Anti-Patterns

- Overlapping cards — tilt on one affects cards behind it via z-index
- Missing `transform-style: preserve-3d` — child elements not in 3D space
- Glare opacity too high (> 0.3) — obscures content
- Applying to text-only cards (no visual benefit for tilt)

---

## Checklist

- [ ] `perspective` set on card wrapper
- [ ] `transform-style: preserve-3d` on inner element
- [ ] `translateZ` on content for 3D depth
- [ ] Glare opacity ≤ 0.2
- [ ] Reduced motion: static display
- [ ] Touch fallback (tap to highlight)
