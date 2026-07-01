# Experience 053: Shape Morphing Loader

## Classification
Narrative

## Emotion
Anticipation → Satisfaction

## Difficulty
★★★★☆

## Performance Impact
Medium

## Libraries
GSAP, MorphSVG (optional)

---

## Description

A loading animation where a shape morphs from one form to another — typically a circle transitions into a line, then into a checkmark. Each morph represents a loading stage or progress milestone. The smooth SVG path morphing creates a polished, branded loading experience.

Use for payment processing, form submission, file uploads, or any multi-step async process where the user should wait with visual reassurance.

---

## Timeline

| Moment | Time | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0ms | Circle | Scale in + draw | 500ms | Back.out(1.5) |
| 2 | 200-800ms | Circle → Line | Morph path | 600ms | Power3.inOut |
| 3 | 800-1400ms | Line → Checkmark | Morph path | 600ms | Power3.inOut |
| 4 | 1400-1600ms | Checkmark | Bounce scale | 200ms | Elastic.out(1, 0.3) |
| 5 | 1600ms | Content | Fade in | 400ms | Power2.out |

---

## Psychology

- **Progress Visualization:** Each morph communicates a distinct stage — the user can see the process advancing.
- **Satisfying Resolution:** The circle → line → checkmark sequence tells a micro-story with a clear happy ending.
- **Perceived Speed:** A well-designed morph animation feels faster than a spinning spinner, even if the actual time is the same.

---

## Implementation

```html
<div id="morph-loader" style="position: fixed; inset: 0; z-index: 9999; background: #0a0a1a; display: flex; align-items: center; justify-content: center; flex-direction: column;">
  <svg class="morph-svg" width="120" height="120" viewBox="0 0 120 120" style="overflow: visible;">
    <path class="morph-path" d="M60 10 C 80 10, 110 30, 110 60 C 110 90, 90 110, 60 110 C 30 110, 10 80, 10 60 C 10 30, 40 10, 60 10Z"
      fill="none" stroke="#6c5ce7" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"
      stroke-dasharray="380" stroke-dashoffset="380" />
  </svg>
  <p class="morph-status" style="color: #888; font-family: system-ui; margin-top: 1.5rem; font-size: 0.9rem; letter-spacing: 0.05em;">Processing...</p>
</div>

<div id="morph-content" style="display: none; height: 100vh; display: flex; align-items: center; justify-content: center; background: #0a0a1a;">
  <div style="text-align: center; color: white; font-family: system-ui;">
    <div style="font-size: 4rem; margin-bottom: 1rem;">✓</div>
    <h2 style="margin: 0;">Complete!</h2>
  </div>
</div>
```

```javascript
const morphPath = document.querySelector('.morph-path');
const status = document.querySelector('.morph-status');
const morphContent = document.getElementById('morph-content');

// Circle path
const circlePath = 'M60 10 C 80 10, 110 30, 110 60 C 110 90, 90 110, 60 110 C 30 110, 10 80, 10 60 C 10 30, 40 10, 60 10Z';
// Line path (left-to-right straight line)
const linePath = 'M20 60 L 100 60';
// Checkmark path
const checkPath = 'M35 60 L 50 75 L 85 40';

const tl = gsap.timeline({ defaults: { ease: 'power3.inOut' } });

morphContent.style.display = 'none';

tl.set(morphPath, { attr: { d: circlePath, strokeDashoffset: 380 } }, 0)
  .to(morphPath, { attr: { strokeDashoffset: 0 }, duration: 0.6, ease: 'power2.out' }, 0.2)

  // Morph to line
  .to(morphPath, {
    attr: { d: linePath },
    strokeDashoffset: 80,
    duration: 0.5
  }, 1.0)
  .to(morphPath, { attr: { strokeDashoffset: 0 }, duration: 0.3 }, 1.3)
  .to(status, { textContent: 'Almost there...', duration: 0.1 }, 1.3)

  // Morph to checkmark
  .to(morphPath, {
    attr: { d: checkPath },
    strokeDashoffset: 70,
    duration: 0.5
  }, 1.8)
  .to(morphPath, { attr: { strokeDashoffset: 0 }, duration: 0.4, ease: 'back.out(2)' }, 2.1)
  .to(status, { textContent: 'Complete!', color: '#2ed573', duration: 0.2 }, 2.3)

  // Bounce check
  .to(morphPath, { scale: 1.15, duration: 0.15, ease: 'power2.out' }, 2.4)
  .to(morphPath, { scale: 1, duration: 0.3, ease: 'elastic.out(1, 0.3)' }, 2.55)

  // Transition out
  .to('#morph-loader', { opacity: 0, duration: 0.4, ease: 'power2.out', onComplete: () => {
    document.getElementById('morph-loader').style.display = 'none';
    morphContent.style.display = 'flex';
    gsap.fromTo(morphContent, { opacity: 0 }, { opacity: 1, duration: 0.5 });
  }}, 2.8);

// Reduced motion
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  tl.clear();
  document.getElementById('morph-loader').style.display = 'none';
  morphContent.style.display = 'flex';
  gsap.set(morphContent, { opacity: 1 });
}
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| SaaS | ★★★★★ | Payment processing |
| E-commerce | ★★★★★ | Checkout loading |
| Technology | ★★★★☆ | App installation |
| Finance | ★★★★☆ | Transaction loading |
| Enterprise | ★★★☆☆ | Form submission |

---

## Accessibility Notes

- Status text must update alongside morph stages for screen reader users
- `prefers-reduced-motion: reduce` — show final checkmark immediately, skip animation
- Total animation must not exceed 4 seconds — user may think process is stuck
- Use `aria-live="polite"` on status text for screen reader announcements

---

## Performance Notes

- SVG path morphing is GPU accelerated
- `stroke-dashoffset` animation is composited
- For complex morphs, use MorphSVGPlugin (GSAP bonus plugin) for smoother interpolation
- Fallback: if MorphSVG is not available, use a crossfade between separate SVG elements

---

## Variants

### Variant A: Logo Morph
Brand logo morphs into the checkmark — reinforces brand identity during loading.

### Variant B: Loading → Success → Error
Three-state morph: circle (loading) → checkmark (success) or X (error) based on outcome.

### Variant C: Multi-Shape Sequence
Circle → Triangle → Square → Checkmark — four stages for complex multi-step processes.

---

## Anti-Patterns

- Morphing between very different shapes without intermediate steps — jarring
- No text status update — user doesn't know what stage the process is in
- Relying on MorphSVG without fallback — basic GSAP may not interpolate cleanly
- Animation continuing after process completes — mismatch between visual and actual state

---

## Checklist

- [ ] Status text updates per stage
- [ ] Total timeline ≤ 4 seconds
- [ ] Reduced motion: skip to checkmark
- [ ] Process state matches animation stage
- [ ] `aria-live="polite"` on status
- [ ] SVG viewBox correctly sized for all morph states
