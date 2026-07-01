# Changelog

All notable changes to Lumary OS will be documented here.

---

## [3.0.0] — 2026-07-01 — Experience Engineering

### Added
- **Philosophy & Pillars** — README rewritten with WHY, Five Pillars (Emotion, Story, Motion, Craft, Performance), "We Believe" principles, psychology section
- **Experience Engineering** — New positioning as a discipline bridging UI/UX/Motion/Frontend. Experience Lifecycle (Research → Emotion Mapping → Story Architecture → Wireframe → Experience Design → Motion → Development → Optimization → Launch → Evolution)
- **Case Studies** (`case-studies/`) — Reverse-engineered experience analysis framework. Planned: Apple, Stripe, Linear, Porsche, Nothing, Airbnb, Spotify Wrapped, Rivian, Framer
- **Labs** (`labs/`) — Experimental interaction playground. Planned: Liquid Navigation, Magnetic Hero, Living Typography, Interactive Shadows, Procedural Backgrounds, Physics Cards, Neural Cursor, 15+ experiments
- **Metrics** (`metrics/`) — Lumary Score measurement system across 8 dimensions: Curiosity, Memory, Interaction Density, Motion Density, Cognitive Load, Conversion Readiness, Performance, Accessibility
- **Experience AI** (`experience-ai/`) — AI-accelerated experience architecture: recommendation engine, prompt chain, skill integration

### Changed
- README fully rewritten — removed "10/10" self-rating, replaced with "Core Capabilities" and objective description
- Repository architecture expanded to 8 top-level directories (was 4)
- Version bumped to 3.0 to reflect architectural scope change

### Fixed
- 10 broken Unsplash photo IDs replaced with working alternatives (18 occurrences across 6 templates)

---

## [2.1.0] — 2026-06-30

### Added
- **E-Commerce**: Product filtering/search — search input + 4 category buttons with real-time filtering, no-results message
- **Restaurant**: Interactive menu expand/collapse — 3 dish cards with GSAP-animated details, dietary tags, preparation notes, ingredient origin, toggle-all button
- **Construction**: Case study detail modal — 6 projects with per-project descriptions and PDF download CTA buttons
- **Real Estate**: Property type filters (Residential/Commercial), schedule-a-tour date picker with min-today constraint, property detail modal with full info
- **Portfolio**: Richer case study content in modal — per-project description, client name, year, measurable results
- **Blog**: Load More pagination — 6 articles split into 2 pages of 3, GSAP reveal animation, integrates with search/filter, respects reduced motion
- **SaaS**: Monthly/annual pricing toggle with 20% savings callout

### Fixed
- 15 placeholder brand names replaced with real names (SaaS, Real Estate, Restaurant)
- 3 WhatsApp URL encoding issues fixed (SaaS + Real Estate + Restaurant)
- Ecommerce Swiper dependency removed — ported to custom vanilla JS carousel with keyboard nav, ARIA, touch/drag, dot pagination
- Portfolio project `#` links → working GSAP-animated detail modal
- Blog `[open]` attribute → `open` on ecommerce FAQ `<details>`
- Portfolio unclosed `<script>` tag fixed (modal HTML was inside JS context)
- Construction email/phone link contrast: light-mode `--muted` changed to WCAG AA-compliant `#475569`
- Theme toggle standardized across all 7 templates (uniform IIFE pattern, consistent `'theme'` localStorage key)

### Changed
- Restaurant inline styles refactored: 33 `style="color: var(...)"` → 4 (all SVG-only), using Tailwind class-based utilities
- Theme toggle code now identical across all 7 templates (IIFE pattern with `setTheme()`/`updateThemeIcons()`)

### Updated
- ERM-AUDIT.md scores — overall average improved from 3.9/5 to 4.27/5
- SKILL.md with ERM scores per template
- README.md stats and version
- CHANGELOG.md with all 15 passes

---

## [2.0.0] — 2026-06-30

### Added
- 3 new premium templates: e-commerce (fashion), portfolio/agency (creative), blog/magazine (editorial)
- 32 new Experience DB entries across 11 categories: hover (5), parallax (3), text (5), forms (3), video (3), audio (2), scrolling (2), images (3), cards (2), navigation (2), loaders (2)
- Style Guide page (style-guide.html) — live interactive catalog of the entire OS
- Experience 054: Infinite Scrolling Carousel — GSAP-powered continuous horizontal loop with drag/swipe, pause-on-hover, and mask-edge fade; implemented in 3 templates (e-commerce "New Arrivals", blog "Trending Now", portfolio client logos)

### Changed
- SaaS, Real Estate, and Restaurant templates rewritten from ~80 lines to 600+ lines — fully OS-compliant with all 18 sections, all experiences, analytics, QA, a11y
- Experience Database expanded from 21 → 53 total entries
- Templates expanded from 4 → 7 total
- Construction template (Jenga Bora) rebranded from generic `[bracket placeholders]` to specific Tanzanian construction brand with 10 SVG section dividers, authentic client names, and real organization references

### Updated
- SKILL.md reference counts
- README.md stats and file counts

---

## [1.1.0] — 2026-06-30

### Added
- Experience Database: 9 new entries (The Transformation, Cursor Reveal, Magnetic Nav, Cinematic Hero, Tilt Card, Brand Loader, Page Transition, Spotlight Hero, Particle Field)
- Pattern Library: 8 new patterns (Primary/Secondary/Ghost/WhatsApp buttons, Contact Form, Footer Standard, Skeleton Loader, CTA Section)
- Component Bible: Button System, Card System
- Templates: Construction template (full), Restaurant template (skeleton)
- Docs: Development Workflow (16), Business Model (17), AI Prompting for Design (18), Stitch Integration (19)

### Changed
- README updated with new file counts

---

## [1.0.0] — 2026-06-30

### Added
- 15 foundational docs (Manifesto through Psychology Atlas)
- 3 Experience DB entries (The Awakening, The Scroll Story, The Signature Moment)
- 5 Pattern Library entries (Hero centered/split, Service Card, Floating Nav, Testimonials)
- Client Acquisition Playbook
- Stitch + OpenCode prompt libraries
- Lumary Studio agent skills (OpenCode + Stitch)
- README with full architecture

---

## Template

```
## [version] — date
### Added
- New features

### Changed
- Modifications to existing features

### Fixed
- Bug fixes

### Removed
- Deprecated features
```
