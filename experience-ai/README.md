# Experience AI — AI-Accelerated Experience Architecture

## Why

Lumary OS is a methodology. AI is the accelerator.

This folder defines how AI agents use the Lumary OS methodology to design, generate, and evaluate digital experiences — not replacing human creativity, but removing repetitive work so creators can focus on emotion, story, and craft.

---

## Architecture

```text
Describe the emotion & industry

↓

AI Recommends:
  - Experience Profile (Energy / Formality / Warmth / Depth / Tempo)
  - Story Arc (beginning → middle → end)
  - WOW Moments (3-5 from Experience DB)
  - Layout (section order)
  - Motion (animations per section)
  - Components (patterns to use)
  - Performance Budget
  - Color Palette + Typography

↓

Implementation:
  - One-shot HTML generation (Pro Max skill)
  - Section-by-section build (Lumary Studio skill)
  - Stitch mockup generation (Lumary Designer skill)

↓

Evaluation:
  - Lumary Score calculation
  - ERM audit
  - Improvement suggestions
```

---

## AI Skills in Lumary OS

| Skill | Purpose | Input | Output |
|-------|---------|-------|--------|
| **Lumary Studio** | Build websites following Lumary OS standards | Industry, emotion, sections | Production HTML file |
| **Lumary Designer** | Generate Stitch UI mockups | Industry, style preferences | Stitch prompt |
| **Lumary Pro Max** | One-shot premium websites with design system | Industry, keywords, target emotion | Complete HTML file with data-driven design |

---

## Prompt Architecture

Each AI interaction follows a structured prompt format:

### Design Brief → AI

```text
Build a [EMOTION] website for [INDUSTRY] called [NAME].

Target feeling: [primary emotion]
Industry: [construction / restaurant / saas / etc.]
WOW intensity: [subtle / moderate / bold]
Performance target: [90+ Lighthouse]
Pages: [single-page / multi-page]
```

### AI → Implementation

The AI uses the following chain:

1. **Design System Generation** (ui-ux-pro-max) → colors, fonts, style
2. **Experience Profile Selection** → Energy, Formality, Warmth, Depth, Tempo
3. **Story Architecture** → section order, narrative arc
4. **WOW Selection** → 3-5 experiences from Experience DB
5. **Implementation** → HTML/CSS/JS with Tailwind + GSAP + Lenis
6. **Quality Check** → Lumary Score + ERM dimensions

---

## Future: Experience Recommendation Engine

```text
Emotion + Industry + Budget

↓

Recommendation Engine

↓

Optimized Experience Stack:
  - Hero: [Experience 001: The Awakening]
  - Cards: [Experience 002: The Cascade] with hover lift
  - Stats: [Experience 003: The Counter]
  - Navigation: [Magnetic Nav]
  - Cursor: [Custom cursor with magnetic hover]
  - Smooth scroll: [Lenis]
  - Page transitions: [Morph Transition]

↓

Estimated Lumary Score: 92/100
```

---

## Related Documents

- `docs/18-ai-prompting-for-design.md` — AI prompting methodology
- `skills/opencode/lumary-pro-max.md` — One-shot Pro Max build
- `skills/opencode/lumary-studio-agent.md` — Standard build
- `prompts/opencode/` — All prompt templates
- `metrics/README.md` — Lumary Score system
