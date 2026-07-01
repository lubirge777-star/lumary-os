# Experience 036: Form Progress Bar

## Classification
Guide

## Emotion
Confidence → Satisfaction

## Difficulty
★★★☆☆

## Performance Impact
Low

## Libraries
GSAP

---

## Description

A multi-step form with a visual progress indicator that animates as the user advances through each step. The progress bar fills, step labels update, and content panels transition smoothly. This reduces form abandonment by clearly communicating how much remains.

Use for lengthy forms: checkout, onboarding, multi-page applications, surveys, or registration flows where completion rate is critical.

---

## Interaction

User clicks "Next" or "Back" buttons to navigate between form steps. GSAP animates the progress bar width, step indicator states (inactive → active → completed), and the sliding transition of form panels. Current step number and total steps are displayed for context.

---

## Psychology

- **Goal Gradient Effect:** Users accelerate as they see progress — the closer to completion, the more motivated they become.
- **Commitment Consistency:** After investing effort in early steps, users are more likely to complete the entire form.
- **Uncertainty Reduction:** A clear progress indicator eliminates "how long is this?" anxiety, reducing abandonment.

---

## Implementation

```html
<div class="form-progress" style="max-width: 600px; margin: 0 auto; font-family: system-ui;">
  <div class="progress-tracker" style="display: flex; justify-content: space-between; margin-bottom: 2rem; position: relative;">
    <div class="progress-bar-bg" style="position: absolute; top: 50%; left: 0; right: 0; height: 3px; background: #333; transform: translateY(-50%);"></div>
    <div class="progress-bar-fill" style="position: absolute; top: 50%; left: 0; height: 3px; background: linear-gradient(90deg, #6c5ce7, #a29bfe); transform: translateY(-50%); width: 0%;"></div>
    <div class="progress-step" data-step="1" style="position: relative; z-index: 1; width: 36px; height: 36px; border-radius: 50%; background: #333; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600; transition: background 0.3s;">1</div>
    <div class="progress-step" data-step="2" style="position: relative; z-index: 1; width: 36px; height: 36px; border-radius: 50%; background: #333; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600;">2</div>
    <div class="progress-step" data-step="3" style="position: relative; z-index: 1; width: 36px; height: 36px; border-radius: 50%; background: #333; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600;">3</div>
    <div class="progress-step" data-step="4" style="position: relative; z-index: 1; width: 36px; height: 36px; border-radius: 50%; background: #333; display: flex; align-items: center; justify-content: center; color: white; font-weight: 600;">4</div>
  </div>
  <div class="form-panels" style="position: relative; overflow: hidden;">
    <div class="form-panel active" data-panel="1" style="padding: 2rem; background: #1a1a2e; border-radius: 16px; color: white;">Step 1: Account Info</div>
    <div class="form-panel" data-panel="2" style="padding: 2rem; background: #1a1a2e; border-radius: 16px; color: white; position: absolute; top: 0; left: 0; width: 100%;">Step 2: Shipping</div>
    <div class="form-panel" data-panel="3" style="padding: 2rem; background: #1a1a2e; border-radius: 16px; color: white; position: absolute; top: 0; left: 0; width: 100%;">Step 3: Payment</div>
    <div class="form-panel" data-panel="4" style="padding: 2rem; background: #1a1a2e; border-radius: 16px; color: white; position: absolute; top: 0; left: 0; width: 100%;">Step 4: Review</div>
  </div>
  <div class="form-nav" style="display: flex; justify-content: space-between; margin-top: 1.5rem;">
    <button class="btn-prev" style="padding: 0.75rem 2rem; border-radius: 8px; border: 1px solid #444; background: transparent; color: white; cursor: pointer;">Back</button>
    <button class="btn-next" style="padding: 0.75rem 2rem; border-radius: 8px; border: none; background: #6c5ce7; color: white; cursor: pointer;">Next</button>
  </div>
</div>
```

```javascript
let currentStep = 1;
const totalSteps = 4;

const fill = document.querySelector('.progress-bar-fill');
const steps = document.querySelectorAll('.progress-step');
const panels = document.querySelectorAll('.form-panel');
const prevBtn = document.querySelector('.btn-prev');
const nextBtn = document.querySelector('.btn-next');

function goToStep(step) {
  currentStep = Math.max(1, Math.min(step, totalSteps));

  // Progress bar
  gsap.to(fill, {
    width: `${((currentStep - 1) / (totalSteps - 1)) * 100}%`,
    duration: 0.5,
    ease: 'power2.inOut'
  });

  // Step indicators
  steps.forEach((s, i) => {
    const stepNum = i + 1;
    gsap.to(s, {
      background: stepNum <= currentStep ? '#6c5ce7' : '#333',
      scale: stepNum === currentStep ? 1.15 : 1,
      duration: 0.3,
      ease: 'power2.out'
    });
  });

  // Panels
  panels.forEach(panel => {
    const panelNum = parseInt(panel.dataset.panel);
    if (panelNum === currentStep) {
      gsap.set(panel, { display: 'block' });
      gsap.fromTo(panel, { x: 30, opacity: 0 }, { x: 0, opacity: 1, duration: 0.4, ease: 'power2.out' });
    } else {
      gsap.set(panel, { display: 'none' });
    }
  });

  // Buttons
  prevBtn.style.display = currentStep === 1 ? 'none' : 'block';
  nextBtn.textContent = currentStep === totalSteps ? 'Submit' : 'Next';
}

nextBtn.addEventListener('click', () => goToStep(currentStep + 1));
prevBtn.addEventListener('click', () => goToStep(currentStep - 1));

goToStep(1);
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| E-commerce | ★★★★★ | Checkout flow |
| SaaS | ★★★★★ | Onboarding wizard |
| Finance | ★★★★☆ | Loan application |
| Healthcare | ★★★★☆ | Patient registration |
| Education | ★★★★☆ | Course enrollment |

---

## Accessibility Notes

- Use `aria-current="step"` on the current step indicator
- Each panel should be a `<fieldset>` with `<legend>` for screen reader context
- Announce step changes via `aria-live="polite"` region
- Keyboard navigation: Enter to proceed, Escape to go back (optional)
- `prefers-reduced-motion: reduce` — snap transitions, no slide animations

---

## Performance Notes

- Only width and transform changes — no layout cost
- Panel transitions use `x` transform — GPU composited
- Preload all panels (hidden with `display: none`) to avoid layout shift
- Max 10 steps before cognitive overload

---

## Variants

### Variant A: Vertical Stepper
Steps displayed vertically with connecting lines — better for sidebars or wide screens.

### Variant B: Circular Progress
A donut/circular progress indicator instead of a horizontal bar. More visual but less space-efficient.

### Variant C: Step Numbered with Descriptions
Each step shows title and brief description below the numbered circle.

---

## Anti-Patterns

- More than 10 steps — causes drop-off regardless of animation
- No "Save & Continue" option — users lose data on browser close
- Linear-only navigation (no step skipping) — frustrates power users when appropriate
- Progress bar reaching 100% too early — creates false completion expectation

---

## Checklist

- [ ] Step count ≤ 10
- [ ] Progress persists across page refresh (sessionStorage)
- [ ] Keyboard navigable (Tab, Enter)
- [ ] `aria-current="step"` implemented
- [ ] Reduced motion: snap transitions
- [ ] Mobile responsive (stacked on small screens)
