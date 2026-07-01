# Experience 043: Horizontal Scroll Section

## Classification
Narrative

## Emotion
Discovery → Engagement

## Difficulty
★★★★☆

## Performance Impact
Medium

## Libraries
GSAP, ScrollTrigger

---

## Description

A section where vertical scrolling translates into horizontal movement of content panels. The section is pinned while panels slide horizontally, creating a "scroll through a gallery" effect. Each panel can contain different content — images, text, or mixed media.

Use for portfolio showcases, product feature walkthroughs, timeline narratives, or any sequential content that benefits from a horizontal reveal.

---

## Timeline

| Moment | Scroll Position | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0% | Section | Pin at top of viewport | — | — |
| 2 | 0%-100% | Panels container | TranslateX from 0 to -(totalWidth - viewport) | viewport | Linear |
| 3 | 100% | Section | Unpin, continue scroll | — | — |

---

## Psychology

- **Spatial Novelty:** Breaking the expected vertical scrolling pattern captures attention and feels exploratory.
- **Sequential Narrative:** Horizontal progression mimics reading a book or walking through a gallery — natural for storytelling.
- **Milestone Satisfaction:** Each panel fully in view feels like "completing" that chapter, encouraging forward motion.

---

## Implementation

```html
<section class="horizontal-scroll" style="height: 300vh; position: relative;">
  <div class="horizontal-sticky" style="position: sticky; top: 0; height: 100vh; overflow: hidden; display: flex; align-items: center; background: #1a1a2e;">
    <div class="horizontal-panels" style="display: flex; gap: 2rem; padding: 2rem; will-change: transform;">
      <div class="h-panel" style="min-width: 80vw; height: 70vh; background: linear-gradient(135deg, #6c5ce7, #a29bfe); border-radius: 24px; display: flex; align-items: center; justify-content: center; color: white; font-family: system-ui; font-size: 3rem; font-weight: 700;">
        Panel 1
      </div>
      <div class="h-panel" style="min-width: 80vw; height: 70vh; background: linear-gradient(135deg, #e17055, #fdcb6e); border-radius: 24px; display: flex; align-items: center; justify-content: center; color: white; font-family: system-ui; font-size: 3rem; font-weight: 700;">
        Panel 2
      </div>
      <div class="h-panel" style="min-width: 80vw; height: 70vh; background: linear-gradient(135deg, #00b894, #55efc4); border-radius: 24px; display: flex; align-items: center; justify-content: center; color: white; font-family: system-ui; font-size: 3rem; font-weight: 700;">
        Panel 3
      </div>
      <div class="h-panel" style="min-width: 80vw; height: 70vh; background: linear-gradient(135deg, #0984e3, #74b9ff); border-radius: 24px; display: flex; align-items: center; justify-content: center; color: white; font-family: system-ui; font-size: 3rem; font-weight: 700;">
        Panel 4
      </div>
    </div>
  </div>
</section>
```

```javascript
gsap.registerPlugin(ScrollTrigger);

const panels = document.querySelector('.horizontal-panels');
const totalWidth = panels.scrollWidth;

gsap.to(panels, {
  x: () => -(totalWidth - window.innerWidth),
  ease: 'none',
  scrollTrigger: {
    trigger: '.horizontal-scroll',
    start: 'top top',
    end: () => `+=${totalWidth - window.innerWidth}`,
    pin: true,
    scrub: 1,
    invalidateOnRefresh: true
  }
});

// Handle resize
window.addEventListener('resize', () => {
  ScrollTrigger.refresh();
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Creative Agency | ★★★★★ | Portfolio gallery |
| Technology | ★★★★★ | Product feature walkthrough |
| Travel | ★★★★☆ | Destination panoramas |
| Real Estate | ★★★★☆ | Property tour |
| Media | ★★★★☆ | Photo essays |

---

## Accessibility Notes

- Content must be fully navigable via keyboard (Tab through panels)
- Provide a "scroll down to continue" hint at the start of the section
- `prefers-reduced-motion: reduce` — stack panels vertically, no horizontal scroll
- Panel content must work when panels are stacked (responsive fallback)
- Screen readers may not detect horizontal scroll — announce section purpose

---

## Performance Notes

- Use `will-change: transform` on the panels container
- For many panels, consider lazy-loading images as they come into view
- `invalidateOnRefresh: true` ensures correct width on resize
- Container width calculation must account for all gaps and padding

---

## Variants

### Variant A: Snap Scroll
Panels snap into view (not smooth scrub) — each panel locks into center on scroll stop.

### Variant B: Horizontal + Vertical
Each horizontal panel itself contains vertical scroll content — nested scroll experiences.

### Variant C: Progress-Linked
A progress indicator at the bottom shows which panel is active / how many remain.

---

## Anti-Patterns

- More than 8 panels — user fatigue from scrolling too long
- Panels with varying widths — inconsistent experience
- No visual hint that horizontal scroll is available — users scroll down and see nothing
- Interactive elements inside panels that conflict with scroll (e.g., horizontal sliders)
- No resize handling — layout breaks on orientation change

---

## Checklist

- [ ] Panel count ≤ 8
- [ ] Scroll hint visible at section start
- [ ] Resize handler with `ScrollTrigger.refresh()`
- [ ] Reduced motion: vertical stack
- [ ] Panels keyboard navigable
- [ ] Tested on mobile (may need tap-to-advance fallback)
