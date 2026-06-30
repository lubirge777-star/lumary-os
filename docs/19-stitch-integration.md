# Stitch Integration Guide

## Version 1.0

---

## Overview
Stitch is used for rapid UI/UX mockup generation. The following workflow ensures every Stitch output is production-ready for OpenCode implementation.

## Workflow

```
Client Brief → Stitch Prompt → Stitch Mockup → Refine → Export Spec → OpenCode Prompt → Implementation
```

## What to Generate in Stitch
- Full landing page layouts (all sections)
- Color palette exploration
- Typography pairings
- Component layout ideas (card grids, hero layouts)
- Mobile views (375px)

## What NOT to Generate in Stitch
- Animations (document in spec only)
- Exact pixel-perfect spacing (Lumary uses 8px system)
- Final copy (placeholders are fine)
- Accessibility details (handled in implementation)

## Export Spec Format
After Stitch generates a mockup, document this spec:

```
## Colors
Primary: #XXXXXX
Secondary: #XXXXXX
Accent: #XXXXXX
Surface: #XXXXXX
Text: #XXXXXX

## Typography
Headings: [Font Name]
Body: [Font Name]

## Section Order
1. Navigation
2. Hero (full viewport, centered/split)
3. [Section Name]
4. ...

## Animation Opportunities
- Hero: word stagger
- Services: card cascade on scroll
- Stats: counter on scroll
- ...

## Notes
- Mobile nav: hamburger → slide-in
- Glassmorphism on scroll
```
