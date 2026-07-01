# Experience 037: Shake on Validation Error

## Classification
Feedback

## Emotion
Alert → Correction

## Difficulty
★★☆☆☆

## Performance Impact
Low

## Libraries
GSAP

---

## Description

A rapid horizontal shake animation on form inputs when validation fails. The motion mimics a "no" head-shake, providing immediate physical feedback that something is wrong. Combined with color change and error message reveal, it creates a multi-modal error signal.

Use on any form where validation feedback needs to be immediate, noticeable, and intuitive.

---

## Interaction

User submits a form or tabs out of an invalid field. If validation fails, GSAP applies a rapid `x` oscillation to the input or the entire field group. The input border turns red, and an error message fades in below. After shaking, the input subtly pulses to draw attention. User corrects the value; the error state clears with a reverse animation.

---

## Psychology

- **Embodied Cognition:** The shake motion physically mimics "no," which is universally understood across cultures.
- **Error Salience:** Motion captures peripheral attention better than static color changes alone.
- **Negative Reinforcement:** The uncomfortable jitter encourages correct input to avoid the sensation again.

---

## Implementation

```html
<form class="shake-form" style="max-width: 400px; font-family: system-ui;">
  <div class="shake-group" style="margin-bottom: 1.5rem;">
    <input type="email" class="shake-input" required placeholder="Email address"
      style="width: 100%; padding: 0.85rem 1rem; border: 2px solid #444; border-radius: 8px; background: #1a1a2e; color: white; font-size: 1rem; outline: none;" />
    <div class="shake-error" style="color: #ff4757; font-size: 0.85rem; margin-top: 0.4rem; height: 0; overflow: hidden; opacity: 0;">Please enter a valid email.</div>
  </div>
  <button type="submit" style="padding: 0.85rem 2rem; background: #6c5ce7; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 1rem;">Submit</button>
</form>
```

```javascript
document.querySelector('.shake-form').addEventListener('submit', (e) => {
  e.preventDefault();
  const input = document.querySelector('.shake-input');
  const error = document.querySelector('.shake-error');
  const group = document.querySelector('.shake-group');

  if (!input.value || !input.value.includes('@')) {
    // Shake animation
    gsap.fromTo(input,
      { x: 0 },
      {
        x: [-8, 8, -6, 6, -4, 4, -2, 2, 0],
        duration: 0.5,
        ease: 'power2.out',
        borderColor: '#ff4757'
      }
    );

    // Show error
    gsap.to(error, {
      height: 'auto',
      opacity: 1,
      duration: 0.3,
      ease: 'power2.out'
    });

    // Pulse border
    gsap.to(input, {
      borderColor: '#ff6b81',
      duration: 0.6,
      yoyo: true,
      repeat: 1,
      delay: 0.6,
      ease: 'power2.inOut'
    });
  } else {
    // Clear error
    gsap.to(input, { borderColor: '#2ed573', duration: 0.3 });
    gsap.to(error, { height: 0, opacity: 0, duration: 0.3 });
  }
});

// Clear error on valid input
document.querySelector('.shake-input').addEventListener('input', function () {
  if (this.value.includes('@')) {
    gsap.to(this, { borderColor: '#2ed573', duration: 0.3 });
    gsap.to(document.querySelector('.shake-error'), { height: 0, opacity: 0, duration: 0.3 });
  }
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| SaaS | ★★★★★ | Auth forms, signup |
| E-commerce | ★★★★★ | Checkout validation |
| Finance | ★★★★☆ | Payment form errors |
| Healthcare | ★★★★☆ | Patient intake forms |
| Enterprise | ★★★☆☆ | Internal tool forms |

---

## Accessibility Notes

- Shake must NOT be the only error indicator — error message text is essential
- `aria-live="polite"` on error message container for screen reader announcement
- `prefers-reduced-motion: reduce` — show error state without shake (just color + message)
- Error messages must be linked to input via `aria-describedby`

---

## Performance Notes

- GSAP keyframe array (`[-8, 8, -6, 6...]`) is highly optimized
- Only `x` transform — no layout thrashing
- Border color animation is GPU-composited in modern browsers

---

## Variants

### Variant A: Input + Field Highlight
Entire field group shakes, and the label also turns red for extra emphasis.

### Variant B: Bounce Validation
Instead of shake, the input "bounces" (scale oscillates) — softer, less aggressive feedback.

### Variant C: Inline + Summary
Individual fields shake, plus a summary banner at the top that lists all errors.

---

## Anti-Patterns

- Shaking the entire form — disorienting and unnecessary
- Shake duration > 600ms — excessive punishment
- No error text — shake alone does not explain what is wrong
- Overusing on every keystroke — only show on blur or submit
- Applying shake to success states — confusing

---

## Checklist

- [ ] Error message text always provided alongside shake
- [ ] `prefers-reduced-motion` — color + message only
- [ ] `aria-describedby` linking input to error
- [ ] Shake duration ≤ 500ms
- [ ] Positive state (green border) when valid
