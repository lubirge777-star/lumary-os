# Experience 006: The Cinematic Hero

## Classification
Narrative

## Emotion
Awe → Excitement

## Difficulty
★★★☆☆

## Performance
High (video is heavy — optimize aggressively)

## Libraries
GSAP, Lenis

---

## Description
A full-viewport hero with a muted autoplay video background. The video creates cinematic atmosphere while text overlays deliver the message. Combined with a slow parallax effect and staggered text reveal.

## Implementation
```html
<section class="hero min-h-screen relative overflow-hidden flex items-center justify-center">
  <!-- Video Background -->
  <video class="absolute inset-0 w-full h-full object-cover"
         autoplay muted loop playsinline
         poster="hero-poster.webp"
         aria-hidden="true">
    <source src="hero.mp4" type="video/mp4" />
  </video>
  
  <!-- Overlay -->
  <div class="absolute inset-0 bg-gradient-to-t from-primary via-primary/60 to-primary/40"></div>
  
  <!-- Content -->
  <div class="relative z-10 text-center max-w-4xl px-6">
    <h1 class="hero-heading text-5xl md:text-7xl font-bold text-white mb-6">
      Experience the Difference
    </h1>
    <p class="hero-subtext text-lg md:text-xl text-gray-300 mb-10 max-w-2xl mx-auto">
      Where quality meets craftsmanship.
    </p>
    <a href="#" class="hero-cta inline-flex items-center gap-2 px-10 py-5 bg-accent text-white rounded-xl font-semibold
                      hover:bg-accent-light transition-all duration-300">
      Get Started
    </a>
  </div>
</section>
```

## Performance Requirements
| Asset | Max Size | Format |
|---|---|---|
| Video | 2MB | MP4 (h.264) |
| Poster image | 200KB | WebP |
| Total page impact | < 3MB | — |

## Optimization
- Compress video with FFmpeg: `ffmpeg -i input.mp4 -vf "scale=-1:1080" -crf 28 -c:v libx264 output.mp4`
- Use `poster` attribute for slow connections
- Detect slow connection: `navigator.connection.effectiveType` — fallback to image

## When to Use
- Hotel / resort landing pages
- Real estate property showcases
- Creative studio portfolios
- Product launch campaigns

## Anti-Patterns
- Auto-playing audio (never — always muted)
- Video > 5MB (kills mobile performance)
- No poster image (blank white screen while video loads)
- Obtrusive overlay text (video should be visible, not 90% covered)
