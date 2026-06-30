# Component Bible: Card System

## Version 1.0

## Variants

| Variant | Border | Background | Shadow | Hover |
|---|---|---|---|---|
| Default | border-white/10 | secondary | shadow-none | y: -8, border-accent/30, shadow-xl |
| Glass | border-white/10 | white/5 backdrop-blur-xl | shadow-none | y: -8, bg-white/10 |
| Elevated | border-none | white/10 | shadow-lg | y: -8, shadow-xl |
| Bordered | border-white/20 | transparent | shadow-none | border-accent/50 |

## Structure
```html
<div class="card group p-8 rounded-xl border border-white/10 bg-secondary
            hover:-translate-y-2 hover:shadow-xl hover:border-accent/30
            transition-all duration-300 cursor-pointer">
  <!-- Icon: w-14 h-14 bg-accent/10 rounded-xl flex items-center justify-center mb-6 -->
  <!-- Title: text-xl font-semibold mb-3 -->
  <!-- Description: text-muted leading-relaxed -->
  <!-- Optionally: link that appears on hover -->
</div>
```

## Responsive Grid
```css
/* 3 columns desktop, 2 tablet, 1 mobile */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}
```
