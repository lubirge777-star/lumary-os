# Caveats — Honest Limitations

Lumary OS aims high. That's the point. But ambition without honesty is marketing, not methodology.

This document acknowledges where the system makes trade-offs, where claims are aspirational rather than proven, and where exceptions are legitimate.

---

## "People remember emotions, not layouts."

**Status:** Guiding principle, not scientific fact.

**Reality:** People remember a combination of factors — brand familiarity, usefulness, content quality, visual identity, **and** emotional moments. The statement is a heuristic to prioritize emotional design, not a claim that layouts are irrelevant.

**Use as:** A north star. Not a citation.

---

## "90+ Lighthouse or it's not finished."

**Status:** Internal engineering standard, not universal law.

**Reality:** There are legitimate cases where 90+ is impractical:

| Scenario | Typical Score | Acceptable Reason |
|---|---|---|
| Heavy media (video hero, 3D) | 70-85 | Cinematic experience requires assets |
| Third-party integrations (maps, chat, analytics) | 75-90 | External scripts impact perf |
| Legacy CMS constraints | 60-80 | Platform limits control |
| Data-heavy dashboards | 60-85 | Real-time data processing |
| Complex animations | 80-90 | GSAP + Lenis have overhead |

**Exception rule:** If you cannot hit 90+, **document why** in the project report and show that you optimized what you could control (images, fonts, CLS, lazy loading).

---

## Lumary Score — What It Actually Measures

The Lumary Score is a **design quality heuristic**, not a statistically validated instrument.

- The Curiosity and Memory dimensions are **estimates based on design patterns**, not measured user behavior
- Real Curiosity scores require analytics (scroll depth, interaction rate)
- Real Memory scores require user surveys (24-hour recall tests)
- The tool is a **guide for improvement**, not a certification of real-world performance

---

## "54 Cataloged Experiences"

These are **documented patterns with conceptual code**, not all production-tested across every browser and device. Each pattern should be tested before client delivery.

---

## "7 Templates scoring 4.93/5"

The ERM (Experience Review Methodology) audit is an **internal quality assessment**, not a third-party evaluation. The score reflects the system's own quality framework applied by its creators.

---

## Experience Profiles — Artistic, Not Scientific

The five Experience Profiles (Premium Minimal, Energetic Bold, etc.) are **design heuristics**, not empirically derived personas. They are a useful shorthand for aligning design direction but should not replace user research on a specific project.

---

## What Lumary OS Does NOT Do

- **Replace user research** — The system provides design direction, not user insights
- **Replace usability testing** — All projects should still be tested with real users
- **Guarantee conversions** — Experience quality supports conversion but doesn't ensure it
- **Replace accessibility testing** — WCAG AA is the floor, not the ceiling; manual testing required
- **Generate production-ready code without review** — Template code should be audited before deployment

---

## When to Break the Rules

Lumary OS is a methodology, not a religion. Break any rule when:

1. **Client constraints demand it** (budget, timeline, platform limitations)
2. **User research contradicts it** (your audience responds differently)
3. **Performance requires it** (a beautiful animation that hurts UX is bad design)
4. **Accessibility requires it** (prefers-reduced-motion, screen reader compatibility)
5. **The specific context warrants it** (an industrial B2B site may not need the same emotional arc as a luxury brand)

Document the exception and why it was made.
