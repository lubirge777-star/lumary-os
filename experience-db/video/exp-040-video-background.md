# Experience 040: Cinematic Background Video

## Classification
Narrative

## Emotion
Immersion → Awe

## Difficulty
★★☆☆☆

## Performance Impact
Medium

## Libraries
GSAP

---

## Description

A full-viewport background video with a color overlay that sets the mood of the section. The video plays silently in the background while content (headline, text, CTAs) sits on top. Subtle zoom or pan animations can be added for extra cinematic feel.

Use for hero sections, landing pages, event pages, or any brand experience that benefits from motion-rich backgrounds.

---

## Timeline

| Moment | Time | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0ms | Video | Start playing (muted) | — | — |
| 2 | 0ms | Overlay | Fade from black to transparent | 1000ms | Power2.out |
| 3 | 500ms | Content | Stagger fade-in | 1200ms | Power3.out |
| 4 | continuous | Video | Slow zoom (1x → 1.05x) | infinite | Linear |

---

## Psychology

- **Contextual Immersion:** Moving backgrounds create a sense of place and atmosphere that static images cannot achieve.
- **Visual Depth:** Video naturally adds a third dimension (time) to the visual experience, keeping engagement higher.
- **Emotional Tuning:** Color overlays combined with video content allow precise emotional targeting (warm = excitement, cool = calm).

---

## Implementation

```html
<section class="video-bg-section" style="position: relative; height: 100vh; overflow: hidden; display: flex; align-items: center; justify-content: center;">
  <div class="video-bg-wrapper" style="position: absolute; inset: -10%;">
    <video class="video-bg" autoplay muted loop playsinline preload="auto" style="width: 100%; height: 100%; object-fit: cover;">
      <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4" />
    </video>
  </div>
  <div class="video-bg-overlay" style="position: absolute; inset: 0; background: linear-gradient(135deg, rgba(26,26,46,0.85), rgba(22,33,62,0.7)); z-index: 1;"></div>
  <div class="video-bg-content" style="position: relative; z-index: 2; text-align: center; color: white; font-family: system-ui; max-width: 700px; padding: 2rem;">
    <h1 style="font-size: 4rem; margin: 0 0 1rem; opacity: 0; transform: translateY(20px);">Lumary OS</h1>
    <p style="font-size: 1.25rem; opacity: 0; transform: translateY(15px); margin: 0 0 2rem;">Design systems powered by motion.</p>
    <a href="#" style="display: inline-block; padding: 0.85rem 2.5rem; background: #6c5ce7; color: white; text-decoration: none; border-radius: 50px; font-weight: 600; opacity: 0; transform: translateY(10px);">Explore</a>
  </div>
</section>
```

```javascript
const tl = gsap.timeline({ defaults: { ease: 'power3.out' } });

tl
  .set('.video-bg-content h1, .video-bg-content p, .video-bg-content a', { opacity: 0 })
  .to('.video-bg-wrapper', { scale: 1.05, duration: 8, ease: 'none' }, 0)
  .to('.video-bg-content h1', { opacity: 1, y: 0, duration: 1 }, 0.5)
  .to('.video-bg-content p', { opacity: 1, y: 0, duration: 0.8 }, 0.9)
  .to('.video-bg-content a', { opacity: 1, y: 0, duration: 0.6 }, 1.2);

// Scroll-driven zoom out
gsap.registerPlugin(ScrollTrigger);
gsap.to('.video-bg-wrapper', {
  scale: 1,
  scrollTrigger: {
    trigger: '.video-bg-section',
    start: 'top top',
    end: 'bottom top',
    scrub: true
  }
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Travel | ★★★★★ | Destination heroes |
| Automotive | ★★★★★ | Car driving footage |
| Technology | ★★★★★ | Product launch |
| Luxury | ★★★★★ | Premium brand experience |
| Real Estate | ★★★★☆ | Property showcase |
| Healthcare | ★★☆☆☆ | Too distracting for clinical |

---

## Accessibility Notes

- Video must be muted (autoplay policy + user comfort)
- Provide a "Pause video" button for users who find motion distracting
- Overlay must ensure sufficient text contrast (min 4.5:1) against varying video content
- `prefers-reduced-motion: reduce` — replace with static background image
- Add `aria-hidden="true"` to video element (decorative)

---

## Performance Notes

- Video should be optimized: H.264, 720p, ≤ 2MB for a 15s loop
- Use `preload="auto"` for instant playback
- Consider a `<picture>` fallback with a static image for slow connections
- The slow zoom transform is GPU-composited — zero extra cost

---

## Variants

### Variant A: Gradient Overlay Emphasis
Stronger gradient overlay with vibrant accent color (brand-matched) for more personality.

### Variant B: Dual Video Split
Two video backgrounds side-by-side with different content (e.g., before/after, day/night).

### Variant C: Video with Particle Overlay
A particle canvas overlay on top of the video for extra visual richness.

---

## Anti-Patterns

- Audio auto-playing — blocked and annoying
- No fallback image — blank space if video fails to load
- Text unreadable against video — always use sufficient overlay opacity
- No pause control — WCAG violation for auto-playing content
- Video loop is jarring — ensure seamless loop or fade to black

---

## Checklist

- [ ] Video muted and looping
- [ ] Overlay opacity ≥ 0.6 for text readability
- [ ] Static image fallback (poster)
- [ ] "Pause video" control available
- [ ] Reduced motion: static background
- [ ] Video optimized (≤ 2MB)
