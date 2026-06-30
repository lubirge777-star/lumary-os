# Accessibility

## Version 1.0

---

## Philosophy

Accessibility is not a feature. It is not an add-on. It is not a checklist to satisfy before launch.

Accessibility is **inclusivity**.

A premium experience that excludes users with disabilities is not premium. It is incomplete.

Approximately 15% of the global population lives with some form of disability. That is not a niche audience. It is a significant portion of every client's potential customer base. Designing for them is not charity. It is smart business.

---

## Standards

We target **WCAG 2.1 Level AA** as the minimum standard for all projects.

---

## The Key Areas

### 1. Color and Contrast

| Requirement | Standard |
|---|---|
| Normal text (< 18px) | 4.5:1 contrast ratio |
| Large text (≥ 18px bold or ≥ 24px) | 3:1 contrast ratio |
| UI components (borders, icons) | 3:1 against adjacent colors |
| Focus indicators | 3:1 against background |

**Implementation:**
```css
/* Always test with tools like axe DevTools or Lighthouse */
.text-body {
  color: #CBD5E1; /* on #0F172A = 9.7:1 ✓ */
}

.text-muted {
  color: #64748B; /* on #0F172A = 4.8:1 ✓ (minimum) */
}
```

### 2. Keyboard Navigation

All interactive elements must be reachable and operable via keyboard.

| Key | Function |
|---|---|
| Tab | Move focus forward |
| Shift + Tab | Move focus backward |
| Enter / Space | Activate button or link |
| Arrow keys | Navigate within a component (tabs, select, menu) |
| Escape | Close modal, dropdown, menu |

**Implementation:**
```html
<button aria-expanded="false" aria-controls="menu-1">
  Menu
</button>
```

### 3. Screen Reader Support

**Semantic HTML first:**
```html
<!-- Correct -->
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
  </ul>
</nav>

<!-- Incorrect -->
<div class="nav">
  <div><a href="/">Home</a></div>
</div>
```

| Element | ARIA / Semantic Requirement |
|---|---|
| Navigation | `<nav>` with `aria-label` |
| Images | `alt` text (decorative: `alt=""` ) |
| Form fields | `<label>` with `for` attribute |
| Errors | `aria-describedby` on input + `role="alert"` on message |
| Live regions | `aria-live="polite"` or `aria-live="assertive"` |
| Modals | `role="dialog"` + `aria-modal="true"` |
| Tabs | `role="tablist"`, `role="tab"`, `role="tabpanel"` |

### 4. Motion and Epilepsy

| Requirement | Implementation |
|---|---|
| `prefers-reduced-motion` | Disable all non-essential animations |
| No flashing content (> 3 flashes/sec) | Avoid stroboscopic effects |
| Pause/Hide moving content | Provide controls for auto-playing video |

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### 5. Touch Targets

| Target | Minimum Size |
|---|---|
| Mobile touch targets | 44px × 44px |
| Desktop click targets | 32px × 32px |
| Spacing between targets | 8px minimum |

### 6. Forms

| Requirement | Implementation |
|---|---|
| Labels | All inputs have visible `<label>` |
| Error association | Error tied to input via `aria-describedby` |
| Required fields | `aria-required="true"` or visual indicator + screen reader text |
| Autocomplete | `autocomplete` attribute on common fields |

---

## Testing Checklist

### Automated
- [ ] Lighthouse accessibility audit (target 90+)
- [ ] axe DevTools scan — zero critical/serious issues
- [ ] WAVE evaluation tool — zero errors

### Manual
- [ ] Tab through entire page — all elements reachable
- [ ] All interactive elements have visible focus indicators
- [ ] Screen reader (NVDA or VoiceOver) reads page logically
- [ ] All images have appropriate alt text
- [ ] Color contrast verified with a standalone tool
- [ ] Zoom to 200% — no content cut off or overlapping
- [ ] Site navigable with keyboard only
- [ ] `prefers-reduced-motion` respected

---

## Anti-Patterns

| Anti-Pattern | Why |
|---|---|
| Using color alone to convey information | Colorblind users cannot perceive the distinction |
| Focus style: `outline: none` without replacement | Keyboard users cannot track their position |
| Auto-playing video without controls | Disorienting, cannot be paused |
| Missing form labels | Screen readers cannot identify the field |
| Low contrast "muted" text | Unreadable for low-vision users |
| Custom elements without ARIA roles | Screen readers see meaningless markup |

---

## Resources

- WCAG 2.1 Quick Reference: https://www.w3.org/WAI/WCAG21/quickref/
- axe DevTools browser extension
- WebAIM contrast checker: https://webaim.org/resources/contrastchecker/
- NVDA screen reader (free, Windows)
- VoiceOver (built into macOS/iOS)

---

## Future Ideas

- Accessibility statement template for client sites
- Automated accessibility audit as part of build process
- "Accessibility-first" component variants
