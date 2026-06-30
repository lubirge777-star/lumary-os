# Experience 002: The Scroll Story

## Classification
Narrative

## Emotion
Curiosity → Satisfaction

## Difficulty
★★★☆☆

## Performance Impact
Medium

## Libraries
GSAP ScrollTrigger, Lenis

---

## Description

The Scroll Story transforms a page into a narrative journey. As the user scrolls, content reveals in sequence, images animate, and the story unfolds at the user's own pace.

Unlike The Awakening (which plays automatically), The Scroll Story is user-controlled. The visitor decides when the next chapter begins by scrolling.

---

## Timeline Structure

```
┌─────────────────────────────────────┐
│  Chapter 1: The Hook                │
│  Hero section with strong headline  │
│  ↓ Scroll                           │
├─────────────────────────────────────┤
│  Chapter 2: The Problem             │
│  Text reveals + supporting visuals  │
│  ↓ Scroll                           │
├─────────────────────────────────────┤
│  Chapter 3: The Solution            │
│  Service cards cascade in           │
│  ↓ Scroll                           │
├─────────────────────────────────────┤
│  Chapter 4: The Proof               │
│  Counters animate, gallery reveals  │
│  ↓ Scroll                           │
├─────────────────────────────────────┤
│  Chapter 5: The Action              │
│  CTA section with final reveal      │
└─────────────────────────────────────┘
```

---

## Psychology

- **Zeigarnik Effect:** Each incomplete chapter creates tension that drives scrolling.
- **Cognitive Fluency:** Sequential reveals reduce cognitive load — user processes one thing at a time.
- **Sense of Progress:** Visual feedback (progress bar or chapter indicator) creates accomplishment.

---

## Implementation

### Section Reveal (Standard)
```javascript
// Base reveal for any section
gsap.fromTo('.section-content',
  { y: 60, opacity: 0 },
  {
    y: 0,
    opacity: 1,
    duration: 0.8,
    ease: 'power3.out',
    scrollTrigger: {
      trigger: '.section',
      start: 'top 85%',
      toggleActions: 'play none none reverse'
    }
  }
);
```

### Gallery with Scroll Progress
```javascript
// Images reveal as user scrolls through gallery
const galleryItems = document.querySelectorAll('.gallery-item');

galleryItems.forEach((item, i) => {
  gsap.fromTo(item,
    { y: 40, opacity: 0 },
    {
      y: 0,
      opacity: 1,
      duration: 0.6,
      delay: i * 0.15,
      scrollTrigger: {
        trigger: item,
        start: 'top 90%',
        toggleActions: 'play none none reverse'
      }
    }
  );
});
```

### Chapter Transitions
```javascript
// Each chapter gets a unique reveal style
const chapters = document.querySelectorAll('.chapter');

chapters.forEach((chapter, i) => {
  const style = i % 2 === 0 ? 'left' : 'right';
  
  gsap.fromTo(chapter.querySelector('.chapter-content'),
    { x: style === 'left' ? -60 : 60, opacity: 0 },
    {
      x: 0,
      opacity: 1,
      duration: 1,
      ease: 'power4.out',
      scrollTrigger: {
        trigger: chapter,
        start: 'top 80%'
      }
    }
  );
});
```

---

## Key Considerations

| Factor | Recommendation |
|---|---|
| Number of chapters | 4-6 maximum |
| ScrollTrigger start | `top 85%` or `top 90%` |
| Duration per reveal | 600-1000ms |
| Easing | Power3.out for reveals |
| Performance | Preload images, lazy-load sections |

---

## Industries

| Industry | Fit |
|---|---|
| Creative Studio | ★★★★★ |
| Construction | ★★★★☆ |
| Real Estate | ★★★★★ |
| Non-Profit | ★★★★★ |
| Education | ★★★★☆ |
| SaaS | ★★★☆☆ |
| E-commerce | ★★☆☆☆ |

---

## Accessibility

- `prefers-reduced-motion` disables all scroll reveals
- Content is fully visible without any scroll-triggered animation
- Focus management: when scrolling to a new chapter, ensure proper heading hierarchy

---

## Variants

### Variant A: Timeline Scroll
Chapters arranged horizontally on a timeline. Best for company history or project process.

### Variant B: Parallax Story
Each chapter has a parallax background that moves at a different speed from the content.

### Variant C: Minimal Scroll
Simple fade-in reveals with no parallax or complex transitions. Best for content-heavy pages.

---

## Anti-Patterns

- **Over-animation:** More than 6 animated elements per section causes cognitive overload.
- **Too slow:** ScrollTrigger starting at `top 95%` means user has already passed the element before it reveals.
- **Identical reveals:** Each chapter should feel slightly different in its reveal style.
- **No visual progress:** User should know how far they are in the story.
- **Auto-scrolling:** Never force the user to watch an animation — let them control scroll speed.

---

## Checklist

- [ ] 4-6 chapters with logical narrative progression
- [ ] Each chapter has a unique reveal style
- [ ] ScrollTrigger start at `top 85%` or later
- [ ] Progress indicator visible (scrollbar, progress bar, or chapter marker)
- [ ] All content accessible without JavaScript
- [ ] `prefers-reduced-motion` respected
- [ ] Tested on mobile (touch scrolling)
- [ ] Performance: Lighthouse 90+
