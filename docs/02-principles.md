# Principles

## Version 1.0

---

## Overview

Principles are not suggestions. They are decision-making frameworks. When a designer or developer faces ambiguity, principles resolve it.

If a choice violates a principle, it is the wrong choice — regardless of how good it looks.

---

## The 8 Principles

### 1. Emotion First

Every design decision must first answer: *What should the user feel?*

- If the emotion is trust → use stable layouts, blue/navy tones, clear hierarchy
- If the emotion is excitement → use dynamic motion, contrasting accents, bold type
- If the emotion is calm → use generous whitespace, soft tones, slow transitions

**Validation:** Before building, write the target emotion in one word. After building, test: does this page evoke that word?

---

### 2. Motion with Meaning

Every animation must serve one of three purposes:
- **Guide** — direct attention to an element or action
- **Feedback** — confirm an action or state change
- **Narrative** — reveal content in a sequence that tells a story

**Validation:** If an animation can be removed and the experience is unchanged, remove it.

---

### 3. The 60-30-10 Color Rule

- 60% — Dominant (backgrounds, large surfaces)
- 30% — Secondary (headers, cards, sections)
- 10% — Accent (CTAs, highlights, interactive elements)

**Validation:** If the accent color appears on more than 10% of the visible surface, reduce it.

---

### 4. The 8px Grid

All spacing, padding, margins, and sizing must be multiples of 8:
4, 8, 16, 24, 32, 48, 64, 96, 128

**Rationale:** Consistent rhythm creates subconscious comfort. Irregular spacing creates visual noise.

**Validation:** Measure any gap between elements. If it is not an 8px multiple, fix it.

---

### 5. Mobile First

Design for 375px width before 1440px.

**Rationale:** Constraints breed creativity. Starting with small screens forces prioritization of content and functionality. Desktop is the expansion, not the starting point.

**Validation:** Every section must pass visual review at 375px before being extended to larger breakpoints.

---

### 6. Performance is UX

- 0–1s load: user feels seamless
- 1–2.5s load: user notices but tolerates
- 2.5s+ load: user abandonment increases by 53%

**Rationale:** No amount of visual polish compensates for a slow experience.

**Validation:** Every page must score 90+ on Lighthouse performance before delivery.

---

### 7. One Primary Action Per View

Each viewport should have exactly one primary action.

**Rationale:** Choice paralysis reduces conversion. When a visitor sees one clear action, they take it. When they see 5, they leave.

**Validation:** Cover all CTAs except the primary one. If the page still communicates its purpose, keep them covered.

---

### 8. The 3-5 WOW Rule

Every website must have 3 to 5 memorable moments — never more, never fewer.

**Examples of a WOW moment:**
- Hero text reveal animation
- Scroll-triggered image parallax
- Animated statistics counter
- Smooth card hover with depth change
- Loading screen that transitions into content

**Validation:** List the 3-5 WOW moments. If any do not elicit a genuine emotional response, replace them.

---

## Principle Priority

When principles conflict, use this hierarchy:

1. Emotion First
2. Performance is UX
3. Mobile First
4. One Primary Action
5. Motion with Meaning
6. 3-5 WOW Rule
7. 8px Grid
8. 60-30-10 Color Rule

---

## Anti-Patterns

| Anti-Pattern | Principle Violated |
|---|---|
| 6 CTAs on the hero | One Primary Action |
| 400kb of animation JS | Performance is UX |
| Desktop-only design | Mobile First |
| Random padding values | 8px Grid |
| 8 different colors used | 60-30-10 Color Rule |
| 15 animated elements per page | 3-5 WOW Rule / Motion with Meaning |
| Animation that serves no purpose | Motion with Meaning |

---

## Checklist

- [ ] Each section has a defined emotional target
- [ ] All animations serve guide / feedback / narrative
- [ ] Colors follow 60-30-10
- [ ] Spacing follows 8px grid
- [ ] Design works at 375px, 768px, 1024px, 1440px
- [ ] Page scores 90+ on Lighthouse Performance
- [ ] Exactly one primary CTA per viewport
- [ ] Exactly 3-5 WOW moments identified
