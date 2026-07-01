# Experience 041: Audio Frequency Visualizer

## Classification
Feedback

## Emotion
Energy → Engagement

## Difficulty
★★★★☆

## Performance Impact
Medium

## Libraries
GSAP

---

## Description

A real-time audio visualizer that renders frequency bars that pulse and animate in response to audio input. Using the Web Audio API, the visualizer analyzes frequency data and maps it to DOM element heights or canvas drawings.

Use for music players, podcast sites, event pages, or any brand that wants to make audio content visually tangible.

---

## Interaction

Audio source plays (either user-initiated or ambient). The Web Audio API connects an `AnalyserNode` to the audio source and extracts frequency byte data at regular intervals. Each frequency bin maps to a bar element whose height is animated with GSAP for smooth interpolation rather than raw data assignment.

---

## Psychology

- **Synesthetic Mapping:** Converting sound to sight creates a multi-sensory experience that deepens engagement.
- **Real-time Feedback:** Immediate visual response to audio changes reinforces the connection between action and reaction.
- **Hypnotic Effect:** Rhythmic motion synchronized to audio can induce a trance-like focus state.

---

## Implementation

```html
<div class="visualizer" style="display: flex; align-items: flex-end; gap: 4px; height: 200px; padding: 1rem; background: #1a1a2e; border-radius: 16px;">
  <div class="viz-bar" style="width: 12px; height: 10px; background: linear-gradient(to top, #6c5ce7, #a29bfe); border-radius: 4px 4px 0 0;"></div>
  <div class="viz-bar" style="width: 12px; height: 15px; background: linear-gradient(to top, #6c5ce7, #a29bfe); border-radius: 4px 4px 0 0;"></div>
  <div class="viz-bar" style="width: 12px; height: 20px; background: linear-gradient(to top, #6c5ce7, #a29bfe); border-radius: 4px 4px 0 0;"></div>
  <div class="viz-bar" style="width: 12px; height: 25px; background: linear-gradient(to top, #6c5ce7, #a29bfe); border-radius: 4px 4px 0 0;"></div>
  <div class="viz-bar" style="width: 12px; height: 30px; background: linear-gradient(to top, #6c5ce7, #a29bfe); border-radius: 4px 4px 0 0;"></div>
  <div class="viz-bar" style="width: 12px; height: 25px; background: linear-gradient(to top, #6c5ce7, #a29bfe); border-radius: 4px 4px 0 0;"></div>
  <div class="viz-bar" style="width: 12px; height: 20px; background: linear-gradient(to top, #6c5ce7, #a29bfe); border-radius: 4px 4px 0 0;"></div>
  <div class="viz-bar" style="width: 12px; height: 15px; background: linear-gradient(to top, #6c5ce7, #a29bfe); border-radius: 4px 4px 0 0;"></div>
  <div class="viz-bar" style="width: 12px; height: 10px; background: linear-gradient(to top, #6c5ce7, #a29bfe); border-radius: 4px 4px 0 0;"></div>
</div>
<button class="viz-play-btn" style="margin-top: 1rem; padding: 0.6rem 1.5rem; background: #6c5ce7; color: white; border: none; border-radius: 8px; cursor: pointer;">Play Audio</button>
```

```javascript
let audioContext, analyser, source, dataArray;
const bars = document.querySelectorAll('.viz-bar');
const playBtn = document.querySelector('.viz-play-btn');
let isPlaying = false;
let animationId;

function initVisualizer(audioUrl) {
  audioContext = new (window.AudioContext || window.webkitAudioContext)();
  analyser = audioContext.createAnalyser();
  analyser.fftSize = 32;
  const bufferLength = analyser.frequencyBinCount;
  dataArray = new Uint8Array(bufferLength);

  const audio = new Audio(audioUrl);
  audio.crossOrigin = 'anonymous';
  source = audioContext.createMediaElementSource(audio);
  source.connect(analyser);
  analyser.connect(audioContext.destination);

  function draw() {
    if (!isPlaying) return;
    analyser.getByteFrequencyData(dataArray);
    animationId = requestAnimationFrame(draw);

    bars.forEach((bar, i) => {
      if (i < bufferLength) {
        const value = dataArray[i] / 255;
        const height = 5 + value * 180;
        gsap.to(bar, {
          height: height,
          duration: 0.1,
          ease: 'power1.out'
        });
      }
    });
  }

  playBtn.textContent = 'Stop';
  audio.play();
  isPlaying = true;
  draw();

  audio.addEventListener('ended', () => {
    isPlaying = false;
    playBtn.textContent = 'Play Audio';
    cancelAnimationFrame(animationId);
    bars.forEach(bar => gsap.to(bar, { height: 15, duration: 0.3 }));
  });
}

playBtn.addEventListener('click', () => {
  if (!isPlaying) {
    initVisualizer('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3');
  } else {
    isPlaying = false;
    playBtn.textContent = 'Play Audio';
    cancelAnimationFrame(animationId);
    bars.forEach(bar => gsap.to(bar, { height: 15, duration: 0.3 }));
  }
});
```

---

## Industries

| Industry | Fit | Notes |
|---|---|---|
| Music | ★★★★★ | Artist pages, players |
| Podcast | ★★★★★ | Episode pages |
| Entertainment | ★★★★☆ | Event pages |
| Technology | ★★★☆☆ | Audio product showcases |
| Education | ★★★☆☆ | Language learning audio |

---

## Accessibility Notes

- Visualizer must be purely decorative — audio content must be accessible without it
- Provide audio play/pause controls separate from visualizer controls
- No flashing or stroboscopic patterns (limit bar update rate to 20fps max)
- `prefers-reduced-motion: reduce` — show static bars, no animation

---

## Performance Notes

- `requestAnimationFrame` throttled to 60fps — battery efficient
- GSAP `.to()` with 0.1s duration smooths raw frequency data (avoids jitter)
- `fftSize: 32` creates only 16 frequency bins — minimal computation
- For canvas-based visualizers, use `OffscreenCanvas` for performance

---

## Variants

### Variant A: Circular Visualizer
Bars arranged in a circle radiating outward — more visually dramatic.

### Variant B: Waveform Visualizer
A continuous waveform line (amplitude over time) instead of frequency bars.

### Variant C: Ambient Visualizer
No audio source — bars react to mouse movement or scroll position as a pseudo-visualizer.

---

## Anti-Patterns

- Starting audio without user interaction — blocked by autoplay policy
- `fftSize` too large (> 256) — too many bars, visual noise
- Raw data without GSAP smoothing — bar movement looks jittery
- No mute/stop control — user cannot escape the audio
- Stroboscopic bar movement — seizure risk

---

## Checklist

- [ ] Audio starts on user gesture (click/tap)
- [ ] FFT size ≤ 64 (for ≤ 10 bars)
- [ ] GSAP smoothing applied to bar heights
- [ ] Reduced motion: static display
- [ ] Play/pause control provided
- [ ] No stroboscopic patterns
