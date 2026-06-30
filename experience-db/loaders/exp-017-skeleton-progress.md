# Experience 017: The Skeleton Progress

## Classification: Guide
## Emotion: Trust
## Difficulty: ★★☆☆☆
## Performance: Low
## Libraries: None (CSS only)

## Description
A skeleton screen that shows the page structure while content loads. Each section has a shimmer animation that mimics content layout. Transitions smoothly to real content.

## Code
```html
<div class="skeleton-page" aria-busy="true">
  <div class="skeleton-nav h-16 bg-white/5 rounded-xl mb-8 animate-pulse"></div>
  <div class="skeleton-hero grid grid-cols-2 gap-8 mb-8">
    <div class="space-y-4">
      <div class="h-12 bg-white/5 rounded-xl w-3/4 animate-pulse"></div>
      <div class="h-6 bg-white/5 rounded-lg w-1/2 animate-pulse"></div>
      <div class="h-14 bg-white/5 rounded-xl w-1/3 animate-pulse mt-8"></div>
    </div>
    <div class="h-96 bg-white/5 rounded-2xl animate-pulse"></div>
  </div>
</div>

<style>
@keyframes shimmer { 0% { opacity: 0.3; } 50% { opacity: 0.6; } 100% { opacity: 0.3; } }
.animate-pulse { animation: shimmer 1.5s ease-in-out infinite; }
</style>
```

## When to Use
- Pages with heavy images/video
- Slow network connections
- API-dependent content
- Single-page applications
