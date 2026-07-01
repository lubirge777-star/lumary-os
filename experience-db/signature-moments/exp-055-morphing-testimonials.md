# Experience 055: Morphing Testimonials

## Classification
Signature Moments → Social Proof

## Emotion
Trust → Inspiration → Connection

## Difficulty
★★☆☆☆

## Performance Impact
Low

## Libraries
GSAP

## Description
A centered, typography-focused testimonial carousel that "morphs" between quotes with smooth blur/fade transitions. Unlike traditional sliders, the text transforms in place — no sliding cards. The current quote fades out with a subtle blur while the next quote fades in, creating a seamless, premium feel. Auto-rotates with pause on hover.

## When to Use
- Any page needing social proof with emotional impact
- Luxury, SaaS, creative agency, and editorial sites
- Replaces traditional Swiper/testimonial sliders for a cleaner look
- Hero-adjacent sections where polish matters most

## Implementation

### HTML
```html
<section class="testimonials-section py-20 md:py-28 px-4 md:px-6">
  <div class="max-w-3xl mx-auto text-center">
    <span class="text-xs md:text-sm font-semibold text-accent uppercase tracking-widest">Testimonials</span>
    <h2 class="font-heading text-4xl md:text-5xl mt-4 mb-14 md:mb-20">What People Say</h2>
    <div class="testimonial-morph relative min-h-[280px] md:min-h-[240px]" role="region" aria-label="Testimonials" aria-live="polite">
      <!-- testimonials injected via JS or static -->
      <div class="testimonial-slide absolute inset-0 flex flex-col items-center justify-center opacity-0 pointer-events-none" data-index="0">
        <svg class="w-10 h-10 md:w-12 md:h-12 text-accent/20 mb-6" fill="currentColor" viewBox="0 0 24 24"><path d="M14.017 21v-7.391c0-5.704 3.731-9.57 8.983-10.609l.995 2.151c-2.432.917-3.995 3.638-3.995 5.849h4v10h-9.983zm-14.017 0v-7.391c0-5.704 3.748-9.57 9-10.609l.996 2.151c-2.433.917-3.996 3.638-3.996 5.849h3.983v10h-9.983z"/></svg>
        <blockquote class="text-lg md:text-2xl lg:text-3xl font-heading leading-relaxed mb-8 max-w-2xl text-[var(--text)]">"The text of the testimonial."</blockquote>
        <div class="author-info">
          <p class="font-semibold text-sm md:text-base text-[var(--text)]">Author Name</p>
          <p class="text-xs md:text-sm text-muted mt-1">Title, Company</p>
        </div>
      </div>
      <!-- more slides -->
    </div>
    <div class="morph-dots flex justify-center gap-3 mt-10" role="tablist" aria-label="Testimonial navigation">
      <button class="morph-dot w-2.5 h-2.5 rounded-full bg-[var(--muted)]/40 hover:bg-accent/60 transition-all duration-300 cursor-pointer" role="tab" aria-selected="false" data-index="0" aria-label="Testimonial 1"></button>
      <!-- more dots -->
    </div>
  </div>
</section>
```

### CSS
```css
.testimonial-slide { transition: opacity 0.6s ease, filter 0.6s ease; will-change: opacity, filter; }
.testimonial-slide.active { opacity: 1; pointer-events: auto; position: relative; }
.testimonial-slide.exit { opacity: 0; filter: blur(4px); transform: translateY(-8px); }
.morph-dot.active { background: var(--accent) !important; transform: scale(1.3); }
```

### JavaScript (GSAP)
```js
function initMorphingTestimonials(container) {
  if (!container) return;
  var slides = container.querySelectorAll('.testimonial-slide');
  var dots = container.querySelectorAll('.morph-dot');
  if (slides.length < 2) return;

  var current = 0;
  var isAnimating = false;
  var interval;

  function showSlide(index) {
    if (isAnimating || index === current) return;
    isAnimating = true;

    var prev = slides[current];
    var next = slides[index];

    // Slide the exit
    gsap.to(prev, { opacity: 0, y: -10, filter: 'blur(4px)', duration: 0.5, ease: 'power2.in', onComplete: function() {
      prev.classList.remove('active');
      prev.style.transform = '';
      prev.style.filter = '';
    }});

    // Slide the entry
    gsap.set(next, { opacity: 0, y: 10, filter: 'blur(4px)' });
    next.classList.add('active');
    gsap.to(next, { opacity: 1, y: 0, filter: 'blur(0px)', duration: 0.7, ease: 'power2.out', onComplete: function() {
      isAnimating = false;
    }});

    // Update dots
    dots.forEach(function(d) { d.classList.remove('active'); d.setAttribute('aria-selected', 'false'); });
    if (dots[index]) { dots[index].classList.add('active'); dots[index].setAttribute('aria-selected', 'true'); }

    current = index;
  }

  function nextSlide() {
    var next = (current + 1) % slides.length;
    showSlide(next);
  }

  // Click dots
  dots.forEach(function(dot) {
    dot.addEventListener('click', function() {
      showSlide(parseInt(this.dataset.index));
      resetInterval();
    });
  });

  // Auto-rotate
  function startInterval() { interval = setInterval(nextSlide, 5000); }
  function resetInterval() { clearInterval(interval); startInterval(); }

  // Pause on hover
  container.addEventListener('mouseenter', function() { clearInterval(interval); });
  container.addEventListener('mouseleave', function() { startInterval(); });

  // Touch swipe support
  var touchStartX = 0;
  container.addEventListener('touchstart', function(e) { touchStartX = e.touches[0].clientX; }, { passive: true });
  container.addEventListener('touchend', function(e) {
    var diff = e.changedTouches[0].clientX - touchStartX;
    if (Math.abs(diff) > 50) {
      if (diff < 0) nextSlide();
      else showSlide((current - 1 + slides.length) % slides.length);
      resetInterval();
    }
  }, { passive: true });

  // Keyboard navigation
  container.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowRight') { nextSlide(); resetInterval(); }
    if (e.key === 'ArrowLeft') { showSlide((current - 1 + slides.length) % slides.length); resetInterval(); }
  });

  // Initialize first slide
  slides[0].classList.add('active');
  gsap.set(slides[0], { opacity: 1, y: 0, filter: 'blur(0px)' });
  if (dots[0]) { dots[0].classList.add('active'); dots[0].setAttribute('aria-selected', 'true'); }
  startInterval();
}

// Initialize on DOMContentLoaded
document.querySelectorAll('.testimonial-morph').forEach(initMorphingTestimonials);
```

## Variants

### Variant A: Minimal
- Smaller quote text, no quotation mark SVG icon
- Fade-only transition (no blur/y-offset)
- Simple dot navigation

### Variant B: Featured
- Large hero-style quote (clamp 2rem-4rem)
- Author image circle next to name
- Subtle background gradient shift per slide

### Variant C: Side-by-side
- Two columns: quote + author image
- Morph transition on the quote side, cross-fade on image

## Accessibility
- `role="region"` with `aria-label="Testimonials"` on container
- `aria-live="polite"` so screen readers announce changes
- `role="tablist"` and `role="tab"` on dot navigation
- `aria-selected` on active dot
- `aria-hidden="true"` on non-active slides (set via pointer-events)
- Keyboard navigation: Left/Right arrow keys
- Respects `prefers-reduced-motion` — fade only, no blur
- Pause on hover for cognitive accessibility

## Related
- exp-003: The Signature Moment (emotional payoff section)
- exp-024: Minimal Hero (clean typography approach)
- exp-054: Infinite Scrolling Carousel (alternative for multi-card display)
