# Experience 029: Multiplane Parallax with Depth Map

## Classification
Narrative

## Emotion
Awe → Immersion

## Difficulty
★★★★★

## Performance Impact
High

## Libraries
GSAP, ScrollTrigger, Three.js (optional)

---

## Description

An advanced multiplane parallax system that uses a depth map (z-depth data per pixel) to create a true 3D parallax effect. Each element is positioned at a specific z-depth and moves with perspective-correct velocity based on its depth value. This creates the most realistic parallax effect available in the browser.

Use for hero sections that demand maximum visual impact — product launches, cinematic storytelling, or immersive brand experiences.

---

## Timeline

| Moment | Time | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | scroll 0% | Deep background | Slow drift at 0.1x speed | viewport | Linear |
| 2 | scroll 0% | Mid-background | Parallax at 0.3x speed | viewport | Linear |
| 3 | scroll 0% | Foreground elements | Parallax at 0.6x speed | viewport | Linear |
| 4 | scroll 0% | UI overlays | Static (0x speed) | viewport | — |
| 5 | scroll 80% | All layers | Deceleration ease-out | 300ms | Power2.out |

---

## Psychology

- **Immersion via Realism:** Depth-map-based parallax closely mimics human binocular vision, creating strong presence.
- **Spatial Memory:** Users remember the spatial layout of 3D content better than flat content.
- **Awe Response:** Highly realistic depth effects trigger genuine emotional responses, increasing brand recall.

---

## Implementation

```html
<section class="multiplane" style="height: 300vh; position: relative; overflow: hidden;">
  <div class="mp-scene" style="position: sticky; top: 0; height: 100vh; overflow: hidden;">
    <div class="mp-plane" data-z="0.9" style="position: absolute; inset: -5%;">
      <img src="https://picsum.photos/1920/1080?random=bg" alt="" style="width: 100%; height: 100%; object-fit: cover;" />
    </div>
    <div class="mp-plane" data-z="0.6" style="position: absolute; top: 15%; left: 10%; width: 30%;">
      <img src="https://picsum.photos/500/600?random=mnt" alt="" style="width: 100%; border-radius: 16px; box-shadow: 0 20px 60px rgba(0,0,0,0.5);" />
    </div>
    <div class="mp-plane" data-z="0.3" style="position: absolute; bottom: 10%; right: 8%; width: 25%;">
      <img src="https://picsum.photos/400/300?random=tree" alt="" style="width: 100%; border-radius: 16px; box-shadow: 0 20px 60px rgba(0,0,0,0.5);" />
    </div>
    <div class="mp-plane" data-z="0.1" style="position: absolute; bottom: 5%; left: 20%; width: 15%;">
      <div style="width: 100%; aspect-ratio: 1; background: #a29bfe; border-radius: 50%; filter: blur(4px); opacity: 0.6;"></div>
    </div>
    <h2 class="mp-title" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-family: system-ui; font-size: 4rem; text-shadow: 0 4px 30px rgba(0,0,0,0.8); z-index: 10; text-align: center;">
      Multiplane<br />Depth
    </h2>
  </div>
</section>
```

```javascript
gsap.registerPlugin(ScrollTrigger);

const scene = document.querySelector('.mp-scene');
const planes = scene.querySelectorAll('.mp-plane');
const strength = 200;

// Convert z-depth (0 to 1) into a parallax offset for a scroll range
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: '.multiplane',
    start: 'top top',
    end: 'bottom bottom',
    scrub: 2
  }
});

planes.forEach(plane => {
  const z = parseFloat(plane.dataset.z);
  const offset = (1 - z) * strength;

  tl.to(plane, {
    y: offset,
    scale: 1 - (1 - z) * 0.05,
    duration: 1
  }, 0);
});

// Fade title as we scroll through
tl.to('.mp-title', {
  opacity: 0,
  scale: 0.95,
  duration: 1
}, 0);
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Film / Media | ★★★★★ | Cinematic promotional pages |
| Gaming | ★★★★★ | Game world reveals |
| Automotive | ★★★★☆ | Car showcase with depth |
| Luxury | ★★★★☆ | Premium brand storytelling |
| Technology | ★★★☆☆ | Product launches only |

---

## Accessibility Notes

- Full content must be available without multiplane motion
- Disable entirely under `prefers-reduced-motion: reduce` — stack planes in z-order
- Scene images must have descriptive `alt` text for screen readers
- Fixed/sticky container must not trap keyboard focus

---

## Performance Notes

- **Highest performance cost of all parallax variants** — use sparingly
- Max 4 depth planes; each additional plane compounds repaint cost
- Images should be preloaded and optimized to WebP
- Consider using `transform: translateZ()` with `perspective` for GPU acceleration
- Mobile: fall back to static hero or reduce to 2 planes

---

## Variants

### Variant A: Three.js Depth Mesh
Use Three.js with a depth map texture to create genuine 3D geometry displacement for photo-realistic parallax.

### Variant B: CSS 3D Transform Stack
Use CSS `perspective` + `translateZ` to let the browser handle depth automatically — less control but better performance.

### Variant C: Scroll-Driven Opacity Blend
Planes at different depths fade in/out as they pass through a scroll-driven z-plane focus zone.

---

## Anti-Patterns

- Using depth map on text — makes it unreadable
- More than 5 planes — destroys performance
- No mobile fallback — high-performance feature will fail on phone GPUs
- Interactive elements inside moving planes — click targets misalign

---

## Checklist

- [ ] Max 4 depth planes
- [ ] All images preloaded
- [ ] Reduced motion respected
- [ ] Mobile fallback (static hero)
- [ ] z-index properly ordered (higher depth = lower z-index)
- [ ] Interactive elements excluded from motion
