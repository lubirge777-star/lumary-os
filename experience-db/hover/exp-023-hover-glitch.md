# Experience 023: Glitch Distortion on Hover

## Classification
Feedback

## Emotion
Surprise → Engagement

## Difficulty
★★★★☆

## Performance Impact
Medium

## Libraries
GSAP

---

## Description

A glitch distortion effect triggered on hover that displaces text or image layers with offset, color channel separation, and intermittent clipping. Use for gaming, tech, cyberpunk, or edgy brand identities where a raw digital aesthetic is desired.

The effect simulates screen corruption by rapidly shifting layers with slight timing offsets between red, green, and blue channels, combined with random clip displacements.

---

## Interaction

User hovers over a `.glitch-target` element. GSAP immediately kicks off a timeline that alternates between corrupted and clean states at random intervals. On `mouseleave`, the animation resolves back to the original state with a brief settling transition.

---

## Psychology

- **Startle Pattern:** Sudden visual distortion captures attention by breaking expected visual continuity.
- **Digital Aesthetic Association:** Glitch artifacts subconsciously communicate "tech," "future," or "underground" depending on context.
- **Cognitive Closure:** The brain works to resolve the fragmented image, increasing engagement time.

---

## Implementation

```html
<div class="glitch-target" style="position: relative; display: inline-block; cursor: pointer; font-family: monospace;">
  <h2 class="glitch-text" style="font-size: 4rem; font-weight: 900; color: #fff; letter-spacing: -2px; text-transform: uppercase;">LUMARY</h2>
  <div class="glitch-layer glitch-layer-r" aria-hidden="true" style="position: absolute; top: 0; left: 0; font-size: 4rem; font-weight: 900; color: #ff0040; letter-spacing: -2px; text-transform: uppercase; clip-path: inset(0); pointer-events: none;">LUMARY</div>
  <div class="glitch-layer glitch-layer-b" aria-hidden="true" style="position: absolute; top: 0; left: 0; font-size: 4rem; font-weight: 900; color: #00d4ff; letter-spacing: -2px; text-transform: uppercase; clip-path: inset(0); pointer-events: none;">LUMARY</div>
</div>
```

```javascript
const glitchTarget = document.querySelector('.glitch-target');
const redLayer = glitchTarget.querySelector('.glitch-layer-r');
const blueLayer = glitchTarget.querySelector('.glitch-layer-b');
const mainText = glitchTarget.querySelector('.glitch-text');
let glitchTimeline;

function runGlitch() {
  glitchTimeline = gsap.timeline({ paused: true });

  for (let i = 0; i < 6; i++) {
    const xOffset = gsap.utils.random(-8, 8);
    const yClipTop = gsap.utils.random(0, 60);
    const yClipBottom = gsap.utils.random(40, 100);

    glitchTimeline
      .to([redLayer, blueLayer], {
        x: () => gsap.utils.random(-4, 4),
        clipPath: () => `inset(${gsap.utils.random(0, 30)}% 0 ${gsap.utils.random(30, 70)}% 0)`,
        opacity: 1,
        duration: 0.05
      }, i * 0.08)
      .to(mainText, {
        x: () => gsap.utils.random(-2, 2),
        skewX: () => gsap.utils.random(-2, 2),
        duration: 0.05
      }, i * 0.08)
      .to([redLayer, blueLayer, mainText], {
        x: 0,
        clipPath: 'inset(0% 0 0% 0)',
        skewX: 0,
        opacity: 0,
        duration: 0.05
      }, i * 0.08 + 0.05);
  }
}

runGlitch();

glitchTarget.addEventListener('mouseenter', () => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  glitchTimeline.restart();
});

glitchTarget.addEventListener('mouseleave', () => {
  glitchTimeline.progress(1);
  gsap.set([redLayer, blueLayer, mainText], { x: 0, clipPath: 'inset(0% 0 0% 0)', skewX: 0, opacity: 0 });
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Gaming | ★★★★★ | Perfect for game titles and hero sections |
| Tech / Crypto | ★★★★★ | Blockchain, AI, web3 brands |
| Creative Agency | ★★★★☆ | Portfolio hero impact |
| Fashion | ★★★☆☆ | Avant-garde / streetwear brands |
| Finance | ★☆☆☆☆ | Undermines trust and stability |

---

## Accessibility Notes

- Glitch layers must use `aria-hidden="true"` — they are decorative only
- The primary text remains unshifted in HTML; glitch is purely visual
- Disable entirely under `prefers-reduced-motion: reduce`
- No flashing sequences longer than 3 consecutive frames (avoid seizure risk)

---

## Performance Notes

- GSAP `.to()` calls on text are cheap (compositor only when using transforms)
- `clip-path` repaints — keep active duration short
- Pre-glitch: run `runGlitch()` once on idle to build timeline

---

## Variants

### Variant A: Image Glitch
Apply to images using three overlapping `<img>` or `<canvas>` layers with CSS `mix-blend-mode`.

### Variant B: Scanline Glitch
Add a repeating CSS gradient overlay that shifts vertically on glitch frames for a CRT monitor effect.

### Variant C: Glitch Reveal
Text starts entirely glitched and resolves to clean state on hover (inverse of the standard effect).

---

## Anti-Patterns

- Continuous glitch without trigger — nausea risk, accessibility violation
- Applying to body text — only use on headings and hero titles
- Relying on `mix-blend-mode` without fallback — not supported in all browsers
- Excessive runtime — keep glitch sequences under 1 second total

---

## Checklist

- [ ] Reduced motion respected
- [ ] `aria-hidden="true"` on decorative glitch layers
- [ ] Glitch duration ≤ 800ms on hover
- [ ] Primary content readable without effect
- [ ] Tested on Firefox (clip-path support)
