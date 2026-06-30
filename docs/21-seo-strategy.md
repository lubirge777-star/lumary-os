# SEO Strategy

## Version 1.0

---

## Philosophy
SEO is not a separate effort. It is built into the structure of every page we create. A semantically correct, fast-loading, mobile-responsive page with proper metadata is 80% of SEO. The remaining 20% is content and backlinks.

---

## On-Page SEO Checklist

### Every Page Must Have
```html
<title>[Primary Keyword] | [Business Name] | [Location]</title>
<meta name="description" content="[Compelling 150-160 char description with keyword]" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<link rel="canonical" href="https://domain.com/page" />
<meta property="og:title" content="..." />
<meta property="og:description" content="..." />
<meta property="og:image" content="..." />
<meta name="twitter:card" content="summary_large_image" />
```

### Heading Hierarchy
```
H1: Page title (one per page, includes primary keyword)
H2: Section headings (2-5 per page)
H3: Sub-section headings
H4+: As needed
```

### Content Guidelines
| Element | Requirement |
|---|---|
| Word count per page | 300+ words minimum |
| Keyword in first 100 words | Yes |
| Internal links | 2-5 per page |
| External links (authoritative) | 1-3 per page |
| Image alt text | Descriptive, includes keyword where natural |

---

## Technical SEO

### Structure Data (JSON-LD)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Business Name",
  "image": "https://domain.com/logo.png",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "Dar es Salaam",
    "addressCountry": "TZ"
  },
  "telephone": "+255712345678",
  "openingHours": "Mo-Fr 08:00-17:00",
  "url": "https://domain.com"
}
</script>
```

### Performance (SEO Factor)
- Core Web Vitals: LCP < 2.5s, FID < 100ms, CLS < 0.1
- Mobile-friendly test: Pass
- HTTPS: Required
- XML Sitemap: Submitted to Google Search Console
- robots.txt: Properly configured

---

## Local SEO (Tanzania Focus)
- Google Business Profile: Complete (verified, all info accurate, photos added)
- Local citations: Consistent NAP (Name, Address, Phone) across all directories
- Location pages: Separate page per service area
- WhatsApp click-to-chat: Tracked as conversion

---

## Monthly SEO Maintenance
| Task | Frequency |
|---|---|
| Check Google Search Console for errors | Weekly |
| Review rankings for target keywords | Monthly |
| Update Google Business Profile post | Weekly |
| Check backlinks | Monthly |
| Review competitor keywords | Quarterly |
