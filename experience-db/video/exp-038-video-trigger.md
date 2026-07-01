# Experience 038: Scroll-Triggered Video Play

## Classification
Narrative

## Emotion
Surprise → Immersion

## Difficulty
★★☆☆☆

## Performance Impact
Medium

## Libraries
GSAP, ScrollTrigger

---

## Description

A video automatically plays when the user scrolls it into view, creating a cinematic reveal. The video may be muted (autoplay policy compliant) and can include a fade-in transition as it enters the viewport.

Use for brand stories, product demonstrations, testimonials, or any content where video enhances the narrative but should not play until the user reaches it.

---

## Timeline

| Moment | Time | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | scroll in | Container | Opacity 0 → 1 | 400ms | Power2.out |
| 2 | 50ms | Video | Play | — | — |
| 3 | scroll out | Container | Opacity 1 → 0 | 400ms | Power2.out |
| 4 | scroll out | Video | Pause | — | — |

---

## Psychology

- **Playback Reward:** Video automatically playing on scroll feels like a reward for reaching that content.
- **Narrative Momentum:** Video content at key scroll positions breaks the monotony of text, re-engaging attention.
- **Pacing Control:** Scroll-triggered video respects the user's reading pace — they control when it starts.

---

## Implementation

```html
<section class="video-trigger-section" style="height: 200vh; display: flex; align-items: center; justify-content: center; flex-direction: column;">
  <p style="color: white; font-family: system-ui; margin-bottom: 2rem;">Scroll down for video.</p>
  <div class="video-trigger" style="width: 800px; max-width: 90vw; border-radius: 16px; overflow: hidden; opacity: 0; transform: translateY(30px);">
    <video class="trigger-video" muted playsinline preload="metadata" style="width: 100%; display: block;"
      poster="https://picsum.photos/800/450?random=vid">
      <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4" />
    </video>
  </div>
</section>
```

```javascript
gsap.registerPlugin(ScrollTrigger);

const videoContainer = document.querySelector('.video-trigger');
const video = document.querySelector('.trigger-video');

ScrollTrigger.create({
  trigger: videoContainer,
  start: 'top 80%',
  end: 'bottom 20%',
  onEnter: () => {
    gsap.to(videoContainer, {
      opacity: 1,
      y: 0,
      duration: 0.5,
      ease: 'power2.out'
    });
    video.play().catch(() => {});
  },
  onLeave: () => {
    video.pause();
  },
  onEnterBack: () => {
    video.play().catch(() => {});
  },
  onLeaveBack: () => {
    video.pause();
  }
});

// Also handle reduced motion
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  gsap.set(videoContainer, { opacity: 1, y: 0 });
}
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Creative Agency | ★★★★★ | Showreel, case studies |
| E-commerce | ★★★★☆ | Product demo videos |
| Technology | ★★★★★ | Product launch pages |
| Travel | ★★★★☆ | Destination videos |
| Education | ★★★☆☆ | Course previews |

---

## Accessibility Notes

- Video must not auto-play audio (always muted initially)
- Provide a play/pause button as fallback for keyboard users
- Add captions/subtitles using `<track>` element
- `prefers-reduced-motion: reduce` — show poster image statically, no auto-play
- Video poster is required for users who cannot or choose not to watch video

---

## Performance Notes

- Use `preload="metadata"` to avoid downloading entire video on page load
- Compress video: H.264, ≤ 2MB for a 15s clip
- Consider using `loading="lazy"` on mobile
- Poster image should be WebP, ≤ 100KB

---

## Variants

### Variant A: Autoplay Muted (Hero)
Video plays immediately on page load in the hero section. Classic cinematic opener.

### Variant B: Click to Unmute
Video auto-plays muted; a button appears to enable audio. Satisfies autoplay policies while allowing sound.

### Variant C: Multi-Video Scrollytelling
Multiple video clips that change as user scrolls through sections — a video playlist synchronized to scroll.

---

## Anti-Patterns

- Auto-playing audio — blocked by browsers and annoys users
- No poster image — blank space while video loads
- Video larger than 5MB — users on mobile networks will not wait
- No play/pause controls — keyboard users cannot control playback

---

## Checklist

- [ ] Video muted for auto-play
- [ ] Poster image provided
- [ ] `<track>` captions included
- [ ] Video optimized (H.264, ≤ 2MB)
- [ ] Reduced motion: static poster
- [ ] Play/pause controls available
