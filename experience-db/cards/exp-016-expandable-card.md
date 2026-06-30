# Experience 016: The Expandable Card

## Classification: Feedback
## Emotion: Curiosity → Satisfaction
## Difficulty: ★★★☆☆
## Performance: Low
## Libraries: GSAP

## Description
A card grid where clicking a card expands it to reveal more content while others shrink. Creates an accordion-like experience with smooth height/width transitions.

## Code
```javascript
document.querySelectorAll('.expand-card').forEach(card => {
  card.addEventListener('click', () => {
    const isActive = card.classList.contains('active');
    document.querySelectorAll('.expand-card').forEach(c => {
      gsap.to(c, { flex: c === card && !isActive ? 3 : 1, duration: 0.5, ease: 'power3.inOut' });
      c.classList.toggle('active', c === card && !isActive);
    });
  });
});
```

## When to Use
- Service showcase with detailed descriptions
- Case study previews
- Team member bios
- FAQ with expandable answers

## CSS
```css
.expand-card { flex: 1; transition: flex 0.5s cubic-bezier(0.4, 0, 0.2, 1); }
.expand-card.active { flex: 3; }
.expand-card .extra-content { display: none; }
.expand-card.active .extra-content { display: block; }
```
