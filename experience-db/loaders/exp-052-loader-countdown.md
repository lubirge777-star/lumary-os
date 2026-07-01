# Experience 052: Numeric Countdown Loader

## Classification
Narrative

## Emotion
Anticipation → Energy

## Difficulty
★★☆☆☆

## Performance Impact
Low

## Libraries
GSAP

---

## Description

A numeric countdown loader that cycles through numbers (e.g., 3, 2, 1) before transitioning into the page content. Each number animates with scale and opacity changes, building anticipation. The final number may "shatter" or morph into the hero content.

Use for gaming interfaces, event pages, product launches, or any experience where a dramatic countdown fits the brand energy.

---

## Timeline

| Moment | Time | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0ms | Number 3 | Scale in + fade | 400ms | Back.out(1.5) |
| 2 | 600ms | Number 3 | Scale out + fade | 300ms | Power2.in |
| 3 | 700ms | Number 2 | Scale in + fade | 400ms | Back.out(1.5) |
| 4 | 1300ms | Number 2 | Scale out + fade | 300ms | Power2.in |
| 5 | 1400ms | Number 1 | Scale in + fade | 400ms | Back.out(1.5) |
| 6 | 2000ms | Number 1 | Scale up + fade out (explode) | 400ms | Power4.out |
| 7 | 2400ms | Content | Fade in hero | 600ms | Power3.out |

---

## Psychology

- **Urgency Creation:** Countdowns create time pressure and heighten anticipation for what comes next.
- **Priming:** A 3-2-1 countdown primes the brain for a "launch" moment — the content feels more significant.
- **Pattern Completion:** The brain expects something to happen after 1 — the content reveal satisfies that expectation.

---

## Implementation

```html
<div id="countdown-loader" style="position: fixed; inset: 0; z-index: 9999; background: #0a0a1a; display: flex; align-items: center; justify-content: center; flex-direction: column;">
  <div class="countdown-numbers" style="position: relative; width: 200px; height: 200px; display: flex; align-items: center; justify-content: center;">
    <div class="countdown-num" data-num="3" style="position: absolute; font-family: system-ui; font-size: 8rem; font-weight: 900; color: white; opacity: 0; transform: scale(0);">3</div>
    <div class="countdown-num" data-num="2" style="position: absolute; font-family: system-ui; font-size: 8rem; font-weight: 900; color: white; opacity: 0; transform: scale(0);">2</div>
    <div class="countdown-num" data-num="1" style="position: absolute; font-family: system-ui; font-size: 8rem; font-weight: 900; color: white; opacity: 0; transform: scale(0);">1</div>
  </div>
  <p class="countdown-label" style="color: #888; font-family: system-ui; margin-top: 1rem; letter-spacing: 0.2em; text-transform: uppercase; font-size: 0.85rem;">Get Ready</p>
</div>

<div id="main-content" style="display: none; height: 100vh; display: flex; align-items: center; justify-content: center;">
  <h1 style="color: white; font-family: system-ui; font-size: 4rem;">Welcome</h1>
</div>
```

```javascript
const tl = gsap.timeline({
  defaults: { ease: 'power3.out' },
  onComplete: () => {
    document.getElementById('countdown-loader').style.display = 'none';
  }
});

const nums = document.querySelectorAll('.countdown-num');
const label = document.querySelector('.countdown-label');
const mainContent = document.getElementById('main-content');

// Hide main content initially
mainContent.style.display = 'none';

nums.forEach((num, i) => {
  const timing = i * 0.8;

  // Enter
  tl.fromTo(num, 
    { scale: 0, opacity: 0, rotation: -20 + i * 10 },
    { scale: 1, opacity: 1, rotation: 0, duration: 0.5, ease: 'back.out(1.7)' },
    timing
  );

  // Exit (leave previous visible briefly for overlap)
  if (i > 0) {
    tl.to(nums[i - 1], { scale: 0.5, opacity: 0, duration: 0.3, ease: 'power2.in' }, timing - 0.1);
  }
});

// Last number exit — big scale up
tl.to(nums[2], { scale: 3, opacity: 0, duration: 0.5, ease: 'power4.out' }, '+=0.2');
tl.to(label, { opacity: 0, y: -20, duration: 0.3 }, '-=0.3');

// Show main content
tl.call(() => {
  mainContent.style.display = 'flex';
  gsap.fromTo(mainContent,
    { opacity: 0, y: 30 },
    { opacity: 1, y: 0, duration: 0.6, ease: 'power3.out' }
  );
});

// Reduced motion
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  tl.clear();
  document.getElementById('countdown-loader').style.display = 'none';
  mainContent.style.display = 'flex';
  gsap.set(mainContent, { opacity: 1, y: 0 });
}
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Gaming | ★★★★★ | Game loading screens |
| Events | ★★★★★ | Live stream countdowns |
| Technology | ★★★★☆ | Product launches |
| Entertainment | ★★★★☆ | App opening sequences |
| E-commerce | ★★☆☆☆ | Too slow for shopping |

---

## Accessibility Notes

- Total countdown must be skippable (user can bypass)
- `prefers-reduced-motion: reduce` — skip loader entirely, show content directly
- No flashing or stroboscopic effects between number transitions
- Screen readers: use `aria-live="polite"` if announcing countdown, or skip with `aria-hidden`

---

## Performance Notes

- Only `scale`, `opacity`, `rotation` — all GPU composited
- Total animation time: ~2.5s — short enough to not frustrate
- Use `display: none` after completion to remove from DOM tree
- Preload hero content behind the loader for seamless transition

---

## Variants

### Variant A: Shatter Countdown
Numbers "break apart" using clip-path polygons at the end of each count.

### Variant B: Progress Ring Countdown
Numbers appear in the center of a circular progress ring that fills as time progresses.

### Variant C: Animated Background Countdown
The background color or pattern shifts between each number (e.g., red → yellow → green).

---

## Anti-Patterns

- Countdown longer than 4 seconds — user impatience
- No skip mechanism — users who have seen it before should bypass
- Numbers in wrong order (1, 2, 3) — defeats the purpose
- Large file size for such a simple animation — keep it lightweight

---

## Checklist

- [ ] Total duration ≤ 3 seconds
- [ ] Skip mechanism available (click to skip)
- [ ] Reduced motion: skip loader
- [ ] Hero content preloaded behind loader
- [ ] Number sequence correct (3-2-1)
- [ ] Loader removed from DOM after completion
