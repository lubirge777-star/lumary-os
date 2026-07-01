# Lumary Score Calculator — Example Outputs

## 1. Quick mode (random scores)

```
$ python lumary-score.py --quick

┌──────────────────────────────────────────────────┐
│  Lumary Score Calculator                         │
│  Experiential Quality Report                     │
└──────────────────────────────────────────────────┘

Dimension                     Score   Rating       Bar
────────────────────────────────────────────────────────
△  Curiosity                   78.6   Good         ██████████████░░░░░░
☆  Memory                      84.2   Good         ████████████████░░░░
◇  Interaction Density         91.3   Excellent    ██████████████████░░
▴  Motion Density              67.4   Needs work   █████████████░░░░░░░
⊙  Cognitive Load              73.8   Good         ██████████████░░░░░░
▶  Conversion Readiness        88.1   Excellent    █████████████████░░░
⚡ Performance Budget          95.2   World-class  ███████████████████░
♿ Accessibility                81.5   Good         ████████████████░░░░
────────────────────────────────────────────────────────
Lumary Score                   82.6   Good         ████████████████░░░░

  Rating: Good  |  Score: 82/100
```

## 2. Quick + Verbose (sub-metric breakdowns)

```
$ python lumary-score.py --quick --verbose

┌──────────────────────────────────────────────────┐
│  Lumary Score Calculator                         │
│  Experiential Quality Report                     │
└──────────────────────────────────────────────────┘

Dimension                     Score   Rating       Bar
────────────────────────────────────────────────────────
△  Curiosity                   78.6   Good         ██████████████░░░░░░
  └ Scroll Depth                        85.0
  └ Interaction Rate                    72.0
  └ Time-to-Next-Section                79.0
☆  Memory                      84.2   Good         ████████████████░░░░
  └ WOW Moment Recall                    91.0
  └ CTA Recall                           80.0
  └ Brand Recall                         80.0
◇  Interaction Density         91.3   Excellent    ██████████████████░░
  └ Elements per Viewport                94.0
  └ Response Variety                     88.0
▴  Motion Density              67.4   Needs work   █████████████░░░░░░░
  └ Animated Elements                    55.0
  └ Duration Distribution                72.0
  └ Transition Quality                   76.0
⊙  Cognitive Load              73.8   Good         ██████████████░░░░░░
  └ Info Density                          68.0
  └ Reading Time                          82.0
  └ Distraction Count                     72.0
▶  Conversion Readiness        88.1   Excellent    █████████████████░░░
  └ CTA Visibility                        92.0
  └ Friction Count                        85.0
  └ Trust Signals                         87.0
⚡ Performance Budget          95.2   World-class  ███████████████████░
  └ Lighthouse Score                      98.0
  └ LCP                                   96.0
  └ FID                                   97.0
  └ CLS                                   89.0
♿ Accessibility                81.5   Good         ████████████████░░░░
  └ WCAG AA Compliance                    74.0
  └ Keyboard Navigation                   86.0
  └ Screen Reader                         80.0
  └ Contrast Ratio                        87.0
────────────────────────────────────────────────────────
Lumary Score                   82.6   Good         ████████████████░░░░

  Rating: Good  |  Score: 82/100
```

## 3. JSON output

```
$ python lumary-score.py --quick --json

{
  "lumary_score": 82,
  "rating": "Good",
  "dimensions": {
    "curiosity": {
      "score": 78.6,
      "rating": "Good",
      "sub_metrics": {
        "scroll_depth": 85,
        "interaction_rate": 72,
        "time_to_next": 79
      }
    },
    "memory": {
      "score": 84.2,
      "rating": "Good",
      "sub_metrics": {
        "wow_recall": 91,
        "cta_recall": 80,
        "brand_recall": 80
      }
    },
    ...
  }
}
```

## 4. Specific scores from command-line

```
$ python lumary-score.py --curiosity 85 --memory 92 --interaction 78 --motion 70 --cognitive 88 --conversion 95 --performance 100 --accessibility 90

┌──────────────────────────────────────────────────┐
│  Lumary Score Calculator                         │
│  Experiential Quality Report                     │
└──────────────────────────────────────────────────┘

Dimension                     Score   Rating       Bar
────────────────────────────────────────────────────────
△  Curiosity                   85.0   Excellent    █████████████████░░░
☆  Memory                      92.0   Excellent    ██████████████████░░
◇  Interaction Density         78.0   Good         ████████████████░░░░
▴  Motion Density              70.0   Good         ██████████████░░░░░░
⊙  Cognitive Load              88.0   Excellent    █████████████████░░░
▶  Conversion Readiness        95.0   World-class  ███████████████████░
⚡ Performance Budget         100.0   World-class  ████████████████████
♿ Accessibility                90.0   Excellent    ██████████████████░░
────────────────────────────────────────────────────────
Lumary Score                   87.0   Excellent    █████████████████░░░

  Rating: Excellent  |  Score: 87/100
```

## 5. Interactive mode (no arguments)

```
$ python lumary-score.py

Lumary Score Calculator — Interactive Mode

Enter scores for each dimension (0-100). Press Enter for random (70-90).

  △  Curiosity (0-100) [85]:
  ☆  Memory (0-100) [78]:
  ◇  Interaction Density (0-100) [92]:
  ▴  Motion Density (0-100) [66]:
  ⊙  Cognitive Load (0-100) [81]:
  ▶  Conversion Readiness (0-100) [90]:
  ⚡  Performance Budget (0-100) [97]:
  ♿  Accessibility (0-100) [83]:
```

## 6. Save report

```
$ python lumary-score.py --quick --save my-report.json
  Report saved to my-report.json
```

## 7. Compare two reports

```
$ python lumary-score.py --compare report-alpha.json report-beta.json

  Comparison: report-alpha.json  vs  report-beta.json

  Dimension                     report-alpha.json  report-beta.json    Diff
─────────────────────────────────────────────────────────────────────────────
Curiosity                                78.6           85.0          -6.4 ▼
Memory                                   84.2           92.0          -7.8 ▼
Interaction Density                      91.3           78.0         +13.3 ▲
Motion Density                           67.4           70.0          -2.6
Cognitive Load                           73.8           88.0         -14.2 ▼
Conversion Readiness                     88.1           95.0          -6.9 ▼
Performance Budget                       95.2          100.0          -4.8
Accessibility                            81.5           90.0          -8.5 ▼
─────────────────────────────────────────────────────────────────────────────
Lumary Score                             82.6           87.0          -4.4
```

## Color Reference

| Range      | Color  | Rating        |
|------------|--------|---------------|
| 95–100     | Green  | World-class   |
| 85–94      | Green  | Excellent     |
| 70–84      | Yellow | Good          |
| 50–69      | Red    | Needs work    |
| 0–49       | Red bg | Poor          |
