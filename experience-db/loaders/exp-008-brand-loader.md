# Experience 008: The Brand Reveal Loader

## Classification
Narrative

## Emotion
Anticipation → Satisfaction

## Difficulty
★★★☆☆

## Performance
Medium

## Libraries
GSAP

---

## Description
A branded loading screen that reveals the page content when ready. Logo animates in center, performs a signature animation, then transitions smoothly into the page hero. Creates anticipation and reinforces brand identity.

## Implementation
```html
<div id="loader" class="fixed inset-0 z-[9999] bg-primary flex items-center justify-center">
  <div class="text-center">
    <div class="loader-logo text-4xl font-bold text-white mb-4">LUMARY</div>
    <div class="loader-bar w-48 h-1 bg-white/10 rounded-full overflow-hidden">
      <div class="loader-bar-fill h-full bg-accent rounded-full" style="width: 0%;"></div>
    </div>
  </div>
</div>

<script>
window.addEventListener('load', () => {
  const loader = document.getElementById('loader');
  const bar = loader.querySelector('.loader-bar-fill');
  const logo = loader.querySelector('.loader-logo');
  
  // Animate progress bar to 100%
  gsap.to(bar, {
    width: '100%',
    duration: 0.8,
    ease: 'power3.inOut',
    onComplete: () => {
      // Exit animation
      gsap.to(logo, {
        y: -30,
        opacity: 0,
        duration: 0.4,
        ease: 'power2.in'
      });
      gsap.to(loader, {
        opacity: 0,
        duration: 0.6,
        delay: 0.2,
        ease: 'power2.out',
        onComplete: () => {
          loader.style.display = 'none';
          document.body.style.overflow = '';
          // Start hero animation
          initHeroAnimation();
        }
      });
    }
  });
});
</script>
```

## When to Use
- Premium brand sites
- Heavy media pages (need loading time)
- Portfolio sites (sets creative tone)
- Luxury brands (builds anticipation)

## When NOT to Use
- Content-light pages (loader is faster than content — causes flash)
- Returning visitors (cache loader for repeat visits)
- Slow connections (ironically makes experience worse)

## Performance
- Total animation: ~1200ms
- If page loads faster, minimum 800ms display (avoids flash)
- Cache via sessionStorage to not show on repeat visits

## Anti-Patterns
- Spinner-only (boring, no brand personality)
- Longer than 3 seconds (user abandons)
- No minimum display time (flashes if load is fast)
- Showing on every page visit (only on landing)
