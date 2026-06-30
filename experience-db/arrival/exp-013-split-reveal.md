# Experience 013: The Split Reveal

## Classification: Narrative
## Emotion: Drama → Focus
## Difficulty: ★★★☆☆
## Performance: Low
## Libraries: GSAP, SplitType

## Description
The hero heading splits into two parts that enter from opposite directions (left and right), meeting in the center. Creates a dramatic, memorable first impression.

## Code
```javascript
const tl = gsap.timeline();
tl.fromTo('.hero-line-left', { x: -200, opacity: 0 }, { x: 0, opacity: 1, duration: 1, ease: 'power4.out' })
  .fromTo('.hero-line-right', { x: 200, opacity: 0 }, { x: 0, opacity: 1, duration: 1, ease: 'power4.out' }, '-=0.6')
  .fromTo('.hero-sub', { y: 30, opacity: 0 }, { y: 0, opacity: 1, duration: 0.6 }, '-=0.3');
```

## When to Use
- Brand hero with two-part name/tagline
- Split layout hero sections
- Luxury real estate (exclusive + properties)
