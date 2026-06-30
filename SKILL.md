# Lumary OS — OpenCode Skill

## Name
lumary-os

## Description
Full-stack design system for building premium, animated websites. Includes experience database, pattern library, component bible, motion bible, color bible, psychology atlas, prompt libraries, and client playbooks. Use when building websites that need to feel premium, animated, and conversion-focused.

## Triggers
- "Build a Lumary website"
- "Implement a premium site"
- "Create an animated landing page"
- "Use Lumary design system"
- "Build a website for [industry]"

## Workflow

### 1. Determine Requirements
Ask or extract:
- Business name and industry
- Primary goal
- Target emotion
- Color preference (dark/light)
- Sections needed
- WOW moments (3-5)

### 2. Select Experience Profile
Map industry → emotion → color palette from color-bible/ and docs/13-color-bible.md

### 3. Build Using System
- Use templates/templates/ as starting point
- Add experiences from experience-db/
- Follow patterns from patterns/
- Use component specs from component-bible/
- Reference motion specs from docs/14-motion-bible.md
- Apply psychology from docs/15-psychology-atlas.md

### 4. Quality Check
Run checklist from docs/23-quality-assurance.md
- Visual QA
- Responsive QA (375-1536px)
- Functional QA (all links, forms, interactions)
- Performance QA (Lighthouse 90+)
- Accessibility QA (WCAG AA)
- Content QA (no placeholders)

### 5. Deploy
- Deploy to Vercel
- Verify custom domain and SSL
- Handoff per playbooks/delivery-playbook.md

## Reference Files
- docs/ — All documentation (20+ files)
- experience-db/ — 20+ experience implementations with GSAP code
- patterns/ — 15+ production HTML patterns
- component-bible/ — 5 component systems
- templates/ — 4 industry templates (construction, restaurant, SaaS, real estate)
- color-bible/ — 9 industry palettes
- motion-bible/ — 10 animation recipes
- psychology-atlas/ — 12 cognitive principles
- prompts/ — 7 prompt templates for Stitch + OpenCode
- playbooks/ — Client acquisition, delivery, maintenance
