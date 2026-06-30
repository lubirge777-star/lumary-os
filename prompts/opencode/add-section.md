# OpenCode Prompt: Add a Section

## Version 1.0

## Template
```
Add a [SECTION TYPE] section to the existing [PROJECT NAME] website ([INDUSTRY]).

The section should go between [PREVIOUS SECTION] and [NEXT SECTION].

## Content
- Heading: "[HEADING]"
- Description: "[DESCRIPTION]"
- Items: [LIST ITEMS WITH DESCRIPTIONS]
- CTA: "[CTA TEXT]" (optional)

## Design
- Follow the existing theme (dark mode, [COLOR] accent)
- Use Tailwind classes matching the project
- GSAP animation: fade-in on scroll (ScrollTrigger, start: "top 85%")
- Mobile responsive (single column on mobile)
- Consistent spacing with other sections (py-24)

## Quality
- Semantic HTML
- ARIA labels where needed
- prefers-reduced-motion respected
- Images lazy-loaded with explicit dimensions
```

## Example
```
Add a Testimonials section to the existing Atlas Construct website.

The section should go between Portfolio and CTA sections.

## Content
- Heading: "What Our Clients Say"
- Description: "Trusted by leading construction companies across Tanzania."
- Items: 3 testimonials with name, company, quote, 5-star rating

## Design
- Dark theme, amber accent
- Swiper.js carousel for mobile
- GSAP cascade reveal
```
