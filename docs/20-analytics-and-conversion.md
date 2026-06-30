# Analytics & Conversion Tracking

## Version 1.0

---

## Philosophy
A beautiful website that does not convert visitors into customers is art, not business. Every project must include analytics to measure what works and what does not.

---

## Required Setup

### Google Analytics 4 (GA4)
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Events to Track
| Event | Trigger | Why |
|---|---|---|
| page_view | Page load | Baseline traffic |
| form_submit | Form submission | Lead generation |
| cta_click | Primary CTA click | Conversion intent |
| whatsapp_click | WhatsApp button click | Direct contact |
| phone_click | Phone number click | Call tracking |
| scroll_depth | 25%, 50%, 75%, 100% | Content engagement |
| section_view | Each section enters viewport | Content performance |

### Event Implementation
```javascript
// CTA click
document.querySelectorAll('.btn-primary').forEach(btn => {
  btn.addEventListener('click', () => {
    gtag('event', 'cta_click', {
      'cta_text': btn.textContent.trim(),
      'cta_location': btn.closest('section')?.id || 'unknown'
    });
  });
});

// Form submission
document.querySelector('form')?.addEventListener('submit', () => {
  gtag('event', 'form_submit', {
    'form_location': 'contact'
  });
});

// WhatsApp click
document.querySelector('.whatsapp-float')?.addEventListener('click', () => {
  gtag('event', 'whatsapp_click');
});

// Scroll depth
let trackedDepths = new Set();
window.addEventListener('scroll', () => {
  const depth = Math.round((window.scrollY + window.innerHeight) / document.body.scrollHeight * 100);
  [25, 50, 75, 100].forEach(threshold => {
    if (depth >= threshold && !trackedDepths.has(threshold)) {
      trackedDepths.add(threshold);
      gtag('event', 'scroll_depth', { 'percent': threshold });
    }
  });
});
```

---

## Key Metrics to Monitor

| Metric | Good Target | Great Target |
|---|---|---|
| Bounce Rate | < 60% | < 40% |
| Avg Session Duration | > 2 min | > 4 min |
| Pages per Session | > 2 | > 4 |
| CTA Click Rate | > 2% | > 5% |
| Form Conversion | > 1% | > 3% |
| WhatsApp Click Rate | > 0.5% | > 2% |

---

## Reporting Cadence

| Frequency | What to Review |
|---|---|
| Weekly | Traffic, top pages, bounce rate |
| Monthly | Conversions, goal completions, trends |
| Quarterly | Full performance review, strategy adjustment |

---

## Anti-Patterns

| Anti-Pattern | Why |
|---|---|
| No analytics installed | Flying blind — cannot improve what you do not measure |
| Tracking everything | Noise obscures signal — track only actionable events |
| Ignoring mobile data | 60%+ of traffic is mobile |
| Not setting up goals | Events are data; goals are insights |
| Over-reliance on vanity metrics | Page views mean nothing without conversions |
