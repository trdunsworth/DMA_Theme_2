"""Matplotlib integration for DMA Theme palettes.

Registers DMA colormaps with matplotlib and provides helpers for the
qualitative cycle.

Usage::

    import matplotlib_dma  # registers colormaps once, on import
    import matplotlib.pyplot as plt

    plt.imshow(data, cmap="DMA Blues")
    plt.scatter(x, y, c=z, cmap="DMA Cool")

    # categorical cycle
    matplotlib_dma.use_dma_cycle()

Requires: matplotlib >= 3.3
"""

from __future__ import annotations

from typing import List

import matplotlib
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.pyplot import rcParams

import dma_palette as dma

__all__ = ["register_colormaps", "cmap", "use_dma_cycle", "CMAP_NAMES"]

_SINGLE_HUE = {
    "Blues": dma.BLUE, "Teals": dma.TEAL, "Turquoises": dma.TURQUOISE,
    "Greens": dma.GREEN, "Oranges": dma.WARNING,
}

_SCALE_KEYS = ("50", "100", "200", "300", "400",
               "500", "600", "700", "800", "900")


def _anchors(name_short: str) -> List[str]:
    """Light->dark anchor list for a scheme's short name."""
    if name_short in _SINGLE_HUE:
        scale = _SINGLE_HUE[name_short]
        return [scale[k] for k in _SCALE_KEYS]
    return list(dma.SEQUENTIAL_SCHEMES[name_short])


def CMAP_NAMES() -> List[str]:  # noqa: N802 - constant-like factory
    seq = [f"DMA {s}" for s in
           ("Blues", "Teals", "Turquoises", "Greens", "Oranges",
            "Cool", "Ocean", "Forest")]
    return seq + [f"DMA Div {s}" for s in dma.DIVERGING_SCHEMES]


def register_colormaps() -> None:
    """Register all DMA colormaps with matplotlib (idempotent)."""
    for name in CMAP_NAMES():
        try:
            cm.get_cmap(name)
            continue                      # already registered
        except ValueError:
            pass
        short = (name.removeprefix("DMA Div ")
                 if name.startswith("DMA Div ") else name.removeprefix("DMA "))
        anchors = (dma.DIVERGING_SCHEMES[short]
                   if name.startswith("DMA Div ") else _anchors(short))
        cmap_obj = LinearSegmentedColormap.from_list(name, anchors)
        if hasattr(matplotlib, "colormaps"):          # mpl >= 3.6
            matplotlib.colormaps.register(cmap_obj, name=name)
        else:
            cm.register_cmap(cmap=cmap_obj, name=name)


def cmap(name: str):
    """Fetch a DMA colormap ('DMA Blues', 'DMA Cool', 'DMA Div Red-Blue')."""
    register_colormaps()
    return cm.get_cmap(name)


def use_dma_cycle(n: int = 8) -> None:
    """Set the default axes color cycle to DMA qualitative colors."""
    from cycler import cycler as make_cycler
    rcParams["axes.prop_cycle"] = make_cycler(color=dma.qualitative(n))


register_colormaps()
