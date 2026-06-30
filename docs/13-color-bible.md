# Color Bible

## Version 1.0

---

## Philosophy

Color is the fastest way to communicate emotion.

Before a user reads a single word, their brain has already processed the color palette and formed an emotional impression. This happens in under 100 milliseconds.

Color is not decoration. It is psychological signaling.

---

## The 60-30-10 Rule

- **60% Dominant** — Backgrounds, large surfaces
- **30% Secondary** — Cards, sections, navigation
- **10% Accent** — CTAs, links, highlights, interactive elements

---

## Industry Color Palettes

### Construction & Engineering

```
Primary:   #0F172A (Slate-900)     — Trust, stability
Secondary: #1E293B (Slate-800)     — Depth, structure
Accent:    #F59E0B  (Amber-500)    — Energy, attention
Surface:   #FFFFFF                  — Clarity
Text:      #F8FAFC  (Slate-50)     — Readability
Muted:     #94A3B8  (Slate-400)    — Secondary info
Success:   #22C55E  (Green-500)    — Completed projects
```

**Psychology:** Dark slate communicates solidity and professionalism. Amber accents add approachability without sacrificing seriousness.

**Best for:** Construction firms, engineering companies, architecture studios, real estate developers.

---

### Luxury & Premium

```
Primary:   #0C0C0C                  — Exclusivity, power
Secondary: #1C1C1E                  — Depth, richness
Accent:    #D4AF37  (Gold)          — Prestige, quality
Surface:   #FAFAFA                  — Purity
Text:      #F5F5F7                  — Elegance
Muted:     #8E8E93                  — Subtlety
Success:   #34C759                  — Quality verified
```

**Psychology:** Near-black backgrounds create a canvas that feels expensive. Gold accents signal premium quality without ostentation.

**Best for:** Luxury goods, premium services, high-end real estate, fine dining.

---

### Restaurant & Hospitality

```
Primary:   #1A0F0A                  — Warmth, earthiness
Secondary: #2D1810                  — Depth, richness
Accent:    #E85D3A  (Burnt Orange)  — Appetite, energy
Surface:   #FFF8F0                  — Warmth, comfort
Text:      #F5E6D3                  — Soft readability
Muted:     #A08068                  — Earthy secondary
Success:   #4CAF50                  — Fresh ingredients
```

**Psychology:** Warm browns and oranges stimulate appetite and create a cozy atmosphere. The cream surface feels natural and inviting.

**Best for:** Restaurants, cafes, hotels, bakeries, catering services.

---

### Corporate & SaaS

```
Primary:   #0F172A (Slate-900)     — Professionalism
Secondary: #1E293B (Slate-800)     — Stability
Accent:    #3B82F6  (Blue-500)     — Trust, technology
Surface:   #F8FAFC                  — Clean, modern
Text:      #CBD5E1  (Slate-300)    — Readability
Muted:     #64748B  (Slate-500)    — Secondary info
Success:   #22C55E  (Green-500)    — Growth
Error:     #EF4444  (Red-500)      — Alerts
```

**Psychology:** Blue is the most trusted color across cultures. Paired with clean slate tones, it communicates reliability and technological competence.

**Best for:** SaaS products, B2B services, financial technology, professional services.

---

### Healthcare & Wellness

```
Primary:   #0A1F14                  — Nature, health
Secondary: #0D2818                  — Stability, growth
Accent:    #7EC8A0  (Sage Green)    — Healing, calm
Surface:   #F0F7F3                  — Clean, sterile
Text:      #E0EDE6                  — Soft readability
Muted:     #8FA89B                  — Calm secondary
Success:   #4CAF50                  — Health positive
Error:     #E57373                  — Medical alert
```

**Psychology:** Greens are associated with health, nature, and renewal. The sage accent is calming without feeling cold.

**Best for:** Medical practices, wellness centers, spas, fitness brands, mental health services.

---

### Creative Studio

```
Primary:   #0A0A0A                  — Canvas, focus
Secondary: #18181B                  — Subtle depth
Accent:    #A855F7  (Purple-500)    — Creativity, originality
Surface:   #FAFAFA                  — Clean presentation
Text:      #F4F4F5                  — Readability
Muted:     #71717A                  — Technical info
Success:   #10B981                  — Project delivered
```

**Psychology:** Black backgrounds make creative work pop. Purple accents signal imagination and artistic confidence.

**Best for:** Creative agencies, design studios, production companies, artist portfolios.

---

### Education

```
Primary:   #0F172A                  — Academic seriousness
Secondary: #1E293B                  — Structured learning
Accent:    #F97316  (Orange-500)    — Curiosity, energy
Surface:   #FAFAFA                  — Clean, focused
Text:      #CBD5E1                  — Readability
Muted:     #64748B                  — Calm secondary
Success:   #22C55E                  — Achievement
```

**Psychology:** Orange stimulates curiosity and mental engagement. Paired with academic blues, it balances energy with seriousness.

**Best for:** Schools, universities, e-learning platforms, tutoring services.

---

### E-commerce & Retail

```
Primary:   #0F172A                  — Premium foundation
Secondary: #1E293B                  — Product focus
Accent:    #F43F5E  (Rose-500)      — Urgency, desire
Surface:   #FFFFFF                  — Product clarity
Text:      #0F172A                  — Readability
Muted:     #94A3B8                  — Pricing details
Success:   #22C55E                  — Purchased
Sale:      #EF4444                  — Discount
```

**Psychology:** Rose accents create desire and urgency. The dark/light contrast keeps product imagery as the focus.

**Best for:** Online stores, fashion retail, product showcases, marketplaces.

---

### Technology & AI

```
Primary:   #020617                  — Deep tech
Secondary: #0F172A                  — Technical depth
Accent:    #06B6D4  (Cyan-500)      — Innovation, future
Surface:   #F8FAFC                  — Clean interface
Text:      #E2E8F0                  — Readability
Muted:     #64748B                  — Technical data
Success:   #10B981                  — System online
Warning:   #F59E0B                  — AI confidence low
```

**Psychology:** Cyan accents suggest innovation, technology, and forward thinking. Deep navy backgrounds feel advanced and sophisticated.

**Best for:** AI startups, tech platforms, data visualization, automation tools.

---

## Color Properties Reference

| Property | Usage |
|---|---|
| `--color-primary` | Dominant background (60%) |
| `--color-secondary` | Cards, sections (30%) |
| `--color-accent` | CTAs, highlights (10%) |
| `--color-surface` | Content containers, modals |
| `--color-text` | Primary text |
| `--color-text-muted` | Secondary text |
| `--color-success` | Positive states |
| `--color-error` | Error states |
| `--color-warning` | Warning states |

### CSS Variable Template

```css
:root {
  --color-primary: #0F172A;
  --color-secondary: #1E293B;
  --color-accent: #3B82F6;
  --color-surface: #F8FAFC;
  --color-text: #CBD5E1;
  --color-text-muted: #64748B;
  --color-success: #22C55E;
  --color-error: #EF4444;
  --color-warning: #F59E0B;
}
```

---

## Checklist

- [ ] Industry palette selected and matches brand emotion
- [ ] 60-30-10 rule applied
- [ ] All text meets 4.5:1 contrast ratio (AA)
- [ ] Accent color < 10% of visible area
- [ ] CSS variables created for all color roles
- [ ] Colors tested in both light and dark mode
- [ ] Error/success/warning states defined
- [ ] Color chosen for link states (visited, active, hover)
- [ ] No color used as the sole differentiator (accessibility)

---

## Future Ideas

- Interactive palette explorer where users see color psychologies
- "Color audit" tool that analyzes contrast ratios automatically
- Light mode counterparts for each dark palette
