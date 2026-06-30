# Layout Architecture

## Version 1.0

---

## Layout Philosophy

Layout is hierarchy made visible.

A well-architected layout communicates what matters, what follows, and what to do next — without a single word of instruction.

When a user lands on a page, their eyes should follow a deliberate path:
1. The hero (what is this?)
2. The value (why should I care?)
3. The proof (can I trust them?)
4. The action (what do I do now?)

If the layout does not guide this path, it has failed.

---

## The Section Model

Every page is composed of full-width sections stacked vertically.

### Standard Sections

```
Navigation          — Fixed top, transparent → solid on scroll
Hero                — Full viewport, primary message + CTA
Social Proof        — Logos, awards, stats (optional)
About               — Company/story introduction
Services/Features   — What you offer, card layout
Process             — How you work (optional)
Portfolio/Projects  — Proof of capability
Testimonials        — Social proof
FAQ                 — Address objections (optional)
CTA Section         — Final call to action
Contact             — Form + map + details
Footer              — Links, contact, social, legal
```

### When to Include/Exclude Sections

| Business Type | Must Have | Can Skip |
|---|---|---|
| Construction | Hero, Services, Projects, Testimonials, CTA | FAQ, Blog |
| Restaurant | Hero, Atmosphere, Menu, Location, Booking | Portfolio, Process |
| Real Estate | Hero, Properties, Location, Testimonials, Contact | Process, FAQ |
| SaaS | Hero, Features, Pricing, Testimonials, CTA | Portfolio, About |
| Creative Agency | Hero, Work, Process, Testimonials, Contact | Pricing, FAQ |
| Professional Services | Hero, About, Services, Process, CTA | Gallery, Pricing |

---

## Grid System

### Base Grid
- 12-column grid for desktop
- 6-column for tablet
- 4-column for mobile

### Content Widths

| Breakpoint | Max Width | Columns |
|---|---|---|
| Mobile (< 768px) | 100% - 32px | 4 |
| Tablet (768-1024px) | 720px | 6 |
| Desktop (1024-1440px) | 1100px | 12 |
| Wide (1440px+) | 1200px | 12 |
| Full-width (hero, CTA) | 100% | 12 |

### Column Spanning

```
Full width:         col-span-12
Half width:         col-span-6
Third width:        col-span-4
Quarter width:      col-span-3
Two-thirds:         col-span-8
Content + sidebar:  col-span-8 + col-span-4
```

---

## Vertical Rhythm

Section padding should follow the 8px system.

| Section Type | Padding Top | Padding Bottom |
|---|---|---|
| Hero | 96px (or 0 with full-bleed) | 64px |
| Standard section | 96px | 96px |
| Compact section | 64px | 64px |
| CTA section | 96px | 96px |
| Footer | 64px | 32px |

### Section Spacing Rule

Adjacent sections of the same background color should have 0 gap between them. Adjacent sections of different background colors should have 0 gap between them (the padding creates separation).

---

## The Hero Layout

The hero is the most important layout element. It must communicate:
- Who you are (or what this is)
- What you offer (in one clear sentence)
- What to do next (one primary CTA)

### Hero Variations

**Centered** (best for most businesses)
```
[Logo/Name — centered]
[Headline — large, centered]
[Subheadline — smaller, centered]
[CTA Button — centered]
[Background — full-bleed image or video]
```

**Split** (best for features, product)
```
[Left: Headline + Subheadline + CTA]
[Right: Image or illustration]
```

**Full-screen** (best for luxury, real estate, tourism)
```
[Headline — bottom-left aligned]
[Subheadline — below headline]
[CTA — below subheadline]
[Scroll indicator — bottom center]
[Background — cinematic image or video]
```

---

## Card Layouts

### 3-Column Grid (Default)
```
[Card 1] [Card 2] [Card 3]
— Best for 3 services, 3 features, 3 projects
— Cards wrap to 2 columns on tablet, 1 on mobile
```

### 2-Column Grid
```
[Card 1] [Card 2]
— Best for detailed content, case studies
— Stacks on mobile
```

### 4-Column Grid (Use sparingly)
```
[1] [2] [3] [4]
— Best for icon-only features, team members
— Wraps to 2 on tablet, 1 on mobile
```

### Masonry
```
[ 1 ] [ 2 ]
[  3  ] [ 4 ]
[ 5 ] [  6  ]
— Best for portfolios, galleries
— Requires JS or CSS columns
```

---

## The F-Pattern

For content-heavy pages (about, process), arrange content in the F-pattern:

```
Headline (left-aligned)
Body text (left-aligned)
[List or bullet points]
[Supporting image or diagram]
```

The F-pattern matches natural reading behavior (left-to-right, top-to-bottom).

---

## Whitespace

Whitespace is not empty space. It is breathing room for the eyes.

### When to Increase Whitespace
- Luxury / premium brands
- Low word count pages
- Single CTA hero sections

### When to Decrease Whitespace
- Information-heavy pages (FAQ, pricing)
- Dashboard-like layouts
- Content-rich storytelling pages

### The Whitespace Trap

Too much whitespace on a content page makes it feel sparse. Too little on a luxury page makes it feel cheap. Balance is contextual.

---

## Responsive Breakpoints

```
375px   — Small mobile
768px   — Tablet portrait
1024px  — Tablet landscape / small desktop
1440px  — Desktop
1920px  — Wide
```

### Mobile-First Stacking Rule

Every multi-column layout must be tested at 375px. If it does not clearly communicate its message in a single column, redesign it.

---

## Anti-Patterns

| Anti-Pattern | Why |
|---|---|
| Content that spans 100% width on desktop | Hard to read, line length too long |
| Different max-widths on different sections | Feels inconsistent, disjointed |
| Cards with different heights in the same row | Breaks visual alignment (use match-height) |
| No clear visual hierarchy | User does not know where to look first |
| Content buried below the fold without indication | User leaves before scrolling |
| Inconsistent section padding | Feels unplanned, unprofessional |

---

## Checklist

- [ ] Section order follows logical narrative
- [ ] Grid system used consistently (12/6/4)
- [ ] Hero communicates value + CTA in under 3 seconds
- [ ] F-pattern used for content-heavy sections
- [ ] Section padding follows 8px system
- [ ] Cards in the same row have equal height
- [ ] Layout tested at 375, 768, 1024, 1440px
- [ ] Max line length < 75 characters for body text
- [ ] Whitespace is intentional, not accidental
- [ ] No full-width content without a max-width container

---

## Future Ideas

- Section builder tool — drag-and-drop section ordering
- Layout template generator from industry selection
- "Mobile-first audit" — automated check of layout at all breakpoints
