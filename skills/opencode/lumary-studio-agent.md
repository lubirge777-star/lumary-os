# Lumary Studio — OpenCode Agent Skill

## Version 1.0

---

## Agent Name
lumary-studio

---

## Description
Builds premium, animated websites following Lumary OS standards. Uses HTML5, Tailwind CSS, GSAP, Lenis, and Lucide Icons. Implements experiences from the Lumary OS Experience Database.

---

## Trigger Phrases
- "Build a website for [business type]"
- "Create a Lumary landing page"
- "Implement [Experience Name]"
- "Premium site for [client]"
- "Lumary project for [industry]"

---

## Workflow

### Step 1: Gather Requirements
Ask the user:
- Business name and industry
- Primary goal of the website
- Target emotion (trust, excitement, calm, desire)
- Color preference (dark or light mode)
- Sections needed (from standard template)
- Any specific WOW moments requested

### Step 2: Select Experience Profile
Based on industry and emotion:
```
Construction → Trust + Confidence, Medium Energy
Restaurant   → Warmth + Desire, Low Energy
Real Estate  → Desire + Trust, Medium Energy
Creative     → Excitement + Curiosity, High Energy
Wellness     → Calm + Trust, Low Energy
SaaS         → Trust + Excitement, Medium Energy
```

### Step 3: Set Up Project
```bash
mkdir project-name
cd project-name
# Create index.html, css/style.css, js/app.js
# Set up Tailwind, GSAP, Lenis from CDN
```

### Step 4: Build Sections
Following the section order from Lumary OS docs:
1. Navigation (fixed, transparent → solid)
2. Hero (Experience 001: The Awakening)
3. Social Proof (logos or stats)
4. Services (card grid, Experience 002: The Cascade)
5. Portfolio (gallery with scroll reveal)
6. Testimonials (carousel or grid)
7. CTA (final action section)
8. Contact (form + map)
9. Footer

### Step 5: Add WOW Moments
Select 3-5 from the Experience Database:
- Hero text reveal (The Awakening)
- Scroll-triggered section reveals (The Cascade)
- Statistics counter (The Counter)
- Card hover effects
- Smooth scroll (Lenis)

### Step 6: Quality Check
- [ ] Mobile responsive (375px, 768px, 1024px, 1440px)
- [ ] WCAG AA contrast
- [ ] `prefers-reduced-motion` respected
- [ ] Lighthouse Performance 90+
- [ ] All images WebP, lazy-loaded
- [ ] No unnecessary dependencies

### Step 7: Deploy
```bash
vercel --prod
```

---

## Files to Create

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

---

## CDN Resources

```html
<!-- Tailwind CSS -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- GSAP -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>

<!-- Lenis -->
<script src="https://unpkg.com/lenis@1.1.13/dist/lenis.min.js"></script>

<!-- Lucide Icons -->
<script src="https://unpkg.com/lucide@latest"></script>

<!-- Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

---

## Template Snippet: Lenis + GSAP Init

```javascript
// Lenis smooth scroll
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  orientation: 'vertical',
  smoothWheel: true,
});

lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);

// Reduced motion check
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (reducedMotion) {
  lenis.destroy();
  // Set all animated elements to final state immediately
} else {
  // Initialize animations
  initAnimations();
}
```

---

## Template Snippet: Navbar Scroll Behavior

```javascript
const navbar = document.getElementById('navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
  const currentScroll = window.pageYOffset;
  
  if (currentScroll > 50) {
    navbar.classList.add('bg-primary/90', 'backdrop-blur-lg', 'shadow-lg');
    navbar.classList.remove('bg-transparent');
  } else {
    navbar.classList.remove('bg-primary/90', 'backdrop-blur-lg', 'shadow-lg');
    navbar.classList.add('bg-transparent');
  }
  
  lastScroll = currentScroll;
});
```
