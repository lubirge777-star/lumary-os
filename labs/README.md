# Labs — Experimental Interaction Playground

## Why

Not every idea needs to be production-ready. Some ideas need room to *breathe* — to be explored, broken, iterated, and sometimes abandoned.

The Labs folder is where Lumary OS experiments with interactions that may never ship to clients. These are pure R&D: no deadlines, no constraints, no compromises.

**Every great production experience started as a lab experiment.**

---

## Lab Notebooks

| Experiment | Status | Description |
|------------|--------|-------------|
| Liquid Navigation | 🔬 Planned | Nav bar that deforms and flows like liquid on scroll |
| Magnetic Hero | 🔬 Planned | Hero content that follows cursor with magnetic pull |
| Living Typography | 🔬 Planned | Text that responds to scroll speed, mouse position, audio |
| Interactive Shadows | 🔬 Planned | Dynamic shadow casting based on light source position |
| Procedural Backgrounds | 🔬 Planned | GPU-generated backgrounds that evolve over time |
| Noise Engine | 🔬 Planned | Subtle grain/noise overlay that adds texture |
| Mouse Physics | 🔬 Planned | Elements with mass, friction, bounce that react to cursor |
| Physics Cards | 🔬 Planned | Card grid with spring physics, fling, stacking |
| Particle Logo | 🔬 Planned | Logo that scatters and reforms on interaction |
| Neural Cursor | 🔬 Planned | Cursor trail using lightweight neural prediction |
| 3D Depth Hero | 🔬 Planned | Hero with real-time 3D depth using Three.js |
| Scroll Ripple | 🔬 Planned | Ripple effect emanating from scroll position |
| Audio-Reactive UI | 🔬 Planned | Interface elements that pulse with ambient sound |
| Gesture Navigation | 🔬 Planned | Mobile navigation driven by swipe gestures |
| Morphing Grid | 🔬 Planned | Grid items that morph into detail views |

---

## Lab Structure

Each experiment follows this format:

```text
experiment-name/
├── README.md           # Concept, approach, findings
├── index.html          # Self-contained demo
├── assets/             # Any needed resources
└── notes.md           # Learnings, failures, insights
```

---

## Principles

1. **Ship early, ship ugly** — First version can be broken. Iterate later.
2. **One interaction per experiment** — Focus isolates learning.
3. **Document failures** — "This didn't work" is as valuable as "this worked."
4. **Performance budget: 60fps** — Even experiments should not lag.
5. **License: MIT** — Anyone can use, remix, or discard.
