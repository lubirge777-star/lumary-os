# Experience 044: Pinned Section with Accordion

## Classification
Narrative

## Emotion
Clarity → Satisfaction

## Difficulty
★★★★☆

## Performance Impact
Medium

## Libraries
GSAP, ScrollTrigger

---

## Description

A pinned section where scrolling expands accordion items one by one. As the user scrolls, each accordion panel expands to reveal its content, then collapses as the next one opens. The section stays pinned until all panels have been expanded.

Use for FAQs, step-by-step processes, team member bios, timeline events, or any sequential reveal where content density benefits from progressive disclosure.

---

## Timeline

| Moment | Scroll Position | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0% | Accordion container | Pin in viewport | — | — |
| 2 | 0%-25% | Accordion item 1 | Expand (height: 0 → auto) | viewport/4 | Power2.out |
| 3 | 25%-50% | Item 2 expand, Item 1 collapse | — | viewport/4 | Power2.out |
| 4 | 50%-75% | Item 3 expand, Item 2 collapse | — | viewport/4 | Power2.out |
| 5 | 75%-100% | Item 4 expand, Item 3 collapse | — | viewport/4 | Power2.out |
| 6 | 100% | Section | Unpin | — | — |

---

## Psychology

- **Progressive Disclosure:** Information is presented in digestible chunks — reduces cognitive overload.
- **Completion Urge:** Seeing unopened panels motivates the user to scroll further to "complete" the set.
- **Serial Position Effect:** Each panel gets focused attention because only one is open at a time.

---

## Implementation

```html
<section class="pin-accordion-section" style="height: 500vh; position: relative;">
  <div class="pin-accordion" style="position: sticky; top: 0; height: 100vh; display: flex; align-items: center; justify-content: center; background: #1a1a2e; padding: 4rem;">
    <div class="accordion-container" style="width: 600px; max-width: 90vw;">
      <h2 style="color: white; font-family: system-ui; margin-bottom: 2rem;">How It Works</h2>
      <div class="accordion-item" data-index="0" style="border-bottom: 1px solid #333;">
        <div class="accordion-header" style="padding: 1rem 0; color: white; font-family: system-ui; font-weight: 600; cursor: default;">01. Discovery</div>
        <div class="accordion-body" style="height: 0; overflow: hidden; color: #aaa; font-family: system-ui; font-size: 0.9rem; line-height: 1.6;">
          <div style="padding-bottom: 1rem;">We research your market, competitors, and user needs to define the project scope.</div>
        </div>
      </div>
      <div class="accordion-item" data-index="1" style="border-bottom: 1px solid #333;">
        <div class="accordion-header" style="padding: 1rem 0; color: white; font-family: system-ui; font-weight: 600; cursor: default;">02. Design</div>
        <div class="accordion-body" style="height: 0; overflow: hidden; color: #aaa; font-family: system-ui; font-size: 0.9rem; line-height: 1.6;">
          <div style="padding-bottom: 1rem;">Wireframes, prototypes, and visual design crafted through iterative feedback.</div>
        </div>
      </div>
      <div class="accordion-item" data-index="2" style="border-bottom: 1px solid #333;">
        <div class="accordion-header" style="padding: 1rem 0; color: white; font-family: system-ui; font-weight: 600; cursor: default;">03. Build</div>
        <div class="accordion-body" style="height: 0; overflow: hidden; color: #aaa; font-family: system-ui; font-size: 0.9rem; line-height: 1.6;">
          <div style="padding-bottom: 1rem;">Development with continuous integration, testing, and performance optimization.</div>
        </div>
      </div>
      <div class="accordion-item" data-index="3" style="border-bottom: 1px solid #333;">
        <div class="accordion-header" style="padding: 1rem 0; color: white; font-family: system-ui; font-weight: 600; cursor: default;">04. Launch</div>
        <div class="accordion-body" style="height: 0; overflow: hidden; color: #aaa; font-family: system-ui; font-size: 0.9rem; line-height: 1.6;">
          <div style="padding-bottom: 1rem;">Deploy, monitor, and iterate based on real user data and feedback.</div>
        </div>
      </div>
    </div>
  </div>
</section>
```

```javascript
gsap.registerPlugin(ScrollTrigger);

const items = document.querySelectorAll('.accordion-item');
const bodies = document.querySelectorAll('.accordion-body');
const totalItems = items.length;

// Calculate body heights for animation
bodies.forEach(body => {
  const child = body.firstElementChild;
  body.dataset.fullHeight = child ? child.offsetHeight + 'px' : '0px';
});

ScrollTrigger.create({
  trigger: '.pin-accordion-section',
  start: 'top top',
  end: `+=${totalItems * 100}vh`,
  pin: '.pin-accordion',
  scrub: 1
});

items.forEach((item, index) => {
  const body = item.querySelector('.accordion-body');
  const fullHeight = body.dataset.fullHeight || '100px';

  ScrollTrigger.create({
    trigger: '.pin-accordion-section',
    start: `top top+=${index * 100}vh`,
    end: `top top+=${(index + 1) * 100}vh`,
    scrub: 1,
    onUpdate: (self) => {
      const progress = self.progress;
      const prevBody = index > 0 ? items[index - 1].querySelector('.accordion-body') : null;

      // Expand current
      if (progress > 0.5) {
        gsap.to(body, { height: fullHeight, duration: 0.4, ease: 'power2.out' });
      } else {
        gsap.to(body, { height: 0, duration: 0.3, ease: 'power2.in' });
      }

      // Collapse previous
      if (prevBody && progress < 0.8) {
        gsap.to(prevBody, { height: 0, duration: 0.3, ease: 'power2.in' });
      }
    }
  });
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| SaaS | ★★★★★ | Feature walkthroughs |
| Education | ★★★★★ | Course curriculum |
| Professional Services | ★★★★☆ | Process explanation |
| Real Estate | ★★★★☆ | Property features |
| Healthcare | ★★★☆☆ | Treatment steps |

---

## Accessibility Notes

- Accordion headers must be `<button>` elements for keyboard accessibility in interactive mode
- For scroll-driven mode, provide a clickable accordion fallback
- Use `aria-expanded` and `aria-controls` for interactive state
- `prefers-reduced-motion: reduce` — show all panels expanded, no scroll pinning
- Announce section changes to screen readers via `aria-live` region

---

## Performance Notes

- Animating `height` triggers layout — use `max-height` or a wrapper with `clip-path` if possible
- For smoother performance, animate `clip-path: inset(0 0 100% 0)` instead of `height`
- Use `will-change: height` on accordion bodies (or `clip-path`)
- Pre-calculate body heights to avoid layout thrashing during scroll

---

## Variants

### Variant A: Single Open
Only one accordion open at a time (classic accordion). Scroll advances through them sequentially.

### Variant B: Multi-Open Stack
Previous items stay expanded as new ones open — user sees the full accumulated content.

### Variant C: Visual Timeline
Accordions arranged along a vertical timeline line with scroll-triggered dot animations.

---

## Anti-Patterns

- Accordion bodies with dynamic/unknown height — height animation breaks
- More than 6 items — too much scrolling for too little content
- Content inside accordion that itself needs scrolling — nested scroll conflicts
- No click fallback — scroll-only accordion fails keyboard users

---

## Checklist

- [ ] Item count ≤ 6
- [ ] Body heights pre-calculated
- [ ] Reduced motion: show all expanded
- [ ] Click fallback for accordion interaction
- [ ] `aria-expanded` states managed
- [ ] Tested with keyboard navigation
