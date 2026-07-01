# Experience 049: Card Stack Fan Reveal

## Classification
Narrative

## Emotion
Curiosity → Engagement

## Difficulty
★★★★☆

## Performance Impact
Medium

## Libraries
GSAP, ScrollTrigger

---

## Description

A stack of cards fans out as the user scrolls, revealing each card beneath. Starting as a compact pile, each card rotates and translates to its position as the scroll progresses. Creates a physical, tactile reveal that feels like riffling through a deck.

Use for portfolio showcases, team member cards, product collections, or any set of items where sequential reveal adds dramatic value.

---

## Timeline

| Moment | Scroll Position | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0% | All cards | Stacked at center, small rotation offsets | 0ms | — |
| 2 | 0%-20% | Card 1 | Fan to position (rotate + translate) | viewport/5 | Power3.out |
| 3 | 20%-40% | Card 2 | Fan to position | viewport/5 | Power3.out |
| 4 | 40%-60% | Card 3 | Fan to position | viewport/5 | Power3.out |
| 5 | 60%-80% | Card 4 | Fan to position | viewport/5 | Power3.out |
| 6 | 80%-100% | Card 5 | Fan to position | viewport/5 | Power3.out |

---

## Psychology

- **Physical Metaphor:** The deck-of-cards metaphor is universally understood — users instinctively know this is a collection.
- **Sequential Curiosity:** Each revealed card creates anticipation for the next — "What's underneath?"
- **Collection Value:** Presenting items as a stack implies a curated set, increasing perceived value of each item.

---

## Implementation

```html
<section class="card-stack-section" style="height: 500vh; position: relative; display: flex; align-items: center; justify-content: center;">
  <div class="card-stack" style="position: sticky; top: 50%; transform: translateY(-50%); width: 320px; height: 420px;">
    <div class="stack-card" style="position: absolute; inset: 0; border-radius: 20px; background: linear-gradient(135deg, #6c5ce7, #a29bfe); display: flex; align-items: center; justify-content: center; color: white; font-family: system-ui; font-size: 1.5rem; font-weight: 700; box-shadow: 0 10px 40px rgba(0,0,0,0.3); transform-origin: center bottom;">
      Card 1
    </div>
    <div class="stack-card" style="position: absolute; inset: 0; border-radius: 20px; background: linear-gradient(135deg, #e17055, #fdcb6e); display: flex; align-items: center; justify-content: center; color: white; font-family: system-ui; font-size: 1.5rem; font-weight: 700; box-shadow: 0 10px 40px rgba(0,0,0,0.3); transform-origin: center bottom;">
      Card 2
    </div>
    <div class="stack-card" style="position: absolute; inset: 0; border-radius: 20px; background: linear-gradient(135deg, #00b894, #55efc4); display: flex; align-items: center; justify-content: center; color: white; font-family: system-ui; font-size: 1.5rem; font-weight: 700; box-shadow: 0 10px 40px rgba(0,0,0,0.3); transform-origin: center bottom;">
      Card 3
    </div>
    <div class="stack-card" style="position: absolute; inset: 0; border-radius: 20px; background: linear-gradient(135deg, #0984e3, #74b9ff); display: flex; align-items: center; justify-content: center; color: white; font-family: system-ui; font-size: 1.5rem; font-weight: 700; box-shadow: 0 10px 40px rgba(0,0,0,0.3); transform-origin: center bottom;">
      Card 4
    </div>
    <div class="stack-card" style="position: absolute; inset: 0; border-radius: 20px; background: linear-gradient(135deg, #fd79a8, #e84393); display: flex; align-items: center; justify-content: center; color: white; font-family: system-ui; font-size: 1.5rem; font-weight: 700; box-shadow: 0 10px 40px rgba(0,0,0,0.3); transform-origin: center bottom;">
      Card 5
    </div>
  </div>
</section>
```

```javascript
gsap.registerPlugin(ScrollTrigger);

const cards = document.querySelectorAll('.stack-card');
const totalCards = cards.length;

cards.forEach((card, index) => {
  const progressStart = index / totalCards;
  const progressEnd = (index + 1) / totalCards;

  gsap.set(card, {
    rotation: gsap.utils.random(-3, 3),
    y: gsap.utils.random(-5, 5)
  });

  ScrollTrigger.create({
    trigger: '.card-stack-section',
    start: 'top top',
    end: 'bottom bottom',
    scrub: 1,
    onUpdate: (self) => {
      const progress = self.progress;

      if (progress >= progressStart && progress <= progressEnd) {
        const localProgress = (progress - progressStart) / (progressEnd - progressStart);
        const eased = gsap.parseEase('power3.out')(localProgress);

        const angle = (index - (totalCards - 1) / 2) * 4;
        const yOffset = index * -20;

        gsap.set(card, {
          rotation: angle * eased,
          y: yOffset * eased,
          z: index * -10,
          opacity: 0.6 + 0.4 * eased
        });
      } else if (progress > progressEnd) {
        const angle = (index - (totalCards - 1) / 2) * 4;
        const yOffset = index * -20;

        gsap.set(card, {
          rotation: angle,
          y: yOffset,
          z: index * -10,
          opacity: 1
        });
      } else {
        gsap.set(card, {
          rotation: gsap.utils.random(-3, 3),
          y: gsap.utils.random(-5, 5),
          z: 0,
          opacity: 0.7
        });
      }
    }
  });
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Creative Agency | ★★★★★ | Portfolio pieces |
| E-commerce | ★★★★☆ | Product line reveal |
| Technology | ★★★★☆ | Feature stack |
| Gaming | ★★★★★ | Character/ability cards |
| Education | ★★★☆☆ | Course modules |

---

## Accessibility Notes

- Content of each card must be accessible without the fan animation
- `prefers-reduced-motion: reduce` — show cards in a vertical list, stacked normally
- Cards should have focusable content for keyboard users
- Ensure z-index ordering makes all cards hoverable/clickable after fan-out

---

## Performance Notes

- Uses `gsap.set` on scroll update (no `.to()` per frame) — optimized
- Only `rotation`, `y`, `z` (translateZ), and `opacity` — all composited
- For > 8 cards, consider reducing `totalCards` or using canvas render
- Manual scrub approach avoids ScrollTrigger tween overhead

---

## Variants

### Variant A: Horizontal Fan
Cards fan out horizontally (like a hand of playing cards) instead of vertically.

### Variant B: Click-to-Fan
Clicking a button reveals the next card — scroll-independent, good for mobile.

### Variant C: 3D Carousel Fan
Cards fan in 3D space with perspective, creating a more dramatic depth effect.

---

## Anti-Patterns

- More than 8 cards — too much scroll distance required
- Cards overlapping interactive content — ensure CTAs are accessible after fan
- All cards fanning simultaneously — destroys the sequential reveal magic
- No container overflow handling — cards clip at section boundaries

---

## Checklist

- [ ] Card count ≤ 8
- [ ] Initial stack position set with `gsap.set()`
- [ ] Reduced motion: vertical list
- [ ] Cards clickable after fan-out
- [ ] z-index managed properly (last card on top)
- [ ] Scroll section height correctly calculated (totalCards * 100vh)
