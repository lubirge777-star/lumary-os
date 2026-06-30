# OpenCode Prompt: Implement from Stitch Design

## Version 1.0

---

## Purpose
Convert a Stitch-generated mockup into production-ready HTML/CSS/JS code using OpenCode, following Lumary OS standards.

---

## Prompt Template

```
Build a premium, fully animated landing page for [COMPANY NAME] ([INDUSTRY]).

## Technology Stack
- HTML5
- Tailwind CSS (via CDN or build)
- Vanilla JavaScript (ES6+)
- GSAP (from CDN)
- Lenis (smooth scroll)
- Lucide Icons (from CDN)
- Google Fonts: [FONT PAIRING]

## Design System
- Primary color: [HEX] (backgrounds, large surfaces)
- Secondary color: [HEX] (cards, sections)
- Accent color: [HEX] (CTAs, highlights)
- Surface color: [HEX] (content containers)
- Text color: [HEX]
- Border radius: medium (12px)
- Spacing system: 8px grid (16, 24, 32, 48, 64, 96)

## Sections (in order)
[LIST SECTIONS FROM STITCH MOCKUP]

## Animation Requirements
- Hero: The Awakening experience (staggered text + CTA reveal on load)
- Section reveals: The Cascade (scroll-triggered fade-in + translate)
- Cards: hover lift effect (y: -8px, shadow increase, 300ms)
- Statistics: The Counter (animate numbers on scroll)
- Navigation: transparent → glassmorphism on scroll
- Overall: Lenis smooth scroll enabled

## Quality Standards
- Mobile-first responsive (375px, 768px, 1024px, 1440px)
- WCAG AA contrast (4.5:1 text)
- prefers-reduced-motion respected
- Lighthouse Performance 90+
- All images: WebP format, lazy-loaded, explicit dimensions
- No jQuery, no unnecessary dependencies
- Clean, commented code following Lumary OS standards

## WOW Moments (3-5)
1. [MOMENT 1]
2. [MOMENT 2]
3. [MOMENT 3]
4. [MOMENT 4] (optional)
5. [MOMENT 5] (optional)
```

---

## Implementation Workflow

### Step 1: Foundation
```
1. Create project folder and index.html
2. Set up Tailwind CSS config
3. Set up font loading
4. Create CSS structure (style.css, animations.css, responsive.css)
5. Create JS structure (app.js, animations.js, utils.js)
```

### Step 2: Structure
```
6. Build HTML sections in order (Hero → ... → Footer)
7. Apply Tailwind utility classes for layout
8. Add responsive breakpoints
9. Ensure semantic HTML and ARIA attributes
```

### Step 3: Animations
```
10. Initialize Lenis
11. Create GSAP timeline per section
12. Add scroll triggers for reveals
13. Add micro-interactions (hover, click)
14. Test prefers-reduced-motion
```

### Step 4: Polish
```
15. Optimize all images
16. Test at all breakpoints
17. Run Lighthouse audit
18. Test keyboard navigation
19. Deploy to Vercel
```

---

## Common Patterns to Include

### Navigation
```html
<nav class="fixed top-0 left-0 right-0 z-50 transition-all duration-300"
     id="navbar">
  <div class="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
    <a href="/" class="text-xl font-bold">Logo</a>
    <div class="hidden md:flex items-center gap-8">
      <a href="#services">Services</a>
      <a href="#work">Work</a>
      <a href="#contact">Contact</a>
    </div>
    <button class="md:hidden" aria-label="Menu">☰</button>
  </div>
</nav>
```

### Hero (The Awakening)
```html
<section class="hero min-h-screen flex items-center justify-center relative overflow-hidden">
  <div class="hero-bg absolute inset-0">
    <img src="hero.webp" alt="" class="w-full h-full object-cover"
         loading="eager" />
    <div class="absolute inset-0 bg-black/50"></div>
  </div>
  <div class="hero-content relative z-10 text-center max-w-4xl px-6">
    <h1 class="hero-heading text-5xl md:text-7xl font-bold text-white mb-6">
      Build Beyond Boundaries
    </h1>
    <p class="hero-subtext text-lg md:text-xl text-gray-300 mb-8 max-w-2xl mx-auto">
      Premium construction services for ambitious projects.
    </p>
    <a href="#contact" class="hero-cta inline-block px-8 py-4 bg-accent text-white rounded-xl font-semibold
                              hover:bg-accent-light transition-all duration-300">
      Start Your Project
    </a>
  </div>
</section>
```

### Section Reveal (The Cascade)
```html
<section class="py-24 px-6">
  <div class="max-w-6xl mx-auto">
    <h2 class="text-4xl font-bold mb-16 text-center">Our Services</h2>
    <div class="grid md:grid-cols-3 gap-8">
      <div class="card p-8 rounded-xl border border-white/10 bg-secondary
                  hover:-translate-y-2 hover:shadow-xl transition-all duration-300 cursor-pointer">
        <div class="w-12 h-12 bg-accent/20 rounded-lg flex items-center justify-center mb-6">
          <i data-lucide="building-2" class="w-6 h-6 text-accent"></i>
        </div>
        <h3 class="text-xl font-semibold mb-3">General Construction</h3>
        <p class="text-muted">Description of service goes here.</p>
      </div>
      <!-- Repeat cards -->
    </div>
  </div>
</section>
```

---

## Quick Reference

| Element | Tailwind Classes | GSAP | Notes |
|---|---|---|---|
| Nav | `fixed top-0 z-50` | `y` on scroll | Glassmorphism on scroll |
| Hero heading | `text-5xl md:text-7xl font-bold` | stagger words | SplitType or manual spans |
| Cards | `rounded-xl border p-8` | hover: `y: -8` | Match height in row |
| CTA button | `px-8 py-4 rounded-xl font-semibold` | hover: scale 1.02 | Accent color |
| Section | `py-24 px-6` | ScrollTrigger reveal | 96px padding |
| Gallery | `grid grid-cols-2 md:grid-cols-3 gap-4` | stagger grid items | Lazy load images |
| Stats | `text-5xl font-bold` | Counter animation | ScrollTrigger |
| Footer | `py-16` | none | Links + social + legal |
