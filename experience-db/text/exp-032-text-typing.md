# Experience 032: Typewriter Effect

## Classification
Narrative

## Emotion
Anticipation → Engagement

## Difficulty
★★☆☆☆

## Performance Impact
Low

## Libraries
GSAP

---

## Description

A typewriter animation that reveals text character by character with a blinking cursor at the end. Simulates real-time typing, creating a conversational, human feel. Perfect for hero taglines, code demonstrations, chat interfaces, or landing page subheadings.

The effect uses a JavaScript interval to append characters to a visible string while GSAP manages the cursor blink animation.

---

## Timeline

| Moment | Time | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0ms | Cursor | Start blinking | infinite | step-end |
| 2 | 0ms | Text | Append character | 50ms per char | — |
| 3 | text-end | Cursor | Continue blink | infinite | step-end |

---

## Psychology

- **Human Connection:** Typewriter effect mimics human typing, creating warmth and authenticity.
- **Pacing Control:** Slower reveals force the user to read at a deliberate pace — improves comprehension.
- **Anticipation:** Each new character creates micro-suspense — "What comes next?"

---

## Implementation

```html
<div class="typewriter" style="font-family: 'Courier New', monospace; font-size: 2rem; color: white; display: inline-flex; align-items: center;">
  <span class="typewriter-text"></span>
  <span class="typewriter-cursor" style="display: inline-block; width: 2px; height: 1.2em; background: #a29bfe; margin-left: 2px; animation: blink 0.8s step-end infinite;">&nbsp;</span>
</div>

<style>
@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}
</style>
```

```javascript
function typeWriter(elementSelector, text, speed = 50) {
  const el = document.querySelector(elementSelector);
  if (!el || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    if (el) el.textContent = text;
    return;
  }

  let index = 0;

  function type() {
    if (index < text.length) {
      el.textContent += text.charAt(index);
      index++;
      setTimeout(type, speed);
    }
  }

  type();
}

typeWriter('.typewriter-text', 'Build Beyond Boundaries.', 60);

// Scroll-triggered variant
gsap.registerPlugin(ScrollTrigger);

ScrollTrigger.create({
  trigger: '.typewriter',
  start: 'top 85%',
  onEnter: () => typeWriter('.typewriter-text', 'Scroll-triggered typing.', 50),
  once: true
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Technology | ★★★★★ | Code demos, taglines |
| Creative | ★★★★☆ | Portfolio introductions |
| Education | ★★★★★ | Step-by-step tutorials |
| SaaS | ★★★☆☆ | Landing page headlines |
| Legal | ★☆☆☆☆ | Too informal |

---

## Accessibility Notes

- Entire text must be available to screen readers immediately (use `aria-label` on container)
- Cursor blink must stop after 5 seconds or respect `prefers-reduced-motion`
- Speed must be adjustable — default 50ms per character is safe
- Full text rendered immediately when `prefers-reduced-motion: reduce` is set

---

## Performance Notes

- Uses `setTimeout` — negligible performance cost
- Cursor blink via CSS animation is GPU composited
- No DOM manipulation beyond `textContent` updates — zero layout cost

---

## Variants

### Variant A: Multi-Line Typewriter
Multiple lines type in sequence — first finishes, then second starts.

### Variant B: Typewriter with Backspace
Types forward, pauses, then backspaces and types the next phrase — cyclical.

### Variant C: Humanized Typos
Simulates typing mistakes — types wrong character, pauses, backspaces, types correct one.

---

## Anti-Patterns

- Typing very long paragraphs (user waits too long)
- No cursor — removes the typewriter illusion
- Speed too slow (> 100ms per char) — feels sluggish
- Not stopping cursor blink — WCAG failure for flashing content
- Typing effect on critical instructions users need immediately

---

## Checklist

- [ ] Full text available via `aria-label`
- [ ] Reduced motion: show full text immediately
- [ ] Cursor blink stops or respects reduced motion
- [ ] Type speed between 40-80ms per character
- [ ] Scroll-trigger variant resets correctly
