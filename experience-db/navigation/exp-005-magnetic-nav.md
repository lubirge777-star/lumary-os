# Experience 005: The Magnetic Navigation

## Classification
Feedback / Guide

## Emotion
Delight → Trust

## Difficulty
★★★☆☆

## Performance
Low

## Libraries
GSAP

---

## Description
Navigation links subtly follow the cursor when hovered, creating a magnetic pull effect. Each link slightly shifts toward the cursor position then springs back on leave. A premium micro-interaction that makes navigation feel alive.

## Implementation
```javascript
document.querySelectorAll('.nav-link').forEach(link => {
  const text = link.querySelector('span');
  
  link.addEventListener('mousemove', (e) => {
    const rect = link.getBoundingClientRect();
    const x = (e.clientX - rect.left - rect.width / 2) * 0.2;
    const y = (e.clientY - rect.top - rect.height / 2) * 0.2;
    
    gsap.to(text, {
      x, y,
      duration: 0.4,
      ease: 'power2.out'
    });
  });
  
  link.addEventListener('mouseleave', () => {
    gsap.to(text, {
      x: 0, y: 0,
      duration: 0.6,
      ease: 'elastic.out(1, 0.3)'
    });
  });
});
```

## When to Use
- Premium brand navigation
- Creative agency headers
- Luxury product sites
- Any site where navigation is a design focal point

## Anti-Patterns
- Applying to mobile navigation (touch has no hover)
- Too much movement (keep shift < 15px)
- Conflicting with link click area

## Accessibility
- Only visual movement — click target remains unchanged
- `prefers-reduced-motion` disables entirely
- Keyboard users unaffected (they see focus state instead)
