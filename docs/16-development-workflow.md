# Development Workflow

## Version 1.0

---

## Philosophy
Code is a means to an end — that end is a premium user experience. Every line of code should serve the emotional outcome, the performance budget, and the maintainability of the system.

---

## Project Setup

### Step 1: Initialize
```bash
mkdir project-name
cd project-name
git init
echo "node_modules/\n.DS_Store\n*.log" > .gitignore
```

### Step 2: Create Structure
```
project/
├── index.html
├── assets/
│   ├── images/
│   ├── icons/
│   └── fonts/
├── css/
│   ├── style.css
│   ├── components.css
│   ├── animations.css
│   └── responsive.css
├── js/
│   ├── app.js
│   ├── animations.js
│   └── utils.js
└── README.md
```

### Step 3: CDN Includes (in `<head>`)
```html
<!-- Tailwind -->
<script src="https://cdn.tailwindcss.com"></script>
<!-- GSAP -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<!-- Lenis -->
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>
<!-- Lucide -->
<script src="https://unpkg.com/lucide@latest"></script>
```

### Step 4: Initialize (end of `<body>`)
```javascript
// Lenis
const lenis = new Lenis({ duration: 1.2 });
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);

// Reduced motion
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  lenis.destroy();
}

// Lucide icons
lucide.createIcons();
```

---

## Build Order

1. **HTML structure** — semantic markup, sections in order
2. **Tailwind styling** — layout, spacing, colors, responsive
3. **CSS custom** — overrides, keyframes, glass effects
4. **Navigation** — scroll behavior, mobile menu, active states
5. **Hero animation** — The Awakening timeline
6. **Section reveals** — The Cascade with ScrollTrigger
7. **Micro-interactions** — button hover, card hover, counters
8. **Forms** — validation, submission, states
9. **Performance** — images, lazy-loading, font optimization
10. **Accessibility** — contrast, keyboard, screen readers, reduced motion
11. **QA** — Lighthouse, real device testing, edge cases

---

## Code Quality Standards

| Standard | Requirement |
|---|---|
| Indentation | 2 spaces |
| Max line length | 100 characters |
| Naming | kebab-case for CSS classes, camelCase for JS |
| Comments | Explain WHY, not WHAT |
| No dead code | Unused styles/scripts removed before deploy |
| No console.log in production | Stripped before deploy |

---

## Performance Checklist (Every Project)

- [ ] All images: WebP, lazy-loaded, explicit width/height
- [ ] Fonts: self-hosted or preloaded, `font-display: swap`
- [ ] JS: `defer` or placed before `</body>`
- [ ] CSS: Tailwind purged (production build)
- [ ] No render-blocking resources above the fold
- [ ] Lighthouse: Performance 90+, Accessibility 90+
- [ ] Page weight: < 2MB desktop, < 1.5MB mobile
- [ ] No jQuery or other heavy libraries

---

## Deployment

```bash
# Vercel (recommended)
vercel --prod

# Cloudflare Pages
npm run build  # if using build step
# or drag folder to Cloudflare dashboard

# GitHub Pages
git push origin main
# Settings → Pages → Source: main branch /root
```

---

## Anti-Patterns

| Anti-Pattern | Why |
|---|---|
| Starting with CSS before HTML | Structure determines styling |
| Writing JS before content works | Animations should enhance, not depend on, content |
| No git until the end | Lose work, no history |
| Testing only on desktop | Mobile users are 60%+ of traffic |
| One giant JS file | Hard to maintain, no separation of concerns |
| Forgetting reduced-motion | Excludes users with vestibular disorders |
