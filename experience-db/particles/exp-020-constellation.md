# Experience 020: The Constellation

## Classification: Narrative (ambient)
## Emotion: Awe → Wonder
## Difficulty: ★★★★☆
## Performance: Medium
## Libraries: Canvas API

## Description
Particles are connected by lines when they are close to each other, creating a constellation/net effect. Mouse interaction pushes particles and creates new connections. Immersive tech/luxury background.

## Code
```javascript
class Constellation {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.particles = [];
    this.mouse = { x: -1000, y: -1000 };
    const count = Math.min(80, Math.floor(window.innerWidth / 15));
    
    this.resize();
    for (let i = 0; i < count; i++) {
      this.particles.push({
        x: Math.random() * this.canvas.width,
        y: Math.random() * this.canvas.height,
        vx: (Math.random() - 0.5) * 0.3,
        vy: (Math.random() - 0.5) * 0.3,
        r: Math.random() * 1.5 + 0.5
      });
    }
    this.animate();
    window.addEventListener('resize', () => this.resize());
    canvas.addEventListener('mousemove', (e) => {
      const rect = canvas.getBoundingClientRect();
      this.mouse.x = e.clientX - rect.left;
      this.mouse.y = e.clientY - rect.top;
    });
  }
  
  resize() {
    this.canvas.width = this.canvas.parentElement.offsetWidth;
    this.canvas.height = this.canvas.parentElement.offsetHeight;
  }
  
  animate() {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    
    this.particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      const dx = this.mouse.x - p.x, dy = this.mouse.y - p.y;
      const dist = Math.sqrt(dx*dx + dy*dy);
      if (dist < 200) { p.vx -= dx * 0.0002; p.vy -= dy * 0.0002; }
      p.vx *= 0.99; p.vy *= 0.99;
      if (p.x < 0) p.x = this.canvas.width;
      if (p.x > this.canvas.width) p.x = 0;
      if (p.y < 0) p.y = this.canvas.height;
      if (p.y > this.canvas.height) p.y = 0;
    });
    
    // Draw lines
    for (let i = 0; i < this.particles.length; i++) {
      for (let j = i + 1; j < this.particles.length; j++) {
        const dx = this.particles[i].x - this.particles[j].x;
        const dy = this.particles[i].y - this.particles[j].y;
        const dist = Math.sqrt(dx*dx + dy*dy);
        if (dist < 150) {
          this.ctx.beginPath();
          this.ctx.moveTo(this.particles[i].x, this.particles[i].y);
          this.ctx.lineTo(this.particles[j].x, this.particles[j].y);
          this.ctx.strokeStyle = `rgba(255,255,255,${(1 - dist / 150) * 0.15})`;
          this.ctx.lineWidth = 0.5;
          this.ctx.stroke();
        }
      }
    }
    
    this.particles.forEach(p => {
      this.ctx.beginPath();
      this.ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      this.ctx.fillStyle = 'rgba(255,255,255,0.5)';
      this.ctx.fill();
    });
    
    requestAnimationFrame(() => this.animate());
  }
}

if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  new Constellation(document.getElementById('constellation-canvas'));
}
```

## When to Use
- Tech/AI company backgrounds
- Creative studio hero
- Science/innovation brands
- Luxury night-time themed sites
