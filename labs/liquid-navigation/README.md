# Liquid Navigation — Lumary OS Lab

## Concept
A morphing navigation bar that transitions between a thick (80px) prominent state and a sleek (60px) minimal floating element as the user scrolls. Links feature a magnetic hover effect where text subtly shifts toward the cursor, creating a responsive, organic feel.

## Approach
- **Scroll morph**: CSS class `.scrolled` toggled on `<nav>` at `scrollY > 100px`. CSS custom properties control dimensions, blur, and alpha for clean separation of concerns.
- **Magnetic hover**: JS `mousemove` computes cursor-to-center delta per link, applies clamped `translate()` on `.link-text` span. Radial gradient glow follows cursor via `--mx`/`--my` custom properties.
- **Glassmorphism**: `backdrop-filter: blur(18px)` with semi-transparent background activates on scrolled state. `will-change` hints and `requestAnimationFrame` throttling keep performance at 60fps.
- **Responsive**: Hamburger menu at 768px breakpoint with slide-in panel using `translateX`. Backdrop-filter toggled only when scrolled on mobile.
- **Zero dependencies**: Pure HTML + CSS + vanilla JS. No CDN, no GSAP, no libraries.

## Notes
- Custom easing `cubic-bezier(0.22, 1, 0.36, 1)` used for the nav morph — gives a soft deceleration feel.
- All transitions limited to GPU-composited properties (`transform`, `opacity`, `backdrop-filter`) to avoid layout recalculations.
- Magnetic displacement capped at 4px to keep the effect subtle and non-distracting.
- Dark theme with purple accent (`#6c5ce7`) and frosted-glass overlays for a premium aesthetic.
