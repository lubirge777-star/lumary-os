# Experience 034: Wavy Text Animation

## Classification
Narrative

## Emotion
Playfulness → Energy

## Difficulty
★★☆☆☆

## Performance Impact
Low

## Libraries
GSAP

---

## Description

Text animates in a sine-wave pattern where each character's `y` position oscillates with a phase offset, creating an undulating wave effect. Characters appear to dance or flow like a ribbon in motion.

Use for entertainment sites, event pages, children's products, or any brand that wants to convey energy and playfulness through typography.

---

## Timeline

| Moment | Time | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0ms | Each character | Set initial y offset based on sine wave | 0ms | — |
| 2 | 0ms | All characters | Animate y offset continuously with phase shift | infinite | Linear |
| 3 | on-hover | Characters | Amplitude increases | 300ms | Power2.out |
| 4 | hover-end | Characters | Amplitude returns to base | 300ms | Power2.out |

---

## Psychology

- **Biophilic Connection:** Wave motion mimics natural phenomena (water, wind, sound waves), creating organic appeal.
- **Attention Capture:** Animated text stands out against static content — eyes are drawn to motion.
- **Energy Signal:** Wavy motion communicates liveliness, youthfulness, and creativity.

---

## Implementation

```html
<h2 class="wave-text" style="font-family: system-ui; font-size: 4rem; font-weight: 900; color: white; display: flex; flex-wrap: wrap;">
  <span class="wave-char" style="display: inline-block;">L</span>
  <span class="wave-char" style="display: inline-block;">u</span>
  <span class="wave-char" style="display: inline-block;">m</span>
  <span class="wave-char" style="display: inline-block;">a</span>
  <span class="wave-char" style="display: inline-block;">r</span>
  <span class="wave-char" style="display: inline-block;">y</span>
</h2>
```

```javascript
function initWave(selector, amplitude = 10, frequency = 2, speed = 0.8) {
  const container = document.querySelector(selector);
  if (!container || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const chars = container.querySelectorAll('.wave-char');
  const len = chars.length;
  let time = 0;

  function animateWave() {
    time += speed * 0.02;
    chars.forEach((char, i) => {
      const phase = (i / len) * Math.PI * frequency;
      const y = Math.sin(time + phase) * amplitude;
      char.style.transform = `translateY(${y}px)`;
    });
    requestAnimationFrame(animateWave);
  }

  animateWave();

  // Amplify on hover
  container.addEventListener('mouseenter', () => {
    amplitude = amplitude * 2;
  });

  container.addEventListener('mouseleave', () => {
    amplitude = amplitude / 2;
  });
}

initWave('.wave-text', 12, 2.5, 1);

// GSAP-powered variant for scroll-triggered entrance
gsap.registerPlugin(ScrollTrigger);

document.querySelectorAll('.wave-text').forEach(el => {
  const chars = el.querySelectorAll('.wave-char');
  gsap.set(chars, { y: (i) => Math.sin((i / chars.length) * Math.PI * 2) * 20 });

  ScrollTrigger.create({
    trigger: el,
    start: 'top 85%',
    onEnter: () => {
      gsap.to(chars, {
        y: 0,
        duration: 0.6,
        stagger: 0.03,
        ease: 'back.out(1.5)',
        onComplete: () => initWave('.wave-text', 10, 2, 0.8)
      });
    },
    once: true
  });
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Entertainment | ★★★★★ | Movie titles, show names |
| Children | ★★★★★ | Fun, energetic brands |
| Music | ★★★★★ | Band names, festival headers |
| Education | ★★★☆☆ | Creative learning platforms |
| Finance | ★☆☆☆☆ | Undermines serious tone |

---

## Accessibility Notes

- Wave animation is purely decorative — text must be readable without it
- `prefers-reduced-motion: reduce` — display text statically, no wave
- Continuous motion may cause discomfort — limit to short phrases only
- Ensure sufficient character spacing so overlapping doesn't occur at wave peaks

---

## Performance Notes

- `requestAnimationFrame` is efficient and syncs with refresh rate
- Only `transform: translateY()` — GPU accelerated
- For long text, wrap each word rather than each character (fewer DOM nodes)

---

## Variants

### Variant A: Color Wave
Characters also cycle through hue or opacity offset, creating a rainbow wave.

### Variant B: Scale Wave
Characters scale up/down in addition to y-offset for a 3D "bouncing" effect.

### Variant C: Scroll Depth Wave
Wave amplitude and speed increase as user scrolls down, peaking at mid-page.

---

## Anti-Patterns

- Waving entire paragraphs — overwhelming. Limit to 1-2 lines.
- Characters overlapping at peak amplitude — check spacing
- Running at 60fps on battery — not a concern for short text
- No reduced-motion fallback — violation if animation is continuous

---

## Checklist

- [ ] Amplitude ≤ 15px (subtle)
- [ ] Reduced motion: static text
- [ ] Characters don't overlap at peak
- [ ] Limited to headings (≤ 20 chars)
- [ ] Pauses or stops after 5 seconds (optional)
