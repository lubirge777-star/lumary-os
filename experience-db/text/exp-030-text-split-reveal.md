# Experience 030: Split Text Character/Word Reveal

## Classification
Narrative

## Emotion
Anticipation → Satisfaction

## Difficulty
★★★☆☆

## Performance Impact
Medium

## Libraries
GSAP, ScrollTrigger

---

## Description

Text animates in by splitting into individual characters, words, or lines, then staggering their entrance with a smooth motion. This creates a sophisticated typographic reveal without relying on SplitType library — all splitting is done via vanilla JavaScript.

Use for headings, hero text, or any typography that needs to feel deliberate and crafted.

---

## Timeline

| Moment | Time | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0ms | Container | Clip text to hidden overflow | 0ms | — |
| 2 | 0ms | Split elements | y: 100%, opacity: 0 (initial) | 0ms | — |
| 3 | 0ms | Split elements | Stagger in y: 100% → 0%, opacity: 0 → 1 | 1200ms total | Power3.out |
| 4 | stagger-end | Container | Overflow visible restored | 0ms | — |

---

## Psychology

- **Serial Processing:** The brain reads words one at a time; staggering their entrance aligns with natural reading rhythm.
- **Anchoring:** Each word appearing sequentially anchors attention, preventing skimming.
- **Pacing Control:** The designer controls the speed of consumption, emphasizing deliberate reading.

---

## Implementation

```html
<h2 class="split-reveal" style="font-family: system-ui; font-size: 3.5rem; line-height: 1.2; overflow: hidden; color: white; max-width: 800px;">
  <span class="split-line">
    <span class="split-word">Design</span>
    <span class="split-word">Without</span>
    <span class="split-word">Boundaries</span>
  </span>
  <span class="split-line">
    <span class="split-word">Built</span>
    <span class="split-word">For</span>
    <span class="split-word">Motion</span>
  </span>
</h2>
```

```javascript
function splitText(selector) {
  const el = document.querySelector(selector);
  if (!el) return;

  const words = el.textContent.trim().split(/\s+/);
  const chars = words.map(w => [...w]);
  el.innerHTML = '';

  words.forEach((word, wi) => {
    const wordSpan = document.createElement('span');
    wordSpan.className = 'split-word';
    wordSpan.style.display = 'inline-block';
    wordSpan.style.overflow = 'hidden';
    wordSpan.style.verticalAlign = 'top';

    [...word].forEach((char, ci) => {
      const charSpan = document.createElement('span');
      charSpan.className = 'split-char';
      charSpan.textContent = char;
      charSpan.style.display = 'inline-block';
      charSpan.style.transform = 'translateY(100%)';
      charSpan.style.opacity = '0';
      wordSpan.appendChild(charSpan);
    });

    if (wi < words.length - 1) {
      const space = document.createTextNode('\u00A0');
      el.appendChild(wordSpan);
      el.appendChild(space);
    } else {
      el.appendChild(wordSpan);
    }
  });
}

splitText('.split-reveal');

gsap.registerPlugin(ScrollTrigger);

const chars = document.querySelectorAll('.split-reveal .split-char');

gsap.to(chars, {
  y: 0,
  opacity: 1,
  duration: 0.6,
  stagger: 0.03,
  ease: 'power3.out',
  scrollTrigger: {
    trigger: '.split-reveal',
    start: 'top 85%',
    toggleActions: 'play none none reverse'
  }
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Creative Agency | ★★★★★ | Hero headlines |
| Technology | ★★★★☆ | Product taglines |
| Luxury | ★★★★★ | Brand messaging |
| Education | ★★★☆☆ | Course titles |
| E-commerce | ★★★☆☆ | Campaign headers |

---

## Accessibility Notes

- Content must be fully visible without JavaScript — use SSR with visible text
- Split characters must retain correct reading order for screen readers
- `prefers-reduced-motion: reduce` — reveal text immediately with no animation
- Avoid splitting individual characters for large bodies of text (use word-split only)

---

## Performance Notes

- DOM splitting creates many elements — limit to headings only (not paragraphs)
- Use `will-change: transform` on `.split-char` elements
- For long text, prefer word-split over character-split (fewer DOM nodes)
- Stagger interval 0.02-0.05s is optimal for readability

---

## Variants

### Variant A: Word-Reveal Only
Split by word (no character splitting). Faster performance, cleaner look.

### Variant B: Line-Reveal (Sliding Mask)
Each line slides up with a CSS `clip-path` mask for a cleaner reveal without individual spans.

### Variant C: Scramble-Reveal
Characters start as random letters and unscramble into the correct text — puzzle-like reveal.

---

## Anti-Patterns

- Splitting entire paragraphs into characters (thousands of DOM nodes — performance disaster)
- Forgetting `overflow: hidden` on word containers — reveals look broken
- Stagger too fast (< 0.02s) — no visible sequence
- Stagger too slow (> 0.1s) — feels labored
- No SSR fallback — blank text if JS fails

---

## Checklist

- [ ] Character split only on headings (≤ 30 chars)
- [ ] Word-wrap handling for responsive text
- [ ] Reduced motion: reveal immediately
- [ ] SSR fallback with visible text
- [ ] `overflow: hidden` on each word wrapper
