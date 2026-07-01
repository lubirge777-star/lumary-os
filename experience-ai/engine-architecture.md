# Lumary OS — Experience Recommendation Engine Architecture

## Overview

The Experience Recommendation Engine maps **(Industry + Emotion + Budget)** into a complete experience blueprint consisting of:

- An **Experience Profile** (design personality)
- **Top-5 WOW Moments** (ranked interaction patterns)
- A **Story Arc** (section order for the page)
- A **Lumary Score Estimate** (quality/impact metric)
- An **AI Generation Prompt** (ready-to-use)

---

## Data Flow

```
┌──────────┐   ┌──────────┐   ┌──────────┐
│ Industry  │   │ Emotion  │   │  Budget  │
└─────┬────┘   └─────┬────┘   └────┬─────┘
      │               │             │
      ▼               ▼             │
┌─────────────────────────┐         │
│  Profile Selection      │         │
│  (weighted affinity)    │         │
└───────────┬─────────────┘         │
            │                       │
            ▼                       │
┌─────────────────────────┐         │
│  Experience Scoring      │         │
│  (3-factor weighted)     │         │
└───────────┬─────────────┘         │
            │                       │
            ▼                       ▼
┌─────────────────────────────────────┐
│  Story Arc Generation               │
│  (industry-arced + profile default) │
└───────────┬─────────────────────────┘
            │
            ▼
┌─────────────────────────────────────┐
│  Lumary Score Calculation           │
│  (base + experience bonus × budget) │
└───────────┬─────────────────────────┘
            │
            ▼
┌─────────────────────────────────────┐
│  AI Prompt Synthesis                │
│  (natural language generation spec) │
└─────────────────────────────────────┘
```

---

## Component Details

### 1. Embedded Database

| Dataset | Size | Description |
|---|---|---|
| Industries | 12 | SaaS, E-commerce, Restaurant, Construction, Agency, Healthcare, Education, Entertainment, Real Estate, Non-profit, Fitness, Fashion |
| Emotions | 8 | Trust, Excitement, Calm, Desire, Curiosity, Urgency, Luxury, Playful |
| Experience Profiles | 5 | Premium Minimal, Energetic Bold, Warm Organic, Deep Immersive, Playful Vibrant |
| Experiences | 26 | Mapped from Lumary OS patterns with 5-dimensional attributes |

### 2. Profile Selection Algorithm

For each `(industry, emotion)` pair, every profile receives a composite score:

```
profile_score = (industry_affinity × 0.5) + (emotion_affinity × 0.5)
```

Where affinity values are pre-defined in `INDUSTRY_PROFILE_AFFINITY` and `EMOTION_PROFILE_AFFINITY` matrices. The profile with the highest score is selected.

### 3. Experience Scoring Algorithm

Each experience receives a relevance score using three weighted factors:

```
relevance = (industry_match × 0.3) + (emotion_match × 0.4) + (profile_similarity × 0.3)
```

- **Industry Match** (0.3): Binary — does the experience's industry_tags include the target industry?
- **Emotion Match** (0.4): Binary — does the experience's emotion_tags include the target emotion?
- **Profile Similarity** (0.3): Euclidean-style distance across 5 dimensions:

```
distance = |energy_diff|/9 + |formality_diff|/9 + |warmth_diff|/9 + |depth_diff|/9 + tempo_penalty
similarity = 1 - (distance / max_possible_distance)
```

Tempo penalty: 0 if exact match, 0.5 if one is "moderate", 1.0 otherwise.

### 4. Story Arc Generation

Industry-specific arcs are preferred (defined in `INDUSTRY_STORY_ARCS`). If none exists, the profile's default arc is used. Budget affects arc length:

- **Low**: First 3 sections only
- **Medium**: Standard arc
- **High**: Arc expanded with a "Deep Dive" insert

### 5. Lumary Score Estimate

```
lumary_score = (profile_base + experience_bonus) × budget_multiplier
```

- **Profile Base**: 82–90 (inherent quality of the profile)
- **Experience Bonus**: min(scored_experiences_count × 2, 10)
- **Budget Multiplier**: low=0.90, medium=1.00, high=1.08
- **Capped at 100**

### 6. AI Prompt Synthesis

Concatenates all selected data into a structured natural language prompt that a generative AI can use to produce a complete HTML prototype page.

---

## Experience Dimensional Model

Each experience is stored with 5 core dimensions:

| Dimension | Range | Description |
|---|---|---|
| Energy | 1–10 | Visual intensity, motion level |
| Formality | 1–10 | Structure, polish, convention |
| Warmth | 1–10 | Human feel, approachability |
| Depth | 1–10 | Complexity, information richness |
| Tempo | slow/moderate/fast | Pace of interaction |

---

## CLI Interface

```
python recommendation-engine.py --industry saas --emotion trust
python recommendation-engine.py --industry restaurant --emotion desire --budget high
python recommendation-engine.py --industry fashion --emotion luxury --verbose
python recommendation-engine.py --interactive
python recommendation-engine.py --list-industries
python recommendation-engine.py --list-emotions
python recommendation-engine.py --json
```

Flags:
- `--industry`, `--emotion`, `--budget`: Direct input
- `--interactive` / `-i`: Guided prompt mode
- `--verbose` / `-v`: Display all 26 experiences with scores
- `--list-industries`, `--list-emotions`: List available options
- `--json`: Machine-readable JSON output

---

## File Structure

```
experience-ai/
├── recommendation-engine.py   # Main engine (CLI + algorithm + output)
└── engine-architecture.md     # This document
```

Standard library only — no external dependencies.
