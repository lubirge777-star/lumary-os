# Experience 039: Scroll-Scrubbed Video

## Classification
Narrative

## Emotion
Control → Engagement

## Difficulty
★★★★☆

## Performance Impact
High

## Libraries
GSAP, ScrollTrigger

---

## Description

Video playback is linked directly to scroll position — scrolling forward advances the video, scrolling backward rewinds it. The video acts as a visual storyboard where the user controls pacing by scrolling.

Use for product reveals, before/after comparisons, frame-by-frame demonstrations, or cinematic brand storytelling where precise visual control enhances the narrative.

---

## Timeline

| Moment | Scroll Position | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0%-5% | Video | Frame 0 (poster) | — | — |
| 2 | 5%-100% | Video | Scrub forward with scroll | viewport | Linear |
| 3 | 100% | Video | Final frame | — | — |

---

## Psychology

- **Direct Manipulation:** Scroll-to-scrub gives users an unprecedented level of control over visual playback.
- **Exploration Reward:** Users can rewatch specific segments by scrolling back, increasing time-on-page.
- **Pacing Autonomy:** Unlike auto-play video, the user controls the speed — reduces anxiety of missing something.

---

## Implementation

```html
<section class="video-scrub-section" style="height: 500vh; position: relative;">
  <div class="video-scrub-sticky" style="position: sticky; top: 0; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden;">
    <video class="scrub-video" muted playsinline preload="auto" style="width: 100%; height: 100%; object-fit: cover;"
      poster="https://picsum.photos/1920/1080?random=scrub">
      <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4" />
    </video>
    <div class="scrub-overlay" style="position: absolute; bottom: 2rem; left: 50%; transform: translateX(-50%); color: white; font-family: system-ui; background: rgba(0,0,0,0.6); padding: 0.5rem 1rem; border-radius: 8px; font-size: 0.85rem;">
      Scroll to control video
    </div>
  </div>
</section>
```

```javascript
gsap.registerPlugin(ScrollTrigger);

const video = document.querySelector('.scrub-video');

// Wait for video metadata to load
video.addEventListener('loadedmetadata', () => {
  const duration = video.duration;

  ScrollTrigger.create({
    trigger: '.video-scrub-section',
    start: 'top top',
    end: 'bottom bottom',
    scrub: 1,
    onUpdate: (self) => {
      video.currentTime = self.progress * duration;
    }
  });
});

// Reduced motion fallback
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  video.pause();
  ScrollTrigger.getAll().forEach(st => st.disable());
}
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Automotive | ★★★★★ | Car reveal — scrub through design details |
| Fashion | ★★★★★ | Lookbook — frame-perfect collection view |
| Technology | ★★★★★ | Product feature deep-dive |
| Film | ★★★★★ | Trailer breakdowns |
| Real Estate | ★★★★☆ | Virtual property tour |

---

## Accessibility Notes

- Provide a play/pause fallback — scrub is not usable by keyboard-only or screen reader users
- `prefers-reduced-motion: reduce` — show poster image or auto-play standard video
- Add `aria-label` describing the scrub interaction
- Scrub speed must not exceed video frame rate (avoid frame skipping)

---

## Performance Notes

- **Highest performance cost** — video decoding on scroll is expensive
- Compress video aggressively (H.264, 720p max, variable bitrate)
- Use `preload="auto"` to fully buffer the video before scrubbing
- On mobile, reduce video resolution or fall back to image sequence
- Consider an image sprite sequence as a lighter-weight alternative

---

## Variants

### Variant A: Image Sprite Scrub
Replace video with a spritesheet of JPEG frames scrubbed via `background-position`. Lower quality but better performance.

### Variant B: Canvas Scrub
Video frames rendered to `<canvas>` for custom frame-accurate overlays (timestamps, hot spots).

### Variant C: Multi-Video Timeline
Multiple video clips play in sequence as user scrolls through sections — each with their own scrub range.

---

## Anti-Patterns

- Long videos (> 30s) — huge file size, long scroll section, user fatigue
- No compression — 10MB+ video will stutter on scroll
- No poster — blank sticky area until video loads
- Audio on scrub video — audio stutters with scroll; always mute
- Mobile unfriendly — 500vh sections are painful on phone

---

## Checklist

- [ ] Video duration ≤ 30s
- [ ] Video compressed (H.264, ≤ 3MB)
- [ ] `preload="auto"` set
- [ ] Fallback play/pause controls
- [ ] Reduced motion: static poster
- [ ] Mobile: image sprite fallback
