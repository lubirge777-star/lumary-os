# OpenCode Prompt: Request a Specific Experience

## Version 1.0

---

## Purpose
Request a specific Experience from the Experience Database to be implemented in a project.

---

## Template

```
Implement Experience [NUMBER]: [NAME] from Lumary OS Experience Database.

## Context
This experience will be used on the [SECTION NAME] of [COMPANY NAME]'s website ([INDUSTRY]).

## The Experience
[COPY FULL ENTRY FROM experience-db/]

## Project Specifics
- Background asset: [PATH / URL]
- Heading text: "[HEADING]"
- Subtext: "[SUBTEXT]"
- CTA text: "[CTA]"
- CTA link: "[URL]"
- Colors: Match project theme ([HEX COLORS])

## Adjustments
- Duration: [FASTER / SAME / SLOWER] than default
- Mobile adjustments: [NOTES]
- Reduced motion fallback: [NOTES]

## Integration
This section sits between [SECTION ABOVE] and [SECTION BELOW].
The project already has [LIBRARIES ALREADY LOADED].
```

---

## Example

```
Implement Experience 001: The Awakening from Lumary OS Experience Database.

## Context
This experience will be used on the Hero section of Atlas Construct's website (Construction).

## The Experience
[Refer to experience-db/arrival/exp-001-awakening.md]

## Project Specifics
- Background asset: /assets/images/hero-construction.webp
- Heading text: "Build Beyond Boundaries"
- Subtext: "Premium construction services for ambitious projects in Dar es Salaam"
- CTA text: "Start Your Project"
- CTA link: "#contact"
- Colors: Primary #0F172A, Accent #F59E0B, Text #F8FAFC

## Adjustments
- Duration: 1.5x faster than default (Tanzanian audience prefers quicker delivery)
- Mobile: Reduce heading to 2.5rem, remove decorative elements
- Reduced motion: Fade-in only, no parallax
```
