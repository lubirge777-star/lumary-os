# Experience 045: Parallax Image Within Container

## Classification
Narrative

## Emotion
Depth → Engagement

## Difficulty
★★☆☆☆

## Performance Impact
Low

## Libraries
GSAP, ScrollTrigger

---

## Description

An image moves at a different speed than the container as the user scrolls, creating a parallax effect within a fixed frame. The image is larger than its container, and `translateY` shifts it as the container scrolls past, revealing different parts of the image.

Use for hero images, blog featured images, product photos, or any visual where adding depth to a contained image elevates the browsing experience.

---

## Timeline

| Moment | Scroll Position | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | enter viewport | Image | Begin translateY | viewport | Linear |
| 2 | 0%-100% | Image | Shift from 0 to -(imageHeight - containerHeight) | viewport | Linear |
| 3 | leave viewport | Image | Stop parallax | — | — |

---

## Psychology

- **Visual Interest:** Movement within a static frame draws and holds the eye longer than a still image.
- **Depth Illusion:** Slower-moving content behind a faster-moving frame creates perceived depth.
- **Exploration Reward:** Users feel rewarded for scrolling as each scroll reveals new parts of the image.

---

## Implementation

```html
<div class="parallax-image-wrap" style="height: 500px; overflow: hidden; border-radius: 16px; position: relative; width: 800px; max-width: 90vw; margin: 0 auto;">
  <img class="parallax-image" src="https://picsum.photos/800/900?random=parallax" alt="Parallax example"
    style="width: 100%; height: 130%; object-fit: cover; will-change: transform;" />
</div>

<!-- Spacer for scroll -->
<div style="height: 100vh;"></div>
```

```javascript
gsap.registerPlugin(ScrollTrigger);

const imageWrap = document.querySelector('.parallax-image-wrap');
const image = document.querySelector('.parallax-image');

gsap.fromTo(image,
  { y: 0 },
  {
    y: () => -(image.offsetHeight - imageWrap.offsetHeight),
    ease: 'none',
    scrollTrigger: {
      trigger: imageWrap,
      start: 'top bottom',
      end: 'bottom top',
      scrub: true,
      invalidateOnRefresh: true
    }
  }
);

// Reduced motion
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  gsap.set(image, { y: 0 });
  ScrollTrigger.getAll().forEach(st => st.disable());
}
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Creative | ★★★★★ | Portfolio images |
| Travel | ★★★★★ | Destination photos |
| Real Estate | ★★★★☆ | Property photos |
| E-commerce | ★★★★☆ | Product hero images |
| Blog / Media | ★★★★☆ | Featured images |

---

## Accessibility Notes

- Image must have descriptive `alt` text — parallax is decorative motion
- `prefers-reduced-motion: reduce` — display image centered, no parallax
- Ensure no important image content is cropped by the container when parallax is disabled
- Container must have `overflow: hidden` to prevent layout breakage

---

## Performance Notes

- Only `y` transform — fully GPU composited
- `will-change: transform` on the image for compositor layer promotion
- Image height: 130-150% of container for sufficient parallax travel
- No layout triggers — one of the cheapest visual effects available

---

## Variants

### Variant A: Reverse Parallax
Image moves faster than container (shifts in opposite direction) for a more dramatic effect.

### Variant B: Scale + Parallax
Image scales from 1.1x down to 1x while translating for a "zoom out while scrolling" effect.

### Variant C: Multi-Image Grid
A grid of images each with their own parallax — staggered start/end for a wave-like reveal.

---

## Anti-Patterns

- Image only 100% container height — no room for parallax motion
- Container without `overflow: hidden` — image spills out
- Image cropped at important focal points — parallax may hide faces or text in image
- Too much travel (> 30% offset) — reveals edges of image

---

## Checklist

- [ ] Image height ≥ 120% of container height
- [ ] Container has `overflow: hidden`
- [ ] `will-change: transform` on image
- [ ] Reduced motion: centered static image
- [ ] `alt` text provided
- [ ] Tested with different screen sizes
