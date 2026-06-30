# Motion Language

## Version 1.0

---

## Motion Philosophy

Motion is physics for the digital world.

When elements move with the same physics as the physical world, the brain accepts them as real. When they teleport, snap, or behave unpredictably, the experience feels broken — even if the user cannot articulate why.

Every animation must serve one of three purposes:
- **Guide** — direct attention
- **Feedback** — confirm interaction
- **Narrative** — reveal story

If an animation does none of these, remove it.

---

## Easing Curves

Easing is the single most important motion parameter. It defines the *personality* of the movement.

### Standard Easing

```
Power2.out    — Default for UI elements (cards, buttons, modals)
Power3.out    — Sections, reveals, hero animations
Power4.out    — Large cinematic transitions
```

### Easing Use Cases

| Context | Easing | Duration | Effect |
|---|---|---|---|
| Button hover | Power1.out | 150ms | Quick, responsive |
| Card hover | Power2.out | 300ms | Smooth lift |
| Section reveal | Power3.out | 600-800ms | Elegant entry |
| Hero text reveal | Power4.out | 800-1000ms | Cinematic |
| Page transition | Power4.inOut | 600-1200ms | Seamless |
| Loading animation | Custom ease | 1000-2000ms | Engaging |
| Stagger children | Power2.out | 50-100ms stagger | Sequential flow |

### Do Not Use

- Bounce (except entertainment contexts)
- Elastic (hurts readability)
- Linear (feels robotic)
- Extreme overshoot (feels aggressive)

---

## Duration

| Element | Duration |
|---|---|
| Hover state change | 150-200ms |
| Micro-interaction | 200-300ms |
| Card reveal | 400-600ms |
| Section entry | 600-800ms |
| Hero reveal (staggered) | 800-1200ms total |
| Page transition | 600-1200ms |
| Loading sequence | 1000-3000ms |

**Rule:** Shorter for functional elements, longer for emotional ones.

---

## Staggered Reveals

Staggering is one of the most powerful tools for creating premium feel.

### The Hierarchy Rule

Elements within a group should stagger in order of importance:

1. Heading (enters first — sets context)
2. Body text (enters second — provides information)
3. Image / visual (enters third — confirms message)
4. CTA (enters last — invites action)

### Stagger Timing

| Element Count | Stagger Delay | Total Duration |
|---|---|---|
| 3 items | 80ms | ~240ms |
| 4 items | 80ms | ~320ms |
| 6 items | 60ms | ~360ms |
| 12 items | 40ms | ~480ms |

---

## Scroll-Triggered Animation

Use GSAP ScrollTrigger for all scroll-based animations.

### Category 1: Reveal

Elements fade + translate up as they enter the viewport.

**Spec:**
```
opacity: 0 → 1
y: 60 → 0
duration: 0.7s
ease: Power3.out
start: "top 85%"
```

### Category 2: Parallax

Background or decorative elements move slower than the scroll speed.

**Spec:**
```
y: (scroll amount * 0.3)
ease: none (scrub: true)
```

### Category 3: Progress

A bar or indicator fills as the user scrolls through content.

**Spec:**
```
scaleX: 0 → 1
ease: none (scrub: true)
```

### Category 4: Pin

An element stays fixed while content scrolls past it.

**Spec:**
```
pin: true
anticipatePin: 1
```

---

## Micro-Interactions

### Button

```
onHover:
  scale: 1.02
  duration: 150ms
  ease: Power1.out

onClick:
  scale: 0.97 → 1
  duration: 100ms → 150ms
  ease: Power1.out
```

### Card

```
onHover:
  y: -8
  shadow: sm → md
  duration: 300ms
  ease: Power2.out

onLeave:
  reverse
  duration: 250ms
```

### Link / Nav Item

```
onHover:
  color: accent (or underline expand)
  duration: 200ms

Active:
  color: accent + bottom indicator
```

---

## Loading States

### Page Load

- Show skeleton or branded loader if > 500ms
- Transition loader out with fade + scale (500ms)
- Reveal content with staggered entry

### Button Loading

- Replace text with spinner
- Disable interaction
- Duration: match actual request time
- On success: brief checkmark (300ms) before reverting
- On error: shake animation (300ms) + error message

---

## Transition Guide

### Same-Page Section Transition

No transition between sections. Sections reveal on scroll via ScrollTrigger.

### Page-to-Page (Multi-Page Sites)

**Recommended:** 600ms fade + translate up on exit, 600ms fade + translate up on enter.

Using barba.js or simple JS page transitions.

### Modal / Overlay

```
Enter:
  backdrop: fade in 300ms
  modal: scale 0.95→1 + fade 400ms, Power3.out

Exit:
  backdrop: fade out 200ms
  modal: scale 0.95 + fade 200ms, Power2.in
```

---

## Anti-Patterns

| Anti-Pattern | Why |
|---|---|
| Linear easing everywhere | Feels robotic, unnatural |
| 2000ms hero animation | User waits too long to see content |
| Animating everything on the page | Overwhelming, slows performance |
| Bounce on UI elements | Distracting, unprofessional |
| No reduced-motion support | Excludes users with vestibular disorders |
| Layout-animating properties (width, height, top) | Causes layout thrashing, poor performance |
| All animations identical | Predictable = boring after 2 sections |

---

## Reduced Motion

All animations must respect `prefers-reduced-motion: reduce`.

**Implementation:**
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

**JS fallback:**
```javascript
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!reducedMotion) {
  // initialize GSAP animations
}
```

---

## GSAP Best Practices

| Practice | Why |
|---|---|
| Use timelines for sequenced animations | Clear ordering, easy control |
| Kill tweens before component unmount | Prevents memory leaks |
| Use `will-change` sparingly | Only on elements that animate frequently |
| Batch DOM reads/writes | Avoid forced reflow |
| Prefer transforms over layout properties | GPU-accelerated, 60fps |

---

## Checklist

- [ ] All animations serve Guide / Feedback / Narrative
- [ ] Easing curves chosen with purpose
- [ ] Durations follow the spec (150ms hover — 1200ms hero)
- [ ] Stagger order follows Hierarchy Rule
- [ ] ScrollTrigger used for section reveals
- [ ] Micro-interactions defined for buttons, cards, links
- [ ] Loading states designed
- [ ] Page transitions planned
- [ ] reduced-motion media query implemented
- [ ] GSAP best practices followed
- [ ] No animation exceeds 3s total duration

---

## Future Ideas

- Motion Bible (separate file) with 100+ GSAP snippet recipes
- Interactive easing curve explorer for the team
- "Motion audit" tool that analyzes a page and reports animation performance
