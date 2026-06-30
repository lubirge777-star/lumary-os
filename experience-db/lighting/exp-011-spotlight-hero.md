# Experience 011: The Spotlight Hero

## Classification
Narrative

## Emotion
Drama → Focus

## Difficulty
★★★★☆

## Performance
Medium

## Libraries
GSAP

---

## Description
A hero section with a radial spotlight effect that follows the cursor. The background is dark, but a soft circular glow follows mouse movement, illuminating the hero content. Creates a dramatic, theatrical feel.

## Implementation
```html
<style>
.spotlight-hero {
  position: relative;
  overflow: hidden;
}
.spotlight-overlay {
  position: absolute;
  inset: -200px;
  background: radial-gradient(
    circle 400px at var(--mouse-x, 50%) var(--mouse-y, 50%),
    rgba(255,255,255,0.08) 0%,
    transparent 70%
  );
  pointer-events: none;
  transition: background 0.1s;
}
</style>

<section class="spotlight-hero min-h-screen relative flex items-center justify-center bg-primary">
  <div class="spotlight-overlay" id="spotlight"></div>
  <div class="relative z-10 text-center max-w-4xl px-6">
    <h1 class="text-5xl md:text-7xl font-bold text-white mb-6">Your Vision, Built</h1>
    <p class="text-lg text-gray-400 mb-10">Premium construction for those who demand excellence.</p>
    <a href="#" class="px-10 py-5 bg-accent text-white rounded-xl font-semibold">Get Started</a>
  </div>
</section>

<script>
const spotlight = document.getElementById('spotlight');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!reducedMotion) {
  document.querySelector('.spotlight-hero').addEventListener('mousemove', (e) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width) * 100;
    const y = ((e.clientY - rect.top) / rect.height) * 100;
    spotlight.style.setProperty('--mouse-x', `${x}%`);
    spotlight.style.setProperty('--mouse-y', `${y}%`);
  });
}
</script>
```

## When to Use
- Luxury brand hero sections
- Construction/real estate premium landing
- Product hero with dramatic photography
- Entertainment / media

## Anti-Patterns
- Over-bright spotlight (washes out text contrast)
- Mobile (no cursor — fallback to static gradient)
- `prefers-reduced-motion` (static gradient only)
