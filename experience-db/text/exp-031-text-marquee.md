# Experience 031: Infinite Scrolling Marquee Text

## Classification
Narrative

## Emotion
Energy → Dynamism

## Difficulty
★★☆☆☆

## Performance Impact
Medium

## Libraries
GSAP

---

## Description

An infinite horizontal scrolling marquee that loops seamlessly. Text scrolls continuously in one direction, creating a sense of motion, urgency, or brand energy. Often used in tech websites, event pages, and creative portfolios.

The effect duplicates the text content to create a seamless loop, then animates the `x` position. When one instance scrolls past the viewport, it snaps back to the start without a visible seam.

---

## Timeline

| Moment | Time | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0ms | Marquee track | Start scrolling left | infinite | Linear (none) |
| 2 | loop-end | Duplicate | Snap back to start | 0ms | — |

---

## Psychology

- **Kinetic Energy:** Moving text subconsciously suggests activity, pace, and progress.
- **Endless Loop:** The absence of an endpoint creates a hypnotic effect — users stay engaged longer.
- **Information Density:** Scrolling text allows more content to be displayed in limited horizontal space.

---

## Implementation

```html
<div class="marquee" style="width: 100%; overflow: hidden; background: #1a1a2e; padding: 1.5rem 0; position: relative;">
  <div class="marquee-track" style="display: flex; white-space: nowrap; width: fit-content;">
    <div class="marquee-content" style="font-family: system-ui; font-size: 3rem; font-weight: 700; color: white; padding-right: 3rem;">
      ✦ Lumary OS &bull; Design Systems &bull; Motion &bull; Experience &bull;
    </div>
    <div class="marquee-content" style="font-family: system-ui; font-size: 3rem; font-weight: 700; color: white; padding-right: 3rem;">
      ✦ Lumary OS &bull; Design Systems &bull; Motion &bull; Experience &bull;
    </div>
  </div>
</div>
```

```javascript
const track = document.querySelector('.marquee-track');
const contents = track.querySelectorAll('.marquee-content');
const speed = 1.5; // pixels per frame at 60fps

let x = 0;
let animationId;

function animateMarquee() {
  x -= speed;
  const contentWidth = contents[0].offsetWidth;

  if (Math.abs(x) >= contentWidth) {
    x = 0;
  }

  gsap.set(track, { x });
  animationId = requestAnimationFrame(animateMarquee);
}

// Pause on hover
track.parentElement.addEventListener('mouseenter', () => {
  cancelAnimationFrame(animationId);
});

track.parentElement.addEventListener('mouseleave', () => {
  animateMarquee();
});

animateMarquee();
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Technology | ★★★★★ | Conference banners, features lists |
| E-commerce | ★★★★☆ | Sale announcements, brand slogans |
| Creative | ★★★★★ | Studio reel, client list |
| Events | ★★★★★ | Event info, dates, speakers |
| Finance | ★★☆☆☆ | Too distracting for financial sites |

---

## Accessibility Notes

- Marquee must pause on hover and focus (WCAG 2.2.2 — Pause, Stop, Hide)
- Content must be available in static form elsewhere on page or via `aria-label`
- Use `prefers-reduced-motion: reduce` to show static, non-scrolling text
- Ensure text contrast ratio ≥ 4.5:1 against background

---

## Performance Notes

- `requestAnimationFrame` is battery-friendly and syncs with screen refresh
- Use `transform: translateX()` — no layout or paint
- Duplicate content in DOM — ensure both copies are identical
- For very long content, cap speed at 120px/s max to avoid nausea

---

## Variants

### Variant A: Reverse Marquee
Scrolling right-to-left (traditional) or left-to-right (reverse direction).

### Variant B: Multi-Speed Marquee
Two marquee rows scrolling at different speeds in opposite directions for visual depth.

### Variant C: Gradient Fade Edges
Add CSS `mask-image: linear-gradient(to right, transparent 5%, black 15%, black 85%, transparent 95%)` for a fade-in/out effect on edges.

---

## Anti-Patterns

- No pause on hover — fails WCAG success criterion 2.2.2
- Scrolling too fast (> 3px per frame) — unreadable
- Critical content only in marquee — users may miss it
- Using on mobile — takes up valuable vertical space and drains battery

---

## Checklist

- [ ] Pauses on hover and focus
- [ ] Reduced motion: static display
- [ ] Duplicate content matches exactly
- [ ] Speed ≤ 120px/second
- [ ] Gradient fade at edges (optional but recommended)
