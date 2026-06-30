# Experience 021: The Timeline Scroll

## Classification: Narrative
## Emotion: Trust → Satisfaction
## Difficulty: ★★★☆☆
## Performance: Low
## Libraries: GSAP ScrollTrigger

## Description
A vertical or horizontal timeline that reveals milestones as the user scrolls. Each milestone has a date, title, description, and optional media. The connecting line draws progressively. Best for company history, project phases, or personal journey.

## Code
```html
<div class="timeline relative pl-8 before:absolute before:left-3 before:top-0 before:bottom-0 before:w-0.5 before:bg-white/10">
  <div class="timeline-item relative mb-16" data-year="2016">
    <div class="absolute left-[-26px] top-1 w-4 h-4 rounded-full bg-accent border-4 border-primary"></div>
    <span class="text-sm font-semibold text-accent">2016</span>
    <h3 class="text-xl font-bold mt-2 mb-2">Company Founded</h3>
    <p class="text-muted">Started with a vision to transform the industry.</p>
  </div>
  <div class="timeline-item relative mb-16" data-year="2018">
    <div class="absolute left-[-26px] top-1 w-4 h-4 rounded-full bg-accent border-4 border-primary"></div>
    <span class="text-sm font-semibold text-accent">2018</span>
    <h3 class="text-xl font-bold mt-2 mb-2">First Major Project</h3>
    <p class="text-muted">Completed our first large-scale commercial project.</p>
  </div>
</div>

<script>
gsap.utils.toArray('.timeline-item').forEach((item, i) => {
  gsap.from(item, {
    x: -30, opacity: 0, duration: 0.6, delay: i * 0.2,
    scrollTrigger: { trigger: item, start: 'top 85%' }
  });
});
</script>
```

## When to Use
- Company history / About page
- Project process / methodology
- Career timeline / resume
- Product development story
