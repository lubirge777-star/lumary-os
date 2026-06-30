# Performance

## Version 1.0

---

## Philosophy

Performance is user experience.

A beautiful page that loads slowly is a failed experience. No amount of visual polish, animation quality, or typography choices compensates for a site that takes 4 seconds to become interactive.

Performance is a design concern, not just a development concern. Every image, every font, every JavaScript library, and every animation must earn its place by proving it provides value that justifies its performance cost.

---

## Core Web Vitals

| Metric | Target | What It Measures |
|---|---|---|
| LCP (Largest Contentful Paint) | ≤ 2.5s | Loading performance |
| FID (First Input Delay) | ≤ 100ms | Interactivity |
| CLS (Cumulative Layout Shift) | ≤ 0.1 | Visual stability |
| TTFB (Time to First Byte) | ≤ 800ms | Server response |
| INP (Interaction to Next Paint) | ≤ 200ms | Overall responsiveness |

---

## Performance Budget

Every project must stay within the following budget:

| Resource | Desktop Budget | Mobile Budget |
|---|---|---|
| Total page weight | < 2MB | < 1.5MB |
| Images | < 1MB | < 700KB |
| JavaScript | < 300KB | < 200KB |
| CSS | < 100KB | < 100KB |
| Fonts | < 150KB | < 150KB |
| Total requests | < 30 | < 25 |

---

## Image Optimization

Images are the #1 cause of slow websites.

### Rules
- Always compress images (WebP or AVIF format)
- Serve responsive images via srcset
- Lazy-load below-the-fold images
- Use appropriate dimensions (never serve 4000px wide for a 300px card)
- Decorative images should be CSS backgrounds

```html
<img
  src="hero-400.webp"
  srcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w"
  sizes="(max-width: 768px) 100vw, 50vw"
  alt="Description"
  loading="lazy"
  decoding="async"
  width="800"
  height="600"
/>
```

### Tools
- Squoosh (https://squoosh.app)
- ImageOptim (macOS)
- Sharp (Node.js library)
- Cloudinary / imgix (CDN-based)

---

## Font Optimization

- Use `font-display: swap` to prevent invisible text
- Subset fonts to only the characters needed
- Prefer variable fonts (single file, multiple weights)
- Self-host fonts instead of using Google Fonts CDN (avoids DNS lookup)

```html
<link rel="preload" href="/fonts/inter-variable.woff2" as="font" type="font/woff2" crossorigin>
```

```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/inter-variable.woff2') format('woff2');
  font-display: swap;
  font-weight: 100 900;
}
```

---

## CSS Optimization

- Use Tailwind CSS (purges unused styles in production)
- Avoid @import (blocks rendering)
- Critical CSS inlined in `<head>`
- Defer non-critical CSS

---

## JavaScript Optimization

- Defer non-critical JS using `defer` or `async`
- Vanilla JS preferred over libraries where possible
- GSAP only — avoid jQuery
- Code-split third-party scripts (analytics, maps, chat widgets)
- Lazy-load non-critical JS modules

```html
<script src="/js/app.js" defer></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXX"></script>
```

---

## Animation Performance

| Technique | GPU Accelerated? | Use For |
|---|---|---|
| `transform` (translate, scale, rotate) | Yes | Most animations |
| `opacity` | Yes | Fades, reveals |
| `clip-path` | Yes | Shape reveals |
| `filter` (blur, brightness) | Conditional | Effects — test on mobile |
| `width`, `height`, `top`, `left` | No | Avoid at all costs |

**Always prefer transforms over layout-triggering properties.**

---

## Lighthouse Targets

| Category | Minimum Target |
|---|---|
| Performance | 90+ |
| Accessibility | 90+ |
| Best Practices | 90+ |
| SEO | 90+ |

---

## Performance Testing Process

1. Build complete
2. Run Lighthouse in incognito (desktop + mobile)
3. Check WebPageTest (https://webpagetest.org)
4. Test on real devices (mid-range Android, older iPhone)
5. Check Core Web Vitals in Chrome DevTools Performance panel
6. Fix any red flags before delivery

---

## Anti-Patterns

| Anti-Pattern | Penalty |
|---|---|
| Uncompressed hero image (2MB+) | +3s LCP |
| Google Fonts render-blocking | +300-500ms to FCP |
| No lazy-load on images below fold | +1-2s to load time |
| jQuery included for one selector | +85KB for 3 lines of code |
| Auto-playing video without compression | +2-10MB page weight |
| Importing entire icon library for 5 icons | +100-500KB unused CSS/JS |

---

## Checklist

- [ ] Page weight budget established and met
- [ ] All images compressed, sized, and in WebP/AVIF
- [ ] Images use lazy-loading with explicit width/height
- [ ] Fonts self-hosted with `font-display: swap`
- [ ] Critical CSS inlined (for above-fold content)
- [ ] JS deferred / async — no render-blocking scripts
- [ ] Animations use `transform` and `opacity` only
- [ ] LCP element optimized (hero image or heading)
- [ ] CLS checked — no layout shifts
- [ ] Lighthouse score 90+ all categories
- [ ] Tested on real mobile device

---

## Future Ideas

- Automated performance budget checker in CI pipeline
- "Performance profile" for each client project showing before/after improvements
- Image CDN with automatic format negotiation for all projects
