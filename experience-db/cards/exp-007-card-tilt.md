# Experience 007: The Tilt Card

## Classification
Feedback

## Emotion
Delight

## Difficulty
★★★☆☆

## Performance
Low

## Libraries
GSAP

---

## Description
Cards tilt in 3D space following the cursor position, creating a tactile, physical feel. Combined with dynamic shadow and glare effect for maximum premium aesthetic.

## Implementation
```javascript
document.querySelectorAll('.tilt-card').forEach(card => {
  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width - 0.5;
    const y = (e.clientY - rect.top) / rect.height - 0.5;
    
    gsap.to(card, {
      rotateX: y * -10,
      rotateY: x * 10,
      transformPerspective: 1000,
      duration: 0.4,
      ease: 'power2.out'
    });
  });
  
  card.addEventListener('mouseleave', () => {
    gsap.to(card, {
      rotateX: 0,
      rotateY: 0,
      duration: 0.6,
      ease: 'power3.out'
    });
  });
});
```

## CSS Enhancement
```css
.tilt-card {
  transform-style: preserve-3d;
  will-change: transform;
}
.tilt-card-content {
  transform: translateZ(20px);
}
.tilt-card-glare {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, transparent 50%);
  pointer-events: none;
  border-radius: inherit;
}
```

## When to Use
- Premium service cards
- Team member profiles
- Product showcases
- Portfolio items

## Anti-Patterns
- Tilt on entire page sections (causes motion sickness)
- Mobile devices (no hover/tilt — use static)
- `prefers-reduced-motion` (disable entirely)

## Performance Note
- Uses GPU-accelerated transforms
- `will-change: transform` for compositor optimization
- No layout thrashing (only compositor properties)
