# Experience 014: The Progress Navigation

## Classification: Guide
## Emotion: Trust
## Difficulty: ★★☆☆☆
## Performance: Low
## Libraries: GSAP ScrollTrigger

## Description
A horizontal progress bar at the top of the viewport that fills as the user scrolls through the page. Combined with section labels that highlight as each section enters view.

## Code
```javascript
// Progress bar
gsap.to('.progress-fill', {
  scaleX: 1, transformOrigin: 'left center', ease: 'none',
  scrollTrigger: { trigger: 'body', start: 'top top', end: 'bottom bottom', scrub: true }
});

// Section labels
const sections = document.querySelectorAll('[data-section]');
sections.forEach(section => {
  ScrollTrigger.create({
    trigger: section, start: 'top center', end: 'bottom center',
    onEnter: () => highlightNav(section.dataset.section),
    onEnterBack: () => highlightNav(section.dataset.section)
  });
});
```

## When to Use
- Long scrolling pages (5+ sections)
- Storytelling/narrative pages
- Portfolio with multiple chapters
