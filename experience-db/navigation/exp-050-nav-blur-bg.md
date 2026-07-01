# Experience 050: Background Blur Navigation

## Classification
Narrative

## Emotion
Clarity → Sophistication

## Difficulty
★★☆☆☆

## Performance Impact
Low

## Libraries
GSAP, ScrollTrigger

---

## Description

The navigation bar's background blur intensity increases as the user scrolls down the page. At the top of the page, the nav may be fully transparent or have minimal blur. As content scrolls underneath, the blur intensifies, maintaining legibility of the nav text while revealing page content behind.

Use on any page with a fixed/sticky header where you want the nav to feel integrated with the content rather than floating above it.

---

## Timeline

| Moment | Scroll Position | Element | Action | Duration | Ease |
|---|---|---|---|---|---|
| 1 | 0-100px | Nav background | `opacity` 0 → 1 | 100px scroll | Power2.out |
| 2 | 0-100px | Nav backdrop-filter | `blur(0px)` → `blur(12px)` | 100px scroll | Power2.out |
| 3 | 100px+ | Nav | Full blur, solid background | — | — |

---

## Psychology

- **Content Integration:** A blurring background behind the nav maintains visual connection with the page content.
- **Progressive Enhancement:** The nav starts minimal and gains visual weight as needed — reducing initial visual clutter.
- **Depth Signaling:** The blur creates a clear visual layer separation between nav and content, reinforcing hierarchy.

---

## Implementation

```html
<nav class="blur-nav" style="position: fixed; top: 0; left: 0; right: 0; z-index: 100; padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; font-family: system-ui;">
  <div class="blur-nav-bg" style="position: absolute; inset: 0; background: rgba(26,26,46,0.85); backdrop-filter: blur(0px); -webkit-backdrop-filter: blur(0px); opacity: 0; z-index: -1;"></div>
  <div class="blur-nav-border" style="position: absolute; bottom: 0; left: 0; right: 0; height: 1px; background: rgba(255,255,255,0.05); opacity: 0; z-index: -1;"></div>
  <span class="nav-logo" style="color: white; font-weight: 700; font-size: 1.25rem; position: relative; z-index: 1;">Lumary</span>
  <div class="nav-links" style="display: flex; gap: 2rem; position: relative; z-index: 1;">
    <a href="#" style="color: rgba(255,255,255,0.7); text-decoration: none;">Features</a>
    <a href="#" style="color: rgba(255,255,255,0.7); text-decoration: none;">Pricing</a>
    <a href="#" style="color: rgba(255,255,255,0.7); text-decoration: none;">About</a>
  </div>
</nav>

<div style="height: 200vh; padding-top: 80px; color: white; font-family: system-ui;">
  <p style="padding: 2rem;">Scroll down to see the navigation blur intensify.</p>
</div>
```

```javascript
gsap.registerPlugin(ScrollTrigger);

const navBg = document.querySelector('.blur-nav-bg');
const navBorder = document.querySelector('.blur-nav-border');
const navLinks = document.querySelectorAll('.nav-links a');

ScrollTrigger.create({
  start: 'top top',
  end: '100px',
  scrub: true,
  onUpdate: (self) => {
    const progress = self.progress;

    gsap.to(navBg, {
      opacity: progress,
      backdropFilter: `blur(${progress * 12}px)`,
      duration: 0.1,
      ease: 'none',
      overwrite: 'auto'
    });

    gsap.to(navBorder, {
      opacity: progress,
      duration: 0.1,
      ease: 'none',
      overwrite: 'auto'
    });

    navLinks.forEach(link => {
      gsap.to(link, {
        color: `rgba(255,255,255,${0.5 + progress * 0.5})`,
        duration: 0.1,
        ease: 'none',
        overwrite: 'auto'
      });
    });
  }
});

// Reduced motion
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  gsap.set(navBg, { opacity: 1, backdropFilter: 'blur(12px)' });
  gsap.set(navBorder, { opacity: 1 });
  ScrollTrigger.getAll().forEach(st => st.disable());
}
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Creative Agency | ★★★★★ | Portfolio sites |
| Technology | ★★★★★ | Product landing pages |
| Media / Blog | ★★★★☆ | Content sites |
| Luxury | ★★★★☆ | Brand experience |
| E-commerce | ★★★★☆ | Brand-forward stores |

---

## Accessibility Notes

- Navigation text must have sufficient contrast against all background blur levels
- `backdrop-filter` is purely visual — navigation must work without it
- `prefers-reduced-motion: reduce` — apply full blur immediately on load
- Ensure keyboard focus indicators are visible against variable backgrounds

---

## Performance Notes

- `backdrop-filter` is GPU accelerated in modern browsers
- `opacity` changes are compositor-only
- Avoid animating `background-color` directly — use the opacity of an overlay element
- `-webkit-backdrop-filter` for Safari support (vendor prefix needed)

---

## Variants

### Variant A: Color Shift Nav
Nav background transitions from transparent to a solid brand color as scroll progresses.

### Variant B: Nav Shrink
Nav height reduces (padding scales down) as user scrolls — creates more space for content.

### Variant C: Reveal Nav Items
Secondary nav items (icons, search, avatar) fade in as scroll progresses and the nav becomes "active."

---

## Anti-Patterns

- No backdrop-filter fallback — some browsers (Firefox on Linux) may not support it
- Animating the filter on the entire nav instead of a separate background element — repaints the whole nav
- Blur too strong (> 20px) — disorienting background distortion
- No minimum contrast — white text on light page content blurred is still unreadable

---

## Checklist

- [ ] `backdrop-filter` fallback (solid background) for unsupported browsers
- [ ] `-webkit-backdrop-filter` for Safari
- [ ] Text contrast ≥ 4.5:1 at all scroll positions
- [ ] Reduced motion: full blur immediately
- [ ] Scroll distance ≤ 200px before full blur
