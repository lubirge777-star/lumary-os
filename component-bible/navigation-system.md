# Component Bible: Navigation System

## Version 1.0

## Variants

| Variant | Use | Scroll Behavior |
|---|---|---|
| Floating | Default for all projects | transparent → glassmorphism (bg-primary/90 backdrop-blur-xl) |
| Fixed Top | Landing pages | always solid, smaller on scroll |
| Transparent | Luxury/creative | always transparent, white text |

## Structure
```html
<nav class="fixed top-4 left-4 right-4 z-50">
  <div class="max-w-6xl mx-auto px-6 py-4 rounded-2xl transition-all duration-500 bg-transparent">
    <div class="flex items-center justify-between">
      <a href="/" class="text-xl font-bold text-white">Logo</a>
      <!-- Desktop -->
      <div class="hidden md:flex items-center gap-8">
        <a href="#section" class="text-sm text-white/80 hover:text-white transition-colors">Link</a>
        <a href="#cta" class="px-5 py-2.5 bg-accent text-white rounded-lg text-sm font-semibold">CTA</a>
      </div>
      <!-- Mobile -->
      <button class="md:hidden text-white" aria-label="Menu">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
      </button>
    </div>
  </div>
  <!-- Mobile Menu -->
  <div class="mobile-menu fixed inset-0 bg-primary z-[-1] translate-x-full transition-transform duration-300 md:hidden">
    <div class="flex flex-col items-center justify-center h-full gap-8">
      <a href="#section" class="text-2xl text-white" onclick="closeMenu()">Link</a>
    </div>
  </div>
</nav>
```

## Scroll Behavior JS
```javascript
const navInner = document.querySelector('nav > div');
window.addEventListener('scroll', () => {
  if (window.scrollY > 100) {
    navInner.classList.remove('bg-transparent');
    navInner.classList.add('bg-primary/90', 'backdrop-blur-xl', 'shadow-lg', 'border', 'border-white/10');
  } else {
    navInner.classList.remove('bg-primary/90', 'backdrop-blur-xl', 'shadow-lg', 'border', 'border-white/10');
    navInner.classList.add('bg-transparent');
  }
});
```

## Mobile Menu JS
```javascript
const menuBtn = document.querySelector('[aria-label="Menu"]');
const mobileMenu = document.querySelector('.mobile-menu');
let menuOpen = false;
menuBtn?.addEventListener('click', () => {
  menuOpen = !menuOpen;
  mobileMenu.style.transform = menuOpen ? 'translateX(0)' : 'translateX(100%)';
  menuBtn.setAttribute('aria-label', menuOpen ? 'Close menu' : 'Menu');
});
function closeMenu() { menuOpen = false; mobileMenu.style.transform = 'translateX(100%)'; menuBtn.setAttribute('aria-label', 'Menu'); }
```
