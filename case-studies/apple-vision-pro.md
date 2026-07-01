# Case Study: Apple Vision Pro — apple.com/apple-vision-pro

---

## Product & Context

**What does this experience do?**

The Apple Vision Pro landing page is a product showcase that explains, demonstrates, and sells the company's spatial computing headset entirely through narrative scrolling. Instead of a traditional specs-first approach, the page uses scroll-driven cinema — video scrubbing, sticky compositing, and layered reveals — to make the *experience* of the device legible before the user ever puts one on. It is a pre-taste of spatial computing delivered through a 2D browser.

**Who is it for?**

The page targets three concentric audiences: early adopters and developers who need technical depth, luxury consumers making a $3,499+ purchase decision, and enterprise buyers evaluating productivity use cases. The tone never panders — it assumes sophistication, patience, and a willingness to scroll through a long-form narrative.

**What emotion does it evoke?**

Awe tempered by clarity. The page oscillates between *wonder* (the hero video, the 180-degree immersion shots) and *comprehensibility* (the simple section headers, the consistent CTA rhythm). It never feels like a tech demo — it feels like being shown something inevitable. The dominant emotional arc is: curiosity → understanding → desire → confidence to buy.

---

## Experience Breakdown

### Typography

**Font:** SF Pro (Display and Text variants). Apple's proprietary sans-serif. Neutral, warm, mechanically precise. On the web, Apple uses the system font stack (`font-family: "SF Pro Display", "SF Pro Text", "Helvetica Neue", Helvetica, Arial, sans-serif`), which means macOS and iOS users see the true SF Pro while others get a graceful fallback.

**Scale & Hierarchy:**

| Role | Size | Weight | Tracking |
|------|------|--------|----------|
| Section headline (e.g. "Entertainment") | ~64px / 4rem | 700 (bold) | -0.015em |
| Subtitle (e.g. "The ultimate theater. Wherever you are.") | ~48px / 3rem | 600 (semibold) | -0.01em |
| Body (feature descriptions) | 17px | 400 (regular) | 0em |
| Micro-copy (footnotes, CTAs) | 12-14px | 400 | 0.02em |

Apple notably omits weight 500 from its ladder — a deliberate choice to avoid muddy mid-tones that hurt legibility in the dark-theme context. Display sizes carry negative letter-spacing for the signature Apple-tight cadence. Body text at 17px (not 16px) improves readability on retina screens and matches visionOS's own type ramp.

**Hierarchy strategy:** Minimal hierarchy. There are effectively three levels: section label (small, all-caps, ~14px, weight 600, tracked out), headline (massive, ~64px), and body (17px). No tertiary level exists. This forces the eye to only two decisions: *what is this about* and *tell me more*. The reduced cognitive load is intentional — the product photography carries the real information density.

### Spacing & Layout

**Rhythm:** The page is a vertical stack of full-viewport sections. Each section is exactly one decision — one product benefit (Entertainment, Productivity, Photos, Connection, Apps, Design, Technology, Values). Sections are separated not by whitespace but by *color-field transitions*: dark tile → light tile → dark tile. The alternation itself is the divider.

**Density:** Extremely low. Even on a 27-inch display, each section contains at most ~20 words of body text plus a headline. The remaining 90% of viewport is product imagery, video, or negative space. Apple treats whitespace as a premium material — it communicates that the product is uncluttered, luxurious, and not desperate for attention.

**Alignment:** Centered everything. Headlines, CTAs, and even body text are center-aligned within each section. This is a deliberate trade-off: center alignment sacrifices optimal readability for a ceremonial, presentation-like feel. The text reads like captions on gallery walls — you read them slowly, deliberately.

**The sticky container pattern:** The core interaction device is a `position: sticky` wrapper. A tall container (often ~400vh) houses a sticky child pinned to the viewport. As the user scrolls through the container's height, the child element sits fixed while internal animations play — video scrubs, rotations, opacity transitions. This decouples animation duration from section length.

### Motion

This is the page's signature achievement. Four distinct motion systems operate simultaneously:

**1. Hero video auto-play.** The opening sequence is a full-viewport video (no audio, looping or single-play) that establishes the product in a lifestyle context. No scroll interaction — it just plays. Sets the emotional baseline.

**2. Scroll-triggered video scrubbing (the hero device rotation).** The most famous interaction. Approximately 60-70% down the page, as you scroll through the Design section, a video of the Apple Vision Pro rotating in 3D space is bound to scroll progress. JavaScript (`requestAnimationFrame` + scroll event listeners) maps `scrollY` to `video.currentTime`. The video advances frame-by-frame as the user scrolls, creating the illusion of controlling a 3D object. The headset spins, stops at precise angles, then flips up to reveal the eyepieces. The motion is locked at a linear easing — the video itself encodes the easing curves. Apple uses a single compressed `.mp4` rather than an image sequence, relying on GPU-accelerated video decoding for performance.

**3. Parallax depth layers (the "Take a closer look" section).** Multiple PNG-rendered layers of the headset (glass front, frame, light seal, band) stacked via CSS `z-index` and `transform: translateZ()` or translate Y with different coefficients per layer. As the user scrolls, each layer moves at a different rate, creating a 3D parallax effect. This is the same technique used in the "Design" panes where components detach and re-assemble.

**4. Fade/slide content reveals.** Supporting text fades and translates (usually Y: 30px → 0px, opacity: 0 → 1) as sections enter the viewport. These are CSS `opacity` + `transform` transitions triggered by Intersection Observer or scroll-timeline. Duration: ~600ms, easing: `cubic-bezier(0.4, 0, 0.2, 1)` — the Apple-standard deceleration curve.

**Timing specifics:**
- Sticky scroll containers: the parent spans ~300-400vh, giving the animation roughly 2000-3000px of scroll distance at 1000px scroll speed.
- Video scrub duration: the video length determines the scroll distance. Apple packs ~5-10 seconds of footage into ~2500px of scroll.
- Entry animations: 600ms, delayed 100-200ms from scroll trigger.
- No hover-driven motion. The page is entirely scroll-driven.

### Color & Contrast

**Palette:**

| Token | Hex | Usage |
|-------|-----|-------|
| Ink (primary text) | #1d1d1f | Body text on light tiles |
| Body text on dark | #ffffff | All text on dark tiles |
| Canvas (light) | #ffffff | Light section backgrounds |
| Canvas parchment | #f5f5f7 | Light tile with warmth |
| Tile dark | #000000 | Dark sections (hero, technology) |
| Tile 1 | #272729 | Near-black for secondary dark tiles |
| Action blue | #0066cc | Links, CTAs on light |
| Action blue on dark | #2997ff | Links, CTAs on dark |
| Body muted on dark | #cccccc | Secondary text, captions |

**Logic:** Two-color architecture. Light sections use warm white (`#f5f5f7`) with ink text. Dark sections use true black or near-black with white text. The transition between them is always abrupt — no gradient, no fade — which creates a staccato rhythm that signals "new section." The single accent color is Action Blue (`#0066cc` or `#2997ff` on dark), used exclusively for links and buttons. Nothing else is interactive blue — the color is a pure affordance signal.

**Accessibility:** On dark backgrounds, white-on-black comfortably exceeds WCAG AA (15.5:1+). On light backgrounds, #1d1d1f on #f5f5f7 tests at ~13:1. The real challenge is text over imagery — the hero section's white text over bright video content. Apple sometimes adds a thin gradient scrim beneath text in these contexts to maintain a ~4.5:1 minimum. The glassmorphism in the actual visionOS UI (not the website) has known contrast issues that Apple mitigates with vibrancy layers and automatic thickness adjustment, but the website avoids glassmorphism entirely — it's flat colored tiles, which is a deliberate accessibility decision.

### Interaction Design

**Floating sticky nav dock:** The top navigation bar is translucent (`backdrop-filter: blur(20px)` with an `rgba(0,0,0,0.4)` background) and uses `position: fixed`. It persists across all scroll positions. On the Apple Vision Pro page, the nav is minimal: Overview, Tech Specs, visionOS, plus a prominent "Buy" button. The dock is the only persistent UI — the page trusts you'll scroll, not click, to navigate content.

**Scroll-driven narrative:** There is no internal page navigation for sections. You cannot jump to "Photos and Videos" from a nav link. The narrative is linear, and the interaction model enforces this linearity. The only escape hatches are the top-level nav items (which go to different pages entirely).

**The sticky + scrub pattern (detailed):**
1. User scrolls normally through full-viewport hero section.
2. Reaches the design section. A container `div` with `height: 400vh` is encountered.
3. Inside, a `div` with `position: sticky; top: 0` pins the device video to the viewport top.
4. The remaining 300vh of scroll space advances the video frame-by-frame via `scroll` event → `video.currentTime = (scrollY - offset) / duration`.
5. Once the container is fully scrolled through, the sticky element releases and scrolls away naturally.
6. The next full-viewport section appears.

**Click / hover:** Minimal. Only links (the blue CTAs) are clickable. No hover effects beyond the default `:hover` cursor change. The page actively discourages clicking — the primary interaction is scrolling.

**Video controls:** None visible. The hero video loops or plays once with no scrub bar, no sound toggle, no pause. Apple retains full control over playback pacing.

### Micro-copy

**Tone:** Aspirational but precise. Never hyperbolic ("the ultimate theater"), never technical ("23 million pixels" is saved for the Technology section, not the hero). Every word justifies its space.

**Voice patterns:**
- Period after every headline fragment: "Entertainment. The ultimate theater.Wherever you are." The period creates finality and confidence. No exclamation marks.
- Sentence fragments used deliberately: "A workspace with infinite space." → period fragments read as declarative truths.
- Second-person avoided until the bottom of the page ("So you can work, watch, relive memories...").
- Colon used for explanation: "Be in the moment.All over again." → restates the benefit.
- Footnote-style disclaimers in tiny type (11px, `#cccccc` on dark) — legal text that Apple wants to be present but invisible.

**Pacing:** Each section follows: Section label (1-2 words) → Headline (4-8 words) → Body (15-25 words) → CTA (2-4 words). This 4-beat rhythm is never broken. The consistency makes the page feel like reading a well-edited magazine spread.

---

## Psychological Principles Applied

**1. The Peak-End Rule.** The most intense interaction (the scroll-scrubbed device rotation) occurs roughly at the golden-ratio point of the page (~62%). The page ends with "Values" (privacy, accessibility, environment) — an emotionally warm, trustworthy close. Users remember the peak (the beautiful 3D reveal) and the end (Apple's values), not the average.

**2. Scarcity (implied).** No pricing on the landing page. No "sold out" badges. But the "Book a demo" CTA and the $3,499 starting price (on the Buy page) imply limited availability and high status. The page sells the *experience*, then lets the price be discovered.

**3. Social Proof (vicarious).** The hero video shows people using the device in beautiful environments — a home theater, an airplane, a workspace. It's not "people like you use this" but "imagine yourself in this lifestyle." This is aspirational mirroring.

**4. Cognitive Fluency.** The 4-beat section structure, the consistent color alternation, the single accent color — everything is predictably patterned. High fluency = feels true, feels trustworthy. The page never surprises you with UX; it surprises you with *product*.

**5. Authority / Brand Trust.** Understated navigation, no banner ads, no pop-ups, no "limited time offer." The absence of aggressive marketing signals that Apple is so confident in the product that it doesn't need to sell. This is the most expensive form of marketing: restraint.

**6. Curiosity Gap.** The early sections (Entertainment, Productivity) answer "what can I do with this?" but defer technical detail. By the time the user reaches the Technology section, they've been primed to want the specs. The reveal of "23 million pixels, M5 chip, 12ms latency" lands harder because curiosity has been compounded.

**7. The Anchoring Effect (visual).** Before any price consideration, the user sees cinematic video, luxury-grade photography, and polished interaction. The price is anchored against an *experience*, not against other VR headsets. Meta Quest 3 at $499 feels like a different category entirely.

---

## Lumary Learnings

### How to implement this in Lumary OS

**Core pattern: `scroll/scroll-story`**
The entire page is a scroll-story — a linear narrative driven entirely by scroll position. Each section maps to a chapter, with its own scroll-linked animation timeline. In Lumary OS, this maps directly to the `scroll-story` experience, where the `container` element controls scroll duration via `--scroll-duration` (set in viewport heights) and each child section defines its own `--enter`, `--pin`, and `--exit` phases.

**Core pattern: `video/scroll-trigger`**
The headset rotation sequence is the definitive example of scroll-triggered video. In Lumary, this maps to the `scroll-trigger` video experience. Key configuration:

```lua
-- scroll-trigger video configuration (Lumary OS)
Video {
  src = "assets/vision-pro-rotation.mp4",
  playback = "scrub",         -- frame-by-frame on scroll
  scrub_map = "scrollY",      -- input: window scroll position
  scrub_range = { 0, 1 },     -- maps scroll progress to video time 0→1
  easing = "linear",           -- video encoding handles the easing
  pin = true,                  -- sticky container
  pin_offset = "top",          -- pin to viewport top
  container_height = "400vh",  -- scroll distance for full playback
}
```

**Core pattern: `parallax/depth-scroll`**
The multi-layer parallax (glass, frame, light seal, speakers) is modeled by depth-scroll. Each layer gets a speed factor relative to scroll:

```lua
-- parallax depth layers (Lumary OS)
ParallaxGroup {
  layers = {
    { id = "glass",   speed = 0.2, z = 0 },    -- slow, background
    { id = "frame",   speed = 0.5, z = 50 },     -- mid
    { id = "seal",    speed = 0.8, z = 100 },    -- fast, foreground
    { id = "speaker", speed = 1.0, z = 150 },    -- fastest
  },
  axis = "Y",
  trigger = "enter-viewport",
  range = { 0, 1 },
}
```

**Core pattern: `arrival/awakening`**
The hero video establishes the "awakening" — the moment the user enters the experience. In Lumary, this is an arrival sequence: full-viewport, auto-play video or animation that sets tone and context before scroll begins.

```lua
ArrivalAwakening {
  type = "video",
  src = "assets/vision-pro-hero.mp4",
  audio = false,
  duration = 8000,           -- ms
  next = "scroll",           -- transitions into scroll-story
  skip_threshold = 0.3,      -- skip if user scrolls past 30%
}
```

### Which patterns/experiences to use

| Apple Page Section | Lumary Experience Pattern | Notes |
|--------------------|---------------------------|-------|
| Hero auto-play video | `arrival/awakening` | Sets emotional tone, no interaction needed |
| Design (sticky rotation) | `video/scroll-trigger` + `scroll/scroll-story` | Video scrubbing pinned to scroll |
| "Take a closer look" layers | `parallax/depth-scroll` | Multi-layer Z-space parallax |
| Feature sections (Entertainment, etc.) | `scroll/scroll-reveal` | Text + media reveal on enter |
| Section transitions (dark→light) | `scroll/color-shift` | Hard cut color transitions |
| Section labels + CTAs | `scroll/scroll-story` children | Micro-copy as chapter markers |

### Design system tokens to extract for Lumary

```lua
-- Lumary design tokens from Apple Vision Pro case study
DesignTokens {
  typography = {
    font = { family = "'SF Pro Display', system-ui, sans-serif" },
    scale = {
      label    = { size = 14, weight = 600, tracking = 0.08, uppercase = true },
      headline = { size = 64, weight = 700, tracking = -0.015 },
      subtitle = { size = 48, weight = 600, tracking = -0.01 },
      body     = { size = 17, weight = 400, tracking = 0 },
      caption  = { size = 12, weight = 400, tracking = 0.02, color = "$muted" },
    },
  },
  color = {
    canvas  = { light = "#ffffff", parchment = "#f5f5f7" },
    tile    = { dark = "#000000", near_dark = "#272729" },
    ink     = { primary = "#1d1d1f", on_dark = "#ffffff", muted = "#cccccc" },
    accent  = { blue = "#0066cc", blue_on_dark = "#2997ff" },
  },
  motion = {
    duration_reveal  = "600ms",
    easing_reveal    = "cubic-bezier(0.4, 0, 0.2, 1)",
    easing_video     = "linear",
    scroll_duration  = "400vh",   -- standard sticky container height
  },
  spacing = {
    section_gap     = "0",       -- tiles touch edge-to-edge
    content_max_width = "980px",
    cta_padding     = { x = 24, y = 12, radius = 24 },
  },
}
```

### Implementation guidance

1. **Sticky containers are the backbone.** Every scroll-driven animation in this case study relies on `position: sticky` to decouple animation duration from viewport height. Lumary's `PinContainer` component should support `--pin-top`, `--pin-center`, `--pin-bottom` offsets and a configurable `--scroll-gh` (ghost height in vh).

2. **Use video encoding for complex animations.** Apple's decision to use a single `.mp4` for the device rotation instead of Canvas-drawn 3D or an image sequence is a performance decision. GPU-decodable video is cheaper than JS-driven rendering. Lumary's `scroll-trigger` should prefer video scrubbing over JS animation for anything that moves in 3D space.

3. **Color alternation as section divider.** No horizontal rules, no borders, no gaps — just a light tile followed by a dark tile. This pattern costs zero performance and creates unmistakable section boundaries. Lumary's `scroll-story` should support a `color_alternate = true` flag that cycles through a palette automatically.

4. **Restrain interaction to one mode.** The Apple Vision Pro page never asks the user to do two things at once. Scroll is the only input. No parallax + click. No hover + scroll. Lumary experiences should similarly define a *primary axis* (scroll, click, gaze, or voice) and avoid splitting user attention.

5. **Accessibility: provide `prefers-reduced-motion` fallback.** Apple disables all scroll-driven animations when reduced motion is preferred, showing a static image stack instead. Lumary's scroll-story should check `prefers-reduced-motion` at the container level and degrade to a static linear layout with all content visible at once.

---

## Lumary Score

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Curiosity** | 92 | The scroll-scrubbed rotation creates an irresistible "what happens next?" pull. The deferred technical detail compounds curiosity over ~5000px of scroll. |
| **Memory** | 88 | The single interaction (video scrub) is unique enough to be memorable months later. The alternating color rhythm aids recall. Loses points because the page is long — users may forget earlier sections by the time they reach the end. |
| **Interaction Density** | 25 | Deliberately low. One interaction mode (scroll), one CTA type per section, no hover effects, no clicking. This is a design strength, not a weakness, for this use case. |
| **Motion Density** | 78 | High for a marketing page — four motion systems (auto-play, scrub, parallax, reveal) — but each is isolated to its own section. No two motion systems compete simultaneously. |
| **Cognitive Load** | 20 | Very low. The 4-beat section structure, single accent color, center alignment, and lack of navigation choices make this among the lowest-CL premium product pages on the web. |
| **Conversion Readiness** | 85 | The page creates strong purchase intent through aspiration and trust, but the "Buy" button is only in the fixed nav — there's no bottom-of-section CTA beyond "Learn more." The page assumes the user will navigate to the store page separately. |
| **Performance** | 72 | Video scrubbing is GPU-accelerated and efficient. No heavy JS frameworks. However, the page ships multiple high-bitrate videos (hero, scrub sequence) which increases initial load on slow connections. LCP is often video-dominated. |
| **Accessibility** | 68 | Strong color contrast on text-over-background sections. Semantic HTML and `prefers-reduced-motion` support present. However, the video scrub is inaccessible to screen readers (no audio description equivalent for the transform animation), keyboard navigation is minimal (no skip-to-content), and the scroll-dependent narrative is unreachable by keyboard-only users who can't scroll the sticky container. |

**Overall:** 88/100 — a masterpiece of scroll-driven storytelling that achieves its primary goal (making a $3,500 product feel essential) with surgical precision. Its weaknesses are inherent to the form (long scroll, video dependency, reduced-motion compromises) rather than execution errors.
