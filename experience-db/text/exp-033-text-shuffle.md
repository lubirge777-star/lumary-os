# Experience 033: Text Shuffle / Replace

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

Text shuffles through random characters before resolving into the final word or phrase on hover or scroll trigger. The animation creates a "decryption" effect where gibberish resolves into meaningful text — like a digital lock being decoded.

Use for interactive headlines, "loading complete" transitions, button text swaps, or any element where transformation adds theatrical flair.

---

## Interaction

User hovers over (or scrolls to) a `.shuffle-text` element. JavaScript rapidly cycles through random characters at each position over a series of iterations, gradually decelerating until the final text is revealed. GSAP can coordinate the timing and provide a completion callback.

---

## Psychology

- **Pattern Recognition Urge:** The brain instinctively tries to decode the random characters, keeping attention locked.
- **Reward on Resolution:** The moment gibberish becomes readable triggers a dopamine micro-hit of comprehension.
- **Transformation Narrative:** Watching something change from chaotic to ordered implies effort and craft.

---

## Implementation

```html
<h2 class="shuffle-text" data-text="Lumary OS" style="font-family: monospace; font-size: 4rem; font-weight: 900; color: white; cursor: pointer;">
  Lumary OS
</h2>
```

```javascript
const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()';

function shuffleText(element, target, duration = 1200) {
  const el = typeof element === 'string' ? document.querySelector(element) : element;
  if (!el) return;

  const original = el.textContent;
  const targetText = target || el.dataset.text || original;
  const len = targetText.length;
  const frameRate = 50;
  const totalFrames = duration / frameRate;
  let frame = 0;

  const interval = setInterval(() => {
    const progress = frame / totalFrames;
    let result = '';

    for (let i = 0; i < len; i++) {
      if (progress >= (i + 1) / len) {
        result += targetText[i];
      } else {
        result += chars[Math.floor(Math.random() * chars.length)];
      }
    }

    el.textContent = result;
    frame++;

    if (frame > totalFrames) {
      clearInterval(interval);
      el.textContent = targetText;
    }
  }, frameRate);
}

// Hover trigger
document.querySelectorAll('.shuffle-text').forEach(el => {
  el.addEventListener('mouseenter', () => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    shuffleText(el, el.dataset.text, 800);
  });
});

// Scroll trigger variant
gsap.registerPlugin(ScrollTrigger);

ScrollTrigger.create({
  trigger: '.shuffle-text',
  start: 'top 85%',
  onEnter: () => shuffleText('.shuffle-text', null, 1000),
  once: true
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Technology | ★★★★★ | Product names, feature highlights |
| Gaming | ★★★★★ | Level names, achievements |
| Creative | ★★★★☆ | Portfolio titles |
| Crypto / Web3 | ★★★★☆ | Tech-forward brands |
| Finance | ★★☆☆☆ | Too gimmicky |

---

## Accessibility Notes

- Final text must be available as `aria-label` on the element
- Rapid character changes can be disorienting — keep shuffle under 1.5s
- `prefers-reduced-motion: reduce` — display final text immediately
- Do not shuffle critical information the user needs instantly

---

## Performance Notes

- Only textContent updates — no layout or paint changes
- Interval-based (setInterval at 50ms) is lightweight
- For large blocks of text, limit shuffle to first 5-10 characters

---

## Variants

### Variant A: Number Shuffle (Slot Machine)
Numbers roll up/down like a slot machine before landing on the final value. Great for stats and counters.

### Variant B: Scramble Hover
Text scrambles on hover and resolves when user stops moving — playfully resists being read.

### Variant C: Multi-Word Stagger
Multiple words shuffle and resolve with staggered timing for a wave-like reveal effect.

---

## Anti-Patterns

- Shuffle duration too long (> 2s) — user reads gibberish and moves on
- Shuffling every time user hovers — feels chaotic. Use once per session
- No target text specified — shuffles to empty or undefined
- Shuffling long sentences (> 50 chars) — overwhelm

---

## Checklist

- [ ] Duration ≤ 1200ms
- [ ] `data-text` attribute or target parameter provided
- [ ] Reduced motion: show final immediately
- [ ] `aria-label` with final text
- [ ] Shuffle only on first interaction per session
