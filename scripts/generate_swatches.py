#!/usr/bin/env python3
"""Generate README swatch images from palette.json.

Single source of truth: palette.json. Run from repo root:

    python3 scripts/generate_swatches.py

Outputs PNGs into assets/. Requires matplotlib.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, to_rgb
from matplotlib.patches import FancyBboxPatch, Rectangle

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
PALETTE = json.loads((ROOT / "palette.json").read_text())

PRIMARY = ["blue", "teal", "turquoise", "green"]
SEMANTIC = ["error", "warning", "info", "success"]
STOPS = ["900", "800", "700", "600", "500", "400", "300", "200", "100", "50"]

plt.rcParams["font.family"] = "DejaVu Sans"


def _label_color(hexcode: str) -> str:
    """Black or white text label depending on background lightness."""
    r, g, b = (int(hexcode[i : i + 2], 16) for i in (1, 3, 5))
    lum = 0.2126 * r + 0.7152 * g + 0.0722 * b
    return "black" if lum > 140 else "white"


def scale_strip(rows: list[tuple[str, list[str]]], title: str,
                out: str) -> None:
    """One row per family, one cell per stop, hex labels inside cells."""
    n_rows, n_cols = len(rows), len(STOPS)
    fig, ax = plt.subplots(figsize=(n_cols * 1.1 + 1.6, n_rows * 0.62 + 0.75))
    ax.set_xlim(0, n_cols + 2); ax.set_ylim(0, n_rows)
    ax.invert_yaxis(); ax.axis("off")

    for i, (name, colors) in enumerate(rows):
        ax.text(-0.05, i + 0.5, name, ha="right", va="center",
                fontsize=11, fontweight="bold", color="#333333")
        for j, hx in enumerate(colors):
            ax.add_patch(Rectangle((j + 0.5, i + 0.06), 1, 0.88,
                                   facecolor=hx, edgecolor="none"))
            ax.text(j + 1.0, i + 0.5, hx.lstrip("#"),
                    ha="center", va="center", fontsize=7.5,
                    color=_label_color(hx))
            if i == 0:  # stop headers on first row
                ax.text(j + 1.0, -0.22, STOPS[j], ha="center",
                        fontsize=8, color="#888888")

    ax.set_title(title, fontsize=13, fontweight="bold",
                 loc="left", pad=14)
    fig.savefig(ASSETS / out, dpi=160, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


def ansi_grid(theme_key: str, title: str, out: str) -> None:
    """16 ANSI swatches in a 2x8 grid."""
    t = PALETTE["themes"][theme_key]
    keys = ["Black", "Red", "Green", "Yellow", "Blue", "Magenta", "Cyan",
            "White", "BrightBlack", "BrightRed", "BrightGreen",
            "BrightYellow", "BrightBlue", "BrightMagenta", "BrightCyan",
            "BrightWhite"]
    cells = [(f"terminal{k}", f"{i} {k.replace('Bright', 'br.').lower()}")
             for i, k in enumerate(keys)]

    fig, ax = plt.subplots(figsize=(9.6, 1.9))
    ax.set_xlim(0, 8); ax.set_ylim(0, 2)
    ax.invert_yaxis(); ax.axis("off")
    for pos, (key, label) in enumerate(cells):
        col, row = pos % 8, pos // 8
        hx = t[key]
        ax.add_patch(Rectangle((col + 0.04, row + 0.08), 0.92, 0.78,
                               facecolor=hx, edgecolor="#00000022"))
        ax.text(col + 0.5, row + 0.47, label, ha="center", va="center",
                fontsize=7.5, color=_label_color(hx))
    ax.set_title(title, fontsize=12, fontweight="bold", loc="left", pad=10)
    fig.savefig(ASSETS / out, dpi=160, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Mock editor preview
# ---------------------------------------------------------------------------

CODE_LINES = [
    # (indent, [(text, token_type), ...])
    [(0, [("import", "keyword"), (" numpy ", "plain"), ("as", "keyword"),
          (" np", "plain")])],
    [(0, [("", "plain")])],
    [(0, [("def", "keyword"), (" ", "plain"), ("load_series", "function"),
          ("(", "punct"), ("path", "param"), ("):", "punct")])],
    [(1, [('"""', "string"), ("Read a CSV of daily readings.", "comment_doc"),
          ('"""', "string")])],
    [(1, [("df", "plain"), (" = ", "operator"), ("pd", "plain"),
          (".", "punct"), ("read_csv", "function"), ("(", "punct"),
          ("path", "param"), (",", "punct"), (" parse_dates", "param"),
          ("=", "operator"), ("True", "number"), (")", "punct")])],
    [(1, [("# resample to weekly means", "comment")])],
    [(1, [("return", "keyword"), (" df", "plain"), (".", "punct"),
          ("resample", "function"), ("(", "punct"), ('"W"', "string"),
          (").", "punct"), ("mean", "function"), ("()", "punct")])],
    [(0, [("", "plain")])],
    [(0, [("series", "plain"), (" = ", "operator"),
          ("load_series", "function"), ("(", "punct"),
          ('"data.csv"', "string"), (")", "punct")])],
    [(0, [("print", "function"), ("(", "punct"),
          ("series", "plain"), (".", "punct"), ("shape", "type"),
          (",", "punct"), (" series", "plain"), (".", "punct"),
          ("mean", "function"), ("())  ", "punct"),
          ("# -> (52, 2)", "comment")])],
]

TOKEN_MAP_LIGHT = {
    "plain": "variable", "keyword": "keyword", "function": "function",
    "string": "string", "number": "number", "comment": "comment",
    "comment_doc": "comment", "type": "type", "param": "parameter",
    "operator": "operator", "punct": "punctuation",
}
TOKEN_MAP_DARK = dict(TOKEN_MAP_LIGHT)


def editor_preview(theme_key: str, out: str) -> None:
    t = PALETTE["themes"][theme_key]
    tmap = TOKEN_MAP_LIGHT if theme_key == "light" else TOKEN_MAP_DARK
    fg = t["foreground"]; bg = t["background"]; gutter = t["backgroundAlt"]
    border = t["border"]; accent = t["cursor"]

    fig = plt.figure(figsize=(7.4, 4.35), dpi=160)

    # window chrome
    ax = fig.add_axes([0.01, 0.01, 0.98, 0.98]); ax.axis("off")
    ax.add_patch(FancyBboxPatch(
        (0.005, 0.02), 0.99, 0.96,
        boxstyle="round,pad=0.008,rounding_size=0.025",
        transform=ax.transAxes, facecolor=gutter,
        edgecolor=border, linewidth=1))
    # traffic lights
    for k, c in enumerate(("#FF5F57", "#FEBC2E", "#28C840")):
        ax.add_patch(plt.Circle((0.045 + k * 0.03, 0.945), 0.011,
                                transform=ax.transAxes,
                                facecolor=c, edgecolor="none"))
    ax.text(0.5, 0.952, "series.py — DMA Theme "
            + ("Light" if theme_key == "light" else "Dark"),
            transform=ax.transAxes, ha="center", va="center",
            fontsize=8.5, color=t["foregroundSubtle"] if "foregroundSubtle"
            in t else fg)

    # editor surface
    ed = fig.add_axes([0.06, 0.045, 0.93, 0.87])
    ed.set_xlim(0, 10); ed.set_ylim(len(CODE_LINES), 0); ed.axis("off")
    ed.add_patch(Rectangle((0, 0), 10, len(CODE_LINES),
                           transform=ed.transData, facecolor=bg,
                           edgecolor="none", zorder=0))
    # gutter
    ed.axvspan(0, 0.62, color=gutter, zorder=1)
    ed.text(0.31, -0.55, "▾", ha="center", va="top", fontsize=7,
            color=t["lineNumberActive"], zorder=2)

    mono = {"family": "DejaVu Sans Mono", "size": 8.6}
    for ln, tokens in enumerate(CODE_LINES):
        indent, parts = tokens[0]
        y = ln + 0.62
        ed.text(0.31, y, str(ln + 1), ha="center", va="center",
                fontsize=7.5,
                color=(t["lineNumberActive"] if ln == 2
                       else t["lineNumber"]), zorder=2)
        x = 0.85 + indent * 0.42
        if ln == 2:  # active line highlight
            ed.axhspan(ln, ln + 1, color=t["lineHighlight"], zorder=1)
        for text, tok in parts:
            if not text:
                continue
            style = dict(mono)
            style["color"] = t.get(tmap[tok], fg)
            if tok == "keyword":
                style["fontweight"] = "bold"
            elif tok == "function":
                pass
            elif tok in ("comment", "comment_doc"):
                pass
            ed.text(x, y, text, ha="left", va="center", zorder=3, **style)
            x += len(text) * 0.155

    # cursor on active line
    ed.plot([3.32], [2.62], marker="|", markersize=9, color=accent,
            zorder=4, markeredgewidth=1.4)

    fig.savefig(ASSETS / out, dpi=160, bbox_inches="tight",
                facecolor="#FFFFFF" if theme_key == "light" else "#000000")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Data-viz scheme strips
# ---------------------------------------------------------------------------

def dv_strips() -> None:
    sys.path.insert(0, str(ROOT / "palettes" / "python"))
    import dma_palette as dma  # noqa: E402

    # qualitative
    q = dma.qualitative()
    _strip_rows([("qualitative", q)],
                "DMA Qualitative", "dv-qualitative.png")

    # sequential
    seq_schemes = ["Blues", "Teals", "Turquoises", "Greens", "Oranges",
                   "Cool", "Ocean", "Forest"]
    rows = [(s, dma.sequential(s, 9)) for s in seq_schemes]
    _strip_rows(rows, "DMA Sequential (light → dark)",
                "dv-sequential.png")

    # diverging
    divs = [(s, dma.diverging(s, 11)) for s in dma.DIVERGING_SCHEMES]
    _strip_rows(divs, "DMA Diverging (end → neutral → end)",
                "dv-diverging.png")


def _strip_rows(rows: list[tuple[str, list[str]]], title: str,
                out: str) -> None:
    n = len(rows)
    width = max(len(c) for _, c in rows)
    fig, axes = plt.subplots(n, 1, figsize=(width * 0.72 + 1.5,
                                            n * 0.52 + 0.7))
    if n == 1:
        axes = [axes]
    for ax, (label, colors) in zip(axes, rows):
        ax.imshow(np.arange(len(colors)).reshape(1, -1),
                  cmap=ListedColormap(colors), aspect="auto",
                  extent=[0, len(colors), 0, 1])
        ax.set_yticks([]); ax.set_xticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)
        ax.set_ylabel(label, rotation=0, ha="right", va="center",
                      fontsize=10)
    fig.suptitle(title, x=0.01, ha="left", fontsize=13,
                 fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(ASSETS / out, dpi=160, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


def main() -> None:
    ASSETS.mkdir(exist_ok=True)

    p = PALETTE["palette"]["primary"]
    s = PALETTE["palette"]["semantic"]
    scale_strip([(k.capitalize(), [p[k][stop] for stop in STOPS])
                 for k in PRIMARY],
                "Primary Scales", "palette-primary.png")
    scale_strip([(k.capitalize(), [s[k][stop] for stop in STOPS])
                 for k in SEMANTIC],
                "Semantic Scales", "palette-semantic.png")

    ansi_grid("light", "ANSI Terminal Colors — Light",
              "ansi-light.png")
    ansi_grid("dark", "ANSI Terminal Colors — Dark",
              "ansi-dark.png")

    editor_preview("light", "preview-light.png")
    editor_preview("dark", "preview-dark.png")

    dv_strips()

    print("Wrote:", sorted(f.name for f in ASSETS.glob("*.png")))


if __name__ == "__main__":
    main()
