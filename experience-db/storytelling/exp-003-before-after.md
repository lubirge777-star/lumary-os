# Experience 003: The Transformation

## Classification
Narrative

## Emotion
Trust → Desire

## Difficulty
★★★☆☆

## Performance
Medium

## Libraries
GSAP ScrollTrigger, Swiper.js

---

## Description
A before/after comparison that reveals transformation. Best for construction renovations, wellness results, or any service that changes something from one state to another.

## Implementation
```html
<div class="comparison-slider relative w-full h-[500px] overflow-hidden rounded-2xl" role="img" aria-label="Before and after comparison">
  <div class="absolute inset-0">
    <img src="after.webp" alt="After" class="w-full h-full object-cover" />
  </div>
  <div class="absolute inset-0 before-image" style="clip-path: inset(0 50% 0 0);">
    <img src="before.webp" alt="Before" class="w-full h-full object-cover" />
  </div>
  <div class="absolute top-0 bottom-0 w-1 bg-white cursor-ew-resize" id="slider-handle" style="left: 50%;" role="slider" tabindex="0" aria-label="Comparison slider" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100">
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-10 h-10 bg-white rounded-full shadow-lg flex items-center justify-center">
      <svg class="w-5 h-5 text-gray-800" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7l-4 4m0 0l4 4m-4-4h16"/></svg>
    </div>
  </div>
  <span class="absolute bottom-4 left-4 px-3 py-1 bg-black/60 text-white text-sm rounded-lg">Before</span>
  <span class="absolute bottom-4 right-4 px-3 py-1 bg-black/60 text-white text-sm rounded-lg">After</span>
</div>

<script>
const container = document.querySelector('.comparison-slider');
const before = container.querySelector('.before-image');
const handle = container.querySelector('#slider-handle');

function updateSlider(x) {
  const rect = container.getBoundingClientRect();
  const pct = Math.max(0, Math.min(100, ((x - rect.left) / rect.width) * 100));
  before.style.clipPath = `inset(0 ${100 - pct}% 0 0)`;
  handle.style.left = `${pct}%`;
  handle.setAttribute('aria-valuenow', Math.round(pct));
}

container.addEventListener('mousemove', (e) => updateSlider(e.clientX));
container.addEventListener('touchmove', (e) => updateSlider(e.touches[0].clientX));
</script>
```

## Industries
Construction ★★★★★, Wellness ★★★★★, Beauty ★★★★☆, Real Estate ★★★★☆

## Accessibility
- `role="slider"` with keyboard support (arrow keys)
- Text labels for Before/After
- ARIA live region for current position
