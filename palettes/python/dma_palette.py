"""DMA Theme data-visualization palettes.

Brewer-style color schemes (qualitative, sequential, diverging) constructed
from the DMA Theme brand palette. Inspired by the scheme *taxonomy* of
ColorBrewer (Cynthia Brewer) but synthesized entirely from DMA brand colors —
no ColorBrewer colors are used.

Colors come from ``palette.json`` at the repository root. The blue accent is
``#0077CC`` (v1.1.0+).

Zero third-party dependencies. Integration helpers for matplotlib, seaborn,
and plotnine live in their own modules (``matplotlib_dma``,
``seaborn_dma``, ``plotnine_dma``).

Author: Dunsworth-Mann Analytics LLC
License: MIT
"""

from __future__ import annotations

from typing import Dict, List, Sequence, Tuple

__version__ = "1.1.0"
__all__ = [
    "BLUE", "TEAL", "TURQUOISE", "GREEN",
    "ERROR", "WARNING", "INFO", "SUCCESS",
    "SCALES", "QUALITATIVE", "SEQUENTIAL_SCHEMES", "DIVERGING_SCHEMES",
    "SEMANTIC",
    "hex_to_rgb", "rgb_to_hex", "interpolate",
    "dma_colors", "qualitative", "sequential", "diverging", "semantic",
]

# ---------------------------------------------------------------------------
# Full 10-stop scales from palette.json (900 -> 50, dark to light)
# ---------------------------------------------------------------------------

BLUE: Dict[str, str] = {
    "900": "#002B5C", "800": "#003D7A", "700": "#00529E", "600": "#0069C0",
    "500": "#0077CC", "400": "#1A91E6", "300": "#4DA8EE", "200": "#8FC3F5",
    "100": "#C5DEF9", "50": "#E8F4FC",
}
TEAL: Dict[str, str] = {
    "900": "#004D4D", "800": "#006666", "700": "#007F7F", "600": "#009999",
    "500": "#00B3B3", "400": "#1ACCCC", "300": "#4DE5E5", "200": "#99F0F0",
    "100": "#CCF7F7", "50": "#E6FBFB",
}
TURQUOISE: Dict[str, str] = {
    "900": "#005C5C", "800": "#007373", "700": "#008A8A", "600": "#00A1A1",
    "500": "#00B8B8", "400": "#1ACECE", "300": "#4DDDDD", "200": "#99EDED",
    "100": "#CCF6F6", "50": "#E6FBFB",
}
GREEN: Dict[str, str] = {
    "900": "#004D1A", "800": "#006622", "700": "#007F2A", "600": "#009933",
    "500": "#00B33B", "400": "#1ACC4D", "300": "#4DD966", "200": "#99E599",
    "100": "#CCF0CC", "50": "#E6F8E6",
}
ERROR: Dict[str, str] = {
    "900": "#7A0000", "800": "#9E0000", "700": "#C40000", "600": "#E80000",
    "500": "#FF1A1A", "400": "#FF4D4D", "300": "#FF7A7A", "200": "#FFA8A8",
    "100": "#FFD4D4", "50": "#FFEAEA",
}
WARNING: Dict[str, str] = {
    "900": "#7A4A00", "800": "#9E5E00", "700": "#C47300", "600": "#E88800",
    "500": "#FF9F00", "400": "#FFAD33", "300": "#FFC466", "200": "#FFDB99",
    "100": "#FFF0CC", "50": "#FFF8E6",
}
INFO: Dict[str, str] = {
    "900": "#003D7A", "800": "#00529E", "700": "#0069C0", "600": "#007BDB",
    "500": "#0091E6", "400": "#33A8EE", "300": "#66BFFF", "200": "#99D4FF",
    "100": "#CCE9FF", "50": "#E6F4FF",
}
SUCCESS: Dict[str, str] = {
    "900": "#004D1A", "800": "#006622", "700": "#007F2A", "600": "#009933",
    "500": "#00B33B", "400": "#33CC5A", "300": "#66D97A", "200": "#99E599",
    "100": "#CCF0CC", "50": "#E6F8E6",
}

SCALES: Dict[str, Dict[str, str]] = {
    "blue": BLUE, "teal": TEAL, "turquoise": TURQUOISE, "green": GREEN,
    "error": ERROR, "warning": WARNING, "info": INFO, "success": SUCCESS,
}

# Neutral anchors for diverging midpoints / sequential light ends
NEUTRAL_LIGHT = "#F0F4F8"   # neutral.dark["950"] in palette.json
WHITE = "#FFFFFF"

# ---------------------------------------------------------------------------
# Qualitative schemes (categorical). Ordered to alternate hue family and
# lightness so adjacent categories stay distinguishable.
# ---------------------------------------------------------------------------

QUALITATIVE: List[str] = [
    "#0077CC",  # blue
    "#E88800",  # orange   (warning 600)
    "#009933",  # green
    "#C40000",  # red      (error 700)
    "#00A1A1",  # turquoise
    "#9E5E00",  # bronze   (warning 800)
    "#4DA8EE",  # light blue
    "#66D97A",  # light green
]

# ---------------------------------------------------------------------------
# Sequential schemes: named anchor ramps, light -> dark.
# Single-hue schemes sample the 10-stop scale; multi-hue schemes interpolate
# through explicit anchors.
# ---------------------------------------------------------------------------

SEQUENTIAL_SCHEMES: Dict[str, List[str]] = {
    # Single-hue (sampled from SCALES)
    "Blues": None,      # sentinel -> use BLUE scale
    "Teals": None,
    "Turquoises": None,
    "Greens": None,
    "Oranges": None,    # warning scale; warm but not pastel
    # Multi-hue
    "Cool": [           # green -> teal -> blue (GnBu-like)
        GREEN["50"], GREEN["300"], TEAL["500"], BLUE["500"], BLUE["900"],
    ],
    "Ocean": [          # very light aqua -> deep navy
        TURQUOISE["100"], TURQUOISE["300"], TEAL["600"],
        BLUE["700"], BLUE["900"],
    ],
    "Forest": [         # pale mint -> dark forest green
        GREEN["50"], GREEN["200"], GREEN["500"], GREEN["800"], GREEN["900"],
    ],
}

_SINGLE_HUE_ALIAS = {
    "Blues": "blue", "Teals": "teal", "Turquoises": "turquoise",
    "Greens": "green", "Oranges": "warning",
}

# ---------------------------------------------------------------------------
# Diverging schemes: saturated ends, pale neutral center.
# Anchors run end -> center -> other end.
# ---------------------------------------------------------------------------

DIVERGING_SCHEMES: Dict[str, List[str]] = {
    "Red-Blue": [
        ERROR["800"], ERROR["400"], NEUTRAL_LIGHT, INFO["400"], INFO["900"],
    ],
    "Red-Green": [
        ERROR["800"], ERROR["400"], NEUTRAL_LIGHT, SUCCESS["400"], SUCCESS["900"],
    ],
    "Brown-Teal": [
        WARNING["900"], WARNING["400"], WHITE, TEAL["400"], TEAL["900"],
    ],
}

# Semantic status colors — all clear WCAG AA (>= 4.5:1) on white.
# Warning needs the 800 stop; its 600/700 stops measure 2.6:1 / 3.6:1.
SEMANTIC: Dict[str, str] = {
    "error": ERROR["700"],      # C40000  (6.3:1)
    "warning": WARNING["800"],  # 9E5E00  (5.2:1)
    "info": INFO["700"],        # 0069C0  (5.6:1)
    "success": SUCCESS["700"],  # 007F2A  (~5.8:1)
}

# Default categorical export, matches README example
dma_colors: List[str] = QUALITATIVE


# ---------------------------------------------------------------------------
# Color math (RGB space, piecewise-linear over anchors)
# ---------------------------------------------------------------------------

def hex_to_rgb(value: str) -> Tuple[int, int, int]:
    """'#RRGGBB' -> (r, g, b) ints."""
    value = value.lstrip("#")
    if len(value) != 6:
        raise ValueError(f"Expected '#RRGGBB', got {value!r}")
    return int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)


def rgb_to_hex(rgb: Sequence[float]) -> str:
    """(r, g, b) -> '#RRGGBB', values clipped and rounded."""
    r, g, b = (max(0, min(255, int(round(c)))) for c in rgb)
    return f"#{r:02X}{g:02X}{b:02X}"


def _lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def interpolate(anchors: Sequence[str], n: int) -> List[str]:
    """Interpolate n colors along piecewise-linear RGB between anchors.

    n == len(anchors) returns the anchors themselves; smaller n samples the
    ramp evenly including both endpoints.
    """
    if n < 2:
        raise ValueError("n must be >= 2")
    rgbs = [hex_to_rgb(a) for a in anchors]
    if n == len(rgbs):
        return list(anchors)
    out: List[str] = []
    segments = len(rgbs) - 1
    for i in range(n):
        pos = i * segments / (n - 1)
        seg = min(int(pos), segments - 1)
        t = pos - seg
        c0, c1 = rgbs[seg], rgbs[seg + 1]
        out.append(rgb_to_hex(tuple(_lerp(a, b, t) for a, b in zip(c0, c1))))
    return out


def _sample_scale(scale: Dict[str, str], n: int, reverse: bool) -> List[str]:
    stops = [scale[k] for k in ("900", "800", "700", "600", "500",
                                "400", "300", "200", "100", "50")]
    if not reverse:
        stops = stops[::-1]          # light -> dark
    return interpolate(stops, n)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def qualitative(n: int = 8) -> List[str]:
    """n categorical colors (max 8). Cycles if n exceeds the scheme."""
    if n <= 0:
        raise ValueError("n must be >= 1")
    base = QUALITATIVE
    if n <= len(base):
        return base[:n]
    out: List[str] = []
    while len(out) < n:
        out.extend(base)
    return out[:n]


def sequential(scheme: str = "Blues", n: int = 9) -> List[str]:
    """Sequential ramp of n colors, lightest first.

    Single-hue schemes ('Blues', 'Teals', 'Turquoises', 'Greens',
    'Oranges') sample the corresponding 10-stop brand scale.
    Multi-hue schemes ('Cool', 'Ocean', 'Forest') interpolate anchors.
    """
    if n < 2:
        raise ValueError("sequential() needs n >= 2")
    if scheme in _SINGLE_HUE_ALIAS:
        return _sample_scale(SCALES[_SINGLE_HUE_ALIAS[scheme]], n, reverse=False)
    if scheme in SEQUENTIAL_SCHEMES:
        return interpolate(SEQUENTIAL_SCHEMES[scheme], n)
    raise KeyError(
        f"Unknown scheme {scheme!r}. "
        f"Choose from: {sorted(SEQUENTIAL_SCHEMES)}"
    )


def diverging(scheme: str = "Red-Blue", n: int = 11) -> List[str]:
    """Diverging ramp of n colors, end -> neutral center -> other end.

    Odd n places the exact neutral midpoint at the center position;
    even n straddles it.
    """
    if n < 3:
        raise ValueError("diverging() needs n >= 3")
    if scheme not in DIVERGING_SCHEMES:
        raise KeyError(
            f"Unknown scheme {scheme!r}. "
            f"Choose from: {sorted(DIVERGING_SCHEMES)}"
        )
    anchors = DIVERGING_SCHEMES[scheme]
    left = anchors[:2] + [anchors[2]]       # end, mid-light, neutral
    right = [anchors[2]] + anchors[3:]      # neutral, mid-dark, end
    half = n // 2
    if n % 2 == 1:
        # Odd: exact neutral sits in the middle once
        lo = interpolate(left, half + 1)          # includes center
        hi = interpolate(right, half + 1)[1:]
        return lo + hi
    # Even: straddle the center, never duplicating it
    lo = interpolate(left, half + 1)[:-1]
    hi = interpolate(right, half + 1)[1:]
    return lo + hi


def semantic() -> Dict[str, str]:
    """Status colors keyed error/warning/info/success."""
    return dict(SEMANTIC)


if __name__ == "__main__":
    print("DMA palettes", __version__)
    print("qualitative(8): ", qualitative())
    print("sequential Blues 5:", sequential("Blues", 5))
    print("diverging Red-Green 7:", diverging("Red-Green", 7))
