# Experience 051: Active Section Scroll Indicator

## Classification
Guide

## Emotion
Confidence → Orientation

## Difficulty
★★★☆☆

## Performance Impact
Low

## Libraries
GSAP, ScrollTrigger

---

## Description

A navigation indicator that follows the user's scroll position, highlighting which section of the page is currently in view. The indicator can be a dot in a vertical rail, an underline on a nav item, or a line connecting to the current section.

Use on single-page websites, long-form content, documentation pages, or any page with distinct sections where the user benefits from spatial orientation.

---

## Interaction

As the user scrolls through page sections, the active nav item updates with a smooth animation. The indicator (dot, underline, or filled icon) transitions from the previous active item to the current one. The indicator can use `y` position animation for vertical navigation rails or `x` for horizontal nav bars.

---

## Psychology

- **Wayfinding:** A moving indicator provides continuous spatial orientation — "Where am I?" and "What's next?"
- **Progress Motivation:** Seeing the indicator advance as they scroll rewards users and encourages continued reading.
- **Structure Communication:** The indicator maps out the page structure implicitly, helping users understand content hierarchy.

---

## Implementation

```html
<nav class="indicator-nav" style="position: fixed; right: 2rem; top: 50%; transform: translateY(-50%); z-index: 100; display: flex; flex-direction: column; align-items: center; gap: 1.5rem; font-family: system-ui;">
  <div class="nav-rail" style="position: absolute; top: 0; bottom: 0; left: 50%; width: 2px; background: rgba(255,255,255,0.1); transform: translateX(-50%);"></div>
  <div class="nav-indicator-dot" style="position: absolute; width: 12px; height: 12px; background: #6c5ce7; border-radius: 50%; left: 50%; transform: translateX(-50%); top: 0; z-index: 2; box-shadow: 0 0 12px rgba(108,92,231,0.5);"></div>
  <a class="nav-section-link active" href="#section-1" data-section="0" style="width: 8px; height: 8px; border-radius: 50%; background: rgba(255,255,255,0.4); z-index: 1; cursor: pointer; transition: background 0.3s, transform 0.3s;"></a>
  <a class="nav-section-link" href="#section-2" data-section="1" style="width: 8px; height: 8px; border-radius: 50%; background: rgba(255,255,255,0.4); z-index: 1; cursor: pointer; transition: background 0.3s, transform 0.3s;"></a>
  <a class="nav-section-link" href="#section-3" data-section="2" style="width: 8px; height: 8px; border-radius: 50%; background: rgba(255,255,255,0.4); z-index: 1; cursor: pointer; transition: background 0.3s, transform 0.3s;"></a>
  <a class="nav-section-link" href="#section-4" data-section="3" style="width: 8px; height: 8px; border-radius: 50%; background: rgba(255,255,255,0.4); z-index: 1; cursor: pointer; transition: background 0.3s, transform 0.3s;"></a>
</nav>

<div style="font-family: system-ui; color: white;">
  <section id="section-1" style="height: 100vh; display: flex; align-items: center; justify-content: center; font-size: 3rem;">Introduction</section>
  <section id="section-2" style="height: 100vh; display: flex; align-items: center; justify-content: center; font-size: 3rem;">Features</section>
  <section id="section-3" style="height: 100vh; display: flex; align-items: center; justify-content: center; font-size: 3rem;">Pricing</section>
  <section id="section-4" style="height: 100vh; display: flex; align-items: center; justify-content: center; font-size: 3rem;">Contact</section>
</div>
```

```javascript
gsap.registerPlugin(ScrollTrigger);

const sections = document.querySelectorAll('section[id]');
const links = document.querySelectorAll('.nav-section-link');
const indicator = document.querySelector('.nav-indicator-dot');
const linkHeight = 8 + 24; // dot height + gap

let currentIndex = 0;

// ScrollTrigger for each section
sections.forEach((section, i) => {
  ScrollTrigger.create({
    trigger: section,
    start: 'top 40%',
    end: 'bottom 40%',
    onEnter: () => setActive(i),
    onEnterBack: () => setActive(i)
  });
});

function setActive(index) {
  if (index === currentIndex) return;
  currentIndex = index;

  // Update indicator position
  gsap.to(indicator, {
    top: index * linkHeight,
    duration: 0.5,
    ease: 'power3.out'
  });

  // Update link styles
  links.forEach((link, i) => {
    gsap.to(link, {
      background: i === index ? '#6c5ce7' : 'rgba(255,255,255,0.4)',
      scale: i === index ? 1.5 : 1,
      duration: 0.3,
      ease: 'power2.out'
    });
  });
}

// Click to scroll
links.forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const section = document.querySelector(link.getAttribute('href'));
    if (section) {
      section.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Reduced motion
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  gsap.set(indicator, { top: 0 });
  ScrollTrigger.getAll().forEach(st => st.disable());
}
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Documentation | ★★★★★ | Technical docs, API refs |
| Creative | ★★★★★ | One-page portfolio |
| Technology | ★★★★☆ | Product landing pages |
| Media | ★★★★☆ | Long-form articles |
| Education | ★★★★☆ | Course modules |

---

## Accessibility Notes

- Navigation links must be actual `<a>` elements with `href` for keyboard navigation
- `aria-current="location"` should be set on the active link
- Indicator color change must be accompanied by a non-color cue (size, shape, or text)
- Reduced motion: snap indicator directly, no animation
- Clicking a nav link must scroll the page (smooth scroll or instant)

---

## Performance Notes

- Indicator uses `top` position animation (transform for GPU acceleration)
- Dot color/scale changes are cheap (compositor)
- `ScrollTrigger` observers are lightweight — no polling
- For > 12 sections, consider collapsing into a progress bar instead

---

## Variants

### Variant A: Horizontal Nav Underline
For top nav bars — an underline transitions between nav items as sections change.

### Variant B: Progress Bar
A thin progress bar at the top or bottom of the viewport indicating page reading progress.

### Variant C: Section Counter
A "2 / 8" counter that fades between numbers as user scrolls — minimal and clean.

---

## Anti-Patterns

- More than 12 nav items — too many dots, visual clutter
- Indicator matches section count but IDs are misaligned — broken tracking
- No click-to-scroll — users should be able to jump to sections
- Indicator only updates on `onEnter` without `onEnterBack` — broken reverse scroll
- Using `scroll-behavior: smooth` on the HTML element — conflicts with ScrollTrigger scrub

---

## Checklist

- [ ] Sections mapped to nav items 1:1
- [ ] `aria-current="location"` on active link
- [ ] Click-to-scroll implemented
- [ ] OnEnter + OnEnterBack both handled
- [ ] Reduced motion: snap indicator
- [ ] Section count ≤ 12
