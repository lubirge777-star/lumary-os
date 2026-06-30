# Interaction Language

## Version 1.0

---

## What is Interaction Language?

Interaction Language defines how the user communicates with the interface — and how the interface responds.

While Motion Language defines *how* elements move, Interaction Language defines *when* and *why* they respond.

---

## The Four Interaction Levels

### Level 1: Passive (No interaction — just observing)
- Reading content
- Watching a video
- Viewing an image gallery

**Design implication:** Content must be legible and compelling without interaction. Do not require clicks to access core information.

### Level 2: Reactive (Element responds to presence)
- Hover effects on cards
- Link color changes
- Navigation item highlight on scroll

**Design implication:** Every interactive element must provide visual feedback within 150ms of hover/focus.

### Level 3: Active (User performs an action)
- Clicking a button
- Submitting a form
- Tapping a gallery image
- Opening a menu

**Design implication:** Actions must provide clear feedback — visual, motion, or haptic — that the action was received.

### Level 4: Proactive (System responds to behavior)
- Scroll-triggered animations
- Staggered content reveals
- Adaptive navigation (transparent → solid on scroll)
- Smart form validation as user types

**Design implication:** The interface should anticipate user needs and respond without explicit commands.

---

## Interaction Response Times

| Interaction | Expected Response | Acceptable Max |
|---|---|---|
| Hover | 50-100ms | 150ms |
| Click/Tap | 100-200ms | 300ms |
| Page section reveal | 600-800ms | 1000ms |
| Form submission | < 1s processing | 3s (with loading indicator) |
| Page load | 0-1s | 2.5s |
| Modal open | 300-400ms | 500ms |

---

## State Specification

Every interactive element must define these states:

### Button
```
Resting:    bg-accent, text-white, shadow-sm
Hover:      bg-accent-light, y: -1px, shadow-md, cursor-pointer
Focus:      ring-2 ring-accent ring-offset-2
Active:     scale 0.97
Loading:    spinner, disabled
Disabled:   opacity 50%, cursor-not-allowed
Success:    icon checkmark, green tint (300ms)
Error:      shake animation, red tint (300ms)
```

### Input
```
Resting:    border-subtle, bg-transparent
Focus:      border-accent, ring-1 ring-accent
Hover:      border-medium
Filled:     border-valid or border-invalid
Error:      border-red, red message below
Disabled:   opacity 50%, cursor-not-allowed
```

### Card
```
Resting:    border-subtle, shadow-sm
Hover:      y: -8px, shadow-md, cursor-pointer
Focus:      ring-2 ring-accent
Active:     scale 0.98
Selected:   border-accent, bg-accent-bg
```

---

## Navigation Interaction Patterns

### Desktop Nav
```
Default:    transparent bg (on hero), white links
Scroll:     solid bg with blur, reduced link opacity
Hover:      link color → accent, optional underline expand
Active:     current page indicator
Mobile:     hamburger → slide-in menu with backdrop
```

### Mobile Nav
```
Toggle:     300ms, slide from right, backdrop fade
Link:       tap → close nav, scroll to section
Indicator:  active section highlighted
```

---

## Form Interaction Patterns

### Validation
- Real-time validation (as user types, not on submit only)
- Error message appears below the field, not in a tooltip
- Success state shown briefly after valid input
- Submit button disabled until all required fields valid

### Submission
1. Button → loading state (spinner + disabled)
2. Processing (show progress if > 2s)
3. Success → confirmation message + checkmark animation
4. Error → shake button + inline error message

---

## Scroll Interaction Patterns

### Scrollbar
- Custom scrollbar (subtle, minimal)
- Visible only when scrolling
- Matches brand colors

### Scroll Progress
- Optional: progress bar at top of page
- Fills from 0% to 100% as user scrolls
- Disappears after reaching bottom

### Back to Top
- Appears after scrolling past 1 viewport height
- Smooth scroll to top on click
- Fade in/out 300ms

---

## Cursor Interactions (Optional — Premium only)

For luxury, creative, or portfolio sites only.

- Custom cursor replaces default in content area
- Returns to default on interactive elements
- Scale up on hover (cursor: 32px → 48px)
- Trail effect (optional, very subtle)

**Accessibility:** Must not interfere with click targets. Must respect `prefers-reduced-motion`.

---

## Interaction Anti-Patterns

| Anti-Pattern | Why |
|---|---|
| No hover state on clickable elements | User does not know it is interactive |
| Click target < 44px (mobile) | Hard to tap, violates WCAG |
| No focus state on interactive elements | Keyboard users cannot navigate |
| Hover-only interactions on touch devices | Content becomes inaccessible |
| Delayed click feedback (>300ms) | Feels sluggish, unresponsive |
| Form submits without confirmation | User not sure if action was received |
| Accidental triggers near edges | Mobile users trigger back/home easily |

---

## Checklist

- [ ] All 4 interaction levels considered in design
- [ ] Every interactive element has defined rest/hover/focus/active states
- [ ] Click targets are 44px+ (mobile) and 32px+ (desktop)
- [ ] Hover feedback within 150ms
- [ ] Click feedback within 300ms
- [ ] Form validation is real-time
- [ ] Focus states visible for keyboard navigation
- [ ] Navigation has scroll-responsive behavior
- [ ] Loading and error states defined for all async actions
- [ ] Touch targets have adequate spacing (8px minimum)

---

## Future Ideas

- Interaction pattern database sorted by device type (mouse, touch, keyboard)
- "Interaction audit" checklist for QA before delivery
- Prototype kit with pre-built interaction patterns in HTML/CSS/JS
