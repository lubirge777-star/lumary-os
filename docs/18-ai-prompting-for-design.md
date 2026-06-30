# AI Prompting for Design

## Version 1.0

---

## Philosophy
AI is not a replacement for design thinking. It is a multiplier. The quality of the output is directly proportional to the quality of the input prompt.

Lumary OS provides structured prompts for both Stitch (UI mockup generation) and OpenCode (code implementation). This chapter documents the methodology behind effective prompting.

---

## The Anatomy of a Good Prompt

| Component | Purpose | Example |
|---|---|---|
| Role | Who is the AI acting as? | "You are a senior UI/UX designer at a premium digital studio." |
| Context | What is the project? | "Building a landing page for a luxury construction company." |
| Constraints | What are the boundaries? | "Dark mode only, max 2 fonts, 60-30-10 color rule." |
| Output format | What do you want back? | "HTML file with embedded Tailwind and GSAP." |
| Examples | Reference style | "Similar to Apple's design language — minimalist, spacious." |
| Anti-patterns | What to avoid | "No gradients, no bouncing animations, no stock photos." |

---

## Prompt Templates by Use Case

### UI Mockup (Stitch)
```
Create a [STYLE] landing page for a [INDUSTRY] business.
Style: Minimal, premium, dark mode
Sections: Hero, Services, Portfolio, Testimonials, CTA, Footer
Colors: Primary [HEX], Accent [HEX]
Typography: [Font] for headings, [Font] for body
Key requirement: [SPECIFIC NEED]
```

### Code Implementation (OpenCode)
```
Build a premium landing page for [CLIENT] using HTML + Tailwind + GSAP.
- Dark theme with [COLOR] accent
- Hero: The Awakening experience (staggered reveal)
- Sections: scroll-triggered fade-in (The Cascade)
- Cards: hover lift effect
- Stats: counter animation on scroll
- Navigation: transparent → glassmorphism
- Mobile-first responsive
- prefers-reduced-motion respected
- No jQuery, no unnecessary dependencies
```

### Animation Request
```
Implement Experience [NUMBER] from Lumary OS Experience Database.
Project: [NAME]
Section: Hero
Adjustments: [SPEED, COLORS, CONTENT]
Reduced motion: [FALLBACK BEHAVIOR]
```

---

## Iteration Strategy

Never accept the first output. Always refine:

1. **First prompt**: Broad request (the mockup/design)
2. **Second prompt**: Specific refinements ("Make the heading larger, reduce card count to 3")
3. **Third prompt**: Edge cases ("What does this look like on mobile?")
4. **Fourth prompt**: Performance ("Optimize images, reduce JS")

---

## Anti-Patterns in Prompting

| Anti-Pattern | Why |
|---|---|
| "Make it look good" | Too vague — specify what "good" means |
| One-shot expectation | Good results require iteration |
| No context | AI cannot read minds — explain the project |
| Over-constraining | Too many rules = generic output |
| Ignoring AI limitations | AI cannot test, cannot see, cannot validate |
