# Experience 054: Infinite Scrolling Carousel

## Classification
Narrative → Scrolling

## Emotion
Energy → Engagement → Discovery

## Difficulty
★★★☆☆

## Performance Impact
Low-Medium

## Libraries
GSAP

## Description
A horizontally looping carousel of cards or items that scrolls continuously, creating a seamless infinite feed. Supports drag/swipe interaction, pauses on hover, and auto-plays. Ideal for product showcases, trending articles, client logos, or gallery previews.

## When to Use
- E-commerce: trending products, new arrivals
- Editorial: trending articles, featured stories
- Portfolio: client logos, featured projects
- Any section where you want users to browse endlessly

## Implementation

### HTML
```html
<section class="py-16 md:py-20 lg:py-24 px-4 md:px-6 overflow-hidden">
  <div class="max-w-6xl mx-auto mb-10 md:mb-12 px-4 md:px-6">
    <span class="text-xs md:text-sm font-semibold text-accent uppercase tracking-widest">Trending Now</span>
    <h2 class="font-heading mt-4">New Arrivals</h2>
  </div>
  <div class="infinite-carousel relative" role="region" aria-label="Scrolling carousel">
    <div class="carousel-track flex gap-4 md:gap-6 w-max cursor-grab active:cursor-grabbing select-none" role="list">
      <!-- Items injected via JS -->
    </div>
  </div>
</section>
```

### CSS
Add to existing `<style>` block:
```css
.infinite-carousel {
  mask-image: linear-gradient(to right, transparent 0%, black 5%, black 95%, transparent 100%);
  -webkit-mask-image: linear-gradient(to right, transparent 0%, black 5%, black 95%, transparent 100%);
}
.carousel-item {
  flex-shrink: 0;
  width: clamp(200px, 40vw, 320px);
  border-radius: 16px;
  overflow: hidden;
  user-select: none;
}
@media (min-width: 768px) { .carousel-item { width: clamp(240px, 25vw, 350px); } }
@media (min-width: 1024px) { .carousel-item { width: clamp(280px, 20vw, 380px); } }
```

### JavaScript (GSAP)
```js
function initInfiniteCarousel(container) {
  if (!container || reducedMotion) return;
  const track = container.querySelector('.carousel-track');
  if (!track) return;

  // Gather original items
  const items = Array.from(track.children);
  if (items.length < 2) return;

  // Clone items for seamless loop
  items.forEach(function(item) {
    const clone = item.cloneNode(true);
    clone.setAttribute('aria-hidden', 'true');
    track.appendChild(clone);
  });

  const itemWidth = items[0].offsetWidth + parseFloat(getComputedStyle(track).gap) || 16;
  const halfWidth = itemWidth * items.length;
  var speed = parseFloat(container.dataset.speed) || 40;
  var duration = halfWidth / speed;

  // Create the infinite scroll tween
  var tween = gsap.to(track, {
    x: -halfWidth,
    ease: 'none',
    duration: duration,
    repeat: -1,
    onRepeat: function() { gsap.set(track, { x: 0 }); }
  });

  // Drag support
  var isDragging = false;
  var startX = 0;
  var dragOffset = 0;
  var currentX = 0;

  function onStart(e) {
    isDragging = true;
    tween.pause();
    startX = e.clientX || e.touches[0].clientX;
    currentX = gsap.getProperty(track, 'x');
    track.classList.add('cursor-grabbing');
  }

  function onMove(e) {
    if (!isDragging) return;
    e.preventDefault();
    var clientX = e.clientX || e.touches[0].clientX;
    dragOffset = clientX - startX;
    var newX = currentX + dragOffset;
    // Wrap around for infinite drag feel
    if (newX > 0) newX -= halfWidth;
    if (newX < -halfWidth) newX += halfWidth;
    gsap.set(track, { x: newX });
  }

  function onEnd() {
    if (!isDragging) return;
    isDragging = false;
    track.classList.remove('cursor-grabbing');
    // Resume from nearest wrapped position
    var current = gsap.getProperty(track, 'x');
    var remainder = current % halfWidth;
    var newStart = -halfWidth + remainder;
    gsap.set(track, { x: newStart });
    tween.play();
  }

  track.addEventListener('mousedown', onStart);
  window.addEventListener('mousemove', onMove);
  window.addEventListener('mouseup', onEnd);
  track.addEventListener('touchstart', onStart, { passive: true });
  window.addEventListener('touchmove', onMove, { passive: false });
  window.addEventListener('touchend', onEnd);

  // Pause on hover
  container.addEventListener('mouseenter', function() { tween.pause(); });
  container.addEventListener('mouseleave', function() {
    if (!isDragging) tween.play();
  });

  return tween;
}

// Initialize all carousels on DOMContentLoaded
document.querySelectorAll('.infinite-carousel').forEach(initInfiniteCarousel);
```

## Variants

### Variant A: Slow ambient scroll
- `data-speed="20"` — slow, subtle motion for brand logos

### Variant B: Medium product scroll
- `data-speed="40"` — standard pace for product cards or articles

### Variant C: Fast discovery scroll
- `data-speed="60"` — fast pace for trending items or alerts

### Variant D: Direction reverse
- Change `x: -halfWidth` to `x: halfWidth` and set `track` to start at negative offset

## Accessibility
- Use `role="list"` and `role="listitem"` on carousel items
- Set `aria-hidden="true"` on cloned elements so screen readers don't double-count content
- Pause on hover so users with motion sensitivity can interact
- Respect `prefers-reduced-motion` — disable animation, show static grid
- Touch targets on items should be minimum 44px

## Related
- exp-031: Infinite Scrolling Marquee Text (text-only variant)
- exp-002: The Cascade (staggered reveal for card grids)
