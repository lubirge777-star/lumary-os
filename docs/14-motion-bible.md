# Motion Bible

## Version 1.0

---

## Philosophy

The Motion Bible is the comprehensive reference for all animation patterns used across Lumary Studio projects.

It is separate from the Motion Language (07) because the Bible grows with every project. While the Language defines *philosophy and rules*, the Bible catalogs *specific implementations*.

Every entry in this Bible includes: a use case, GSAP code, duration, easing, and anti-pattern notes.

---

## Entry Format

```
## Entry ###: [Name]

### Classification
[Guide / Feedback / Narrative]

### Emotion
[Trust, Excitement, Calm, Curiosity, Urgency]

### Difficulty
★☆☆☆☆ to ★★★★★

### Performance Impact
[Low / Medium / High]

### Libraries
[GSAP, Lenis, ScrollTrigger, etc.]

### Timing
Duration: [Xms]
Easing: [PowerX.out]
Stagger: [Xms per item] (if applicable)
Delay: [Xms] (if applicable)

### Code
```javascript
// GSAP timeline
```

### When to Use
- Scenario 1
- Scenario 2

### When Not to Use
- Scenario 1
- Scenario 2

### Accessibility
- respects prefers-reduced-motion
- [other notes]
```

---

## Entry 001: The Awakening

**Classification:** Narrative
**Emotion:** Curiosity
**Difficulty:** ★★★★☆
**Performance:** Medium
**Libraries:** GSAP, Lenis

### Description
A cinematic hero reveal where content enters in a carefully choreographed sequence: background first (slow zoom or parallax), then heading (letter-by-letter or word-by-word), then subtext, then CTA. Creates a sense of anticipation and importance.

### Timing
| Element | Start | Duration | Ease |
|---|---|---|---|
| Background | 0ms | 2000ms | Power4.out |
| Heading | 500ms | 1000ms | Power3.out |
| Subtext | 1200ms | 800ms | Power2.out |
| CTA | 1800ms | 600ms | Power2.out |
| Decorative | 600ms | 1200ms | Power4.out |

### Code
```javascript
const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });

tl.fromTo('.hero-bg', 
  { scale: 1.1, opacity: 0 },
  { scale: 1, opacity: 1, duration: 2, ease: 'power4.out' }
)
.fromTo('.hero-heading .word',
  { y: 60, opacity: 0 },
  { y: 0, opacity: 1, duration: 1, stagger: 0.08 },
  '-=0.5'
)
.fromTo('.hero-subtext',
  { y: 30, opacity: 0 },
  { y: 0, opacity: 1, duration: 0.8 },
  '-=0.3'
)
.fromTo('.hero-cta',
  { y: 20, opacity: 0 },
  { y: 0, opacity: 1, duration: 0.6 },
  '-=0.2'
);
```

### When to Use
- Premium brand hero sections
- Luxury real estate listings
- Studio portfolios
- Product launches

### When Not to Use
- Information-heavy landing pages (too slow)
- Low-bandwidth target audience
- When hero must be immediately scannable

### Accessibility
- Entire sequence disabled if `prefers-reduced-motion`
- Content is fully visible without animation

---

## Entry 002: The Cascade

**Classification:** Guide
**Emotion:** Trust
**Difficulty:** ★★☆☆☆
**Performance:** Low
**Libraries:** GSAP ScrollTrigger

### Description
Cards or elements enter sequentially as the user scrolls. Each card fades in and translates up slightly. The stagger creates a controlled, organized feel.

### Timing
| Parameter | Value |
|---|---|
| Duration per item | 600ms |
| Stagger | 100ms |
| Ease | Power2.out |
| ScrollTrigger start | "top 85%" |

### Code
```javascript
gsap.fromTo('.card',
  { y: 60, opacity: 0 },
  { 
    y: 0, 
    opacity: 1, 
    duration: 0.6, 
    stagger: 0.1,
    ease: 'power2.out',
    scrollTrigger: {
      trigger: '.cards-grid',
      start: 'top 85%',
      toggleActions: 'play none none reverse'
    }
  }
);
```

### When to Use
- Services section
- Features grid
- Team members
- Portfolio items

### Accessibility
- Items are visible without animation

---

## Entry 003: The Reveal

**Classification:** Narrative
**Emotion:** Curiosity
**Difficulty:** ★★★☆☆
**Performance:** Low
**Libraries:** GSAP ScrollTrigger

### Description
Content (images or text blocks) are initially clipped and reveal themselves as they enter the viewport. Often combined with a slight upward movement.

### Code
```javascript
// Image reveal with clip
gsap.fromTo('.image-reveal',
  { clipPath: 'inset(0 100% 0 0)' },
  {
    clipPath: 'inset(0 0% 0 0)',
    duration: 1.2,
    ease: 'power4.out',
    scrollTrigger: {
      trigger: '.image-reveal',
      start: 'top 80%'
    }
  }
);
```

---

## Entry 004: The Counter

**Classification:** Guide
**Emotion:** Trust, Excitement
**Difficulty:** ★☆☆☆☆
**Performance:** Low
**Libraries:** GSAP ScrollTrigger

### Description
Numbers animate from 0 to their final value as the section scrolls into view. Validates claims of scale (years, projects, clients) with visual proof.

### Code
```javascript
function animateCounter(element, target, suffix = '') {
  const obj = { val: 0 };
  gsap.to(obj, {
    val: target,
    duration: 2,
    ease: 'power3.out',
    scrollTrigger: {
      trigger: element,
      start: 'top 85%'
    },
    onUpdate: () => {
      element.textContent = Math.floor(obj.val) + suffix;
    }
  });
}

animateCounter(document.querySelector('.stat-projects'), 247, '+');
```

---

## Entry 005: The Float

**Classification:** Guide
**Emotion:** Calm
**Difficulty:** ★☆☆☆☆
**Performance:** Low
**Libraries:** GSAP

### Description
A subtle, continuous floating animation (y-axis oscillation) on decorative or secondary elements. Creates a feeling of lightness and polish.

### Code
```javascript
gsap.to('.float-element', {
  y: -8,
  duration: 2.5,
  ease: 'sine.inOut',
  yoyo: true,
  repeat: -1
});
```

---

## Entry 006: The Parallax Depth

**Classification:** Narrative
**Emotion:** Immersion
**Difficulty:** ★★★★☆
**Performance:** Medium
**Libraries:** GSAP ScrollTrigger

### Description
Multiple layers move at different speeds as the user scrolls, creating a 3D depth effect. Foreground moves faster than background.

### Code
```javascript
// Three layers with different speeds
const layers = [
  { selector: '.parallax-back', speed: 0.2 },
  { selector: '.parallax-mid', speed: 0.5 },
  { selector: '.parallax-front', speed: 0.8 }
];

layers.forEach(({ selector, speed }) => {
  gsap.to(selector, {
    y: () => window.innerHeight * speed * 0.3,
    ease: 'none',
    scrollTrigger: {
      trigger: '.parallax-container',
      scrub: true
    }
  });
});
```

---

## Entry 007: The Magnetic Button

**Classification:** Feedback
**Emotion:** Delight
**Difficulty:** ★★★★☆
**Performance:** Low
**Libraries:** GSAP

### Description
Button subtly follows the cursor position when hovered, creating a magnetic effect. Returns to position on leave.

### Code
```javascript
const btn = document.querySelector('.magnetic-btn');

btn.addEventListener('mousemove', (e) => {
  const rect = btn.getBoundingClientRect();
  const x = (e.clientX - rect.left - rect.width / 2) * 0.3;
  const y = (e.clientY - rect.top - rect.height / 2) * 0.3;
  
  gsap.to(btn, { x, y, duration: 0.3, ease: 'power2.out' });
});

btn.addEventListener('mouseleave', () => {
  gsap.to(btn, { x: 0, y: 0, duration: 0.5, ease: 'power3.out' });
});
```

---

## Entry 008: The Progress Line

**Classification:** Guide
**Emotion:** Trust
**Difficulty:** ★★☆☆☆
**Performance:** Low
**Libraries:** GSAP ScrollTrigger

### Description
A horizontal line at the top of the viewport fills from 0% to 100% as the user scrolls through a section. Provides visual progress feedback.

### Code
```javascript
gsap.to('.progress-line', {
  scaleX: 1,
  transformOrigin: 'left center',
  ease: 'none',
  scrollTrigger: {
    trigger: 'body',
    start: 'top top',
    end: 'bottom bottom',
    scrub: true
  }
});
```

---

## Entry 009: The Stagger Grid

**Classification:** Guide
**Emotion:** Curiosity
**Difficulty:** ★★☆☆☆
**Performance:** Medium
**Libraries:** GSAP ScrollTrigger

### Description
A grid of items enters in a wave pattern — starting from the top-left, cascading diagonally to bottom-right. Each item fades in with a slight scale-up.

### Code
```javascript
gsap.fromTo('.grid-item', 
  { y: 40, opacity: 0, scale: 0.95 },
  {
    y: 0,
    opacity: 1,
    scale: 1,
    duration: 0.6,
    stagger: {
      grid: 'auto',
      from: 'top-left',
      amount: 0.8
    },
    ease: 'power2.out',
    scrollTrigger: {
      trigger: '.grid-container',
      start: 'top 85%'
    }
  }
);
```

---

## Entry 010: The Signature Moment

**Classification:** Narrative
**Emotion:** Excitement
**Difficulty:** ★★★★★
**Performance:** High
**Libraries:** GSAP, Lenis, SplitType

### Description
A full, multi-layered reveal triggered when a specific section enters the viewport. Combines text splitting, parallax, color shifts, and particle-like decorative elements. The most premium experience in our arsenal.

### Code
```javascript
// Complex timeline combining multiple techniques
const sigTl = gsap.timeline({
  scrollTrigger: {
    trigger: '.signature-section',
    start: 'top center',
    toggleActions: 'play none none reverse'
  }
});

// Text split animation
const splitText = new SplitType('.signature-heading', { types: 'lines' });

sigTl
  .fromTo('.signature-bg',
    { scale: 1.2, filter: 'blur(10px)' },
    { scale: 1, filter: 'blur(0px)', duration: 1.5, ease: 'power4.out' }
  )
  .fromTo(splitText.lines,
    { y: 80, opacity: 0 },
    { y: 0, opacity: 1, duration: 1, stagger: 0.15, ease: 'power3.out' },
    '-=0.5'
  )
  .fromTo('.signature-decoration',
    { scale: 0, opacity: 0, rotation: -15 },
    { scale: 1, opacity: 0.6, rotation: 0, duration: 1.2, ease: 'back.out(1.2)' },
    '-=0.8'
  )
  .fromTo('.signature-cta',
    { y: 40, opacity: 0 },
    { y: 0, opacity: 1, duration: 0.8, ease: 'power2.out' },
    '-=0.3'
  );
```

---

## Quick Reference Table

| Entry | Name | Difficulty | Performance | Libraries |
|---|---|---|---|---|
| 001 | The Awakening | ★★★★☆ | Medium | GSAP, Lenis |
| 002 | The Cascade | ★★☆☆☆ | Low | GSAP ScrollTrigger |
| 003 | The Reveal | ★★★☆☆ | Low | GSAP ScrollTrigger |
| 004 | The Counter | ★☆☆☆☆ | Low | GSAP ScrollTrigger |
| 005 | The Float | ★☆☆☆☆ | Low | GSAP |
| 006 | The Parallax Depth | ★★★★☆ | Medium | GSAP ScrollTrigger |
| 007 | The Magnetic Button | ★★★★☆ | Low | GSAP |
| 008 | The Progress Line | ★★☆☆☆ | Low | GSAP ScrollTrigger |
| 009 | The Stagger Grid | ★★☆☆☆ | Medium | GSAP ScrollTrigger |
| 010 | The Signature Moment | ★★★★★ | High | GSAP, Lenis, SplitType |

---

## Checklist

- [ ] Motion chosen matches the Experience Profile (Energy dimension)
- [ ] Entry difficulty is within team capability
- [ ] Performance impact is acceptable for target devices
- [ ] `prefers-reduced-motion` respected
- [ ] Duration and easing follow Motion Language rules
- [ ] Animation serves Guide / Feedback / Narrative purpose
- [ ] Tested at 60fps on target device
- [ ] No layout-triggering properties used (width, height, top, left)

---

## Future Ideas

- Interactive Motion Bible — visual preview of each entry
- Motion search tool — "I need an animation for X purpose"
- Community contributions to the Motion Bible
