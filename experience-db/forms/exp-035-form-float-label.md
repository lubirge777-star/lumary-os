# Experience 035: Floating Label Animation

## Classification
Feedback

## Emotion
Clarity → Satisfaction

## Difficulty
★★☆☆☆

## Performance Impact
Low

## Libraries
GSAP

---

## Description

Labels float from inside the input field to above it when the user focuses or types. This Material Design-inspired pattern saves space while maintaining clear labeling. The motion makes the form feel responsive and thoughtful.

Use on any form — signup, login, contact, checkout — where clean, space-efficient design is desired.

---

## Interaction

User focuses on an input. The label animates from its placeholder position inside the field to a smaller position above the field. When the user leaves the field empty, the label returns. If the field has content, the label stays in the floating position. GSAP animates the `y`, `scale`, and `color` properties for a smooth transition.

---

## Psychology

- **Context Preservation:** Animated labels maintain spatial association between label and input — users don't lose context.
- **Progress Indicator:** Floating label signals "this field has been interacted with" — micro-feedback of progress.
- **Cognitive Load Reduction:** Seeing the label at all times reduces memory load compared to placeholder-only forms.

---

## Implementation

```html
<form class="float-form" style="max-width: 400px; font-family: system-ui;">
  <div class="float-group" style="position: relative; margin-bottom: 2rem;">
    <input type="email" class="float-input" style="width: 100%; padding: 1.2rem 0.75rem 0.4rem; border: 1px solid #444; border-radius: 8px; background: #1a1a2e; color: white; font-size: 1rem; outline: none; transition: border-color 0.2s;" />
    <label class="float-label" style="position: absolute; left: 0.75rem; top: 50%; transform: translateY(-50%); color: #888; font-size: 1rem; pointer-events: none; transition: none;">Email Address</label>
  </div>
  <div class="float-group" style="position: relative; margin-bottom: 2rem;">
    <input type="password" class="float-input" style="width: 100%; padding: 1.2rem 0.75rem 0.4rem; border: 1px solid #444; border-radius: 8px; background: #1a1a2e; color: white; font-size: 1rem; outline: none;" />
    <label class="float-label" style="position: absolute; left: 0.75rem; top: 50%; transform: translateY(-50%); color: #888; font-size: 1rem; pointer-events: none;">Password</label>
  </div>
</form>
```

```javascript
document.querySelectorAll('.float-group').forEach(group => {
  const input = group.querySelector('.float-input');
  const label = group.querySelector('.float-label');
  const activeColor = '#a29bfe';

  function floatUp() {
    gsap.to(label, {
      y: -28,
      scale: 0.75,
      color: activeColor,
      duration: 0.3,
      ease: 'power2.out'
    });
    gsap.to(input, {
      borderColor: activeColor,
      duration: 0.3,
      ease: 'power2.out'
    });
  }

  function floatDown() {
    gsap.to(label, {
      y: 0,
      scale: 1,
      color: '#888',
      duration: 0.3,
      ease: 'power2.out'
    });
    gsap.to(input, {
      borderColor: '#444',
      duration: 0.3,
      ease: 'power2.out'
    });
  }

  input.addEventListener('focus', floatUp);

  input.addEventListener('blur', () => {
    if (!input.value) floatDown();
  });

  // Check initial value
  if (input.value) floatUp();
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| SaaS | ★★★★★ | Signup forms, login |
| E-commerce | ★★★★★ | Checkout forms |
| Finance | ★★★★☆ | Account creation |
| Healthcare | ★★★★☆ | Patient intake |
| Education | ★★★★☆ | Enrollment forms |

---

## Accessibility Notes

- Labels must be genuinely `<label>` elements associated with `for` attribute — not just visual decorations
- Floating animation must not interfere with screen reader label announcement
- Color change must not be the only focus indicator — maintain `:focus-visible` outline
- `prefers-reduced-motion: reduce` — skip animation, snap label to floating position instantly

---

## Performance Notes

- Only `y` and `scale` transforms — no layout cost
- CSS `transition` could replace GSAP for lighter weight
- No event listeners on every keystroke — only focus/blur

---

## Variants

### Variant A: Border Accent
Floating label + input bottom border animates from thin gray to thick accent color on focus.

### Variant B: Icon Float
Input has a leading icon that also floats up with the label, changing color.

### Variant C: Shrink & Lift with Background
Label floats up and gains a small background "pill" behind it (useful when input border is full-width).

---

## Anti-Patterns

- Using placeholder instead of label — kills accessibility
- Floating label overlapping input border — visual confusion
- Label color too similar to input background — contrast failure
- Not handling autofill — browser autofill can leave label in wrong position

---

## Checklist

- [ ] `<label>` associated with `for` attribute
- [ ] Handles autofill (check initial value)
- [ ] Color contrast ≥ 4.5:1 for all label states
- [ ] Reduced motion: snap to position
- [ ] Touch device friendly (no hover dependency)
