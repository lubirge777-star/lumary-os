#!/usr/bin/env python3
"""
Lumary OS — Experience Recommendation Engine
Maps (Industry + Emotion + Budget) to Recommended Experiences,
Experience Profile, Story Arc, and Lumary Score Estimate.
"""

import argparse
import sys
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except (AttributeError, UnicodeDecodeError):
    pass

# ── ANSI Colors ──────────────────────────────────────────────────────
class Style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    GREY = "\033[90m"
    BGRED = "\033[101m"
    BGGREEN = "\033[102m"
    BGYELLOW = "\033[103m"
    BGBLUE = "\033[104m"
    BGMAGENTA = "\033[105m"
    BGCYAN = "\033[106m"

def c(color, text):
    return f"{color}{text}{Style.RESET}"

def banner(text, color=Style.CYAN):
    width = 72
    pad = (width - len(text) - 2) // 2
    return f"{color}{'=' * width}\n{' ' * pad}{text}\n{'=' * width}{Style.RESET}"

# ── DATA ─────────────────────────────────────────────────────────────
INDUSTRIES = [
    "saas", "e-commerce", "restaurant", "construction", "agency",
    "healthcare", "education", "entertainment", "real-estate",
    "non-profit", "fitness", "fashion",
]

EMOTIONS = [
    "trust", "excitement", "calm", "desire", "curiosity",
    "urgency", "luxury", "playful",
]

# Industry relatedness — for partial matching when exact tag missing
INDUSTRY_RELATED = {
    "saas":          ["agency", "e-commerce", "healthcare"],
    "e-commerce":    ["fashion", "saas", "entertainment"],
    "restaurant":    ["fashion", "entertainment", "fitness"],
    "construction":  ["real-estate", "agency", "non-profit"],
    "agency":        ["saas", "fashion", "entertainment", "real-estate"],
    "healthcare":    ["fitness", "non-profit", "education"],
    "education":     ["non-profit", "healthcare", "saas"],
    "entertainment": ["fashion", "agency", "fitness", "restaurant"],
    "real-estate":   ["construction", "agency", "saas"],
    "non-profit":    ["education", "healthcare", "fitness"],
    "fitness":       ["healthcare", "entertainment", "non-profit"],
    "fashion":       ["entertainment", "e-commerce", "agency", "restaurant"],
}

# Emotion relatedness
EMOTION_RELATED = {
    "trust":     ["calm", "luxury"],
    "excitement": ["desire", "playful"],
    "calm":      ["trust", "luxury"],
    "desire":    ["excitement", "luxury"],
    "curiosity": ["playful", "excitement"],
    "urgency":   ["excitement", "desire"],
    "luxury":    ["trust", "calm", "desire"],
    "playful":   ["curiosity", "excitement"],
}

INDUSTRY_LABELS = {
    "saas": "SaaS", "e-commerce": "E-Commerce", "restaurant": "Restaurant",
    "construction": "Construction", "agency": "Agency / Portfolio",
    "healthcare": "Healthcare", "education": "Education",
    "entertainment": "Entertainment", "real-estate": "Real Estate",
    "non-profit": "Non-Profit", "fitness": "Fitness", "fashion": "Fashion",
}

EMOTION_LABELS = {
    "trust": "Trust", "excitement": "Excitement", "calm": "Calm",
    "desire": "Desire", "curiosity": "Curiosity", "urgency": "Urgency",
    "luxury": "Luxury", "playful": "Playful",
}

# ── Experience Profiles ──────────────────────────────────────────────
PROFILES = {
    "premium-minimal": {
        "name": "Premium Minimal",
        "energy": 3, "formality": 9, "warmth": 5, "depth": 8, "tempo": "slow",
        "tagline": "Refined elegance through restraint",
        "mood": "Refined, polished, intentional",
        "palette": "Neutrals, monochrome, single accent",
        "typography": "Serif headlines, generous whitespace",
        "story_arc": ["Hero", "Value Proposition", "Features", "Testimonials", "CTA"],
        "lumary_base": 88,
    },
    "energetic-bold": {
        "name": "Energetic Bold",
        "energy": 9, "formality": 5, "warmth": 3, "depth": 3, "tempo": "fast",
        "tagline": "Impact that commands attention",
        "mood": "Bold, confident, urgent",
        "palette": "High-contrast, saturated primaries",
        "typography": "Sans-serif, heavy weights, tight tracking",
        "story_arc": ["Hero", "Problem", "Solution", "Results", "CTA"],
        "lumary_base": 84,
    },
    "warm-organic": {
        "name": "Warm Organic",
        "energy": 5, "formality": 3, "warmth": 9, "depth": 6, "tempo": "moderate",
        "tagline": "Human connection through design",
        "mood": "Welcoming, earthy, sincere",
        "palette": "Earthy tones, warm accents, soft gradients",
        "typography": "Rounded sans, variable weight, loose leading",
        "story_arc": ["Hero", "Our Story", "Values", "Team", "CTA"],
        "lumary_base": 86,
    },
    "deep-immersive": {
        "name": "Deep Immersive",
        "energy": 4, "formality": 8, "warmth": 3, "depth": 9, "tempo": "slow",
        "tagline": "Worlds that reward exploration",
        "mood": "Mysterious, cinematic, profound",
        "palette": "Dark, jewel tones, atmospheric gradients",
        "typography": "Elegant serif, fine weight contrast",
        "story_arc": ["Hero", "Journey", "Discovery", "Transformation", "CTA"],
        "lumary_base": 90,
    },
    "playful-vibrant": {
        "name": "Playful Vibrant",
        "energy": 8, "formality": 2, "warmth": 8, "depth": 2, "tempo": "fast",
        "tagline": "Joy in every interaction",
        "mood": "Whimsical, lively, friendly",
        "palette": "Bright, pastel-meets-neon, gradients",
        "typography": "Bouncy sans, mixed sizes, variable fonts",
        "story_arc": ["Hero", "Showcase", "Interact", "Social Proof", "CTA"],
        "lumary_base": 82,
    },
}

PROFILE_KEYS = list(PROFILES.keys())

# ── Industry → Profile Affinity (higher spread, sum ≈ 1.0) ───────────
INDUSTRY_PROFILE_AFFINITY = {
    "saas":         {"premium-minimal": 0.45, "deep-immersive": 0.25, "warm-organic": 0.15, "energetic-bold": 0.10, "playful-vibrant": 0.05},
    "e-commerce":   {"energetic-bold": 0.40, "playful-vibrant": 0.25, "premium-minimal": 0.18, "warm-organic": 0.12, "deep-immersive": 0.05},
    "restaurant":   {"warm-organic": 0.50, "playful-vibrant": 0.20, "premium-minimal": 0.15, "energetic-bold": 0.10, "deep-immersive": 0.05},
    "construction": {"premium-minimal": 0.40, "deep-immersive": 0.22, "warm-organic": 0.18, "energetic-bold": 0.15, "playful-vibrant": 0.05},
    "agency":       {"playful-vibrant": 0.35, "energetic-bold": 0.25, "premium-minimal": 0.18, "warm-organic": 0.12, "deep-immersive": 0.10},
    "healthcare":   {"warm-organic": 0.45, "premium-minimal": 0.25, "deep-immersive": 0.15, "energetic-bold": 0.10, "playful-vibrant": 0.05},
    "education":    {"warm-organic": 0.38, "deep-immersive": 0.25, "premium-minimal": 0.18, "playful-vibrant": 0.14, "energetic-bold": 0.05},
    "entertainment":{"playful-vibrant": 0.40, "energetic-bold": 0.30, "deep-immersive": 0.15, "warm-organic": 0.10, "premium-minimal": 0.05},
    "real-estate":  {"premium-minimal": 0.40, "deep-immersive": 0.25, "warm-organic": 0.18, "energetic-bold": 0.12, "playful-vibrant": 0.05},
    "non-profit":   {"warm-organic": 0.45, "premium-minimal": 0.22, "deep-immersive": 0.18, "playful-vibrant": 0.10, "energetic-bold": 0.05},
    "fitness":      {"energetic-bold": 0.45, "playful-vibrant": 0.22, "warm-organic": 0.18, "premium-minimal": 0.10, "deep-immersive": 0.05},
    "fashion":      {"premium-minimal": 0.38, "energetic-bold": 0.22, "playful-vibrant": 0.20, "deep-immersive": 0.12, "warm-organic": 0.08},
}

# ── Emotion → Profile Affinity ───────────────────────────────────────
EMOTION_PROFILE_AFFINITY = {
    "trust":     {"premium-minimal": 0.38, "warm-organic": 0.30, "deep-immersive": 0.18, "energetic-bold": 0.09, "playful-vibrant": 0.05},
    "excitement":{"energetic-bold": 0.50, "playful-vibrant": 0.22, "deep-immersive": 0.13, "warm-organic": 0.10, "premium-minimal": 0.05},
    "calm":      {"premium-minimal": 0.38, "warm-organic": 0.30, "deep-immersive": 0.18, "playful-vibrant": 0.09, "energetic-bold": 0.05},
    "desire":    {"energetic-bold": 0.32, "premium-minimal": 0.25, "deep-immersive": 0.20, "playful-vibrant": 0.13, "warm-organic": 0.10},
    "curiosity": {"deep-immersive": 0.40, "warm-organic": 0.22, "premium-minimal": 0.18, "playful-vibrant": 0.15, "energetic-bold": 0.05},
    "urgency":   {"energetic-bold": 0.50, "playful-vibrant": 0.18, "premium-minimal": 0.14, "deep-immersive": 0.13, "warm-organic": 0.05},
    "luxury":    {"premium-minimal": 0.45, "deep-immersive": 0.28, "energetic-bold": 0.12, "warm-organic": 0.10, "playful-vibrant": 0.05},
    "playful":   {"playful-vibrant": 0.60, "energetic-bold": 0.18, "warm-organic": 0.12, "premium-minimal": 0.05, "deep-immersive": 0.05},
}

# ── Industry-specific Story Arc overrides ────────────────────────────
INDUSTRY_STORY_ARCS = {
    "saas":          ["Hero", "Problem", "Features", "Pricing", "CTA"],
    "e-commerce":    ["Hero", "Showcase", "Benefits", "Testimonials", "CTA"],
    "restaurant":    ["Ambiance Hero", "Menu Preview", "Our Story", "Reservations", "Location"],
    "construction":  ["Project Hero", "Portfolio", "Process", "Testimonials", "Quote"],
    "agency":        ["Hero", "Work", "Process", "About", "Contact"],
    "healthcare":    ["Welcome Hero", "Services", "Team", "Patient Stories", "Appointment"],
    "education":     ["Hero", "Programs", "Values", "Success Stories", "Apply"],
    "entertainment": ["Splash Hero", "Content", "Schedule", "Gallery", "Tickets"],
    "real-estate":   ["Property Hero", "Listings", "Neighborhood", "About", "Tour"],
    "non-profit":    ["Mission Hero", "Impact", "Stories", "Get Involved", "Donate"],
    "fitness":       ["Hero", "Programs", "Trainers", "Results", "Join"],
    "fashion":       ["Lookbook Hero", "Collection", "Editorial", "About", "Shop"],
}

# ── Experience Database (richer tags, 26 experiences) ────────────────
EXPERIENCES = [
    {
        "id": "arrival-awakening",
        "name": "Arrival Awakening",
        "category": "arrival",
        "industry_tags": ["saas", "agency", "real-estate", "education", "construction"],
        "emotion_tags": ["trust", "calm", "luxury"],
        "energy": 2, "formality": 8, "warmth": 6, "depth": 7, "tempo": "slow",
        "description": "A gradual, elegant reveal that introduces the brand with purpose, setting a refined tone from the first interaction.",
    },
    {
        "id": "arrival-split-reveal",
        "name": "Split Reveal",
        "category": "arrival",
        "industry_tags": ["entertainment", "agency", "fashion", "fitness", "restaurant"],
        "emotion_tags": ["excitement", "curiosity", "playful"],
        "energy": 7, "formality": 4, "warmth": 4, "depth": 5, "tempo": "fast",
        "description": "A dramatic split-screen reveal that creates instant intrigue and visual impact from the moment the page loads.",
    },
    {
        "id": "scroll-story",
        "name": "Scroll Story",
        "category": "scroll",
        "industry_tags": ["agency", "non-profit", "education", "saas", "construction", "restaurant"],
        "emotion_tags": ["curiosity", "trust", "calm"],
        "energy": 4, "formality": 5, "warmth": 6, "depth": 8, "tempo": "moderate",
        "description": "A narrative-driven scrolling experience that unfolds content like chapters in a story, rewarding exploration.",
    },
    {
        "id": "signature-moment",
        "name": "Signature Moment",
        "category": "signature-moments",
        "industry_tags": ["fashion", "real-estate", "saas", "agency", "restaurant", "entertainment"],
        "emotion_tags": ["luxury", "trust", "desire"],
        "energy": 5, "formality": 8, "warmth": 5, "depth": 8, "tempo": "slow",
        "description": "A distinctive, high-impact brand moment that becomes the most memorable touchpoint of the entire experience.",
    },
    {
        "id": "storytelling-transformation",
        "name": "Transformation Story",
        "category": "storytelling",
        "industry_tags": ["fitness", "healthcare", "non-profit", "saas", "construction"],
        "emotion_tags": ["trust", "desire", "excitement"],
        "energy": 6, "formality": 5, "warmth": 7, "depth": 8, "tempo": "moderate",
        "description": "A before-and-after narrative arc that showcases real change and builds emotional conviction through contrast.",
    },
    {
        "id": "storytelling-timeline-scroll",
        "name": "Timeline Scroll",
        "category": "storytelling",
        "industry_tags": ["non-profit", "education", "construction", "agency", "real-estate"],
        "emotion_tags": ["trust", "calm", "curiosity"],
        "energy": 3, "formality": 6, "warmth": 5, "depth": 8, "tempo": "slow",
        "description": "A chronological scroll-through that maps the brand's journey, milestones, or evolution with clarity and gravitas.",
    },
    {
        "id": "cursor-reveal",
        "name": "Cursor Reveal",
        "category": "cursor",
        "industry_tags": ["agency", "entertainment", "fashion", "restaurant"],
        "emotion_tags": ["playful", "curiosity", "excitement"],
        "energy": 7, "formality": 2, "warmth": 6, "depth": 2, "tempo": "fast",
        "description": "A custom cursor that reveals hidden content, images, or text on hover — turning navigation into a game.",
    },
    {
        "id": "magnetic-nav",
        "name": "Magnetic Navigation",
        "category": "navigation",
        "industry_tags": ["saas", "agency", "fashion", "real-estate", "restaurant"],
        "emotion_tags": ["curiosity", "playful", "luxury"],
        "energy": 4, "formality": 6, "warmth": 6, "depth": 4, "tempo": "moderate",
        "description": "Navigation links that subtly track the cursor, creating a polished, responsive pull that feels almost alive.",
    },
    {
        "id": "progress-nav",
        "name": "Progress Navigation",
        "category": "navigation",
        "industry_tags": ["education", "saas", "e-commerce", "healthcare", "construction"],
        "emotion_tags": ["trust", "calm", "urgency"],
        "energy": 3, "formality": 7, "warmth": 4, "depth": 5, "tempo": "slow",
        "description": "A visual progress tracker that guides users through multi-step flows with clear orientation and a sense of advancement.",
    },
    {
        "id": "cinematic-hero",
        "name": "Cinematic Hero",
        "category": "heroes",
        "industry_tags": ["entertainment", "agency", "fashion", "real-estate", "restaurant"],
        "emotion_tags": ["excitement", "luxury", "desire"],
        "energy": 8, "formality": 6, "warmth": 3, "depth": 7, "tempo": "fast",
        "description": "An epic, full-viewport hero with motion, video, or parallax that immerses visitors in the brand's world immediately.",
    },
    {
        "id": "minimal-hero",
        "name": "Minimal Hero",
        "category": "heroes",
        "industry_tags": ["saas", "real-estate", "construction", "healthcare", "education"],
        "emotion_tags": ["trust", "calm", "luxury"],
        "energy": 2, "formality": 9, "warmth": 5, "depth": 4, "tempo": "slow",
        "description": "A clean, typographically-driven hero section that communicates authority through restraint and perfect spacing.",
    },
    {
        "id": "tilt-card",
        "name": "Tilt Card",
        "category": "cards",
        "industry_tags": ["agency", "entertainment", "e-commerce", "fashion", "restaurant"],
        "emotion_tags": ["playful", "curiosity", "excitement"],
        "energy": 6, "formality": 3, "warmth": 5, "depth": 3, "tempo": "fast",
        "description": "Interactive cards that respond to mouse movement with 3D tilt, adding a tactile, dimensional quality to content.",
    },
    {
        "id": "expandable-card",
        "name": "Expandable Card",
        "category": "cards",
        "industry_tags": ["education", "saas", "healthcare", "e-commerce", "construction"],
        "emotion_tags": ["curiosity", "trust", "calm"],
        "energy": 4, "formality": 5, "warmth": 5, "depth": 7, "tempo": "moderate",
        "description": "Cards that expand in-place to reveal deeper content without page navigation — ideal for layered storytelling.",
    },
    {
        "id": "brand-loader",
        "name": "Brand Loader",
        "category": "loaders",
        "industry_tags": ["agency", "fashion", "saas", "entertainment"],
        "emotion_tags": ["curiosity", "playful", "luxury"],
        "energy": 4, "formality": 6, "warmth": 5, "depth": 3, "tempo": "moderate",
        "description": "An animated loading sequence that showcases the brand mark or logo in a creative, memorable way before content appears.",
    },
    {
        "id": "page-transition",
        "name": "Page Transition",
        "category": "transitions",
        "industry_tags": ["agency", "fashion", "saas", "real-estate", "restaurant"],
        "emotion_tags": ["calm", "luxury", "trust"],
        "energy": 3, "formality": 8, "warmth": 5, "depth": 6, "tempo": "moderate",
        "description": "Smooth, cinematic page-to-page transitions that make navigation feel seamless and premium.",
    },
    {
        "id": "morph-transition",
        "name": "Morph Transition",
        "category": "transitions",
        "industry_tags": ["agency", "entertainment", "fashion"],
        "emotion_tags": ["playful", "curiosity", "excitement"],
        "energy": 6, "formality": 3, "warmth": 6, "depth": 5, "tempo": "fast",
        "description": "Fluid shape-shifting transitions where one element seamlessly morphs into another, creating visual delight.",
    },
    {
        "id": "hover-3d-tilt",
        "name": "3D Tilt Hover",
        "category": "hover",
        "industry_tags": ["agency", "e-commerce", "fashion", "entertainment", "restaurant"],
        "emotion_tags": ["playful", "curiosity", "desire"],
        "energy": 7, "formality": 2, "warmth": 3, "depth": 3, "tempo": "fast",
        "description": "Elements that respond to cursor position with realistic 3D perspective shifts, adding depth to flat surfaces.",
    },
    {
        "id": "hover-glitch",
        "name": "Glitch Hover",
        "category": "hover",
        "industry_tags": ["entertainment", "agency", "fashion", "fitness"],
        "emotion_tags": ["excitement", "urgency", "playful"],
        "energy": 8, "formality": 3, "warmth": 2, "depth": 4, "tempo": "fast",
        "description": "An edgy, digital distortion effect on hover that evokes a tech-forward, experimental brand attitude.",
    },
    {
        "id": "hover-magnetic",
        "name": "Magnetic Hover",
        "category": "hover",
        "industry_tags": ["agency", "saas", "real-estate", "fashion", "restaurant"],
        "emotion_tags": ["curiosity", "playful", "trust"],
        "energy": 5, "formality": 4, "warmth": 7, "depth": 3, "tempo": "fast",
        "description": "Buttons and elements that subtly attract toward the cursor, creating a playful gravitational pull.",
    },
    {
        "id": "parallax-depth-scroll",
        "name": "Depth Scroll Parallax",
        "category": "parallax",
        "industry_tags": ["real-estate", "entertainment", "agency", "fashion", "construction"],
        "emotion_tags": ["luxury", "curiosity", "calm"],
        "energy": 3, "formality": 7, "warmth": 3, "depth": 9, "tempo": "slow",
        "description": "Multi-layered parallax that creates a profound sense of depth, making the page feel like a living diorama.",
    },
    {
        "id": "text-split-reveal",
        "name": "Split Text Reveal",
        "category": "text",
        "industry_tags": ["agency", "fashion", "saas", "real-estate", "construction"],
        "emotion_tags": ["luxury", "trust", "calm"],
        "energy": 3, "formality": 8, "warmth": 6, "depth": 7, "tempo": "slow",
        "description": "Text that elegantly splits and reveals itself character-by-character, adding typographic sophistication to headings.",
    },
    {
        "id": "text-marquee",
        "name": "Marquee Scroll",
        "category": "text",
        "industry_tags": ["entertainment", "fashion", "agency", "fitness", "restaurant"],
        "emotion_tags": ["excitement", "playful", "desire"],
        "energy": 8, "formality": 2, "warmth": 3, "depth": 2, "tempo": "fast",
        "description": "Continuously scrolling horizontal text that creates energy, movement, and a bold typographic statement.",
    },
    {
        "id": "text-typing",
        "name": "Typing Effect",
        "category": "text",
        "industry_tags": ["education", "saas", "agency", "healthcare", "restaurant"],
        "emotion_tags": ["trust", "calm", "curiosity"],
        "energy": 4, "formality": 4, "warmth": 7, "depth": 5, "tempo": "moderate",
        "description": "Text that types itself out in real-time, creating a conversational, human, and engaging introductory moment.",
    },
    {
        "id": "float-label",
        "name": "Float Label Form",
        "category": "forms",
        "industry_tags": ["saas", "healthcare", "education", "e-commerce", "restaurant", "construction"],
        "emotion_tags": ["trust", "calm", "luxury"],
        "energy": 2, "formality": 8, "warmth": 5, "depth": 4, "tempo": "slow",
        "description": "Form labels that float above inputs on focus — a small detail that signals quality craftsmanship and UX maturity.",
    },
    {
        "id": "video-scroll-trigger",
        "name": "Scroll-Triggered Video",
        "category": "video",
        "industry_tags": ["entertainment", "fashion", "agency", "real-estate", "restaurant"],
        "emotion_tags": ["excitement", "desire", "luxury"],
        "energy": 7, "formality": 5, "warmth": 4, "depth": 8, "tempo": "moderate",
        "description": "Video that plays or advances frame-by-frame based on scroll position, giving users cinematic control of the narrative.",
    },
    {
        "id": "particle-field",
        "name": "Particle Field",
        "category": "particles",
        "industry_tags": ["saas", "entertainment", "agency", "fashion"],
        "emotion_tags": ["luxury", "curiosity", "excitement"],
        "energy": 5, "formality": 7, "warmth": 2, "depth": 8, "tempo": "slow",
        "description": "An atmospheric field of interactive particles that responds to cursor movement, creating a tech-forward ambient backdrop.",
    },
]

# ── ALGORITHM ─────────────────────────────────────────────────────────

def partial_match_score(tag, tag_list, related_map):
    """Score 0-1: 1.0 if exact match, 0.4 if related, 0 otherwise."""
    if tag in tag_list:
        return 1.0
    related = related_map.get(tag, [])
    if any(r in tag_list for r in related):
        return 0.4
    return 0.0


def select_profile(industry, emotion):
    raw = {}
    for pk in PROFILE_KEYS:
        ind_score = INDUSTRY_PROFILE_AFFINITY.get(industry, {}).get(pk, 0)
        emo_score = EMOTION_PROFILE_AFFINITY.get(emotion, {}).get(pk, 0)
        raw[pk] = ind_score * 0.5 + emo_score * 0.5
    best = max(raw, key=raw.get)
    best_val = raw[best]
    # Normalize: top profile = 100%, rest are relative
    scores_pct = {k: round(v / best_val * 100, 1) if best_val > 0 else 0 for k, v in raw.items()}
    return best, scores_pct


def profile_similarity(exp, profile_key):
    p = PROFILES[profile_key]
    ed = abs(exp["energy"] - p["energy"]) / 9.0
    fd = abs(exp["formality"] - p["formality"]) / 9.0
    wd = abs(exp["warmth"] - p["warmth"]) / 9.0
    dd = abs(exp["depth"] - p["depth"]) / 9.0
    if exp["tempo"] == p["tempo"]:
        td = 0
    elif exp["tempo"] == "moderate" or p["tempo"] == "moderate":
        td = 0.5
    else:
        td = 1.0
    total = ed + fd + wd + dd + td
    max_dist = 4 + 1  # 4 dimensions + tempo
    return 1 - (total / max_dist)


def score_experiences(industry, emotion, profile_key):
    scored = []
    for exp in EXPERIENCES:
        ind_match = partial_match_score(industry, exp["industry_tags"], INDUSTRY_RELATED)
        emo_match = partial_match_score(emotion, exp["emotion_tags"], EMOTION_RELATED)
        prof_sim = profile_similarity(exp, profile_key)

        # Weight: industry 0.25, emotion 0.35, profile 0.40
        # Emotion gets more weight since it's the primary driver of experience quality
        total = ind_match * 0.25 + emo_match * 0.35 + prof_sim * 0.40

        # Determine which factor contributed most
        factors = [
            ("industry relevance", ind_match * 0.25),
            ("emotion match", emo_match * 0.35),
            ("profile alignment", prof_sim * 0.40),
        ]
        factors.sort(key=lambda x: -x[1])
        top_reason = factors[0][0]
        second_reason = factors[1][0]

        # Build dynamic explanation
        if total > 0.75:
            why = f"Excellent match — strong {top_reason} reinforced by {second_reason}"
        elif total > 0.50:
            why = f"Good fit — driven primarily by {top_reason}"
        elif total > 0.30:
            why = f"Moderate match — {top_reason} contributes most"
        else:
            why = f"Weak alignment — consider alternative experiences"

        scored.append((total, exp, why, ind_match, emo_match, prof_sim))
    scored.sort(key=lambda x: -x[0])
    return scored


def generate_story_arc(industry, profile_key, budget):
    industry_arc = INDUSTRY_STORY_ARCS.get(industry)
    profile_arc = PROFILES[profile_key]["story_arc"]
    arc = list(industry_arc) if industry_arc else list(profile_arc)
    if budget == "low":
        arc = arc[:3]
    elif budget == "high":
        if len(arc) >= 3:
            # Insert a Deep Dive / Signature Experience section
            arc = arc[:2] + ["Signature Experience"] + arc[2:]
    return arc


def estimate_lumary_score(profile_key, scored_experiences, budget):
    p = PROFILES[profile_key]
    base = p["lumary_base"]

    # Average match score of top 5 experiences
    top5 = [s for s, _, _, _, _, _ in scored_experiences[:5]]
    avg_match = sum(top5) / len(top5) if top5 else 0

    # Score contribution from match quality (0-12 points based on avg)
    quality_bonus = round(avg_match * 12)

    budget_mult = {"low": 0.92, "medium": 1.00, "high": 1.06}
    score = (base + quality_bonus) * budget_mult.get(budget, 1.0)
    return min(round(score), 100)


def generate_ai_prompt(industry, emotion, budget, profile_key, experiences, story_arc):
    exp_list = "\n".join(f"  - {e['name']} ({e['category']})" for e in experiences)
    return (
        f"You are designing a Lumary OS experience for a {INDUSTRY_LABELS.get(industry, industry)} brand "
        f"targeting the emotion of {EMOTION_LABELS.get(emotion, emotion)} "
        f"with a {budget} budget.\n\n"
        f"Selected Profile: {PROFILES[profile_key]['name']}\n"
        f"Mood: {PROFILES[profile_key]['mood']}\n"
        f"Palette: {PROFILES[profile_key]['palette']}\n"
        f"Typography: {PROFILES[profile_key]['typography']}\n\n"
        f"Recommended WOW Moments:\n{exp_list}\n\n"
        "Story Arc (section order): " + " > ".join(story_arc) + "\n\n"
        f"Generate a full-page HTML prototype that brings this experience to life. "
        f"All interactions, scroll-triggered animations, and micro-moments should be implemented "
        f"with production-quality polish. Use the Lumary OS interaction patterns specified."
    )


# ── OUTPUT ────────────────────────────────────────────────────────────

def print_header(industry, emotion, budget):
    print()
    print(banner("Lumary OS Experience Recommendation", Style.BGMAGENTA))
    print()
    print(f"  {c(Style.BOLD, 'Industry')}    {c(Style.CYAN, INDUSTRY_LABELS.get(industry, industry.title()))}")
    print(f"  {c(Style.BOLD, 'Emotion')}    {c(Style.CYAN, EMOTION_LABELS.get(emotion, emotion.title()))}")
    print(f"  {c(Style.BOLD, 'Budget')}     {c(Style.CYAN, budget.title())}")
    print()


def bar_chart(value, color, width=10):
    filled = round(min(max(value, 0), 10) / 10 * width)
    bar = "#" * filled + "-" * (width - filled)
    return f"{color}{bar}{Style.RESET}"


def print_profile(profile_key, profile_scores):
    p = PROFILES[profile_key]
    print(c(Style.BOLD + Style.BGGREEN, "  SELECTED EXPERIENCE PROFILE  "))
    print()
    print(f"  {c(Style.BOLD, p['name'])}")
    print(f"  {c(Style.DIM, p['tagline'])}")
    print()
    print(f"  {c(Style.BOLD, 'Characteristics:')}")
    print(f"    Energy    {bar_chart(p['energy'], Style.YELLOW)}  {p['energy']}/10")
    print(f"    Formality {bar_chart(p['formality'], Style.BLUE)}  {p['formality']}/10")
    print(f"    Warmth    {bar_chart(p['warmth'], Style.RED)}  {p['warmth']}/10")
    print(f"    Depth     {bar_chart(p['depth'], Style.MAGENTA)}  {p['depth']}/10")
    print(f"    Tempo     {c(Style.BOLD, p['tempo'].title())}")
    print()
    print(f"  {c(Style.BOLD, 'Mood:')}       {p['mood']}")
    print(f"  {c(Style.BOLD, 'Palette:')}    {p['palette']}")
    print(f"  {c(Style.BOLD, 'Type:')}       {p['typography']}")
    print()
    print(f"  {c(Style.BOLD, 'Profile Fit Scores:')}")
    for pk, sc in sorted(profile_scores.items(), key=lambda x: -x[1]):
        label = PROFILES[pk]["name"]
        bar = bar_chart(sc / 10, Style.CYAN)
        print(f"    {label:20s} {bar}  {sc:.0f}%")
    print()


def print_experiences(scored_experiences, top_n=5):
    print(c(Style.BOLD + Style.BGBLUE, "  TOP RECOMMENDED WOW MOMENTS  "))
    print()
    for rank, (score, exp, why, ind_match, emo_match, prof_sim) in enumerate(scored_experiences[:top_n], 1):
        pct = score * 100
        color = Style.GREEN if pct >= 70 else (Style.YELLOW if pct >= 50 else Style.GREY)
        rank_str = "#" + str(rank)
        pct_str = f"{pct:.0f}%"
        print("  " + c(Style.BOLD + color, rank_str) + "  " + c(Style.BOLD, exp['name']) + "  " + color + pct_str + Style.RESET)
        print("      " + c(Style.GREY, exp['description']))
        tags_ind = ", ".join(t.title() for t in exp["industry_tags"])
        tags_em = ", ".join(t.title() for t in exp["emotion_tags"])
        print("      " + c(Style.DIM, 'Industry:') + " " + c(Style.CYAN, tags_ind))
        print("      " + c(Style.DIM, 'Emotion:') + "  " + c(Style.MAGENTA, tags_em))
        attrs = f"E:{exp['energy']}  |  F:{exp['formality']}  |  W:{exp['warmth']}  |  D:{exp['depth']}  |  T:{exp['tempo']}"
        print("      " + c(Style.GREY, attrs))
        match_indicators = []
        if ind_match >= 1.0:
            match_indicators.append("industry")
        elif ind_match > 0:
            match_indicators.append("related-industry")
        if emo_match >= 1.0:
            match_indicators.append("emotion")
        elif emo_match > 0:
            match_indicators.append("related-emotion")
        if prof_sim > 0.5:
            match_indicators.append("profile")
        print("      " + c(Style.DIM, 'Match:') + "  " + c(Style.CYAN, ", ".join(match_indicators)))
        print("      " + c(Style.DIM, 'Why:') + " " + why)
        print()
    if len(scored_experiences) > top_n:
        more = len(scored_experiences) - top_n
        msg = f"... and {more} more experiences scored (use --verbose to see all)"
        print("  " + c(Style.DIM, msg))
        print()


def print_story_arc(arc):
    print(c(Style.BOLD + Style.BGYELLOW, "  SUGGESTED STORY ARC  "))
    print()
    for i, section in enumerate(arc, 1):
        arrow = c(Style.CYAN, " > ") if i < len(arc) else ""
        print(f"    {c(Style.BOLD, f'{i}.')} {section}  {arrow}")
    print()


def print_lumary_score(score, profile_key, scored_experiences):
    p = PROFILES[profile_key]
    color = Style.GREEN if score >= 85 else (Style.YELLOW if score >= 70 else Style.RED)
    grade = "A+" if score >= 95 else "A" if score >= 85 else "B+" if score >= 75 else "B" if score >= 65 else "C"

    # Show top 3 match quality
    top3 = [s for s, _, _, _, _, _ in scored_experiences[:3]]
    avg_top3 = sum(top3) / len(top3) if top3 else 0

    print(c(Style.BOLD + Style.BGCYAN, "  LUMARY SCORE ESTIMATE  "))
    print()
    print(f"  {c(Style.BOLD, 'Score:')}   {c(color + Style.BOLD, f'{score}/100')}  ({c(Style.BOLD, grade)})")
    print(f"  {c(Style.BOLD, 'Base:')}    {p['lumary_base']} ({p['name']})")
    print(f"  {c(Style.BOLD, 'Quality:')} Top-3 match avg: {avg_top3:.0%}")

    # Grade description
    descs = {
        "A+": "World-class experience. Ready for production.",
        "A": "Excellent experience. Minor polish recommended.",
        "B+": "Strong experience. Consider additional WOW moments.",
        "B": "Solid foundation. More experiences will elevate.",
        "C": "Adequate. Consider increasing budget for more impact.",
    }
    print(f"  {c(Style.BOLD, 'Grade:')}  {c(color + Style.BOLD, grade)} — {descs.get(grade, '')}")
    print()


def print_ai_prompt(prompt):
    print(c(Style.BOLD + Style.BGRED, "  AI GENERATION PROMPT  "))
    print()
    for line in prompt.strip().split("\n"):
        print(f"  {c(Style.DIM, '|')} {line}")
    print()


def print_verbose(scored_experiences):
    print(c(Style.BOLD + Style.BGYELLOW, "  ALL EXPERIENCES (SCORED & RANKED)  "))
    print()
    for rank, (score, exp, why, _, _, _) in enumerate(scored_experiences, 1):
        pct = score * 100
        color = Style.GREEN if pct >= 60 else (Style.YELLOW if pct >= 40 else Style.GREY)
        bar = bar_chart(pct / 10, color, 8)
        rank_str = f"#{rank:2d}"
        pct_str = f"{pct:.0f}%"
        name_padded = exp['name'].ljust(28)
        print(f"  {c(Style.BOLD, rank_str)}  {bar}  {name_padded}  {color}{pct_str}{Style.RESET}")
    print()


# ── INTERACTIVE MODE ─────────────────────────────────────────────────

def interactive_mode():
    print()
    print(banner("Lumary OS — Interactive Recommendation Engine", Style.BGMAGENTA))
    print()

    print(c(Style.BOLD, "Available Industries:"))
    cols = 4
    for i in range(0, len(INDUSTRIES), cols):
        row = INDUSTRIES[i:i + cols]
        parts = [c(Style.CYAN, ind).ljust(20) for ind in row]
        print("  " + "  ".join(parts))
    print()

    while True:
        industry = input("  " + c(Style.BOLD, 'Industry') + " > ").strip().lower()
        if industry in INDUSTRIES:
            break
        print("  " + c(Style.RED, 'Invalid. Choose from the list above.'))

    print()
    print(c(Style.BOLD, "Available Emotions:"))
    for i in range(0, len(EMOTIONS), 4):
        row = EMOTIONS[i:i + 4]
        parts = [c(Style.MAGENTA, em).ljust(20) for em in row]
        print("  " + "  ".join(parts))
    print()

    while True:
        emotion = input("  " + c(Style.BOLD, 'Emotion') + " > ").strip().lower()
        if emotion in EMOTIONS:
            break
        print("  " + c(Style.RED, 'Invalid. Choose from the list above.'))

    print()
    print("  " + c(Style.BOLD, 'Budget Levels:') + "  " + c(Style.YELLOW, 'low') + ", " + c(Style.YELLOW, 'medium') + ", " + c(Style.YELLOW, 'high'))
    while True:
        budget = input("  " + c(Style.BOLD, 'Budget') + " > ").strip().lower()
        if budget in ("low", "medium", "high"):
            break
        print("  " + c(Style.RED, 'Invalid. Choose low, medium, or high.'))

    return industry, emotion, budget


# ── CLI ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Lumary OS Experience Recommendation Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--industry", help="Target industry")
    parser.add_argument("--emotion", help="Target emotion")
    parser.add_argument("--budget", choices=["low", "medium", "high"], default="medium",
                        help="Budget level (default: medium)")
    parser.add_argument("--interactive", "-i", action="store_true", help="Guided prompt mode")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show all scored experiences")
    parser.add_argument("--list-industries", action="store_true", help="List all industries")
    parser.add_argument("--list-emotions", action="store_true", help="List all emotions")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    if args.list_industries:
        for ind in INDUSTRIES:
            left = c(Style.CYAN, ind).ljust(20)
            print(f"  {left}  {INDUSTRY_LABELS[ind]}")
        return

    if args.list_emotions:
        for em in EMOTIONS:
            left = c(Style.MAGENTA, em).ljust(20)
            print(f"  {left}  {EMOTION_LABELS[em]}")
        return

    if args.interactive:
        industry, emotion, budget = interactive_mode()
    elif args.industry and args.emotion:
        industry = args.industry.lower()
        emotion = args.emotion.lower()
        budget = args.budget.lower()
        if industry not in INDUSTRIES:
            print(f"{c(Style.RED, 'Error:')} Unknown industry '{industry}'.")
            print("  Use --list-industries to see options.")
            sys.exit(1)
        if emotion not in EMOTIONS:
            print(f"{c(Style.RED, 'Error:')} Unknown emotion '{emotion}'.")
            print("  Use --list-emotions to see options.")
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

    # Run engine
    profile_key, profile_scores = select_profile(industry, emotion)
    scored = score_experiences(industry, emotion, profile_key)
    top_n = 5
    top_experiences = [e for _, e, _, _, _, _ in scored[:top_n]]
    story_arc = generate_story_arc(industry, profile_key, budget)
    lumary_score = estimate_lumary_score(profile_key, scored, budget)

    prompt = generate_ai_prompt(industry, emotion, budget, profile_key, top_experiences, story_arc)

    if args.json:
        output = {
            "profile": {
                "key": profile_key,
                "name": PROFILES[profile_key]["name"],
                "characteristics": {
                    "energy": PROFILES[profile_key]["energy"],
                    "formality": PROFILES[profile_key]["formality"],
                    "warmth": PROFILES[profile_key]["warmth"],
                    "depth": PROFILES[profile_key]["depth"],
                    "tempo": PROFILES[profile_key]["tempo"],
                },
                "mood": PROFILES[profile_key]["mood"],
                "palette": PROFILES[profile_key]["palette"],
            },
            "recommendations": [
                {
                    "rank": i + 1,
                    "id": exp["id"],
                    "name": exp["name"],
                    "category": exp["category"],
                    "relevance_score": round(s, 3),
                    "description": exp["description"],
                    "why": why,
                }
                for i, (s, exp, why, _, _, _) in enumerate(scored[:5])
            ],
            "story_arc": story_arc,
            "lumary_score": lumary_score,
            "ai_prompt": prompt,
        }
        print(json.dumps(output, indent=2))
        return

    # Formatted output
    print_header(industry, emotion, budget)
    print_profile(profile_key, profile_scores)
    print_experiences(scored, top_n=5)
    print_story_arc(story_arc)
    print_lumary_score(lumary_score, profile_key, scored)
    print_ai_prompt(prompt)

    if args.verbose:
        print_verbose(scored)


if __name__ == "__main__":
    main()
