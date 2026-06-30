# Experience 009: The Seamless Page Transition

## Classification
Narrative

## Emotion
Satisfaction

## Difficulty
★★★★☆

## Performance
Medium

## Libraries
GSAP, barba.js (or custom)

---

## Description
When navigating between pages, a smooth transition plays instead of the jarring white flash. Current page content fades/slides out, a transition curtain plays, then new page content enters. Makes multi-page sites feel like a native app.

## Implementation (with barba.js)
```javascript
barba.init({
  transitions: [{
    name: 'slide-transition',
    
    leave(data) {
      return gsap.to(data.current.container, {
        y: -30,
        opacity: 0,
        duration: 0.4,
        ease: 'power2.in'
      });
    },
    
    enter(data) {
      return gsap.from(data.next.container, {
        y: 30,
        opacity: 0,
        duration: 0.5,
        ease: 'power3.out',
        onStart: () => {
          window.scrollTo(0, 0);
        }
      });
    }
  }]
});
```

## Transition Types

| Type | Duration | Best For |
|---|---|---|
| Fade | 400ms | Simple, elegant sites |
| Slide (up) | 500ms | Most applications |
| Crossfade | 600ms | Creative portfolios |
| Curtain | 800ms | Premium/luxury |
| Morph | 1000ms | Experimental |

## When to Use
- Multi-page business websites
- Portfolio with individual project pages
- Agency sites with case studies

## When NOT to Use
- Single-page applications (SPA routing already smooth)
- Content-heavy documentation
- Sites with < 3 pages (over-engineering)

## Anti-Patterns
- No skip transition for back button (use barba.js `prevent` logic)
- Transition > 800ms (user feels stuck)
- Not handling scroll position (new page starts scrolled)
- Broken on slow connections (show fallback)

## Accessibility
- `prefers-reduced-motion`: instant page change, no animation
- Focus management: focus first heading of new page
- `aria-live` region announces page change
