# Psychology Atlas

## Version 1.0

---

## Philosophy

Every design decision is a psychological decision.

When a user visits a website, their brain is running unconscious evaluations: *Is this safe? Is this credible? Is this worth my time? Is this for me?*

The Psychology Atlas catalogs the cognitive biases, heuristics, and psychological principles that influence these evaluations. Understanding them allows us to design experiences that align with how the human brain actually works — not how we wish it worked.

---

## Principle 1: Von Restorff Effect (Isolation)

**What it is:** The item that stands out from its peers is most likely to be remembered.

**Application in web design:**
- The primary CTA must be visually distinct from all other page elements
- One accent color element per viewport (the CTA)
- Featured testimonial or case study with distinct styling

**Example:**
A page with 6 outline buttons and 1 filled button. The filled button will be remembered and clicked.

**Anti-pattern:**
Multiple buttons with different styles competing for attention.

---

## Principle 2: Hick's Law

**What it is:** The time required to make a decision increases logarithmically with the number of choices.

**Formula:** `T = b * log2(n + 1)`

**Application:**
- Limit navigation to 5-7 items maximum
- One primary CTA per viewport
- Pricing tiers: 3 options maximum (good, better, best)
- Service offerings: 3-6 items maximum per section

**Example:**
A SaaS page with 3 pricing tiers converts better than one with 7.

**Anti-pattern:**
Navigation with 12 items, 6 CTA buttons on the hero, 8 service options.

---

## Principle 3: Peak-End Rule

**What it is:** People judge an experience largely based on how they felt at its peak (most intense point) and at its end, rather than the total sum or average.

**Application:**
- Design the peak: the WOW moment (3-5 per page)
- Design the end: the CTA or final impression
- Ensure the last thing a user sees before leaving is positive

**Example:**
A portfolio site has an animated project reveal as the peak, and a smooth, satisfying CTA experience at the end.

**Anti-pattern:**
All sections equally weighted, no standout moment, abrupt ending.

---

## Principle 4: Social Proof

**What it is:** People copy the actions of others in an attempt to undertake behavior in a given situation.

**Application:**
- Testimonials with real names, photos, and specific results
- Client logos section
- Live counters (projects completed, clients served)
- Case studies with measurable outcomes

**Research:** 92% of people trust recommendations from peers over branded content.

**Anti-pattern:**
Generic testimonials like "Great service!" without specific detail. No names or photos.

---

## Principle 5: Scarcity

**What it is:** People assign more value to things that are scarce or limited.

**Application:**
- Limited-time offers
- "Only X spots remaining"
- "Join 200+ other businesses"
- Exclusive access indicators

**Use with caution:** Overuse erodes trust. Must be genuine.

**Anti-pattern:**
Fake scarcity (e.g., "Only 1 spot left!" that never changes). Users detect this and lose trust.

---

## Principle 6: Anchoring

**What it is:** People rely heavily on the first piece of information offered (the "anchor") when making decisions.

**Application:**
- Display the highest-priced tier first in pricing
- Show the "before" image before the "after"
- Present the premium package before the standard one

**Example:**
Pricing: Premium ($999) → Standard ($499) → Basic ($199). The $999 anchor makes $499 feel reasonable.

**Anti-pattern:**
Showing the cheapest option first. The user anchors low and perceives all other options as expensive.

---

## Principle 7: Cognitive Fluency

**What it is:** People process information more favorably when it is easy to think about.

**Application:**
- Simple, clear language (avoid jargon)
- High contrast for readability
- Familiar patterns (standard navigation placement)
- Adequate whitespace
- Short paragraphs and sentences

**Research:** Stocks with easier-to-pronounce names outperformed those with complex names in trading volume.

**Anti-pattern:**
Industry jargon, low contrast text, dense paragraphs, complex navigation.

---

## Principle 8: Reciprocity

**What it is:** People feel obligated to return favors.

**Application:**
- Offer free value: guides, templates, checklists
- Free consultations or quotes
- Useful content before asking for the sale
- Tool or calculator that provides immediate value

**Example:**
A construction company offers a free "Home Renovation Budget Calculator" before asking for a consultation booking.

**Anti-pattern:**
Asking for contact information before providing any value.

---

## Principle 9: Loss Aversion

**What it is:** People prefer to avoid losses more than acquiring equivalent gains (losses feel ~2x more powerful).

**Application:**
- "Don't miss out on..." framing
- "Limited time offer" (loss of opportunity)
- "Your competitors are already using this"
- Free trials with automatic expiration

**Anti-pattern:**
Only highlighting gains without creating urgency. Negative framing without positive resolution.

---

## Principle 10: Zeigarnik Effect

**What it is:** People remember uncompleted or interrupted tasks better than completed ones.

**Application:**
- Progress bars in multi-step forms
- "Complete your profile" indicators
- Partial content with "Read more" links
- Sequential reveals (scrolling reveals next section)

**Anti-pattern:**
Presenting all information at once with no progressive disclosure.

---

## Principle 11: Aesthetic-Usability Effect

**What it is:** Users perceive aesthetically pleasing designs as more usable.

**Application:**
- Invest in visual polish — it directly impacts perceived usability
- A beautiful site is forgiven for minor usability issues
- An ugly site is scrutinized for every flaw

**Important caveat:** Aesthetic cannot save fundamentally broken usability. But equal usability is perceived as better when the design is beautiful.

**Anti-pattern:**
Prioritizing aesthetics over basic usability (e.g., beautiful but unclickable buttons).

---

## Principle 12: Serial Position Effect (Primacy & Recency)

**What it is:** People remember the first and last items in a sequence best.

**Application:**
- Put the most important nav item first
- Put the second most important nav item last
- In lists, place key information at the beginning and end
- CTAs at the end of content benefit from recency

**Anti-pattern:**
Burying the most important information in the middle of a list.

---

## Psychology-Driven Page Structure

Applying all principles:

```
Navigation         → Primacy (first items most remembered)
Hero               → Anchoring (first impression sets context)
Social Proof       → Social Proof (trust building)
Problem/Solution   → Cognitive Fluency (clear communication)
Services           → Hick's Law (limited choices)
Process            → Zeigarnik (sequential reveal, incomplete journey)
Case Study         → Peak-End (peak: impressive result)
Testimonials       → Social Proof + Peak-End
CTA                → Scarcity + Loss Aversion
Footer             → Recency (last items well remembered)
```

---

## Anti-Patterns Summary

| Anti-Pattern | Psychology Violated |
|---|---|
| 12 nav items | Hick's Law |
| No testimonials | Social Proof |
| Feature list without benefits | Cognitive Fluency |
| No standout element | Von Restorff Effect |
| Asking before giving | Reciprocity |
| Same CTA style as other buttons | Von Restorff Effect |
| Everything visible at once | Zeigarnik Effect |
| Pricing from low to high | Anchoring |

---

## Checklist

- [ ] Hick's Law: ≤ 7 nav items, ≤ 3 pricing tiers, 1 primary CTA
- [ ] Von Restorff: CTA visually distinct from all other elements
- [ ] Social Proof: testimonials with real details, client logos, case studies
- [ ] Peak-End: 3-5 WOW moments, strong ending
- [ ] Anchoring: pricing displayed high-to-low
- [ ] Cognitive Fluency: clear language, high contrast, familiar patterns
- [ ] Reciprocity: free value before asking for commitment
- [ ] Loss Aversion: urgency framing where appropriate
- [ ] Zeigarnik: progressive disclosure, sequential reveals

---

## Future Ideas

- Psychology profile for clients ("This audience responds best to X principles")
- A/B testing library for psychological triggers
- "Psychology audit" — evaluating a page against all 12 principles
