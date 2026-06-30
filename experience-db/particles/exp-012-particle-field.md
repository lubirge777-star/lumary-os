# Experience 012: The Particle Field

## Classification
Narrative (ambient)

## Emotion
Awe → Immersion

## Difficulty
★★★★☆

## Performance
High (GPU intensive)

## Libraries
GSAP, Three.js (optional)

---

## Description
Floating particles (dots, lines, geometric shapes) that drift slowly across the hero or background section. Particles respond to cursor movement — flowing away or toward the mouse like a living field.

## Implementation (Canvas-based, no Three.js)
```html
<canvas id="particle-canvas" class="absolute inset-0 pointer-events-none" aria-hidden="true"></canvas>

<script>
class ParticleField {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.particles = [];
    this.mouse = { x: 0, y: 0 };
    
    this.resize();
    this.initParticles(60);
    this.animate();
    
    window.addEventListener('resize', () => this.resize());
    canvas.parentElement.addEventListener('mousemove', (e) => {
      const rect = canvas.getBoundingClientRect();
      this.mouse.x = e.clientX - rect.left;
      this.mouse.y = e.clientY - rect.top;
    });
  }
  
  resize() {
    this.canvas.width = this.canvas.parentElement.offsetWidth;
    this.canvas.height = this.canvas.parentElement.offsetHeight;
  }
  
  initParticles(count) {
    for (let i = 0; i < count; i++) {
      this.particles.push({
        x: Math.random() * this.canvas.width,
        y: Math.random() * this.canvas.height,
        vx: (Math.random() - 0.5) * 0.5,
        vy: (Math.random() - 0.5) * 0.5,
        size: Math.random() * 2 + 1,
        opacity: Math.random() * 0.5 + 0.1
      });
    }
  }
  
  animate() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    
    this.particles.forEach(p => {
      // Mouse interaction
      const dx = this.mouse.x - p.x;
      const dy = this.mouse.y - p.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 150) {
        p.vx -= dx * 0.0005;
        p.vy -= dy * 0.0005;
      }
      
      p.x += p.vx;
      p.y += p.vy;
      p.vx *= 0.99;
      p.vy *= 0.99;
      
      // Wrap around edges
      if (p.x < 0) p.x = this.canvas.width;
      if (p.x > this.canvas.width) p.x = 0;
      if (p.y < 0) p.y = this.canvas.height;
      if (p.y > this.canvas.height) p.y = 0;
      
      this.ctx.beginPath();
      this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
      this.ctx.fillStyle = `rgba(255, 255, 255, ${p.opacity})`;
      this.ctx.fill();
    });
    
    requestAnimationFrame(() => this.animate());
  }
}

const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!reducedMotion) {
  new ParticleField(document.getElementById('particle-canvas'));
}
</script>
```

## When to Use
- Tech / AI company hero sections
- Creative studio backgrounds
- Luxury brand ambient effects
- Product launch pages

## Performance Notes
- 60 particles max for mid-range devices
- Canvas-based (not DOM) for GPU acceleration
- Use `devicePixelRatio` scaling for retina
- Disable on mobile (battery + performance)

## Accessibility
- `aria-hidden="true"` (decorative only)
- `prefers-reduced-motion` disables entirely
- No critical information conveyed through particles
