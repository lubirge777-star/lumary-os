# Experience 019: The Gradient Shift

## Classification: Narrative
## Emotion: Calm → Immersion
## Difficulty: ★★☆☆☆
## Performance: Low
## Libraries: GSAP ScrollTrigger

## Description
A background gradient that slowly shifts colors as the user scrolls through sections. Each section has a corresponding gradient variation that subtly transitions into the next. Creates a cohesive, flowing visual journey.

## Code
```javascript
const gradientColors = [
  ['#0F172A', '#1E293B'],  // Section 1
  ['#1A0F0A', '#2D1810'],  // Section 2
  ['#0F172A', '#1A1A2E'],  // Section 3
  ['#0A1F14', '#0D2818'],  // Section 4
];

const sections = document.querySelectorAll('[data-gradient]');
sections.forEach((section, i) => {
  const next = gradientColors[Math.min(i + 1, gradientColors.length - 1)];
  ScrollTrigger.create({
    trigger: section, start: 'top bottom', end: 'bottom top',
    onUpdate: (self) => {
      const progress = self.progress;
      const current = gradientColors[i];
      const bg = `linear-gradient(135deg, 
        ${lerpColor(current[0], next[0], progress)}, 
        ${lerpColor(current[1], next[1], progress)})`;
      section.style.background = bg;
    }
  });
});

function lerpColor(a, b, t) {
  const ah = parseInt(a.replace('#',''), 16), bh = parseInt(b.replace('#',''), 16);
  const rr = Math.round(((ah >> 16) * (1 - t) + (bh >> 16) * t));
  const gg = Math.round((((ah >> 8) & 0xFF) * (1 - t)) + (((bh >> 8) & 0xFF) * t));
  const bb = Math.round(((ah & 0xFF) * (1 - t)) + ((bh & 0xFF) * t));
  return `rgb(${rr},${gg},${bb})`;
}
```

## When to Use
- Long-form storytelling pages
- Brand narratives
- Portfolio journeys
- Any single-page scroll experience
