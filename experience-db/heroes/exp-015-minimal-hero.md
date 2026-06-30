# Experience 015: The Minimal Hero

## Classification: Narrative
## Emotion: Calm → Trust
## Difficulty: ★☆☆☆☆
## Performance: Low
## Libraries: GSAP

## Description
A clean, minimal hero with generous whitespace, large typography, and a single CTA. No background image — uses color or subtle gradient instead. Animates with a simple fade-in.

## Code
```javascript
gsap.from('.minimal-hero-content', {
  y: 40, opacity: 0, duration: 0.8, ease: 'power2.out', delay: 0.3
});
```

## When to Use
- Professional services (lawyers, consultants)
- SaaS landing pages
- Personal portfolios
- Any brand that wants to communicate confidence through restraint

## HTML
```html
<section class="min-h-screen flex items-center justify-center px-6" style="background: linear-gradient(135deg, var(--color-primary), var(--color-secondary))">
  <div class="minimal-hero-content text-center max-w-2xl">
    <span class="text-sm font-semibold text-accent uppercase tracking-widest">Tagline</span>
    <h1 class="text-5xl md:text-7xl font-bold mt-6 mb-6 leading-tight">Clean. Simple. Effective.</h1>
    <p class="text-lg text-muted mb-10 max-w-md mx-auto">One sentence that explains exactly what you do.</p>
    <a href="#" class="btn-primary px-10 py-5 bg-accent text-white rounded-xl font-semibold">Get Started</a>
  </div>
</section>
```
