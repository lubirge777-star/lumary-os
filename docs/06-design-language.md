# Design Language

## Version 1.0

---

## Definition

Design Language is the visual vocabulary of Lumary Studio. It defines how elements look, feel, and relate to each other. It is the implementation of our philosophy and principles into tangible visual rules.

---

## Spacing System

We use an 8px base unit. All spacing, padding, margins, gaps, and element sizing must be a multiple of 8.

```
4     (tiny gap)
8     (tight gap)
16    (standard gap)
24    (comfortable gap)
32    (section gap)
48    (generous gap)
64    (section padding)
96    (large padding)
128   (max padding)
```

**Why 8?** It provides enough granularity for fine-tuning while maintaining consistency across all surfaces. It creates a subconscious rhythm that users perceive as ordered and intentional.

---

## Typography

### Heading Hierarchy

```
H1: 3.5rem (56px) — Hero / Page title
H2: 2.5rem (40px) — Section heading
H3: 2rem   (32px) — Card title
H4: 1.5rem (24px) — Subheading
H5: 1.25rem (20px) — Minor heading
Body: 1rem  (16px) — Paragraph text
Small: 0.875rem (14px) — Captions, metadata
```

### Line Height
- Headings: 1.1–1.2
- Body: 1.6–1.7
- Small: 1.5

### Font Pairing Rules
- Maximum 2 font families per project
- One for headings (serif or sans-serif depending on industry)
- One for body (highly readable sans-serif)
- System font stack acceptable for body if performance is critical

### Recommended Font Combinations
| Industry | Heading | Body |
|---|---|---|
| Luxury | Playfair Display | Inter |
| Corporate | DM Sans | Inter |
| Creative | Space Grotesk | Sora |
| Restaurant | Cormorant Garamond | Nunito |
| Construction | Bebas Neue (all caps) | DM Sans |
| Wellness | Lora | Inter |

---

## Color System

### The 60-30-10 Rule
- **60% Dominant** — Backgrounds, large surfaces (dark or light)
- **30% Secondary** — Cards, sections, headers
- **10% Accent** — CTAs, links, highlights, interactive elements

### Industry Color Palettes

**Construction**
```
Dominant: #0A0A0A (slate-black)
Secondary: #1A1A2E (dark navy)
Accent: #F59E0B (amber)
Surface: #FFFFFF
Text: #F8FAFC
```

**Luxury**
```
Dominant: #0C0C0C (pure black)
Secondary: #1C1C1E (dark gray)
Accent: #D4AF37 (gold)
Surface: #FAFAFA
Text: #F5F5F7
```

**Restaurant**
```
Dominant: #1A0F0A (dark brown)
Secondary: #2D1810 (deep brown)
Accent: #E85D3A (burnt orange)
Surface: #FFF8F0
Text: #F5E6D3
```

**Corporate / SaaS**
```
Dominant: #0F172A (slate-900)
Secondary: #1E293B (slate-800)
Accent: #3B82F6 (blue-500)
Surface: #F8FAFC
Text: #CBD5E1
```

**Wellness**
```
Dominant: #0A1F14 (deep forest)
Secondary: #0D2818 (forest)
Accent: #7EC8A0 (sage green)
Surface: #F0F7F3
Text: #E0EDE6
```

### Accessibility Minimum
- Normal text: 4.5:1 contrast ratio minimum
- Large text (18px+): 3:1 contrast ratio minimum
- UI components: 3:1 minimum against adjacent colors

---

## Border Radius

Use a consistent radius scale:

```
None:   0px     — Buttons (pill), UI elements
Small:  6px     — Inputs, form elements
Medium: 12px    — Cards, containers
Large:  20px    — Modals, hero sections
XLarge: 30px    — Images, decorative elements
```

---

## Shadows

Shadows should be subtle. Never heavy or colored.

```
Sm:   0 1px 3px rgba(0,0,0,0.12)
Md:   0 4px 16px rgba(0,0,0,0.12)
Lg:   0 12px 40px rgba(0,0,0,0.15)
Xl:   0 24px 60px rgba(0,0,0,0.18)
```

---

## Borders

- Default border: 1px solid
- Primary border color: accent color at 20% opacity
- Secondary border color: white at 10% opacity (dark mode) or black at 8% (light mode)
- Focus state: 2px solid accent color with 2px offset

---

## Glassmorphism (Optional Luxury Effect)

Use sparingly — best for navbars, hero overlays, and stat cards.

```
background: rgba(255, 255, 255, 0.05);
backdrop-filter: blur(12px);
border: 1px solid rgba(255, 255, 255, 0.1);
```

**Light mode adjustment:**
```
background: rgba(255, 255, 255, 0.7);
backdrop-filter: blur(12px);
border: 1px solid rgba(0, 0, 0, 0.06);
```

---

## Anti-Patterns

| Anti-Pattern | Why |
|---|---|
| Mixing 3+ border radii | Creates inconsistency, feels sloppy |
| Colored shadows | Feels dated, unprofessional |
| Using opacity for accent colors | Reduces contrast, creates accessibility failures |
| More than 2 font families | Visual chaos, slows performance |
| Random spacing values | Breaks visual rhythm |
| Transparent text on dark backgrounds | Low contrast = hard to read |

---

## Checklist

- [ ] 8px grid used for all spacing
- [ ] Typography hierarchy defined (H1-H5, Body, Small)
- [ ] Max 2 font families per project
- [ ] 60-30-10 color rule applied
- [ ] Industry palette selected
- [ ] All text meets WCAG AA contrast (4.5:1)
- [ ] Consistent border radius used across surfaces
- [ ] Shadows are subtle, not heavy
- [ ] Glassmorphism only in designated surfaces
- [ ] Light and dark modes both tested

---

## Future Ideas

- Interactive color palette generator for clients
- Dynamic typography scale based on viewport width
- "Design Language in 3 clicks" — a tool that generates a full visual spec from an industry selection
