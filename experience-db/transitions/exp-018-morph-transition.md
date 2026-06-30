# Experience 018: The Morph Transition

## Classification: Narrative
## Emotion: Awe
## Difficulty: ★★★★★
## Performance: Medium
## Libraries: GSAP, barba.js (or custom)

## Description
A geometric shape (circle, square, or custom SVG) expands from the click/tap point, covering the current page and revealing the next page underneath. The shape "morphs" from one state to another. Premium, app-like feel.

## Code
```javascript
function morphTransition(e) {
  const morph = document.createElement('div');
  morph.className = 'morph-overlay fixed inset-0 z-[9999] pointer-events-none';
  morph.style.cssText = `
    clip-path: circle(0% at ${e.clientX || window.innerWidth/2}px ${e.clientY || window.innerHeight/2}px);
    background: var(--color-accent);
    transition: clip-path 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  `;
  document.body.appendChild(morph);
  
  requestAnimationFrame(() => {
    morph.style.clipPath = 'circle(150% at 50% 50%)';
  });
  
  setTimeout(() => {
    // Load new page content
    morph.style.clipPath = 'circle(0% at 50% 50%)';
    setTimeout(() => morph.remove(), 600);
  }, 800);
}
```

## When to Use
- Premium agency sites
- Portfolio navigation
- Luxury brand experiences
- Product launch pages

## Anti-Patterns
- Performance impact on mobile
- Motion sickness for some users
- Over-engineering for simple sites
