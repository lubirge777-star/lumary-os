# Responsive Strategy

## Version 1.0

---

## Philosophy
We design mobile first. Desktop is the expansion, not the starting point. Every layout must work beautifully at 375px before we add a single desktop breakpoint.

---

## Breakpoint System

| Name | Width | Device |
|---|---|---|
| Mobile | 375px | Small phones |
| Mobile+ | 414px | Large phones |
| Tablet | 768px | iPad portrait |
| Tablet+ | 1024px | iPad landscape / small desktop |
| Desktop | 1280px | Standard desktop |
| Wide | 1536px | Large monitors |

---

## Mobile-First Approach

### Step 1: Content Audit
- What is the single most important message for mobile users?
- Strip everything non-essential
- Ensure CTAs are thumb-reachable (bottom of viewport)

### Step 2: Single Column Layout
- All multi-column layouts default to single column on mobile
- Test every section at 375px before expanding

### Step 3: Touch Optimization
| Element | Mobile Requirement |
|---|---|
| Tap targets | Min 44x44px, 8px spacing between |
| Forms | Full-width inputs, large labels |
| Navigation | Bottom or hamburger, not top bar |
| Cards | Full-width, stack vertically |
| Modals | Full-screen on mobile |
| Tables | Horizontal scroll or card view |

### Step 4: Desktop Expansion
At each breakpoint, ask:
- Can this section now support 2 columns?
- Does the navigation have room for full links?
- Can images be larger without slowing load?

---

## Responsive Images

```html
<img
  src="image-400.webp"
  srcset="image-400.webp 400w, image-800.webp 800w, image-1200.webp 1200w"
  sizes="(max-width: 768px) 100vw, (max-width: 1024px) 50vw, 33vw"
  alt="Description"
  loading="lazy"
  decoding="async"
  width="800"
  height="600"
/>
```

---

## Navigation Responsive Behavior

| Breakpoint | Navigation Style |
|---|---|
| < 768px | Hamburger → slide-in menu from right, backdrop overlay |
| 768-1024px | Condensed (icon + short label) |
| 1024px+ | Full horizontal links + CTA button |

---

## Testing Protocol

| Device | Screen | Browser |
|---|---|---|
| iPhone SE | 375px | Safari |
| iPhone 14 | 390px | Safari |
| Samsung Galaxy | 412px | Chrome |
| iPad | 768px | Safari |
| iPad Pro | 1024px | Safari |
| 13" laptop | 1280px | Chrome |
| 27" monitor | 1920px | Chrome |

### Checklist
- [ ] No horizontal scroll at any breakpoint
- [ ] All content readable without zooming
- [ ] All CTAs tappable (44px min)
- [ ] Forms usable on mobile keyboard
- [ ] Images not stretched or cropped awkwardly
- [ ] Navigation usable with one hand
- [ ] Loading time acceptable on 3G
