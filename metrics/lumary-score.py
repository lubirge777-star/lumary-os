#!/usr/bin/env python3
"""
Lumary Score Calculator — CLI tool for measuring experiential quality across 8 dimensions.

Usage:
  python lumary-score.py --quick
  python lumary-score.py --quick --verbose
  python lumary-score.py --curiosity 85 --memory 72 --interaction 65 ...
  python lumary-score.py --quick --json
  python lumary-score.py --quick --save my-report.json
  python lumary-score.py --compare report1.json report2.json
"""

import argparse
import io
import json
import math
import os
import random
import sys
from typing import Any

# Reconfigure stdout to support UTF-8 on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
elif sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


# ── ANSI helpers ──────────────────────────────────────────────────────────────

class Style:
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RESET = "\033[0m"
    CLEAR = "\033[2J\033[H"

    @staticmethod
    def fg(r: int, g: int, b: int) -> str:
        return f"\033[38;2;{r};{g};{b}m"

    @staticmethod
    def bg(r: int, g: int, b: int) -> str:
        return f"\033[48;2;{r};{g};{b}m"

    @classmethod
    def colorize(cls, value: float, bold: bool = False) -> str:
        fmt = cls.BOLD if bold else ""
        if value >= 85:
            return f"{fmt}{cls.fg(72, 199, 142)}{Style.RESET}"
        if value >= 70:
            return f"{fmt}{cls.fg(240, 189, 63)}{Style.RESET}"
        return f"{fmt}{cls.fg(229, 83, 75)}{Style.RESET}"

    @classmethod
    def reset(cls) -> str:
        return cls.RESET


# ── Dimension definitions ─────────────────────────────────────────────────────

DIMENSIONS = [
    {
        "key": "curiosity",
        "label": "Curiosity",
        "icon": "?",
        "subs": [
            ("Scroll Depth", "scroll_depth", 0.35),
            ("Interaction Rate", "interaction_rate", 0.35),
            ("Time-to-Next-Section", "time_to_next", 0.30),
        ],
    },
    {
        "key": "memory",
        "label": "Memory",
        "icon": "*",
        "subs": [
            ("WOW Moment Recall", "wow_recall", 0.40),
            ("CTA Recall", "cta_recall", 0.30),
            ("Brand Recall", "brand_recall", 0.30),
        ],
    },
    {
        "key": "interaction",
        "label": "Interaction Density",
        "icon": "+",
        "subs": [
            ("Elements per Viewport", "elements_per_vp", 0.50),
            ("Response Variety", "response_variety", 0.50),
        ],
    },
    {
        "key": "motion",
        "label": "Motion Density",
        "icon": "~",
        "subs": [
            ("Animated Elements", "animated_elements", 0.35),
            ("Duration Distribution", "duration_dist", 0.35),
            ("Transition Quality", "transition_quality", 0.30),
        ],
    },
    {
        "key": "cognitive",
        "label": "Cognitive Load",
        "icon": "o",
        "subs": [
            ("Info Density", "info_density", 0.40),
            ("Reading Time", "reading_time", 0.30),
            ("Distraction Count", "distraction_count", 0.30),
        ],
    },
    {
        "key": "conversion",
        "label": "Conversion Readiness",
        "icon": ">",
        "subs": [
            ("CTA Visibility", "cta_visibility", 0.35),
            ("Friction Count", "friction_count", 0.35),
            ("Trust Signals", "trust_signals", 0.30),
        ],
    },
    {
        "key": "performance",
        "label": "Performance Budget",
        "icon": "!",
        "subs": [
            ("Lighthouse Score", "lighthouse", 0.30),
            ("LCP", "lcp", 0.25),
            ("FID", "fid", 0.25),
            ("CLS", "cls", 0.20),
        ],
    },
    {
        "key": "accessibility",
        "label": "Accessibility",
        "icon": "#",
        "subs": [
            ("WCAG AA Compliance", "wcag_aa", 0.30),
            ("Keyboard Navigation", "keyboard_nav", 0.25),
            ("Screen Reader", "screen_reader", 0.25),
            ("Contrast Ratio", "contrast_ratio", 0.20),
        ],
    },
]

RATINGS = [
    (95, "World-class", Style.fg(56, 178, 112)),
    (85, "Excellent", Style.fg(72, 199, 142)),
    (70, "Good", Style.fg(240, 189, 63)),
    (50, "Needs work", Style.fg(229, 83, 75)),
    (0, "Poor", Style.bg(229, 83, 75) + Style.fg(255, 255, 255)),
]

SUB_KEYS = [sub[1] for dim in DIMENSIONS for sub in dim["subs"]]


# ── Core logic ────────────────────────────────────────────────────────────────

def clamp(val: float, lo: float = 0.0, hi: float = 100.0) -> float:
    return max(lo, min(hi, val))


def score_from_subs(values: dict[str, float], dim: dict) -> float:
    total = 0.0
    for _label, key, weight in dim["subs"]:
        total += clamp(values.get(key, 0.0)) * weight
    return round(total, 1)


def compute_lumary_score(scores: dict[str, float]) -> int:
    total = sum(scores.get(d["key"], 0.0) for d in DIMENSIONS)
    return round(total / len(DIMENSIONS))


def get_rating(value: float) -> tuple[str, str]:
    for lo, label, color in RATINGS:
        if value >= lo:
            return label, color
    return "Unknown", ""


def random_subscore() -> int:
    return random.randint(40, 100)


def generate_random_subs() -> dict[str, float]:
    return {k: random_subscore() for k in SUB_KEYS}


def parse_subs(args) -> dict[str, float] | None:
    vals: dict[str, float] = {}
    # Check if top-level dimension keys provided
    has_dim = any(getattr(args, d["key"], None) is not None for d in DIMENSIONS)
    # Check if any sub-key flag provided
    has_sub = any(
        getattr(args, sub[1], None) is not None
        for dim in DIMENSIONS
        for sub in dim["subs"]
    )
    if not has_dim and not has_sub:
        return None

    # If top-level dims given, distribute evenly to subs
    for dim in DIMENSIONS:
        top = getattr(args, dim["key"], None)
        if top is not None:
            val = clamp(float(top))
            for _label, key, _w in dim["subs"]:
                vals[key] = val

    # Sub-keys override top-level
    for dim in DIMENSIONS:
        for _label, key, _w in dim["subs"]:
            raw = getattr(args, key, None)
            if raw is not None:
                vals[key] = clamp(float(raw))
    return vals


# ── Display helpers ───────────────────────────────────────────────────────────

def _visible_len(s: str) -> int:
    """Return length of string without ANSI escape codes."""
    import re
    return len(re.sub(r"\033\[[0-9;]*m", "", s))


def _ljust_ansi(s: str, width: int) -> str:
    """Left-justify a string that may contain ANSI codes."""
    pad = width - _visible_len(s)
    return s + " " * max(pad, 0)


def _rjust_ansi(s: str, width: int) -> str:
    """Right-justify a string that may contain ANSI codes."""
    pad = width - _visible_len(s)
    return " " * max(pad, 0) + s


def _bar(value: float, width: int = 20) -> str:
    filled = round(value / 100 * width)
    color = Style.colorize(value)
    bar = chr(9608) * filled + chr(9617) * (width - filled)
    return f"{color}{bar}{Style.reset()}"


def _format_score(value: float) -> str:
    color = Style.colorize(value, bold=True)
    return f"{color}{value:>.1f}{Style.reset()}"


def print_table(
    dim_scores: dict[str, float],
    sub_values: dict[str, float] | None = None,
    verbose: bool = False,
    overall: int | None = None,
):
    if overall is None:
        overall = compute_lumary_score(dim_scores)

    rating_label, rating_color = get_rating(overall)

    S = Style
    sep = "\u2500" * 72

    sep = "\u2500" * 72

    def _col_dim(s, a=False):
        return _ljust_ansi(s, 26)

    def _col_score(s, a=False):
        return " " + _rjust_ansi(s, 7)

    def _col_rating(s, a=False):
        return " " + _ljust_ansi(s, 12)

    def _col_bar(s, a=False):
        return "  " + s

    header = _col_dim(f"{S.BOLD}Dimension{S.RESET}")
    header += _col_score(f"{S.BOLD}Score{S.RESET}")
    header += _col_rating(f"{S.BOLD}Rating{S.RESET}")
    header += _col_bar(f"{S.BOLD}Bar{S.RESET}")

    lines = [header, sep]

    for dim in DIMENSIONS:
        key = dim["key"]
        score = dim_scores[key]
        dim_rating, _ = get_rating(score)
        icon = dim["icon"]
        label = f"{icon}  {dim['label']}"

        score_str = _format_score(score)
        bar_str = _bar(score)
        rating_str = dim_rating

        row = _col_dim(label)
        row += _col_score(score_str)
        row += _col_rating(rating_str)
        row += _col_bar(bar_str)
        lines.append(row)

        if verbose and sub_values is not None:
            for sub_label, sub_key, _weight in dim["subs"]:
                sv = sub_values.get(sub_key, 0.0)
                sc = Style.colorize(sv)
                indent = "  " + chr(9492) + " "
                sub_line = f"  {S.DIM}{chr(9492)} {sub_label:<24}{S.RESET}"
                sub_line += _rjust_ansi(f"{sc}{sv:>.1f}{S.RESET}", 20)
                lines.append(sub_line)

    lines.append(sep)

    overall_label = f"{S.BOLD}Lumary Score{S.RESET}"
    overall_score = f"{S.BOLD}{Style.colorize(float(overall), bold=True)}{overall}{S.RESET}"
    overall_rating = f"{rating_color}{S.BOLD}{rating_label}{S.RESET}"
    overall_bar = _bar(overall)

    row = _col_dim(overall_label)
    row += _col_score(overall_score)
    row += _col_rating(overall_rating)
    row += _col_bar(overall_bar)
    lines.append(row)

    print("\n".join(lines))


def print_json(dim_scores: dict[str, float], sub_values: dict[str, float] | None):
    overall = compute_lumary_score(dim_scores)
    rating_label, _ = get_rating(overall)

    data: dict[str, Any] = {
        "lumary_score": overall,
        "rating": rating_label,
        "dimensions": {},
    }
    for dim in DIMENSIONS:
        key = dim["key"]
        dim_rating, _ = get_rating(dim_scores[key])
        entry: dict[str, Any] = {"score": dim_scores[key], "rating": dim_rating}
        if sub_values is not None:
            entry["sub_metrics"] = {
                sub[1]: sub_values[sub[1]]
                for sub in dim["subs"]
                if sub[1] in sub_values
            }
        data["dimensions"][key] = entry

    print(json.dumps(data, indent=2))


def interactive_prompt() -> dict[str, float]:
    print(
        f"{Style.CLEAR}{Style.BOLD}Lumary Score Calculator — Interactive Mode{Style.RESET}\n"
    )
    print("Enter scores for each dimension (0-100). Press Enter for random (70-90).\n")

    result: dict[str, float] = {}
    for dim in DIMENSIONS:
        prompt_str = f"  {dim['icon']}  {dim['label']} (0-100) [{random.randint(70, 90)}]: "
        raw = input(prompt_str).strip()
        if raw == "":
            result[dim["key"]] = float(random.randint(70, 90))
        else:
            try:
                result[dim["key"]] = clamp(float(raw))
            except ValueError:
                print(
                    f"  {Style.fg(229, 83, 75)}Invalid, using random.{Style.RESET}"
                )
                result[dim["key"]] = float(random.randint(70, 90))
    return result


def save_report(
    dim_scores: dict[str, float], sub_values: dict[str, float] | None, filename: str
):
    overall = compute_lumary_score(dim_scores)
    rating_label, _ = get_rating(overall)
    data: dict[str, Any] = {
        "lumary_score": overall,
        "rating": rating_label,
        "dimensions": {},
    }
    for dim in DIMENSIONS:
        key = dim["key"]
        dim_rating, _ = get_rating(dim_scores[key])
        entry: dict[str, Any] = {"score": dim_scores[key], "rating": dim_rating}
        if sub_values is not None:
            entry["sub_metrics"] = {
                sub[1]: sub_values[sub[1]]
                for sub in dim["subs"]
                if sub[1] in sub_values
            }
        data["dimensions"][key] = entry

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"  Report saved to {Style.BOLD}{filename}{Style.RESET}")


def load_report(filename: str) -> dict[str, Any]:
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def cmd_compare(file1: str, file2: str):
    d1 = load_report(file1)
    d2 = load_report(file2)

    f1_name = os.path.basename(file1)
    f2_name = os.path.basename(file2)

    print(
        f"\n  {Style.BOLD}Comparison: {f1_name}  vs  {f2_name}{Style.RESET}\n"
    )

    w1 = len(f1_name) + 2
    w2 = len(f2_name) + 2
    w1 = max(w1, 10)
    w2 = max(w2, 10)

    header = (
        f"{Style.BOLD}{'Dimension':<26}"
        f"{f1_name:>{w1}}  {f2_name:>{w2}}  {'Diff':>7}{Style.RESET}"
    )
    print(header)
    print("─" * (26 + w1 + w2 + 11))

    for dim in DIMENSIONS:
        key = dim["key"]
        s1 = d1["dimensions"][key]["score"]
        s2 = d2["dimensions"][key]["score"]
        diff = s1 - s2
        diff_str = f"{diff:+7.1f}"
        if abs(diff) > 5:
            arrow = "\u25B2" if diff > 0 else "\u25BC"
            diff_str += f" {arrow}"
        s1_str = _format_score(s1)
        s2_str = _format_score(s2)
        print(
            f"{dim['label']:<26}{s1_str:>{w1}}  {s2_str:>{w2}}  {diff_str:>7}"
        )

    o1 = d1["lumary_score"]
    o2 = d2["lumary_score"]
    od = o1 - o2
    od_str = f"{od:+7d}"
    if abs(od) > 5:
        arrow = "\u25B2" if od > 0 else "\u25BC"
        od_str += f" {arrow}"
    o1_str = f"{Style.BOLD}{Style.colorize(float(o1), bold=True)}{o1}{Style.RESET}"
    o2_str = f"{Style.BOLD}{Style.colorize(float(o2), bold=True)}{o2}{Style.RESET}"
    print("─" * (26 + w1 + w2 + 11))
    print(
        f"{Style.BOLD}{'Lumary Score':<26}{o1_str:>{w1}}  {o2_str:>{w2}}  {od_str:>7}"
    )


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Lumary Score Calculator — measure experiential quality across 8 dimensions.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python lumary-score.py --quick\n"
            "  python lumary-score.py --quick --verbose\n"
            "  python lumary-score.py --curiosity 85 --memory 72 --interaction 65\n"
            "  python lumary-score.py --quick --json\n"
            "  python lumary-score.py --quick --save report.json\n"
            "  python lumary-score.py --compare report1.json report2.json\n"
        ),
    )

    parser.add_argument("--quick", action="store_true", help="auto-generate random scores for demo/testing")
    parser.add_argument("--verbose", action="store_true", help="show sub-metric breakdowns")
    parser.add_argument("--json", action="store_true", help="output as JSON")
    parser.add_argument("--save", metavar="FILE", help="save report to JSON file")
    parser.add_argument("--compare", nargs=2, metavar=("FILE1", "FILE2"), help="compare two saved reports")

    # Dimension top-level scores
    dim_help = f"score (0-100) for"
    for dim in DIMENSIONS:
        parser.add_argument(f"--{dim['key']}", type=float, help=f"{dim_help} {dim['label']}")

    # Sub-metric scores
    for dim in DIMENSIONS:
        for sub_label, sub_key, _w in dim["subs"]:
            flag = f"--{sub_key.replace('_', '-')}"
            parser.add_argument(flag, type=float, help=f"sub-score for {sub_label}")

    args = parser.parse_args()

    # ── compare mode ──────────────────────────────────────────────────────
    if args.compare:
        cmd_compare(args.compare[0], args.compare[1])
        return

    # ── gather sub-values ─────────────────────────────────────────────────
    sub_values: dict[str, float] | None = None

    if args.quick:
        sub_values = generate_random_subs()
    else:
        parsed = parse_subs(args)
        if parsed is not None:
            sub_values = parsed
        else:
            # Interactive mode
            dim_scores = interactive_prompt()
            # Still need sub-values for verbose mode — fill from dim averages
            sub_values = {}
            for dim in DIMENSIONS:
                ds = dim_scores[dim["key"]]
                for _label, key, _w in dim["subs"]:
                    sub_values[key] = ds
            _run_display(dim_scores, sub_values, args)
            return

    # Build dimension scores from sub-values
    dim_scores: dict[str, float] = {}
    for dim in DIMENSIONS:
        dim_scores[dim["key"]] = score_from_subs(sub_values, dim)

    _run_display(dim_scores, sub_values, args)


def _run_display(
    dim_scores: dict[str, float],
    sub_values: dict[str, float],
    args: argparse.Namespace,
):
    overall = compute_lumary_score(dim_scores)
    rating_label, rating_color = get_rating(overall)

    if not args.json:
        # ── banner ───────────────────────────────────────────────────────
        banner = (
            f"{Style.BOLD}{Style.fg(155, 133, 255)}"
            f"{'/' + '-' * 50 + chr(92)}\n"
            f"|  Lumary Score Calculator{' ' * 28}|\n"
            f"|  Experiential Quality Report{' ' * 24}|\n"
            f"{chr(92) + '-' * 50 + '/'}"
            f"{Style.RESET}"
        )
        print(banner)
        print()

    if args.json:
        print_json(dim_scores, sub_values)
    else:
        print_table(dim_scores, sub_values, verbose=args.verbose, overall=overall)
        print(
            f"\n  Rating: {rating_color}{Style.BOLD}{rating_label}{Style.RESET}"
            f"  |  Score: {Style.BOLD}{overall}{Style.RESET}/100\n"
        )

    if args.save:
        save_report(dim_scores, sub_values, args.save)


if __name__ == "__main__":
    main()
