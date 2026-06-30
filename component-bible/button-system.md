# Component Bible: Button System

## Version 1.0

---

## Overview
All button variants used across Lumary Studio projects. Each variant has defined states, motion, and accessibility requirements.

## Variants

| Variant | Background | Border | Text | Hover | Active | Use Case |
|---|---|---|---|---|---|---|
| Primary | accent | none | white | lighter bg + lift | scale 0.97 | Main CTA, form submit |
| Secondary | transparent | accent/30 | accent | accent/10 bg + accent/60 border | scale 0.97 | Alternative action |
| Ghost | transparent | none | muted | white/5 bg | scale 0.97 | Tertiary action |
| WhatsApp float | green-500 | none | white | green-400 + scale | — | Permanent contact |

## Sizing

| Size | Padding | Font | Icon |
|---|---|---|---|
| sm | px-4 py-2 | text-sm | w-4 h-4 |
| md (default) | px-6 py-3 | text-base | w-5 h-5 |
| lg | px-8 py-4 | text-lg | w-5 h-5 |
| xl | px-10 py-5 | text-lg | w-6 h-6 |

## States

```
Resting:  bg-accent, text-white, border-none, shadow-sm
Hover:    bg-accent-light, y: -1px, shadow-md, cursor-pointer + 200ms
Focus:    ring-2 ring-accent ring-offset-2 + 150ms
Active:   scale 0.97 + 100ms
Loading:  spinner replaces label, disabled + 300ms
Disabled: opacity 50%, cursor-not-allowed + 200ms
```

## CSS Template
```css
.btn {
  @apply inline-flex items-center justify-center gap-2 font-semibold rounded-xl
         transition-all duration-200
         focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2
         disabled:opacity-50 disabled:cursor-not-allowed;
}
.btn-primary {
  @apply bg-accent text-white hover:bg-accent-light hover:-translate-y-0.5 active:scale-[0.97];
}
.btn-secondary {
  @apply bg-transparent text-accent border-2 border-accent/30 hover:bg-accent/10 hover:border-accent/60 active:scale-[0.97];
}
.btn-ghost {
  @apply bg-transparent text-muted hover:text-white hover:bg-white/5 active:scale-[0.97];
}
```

## HTML Snippet
```html
<button class="btn btn-primary px-8 py-4">
  <span>Get Started</span>
</button>
```
