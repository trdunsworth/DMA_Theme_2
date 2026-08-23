"""Seaborn integration for DMA Theme palettes.

Usage::

    import seaborn as sns
    import seaborn_dma

    sns.set_palette(seaborn_dma.qualitative())       # categorical cycle
    sns.color_palette(seaborn_dma.sequential("Cool", 6))

    # or register once and use by name
    seaborn_dma.register()
    sns.set_palette("dma")                            # qualitative
    sns.color_palette("dma:Teals", 7)                 # sequential, 7 colors

Requires: seaborn >= 0.12 (works with older versions too)
"""

from __future__ import annotations

from typing import List, Optional, Tuple

import dma_palette as dma


def qualitative(n: int = 8) -> List[Tuple[float, float, float]]:
    """DMA categorical palette as seaborn RGB tuples."""
    return _as_rgb(dma.qualitative(n))


def sequential(scheme: str = "Blues", n: int = 9) -> List[Tuple[float, float, float]]:
    """Sequential ramp (light->dark) as seaborn RGB tuples."""
    return _as_rgb(dma.sequential(scheme, n))


def diverging(scheme: str = "Red-Blue", n: int = 11) -> List[Tuple[float, float, float]]:
    """Diverging ramp as seaborn RGB tuples."""
    return _as_rgb(dma.diverging(scheme, n))


def semantic() -> dict:
    """Status colors (hex) keyed error/warning/info/success."""
    return dma.semantic()


def register() -> None:
    """Make 'dma' and 'dma:<scheme>' resolvable through seaborn/matplotlib.

    Registers a matplotlib colormap 'dma_<Scheme>' per DMA scheme so that
    ``sns.color_palette("dma:Teals")`` resolves via matplotlib's cmap lookup.
    """
    import matplotlib_dma
    matplotlib_dma.register_colormaps()   # names: DMA Blues -> usable via mpl


def _as_rgb(hexes: List[str]) -> List[Tuple[float, float, float]]:
    from matplotlib.colors import to_rgb
    return [to_rgb(h) for h in hexes]
