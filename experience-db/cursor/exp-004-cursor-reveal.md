# Experience 004: The Cursor Reveal

## Classification
Feedback

## Emotion
Delight

## Difficulty
★★★★☆

## Performance
Low

## Libraries
GSAP

---

## Description
A custom cursor that reveals hidden content as it moves. When the cursor hovers over images, the cursor itself acts as a "spotlight" or "lens" revealing what's underneath. Premium effect for portfolios and creative sites.

## Implementation
```html
<style>
.custom-cursor {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  position: fixed;
  pointer-events: none;
  z-index: 9999;
  mix-blend-mode: difference;
  background: white;
  transform: translate(-50%, -50%);
  transition: width 0.3s, height 0.3s, background 0.3s;
}
.custom-cursor.hovering {
  width: 160px;
  height: 160px;
  background: transparent;
  border: 2px solid white;
}
</style>

<div class="custom-cursor" id="cursor"></div>

<script>
const cursor = document.getElementById('cursor');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!reducedMotion) {
  document.body.style.cursor = 'none';
  
  document.addEventListener('mousemove', (e) => {
    gsap.to(cursor, {
      x: e.clientX,
      y: e.clientY,
      duration: 0.3,
      ease: 'power2.out'
    });
  });
  
  document.querySelectorAll('[data-cursor-hover]').forEach(el => {
    el.addEventListener('mouseenter', () => cursor.classList.add('hovering'));
    el.addEventListener('mouseleave', () => cursor.classList.remove('hovering'));
  });
}
</script>
```

## When to Use
- Creative agency portfolios
- Photography showcases
- Luxury brand landing pages
- Artistic galleries

## When NOT to Use
- Content-heavy sites (distracting)
- E-commerce (interferes with clicking)
- Enterprise/B2B sites (unprofessional)
- Mobile-only experiences

## Accessibility
- `cursor: none` only applied when NOT `prefers-reduced-motion`
- All interactive elements still show default cursor on hover
- Touch devices unaffected
