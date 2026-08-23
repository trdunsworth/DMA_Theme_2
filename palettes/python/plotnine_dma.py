"""plotnine ("ggplot2 for Python") integration for DMA Theme palettes.

Provides ggplot2-style scale functions::

    from plotnine import ggplot, aes, geom_point
    import plotnine_dma

    (ggplot(df, aes("x", "y", color="group"))
        + geom_point()
        + plotnine_dma.scale_color_dma())               # categorical

    (ggplot(df, aes("x", "y", fill="value"))
        + geom_tile()
        + plotnine_dma.scale_fill_dma_c("DMA Cool"))     # continuous

Scales:
    scale_color_dma()   / scale_fill_dma()      categorical (qualitative)
    scale_color_dma_b() / scale_fill_dma_b()    binned sequential
    scale_color_dma_c() / scale_fill_dma_c()    continuous gradient
    scale_colour_* aliases match R spelling.

Requires: plotnine >= 0.10
"""

from __future__ import annotations

from typing import Dict, Iterable, Optional

import dma_palette as dma

try:
    from plotnine.scales import (
        scale_color_manual,
        scale_fill_manual,
        scale_color_gradientn,
        scale_fill_gradientn,
        scale_color_steps,
        scale_fill_steps,
    )
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "plotnine is required for plotnine_dma. "
        "Install with: pip install plotnine"
    ) from exc


def _resolve(palette: Optional[str], n: Optional[int]) -> list:
    """Colors for a discrete scale."""
    if palette is None or palette.lower() in ("qualitative", "categorical"):
        return dma.qualitative(n or 8)
    if palette in dma.SEQUENTIAL_SCHEMES:
        # Discrete sampling of a sequential scheme (Brewer-style usage)
        return dma.sequential(palette, n or 5)
    if palette in dma.DIVERGING_SCHEMES:
        return dma.diverging(palette, n or 7)
    raise KeyError(f"Unknown DMA palette {palette!r}")


def _discrete_scale(factory, palette, n, name, **kwargs):
    values = _resolve(palette, n)
    label = name or (f"DMA {palette}" if palette else "DMA")
    return factory(values=values, name=label, **kwargs)


def scale_color_dma(
    palette: Optional[str] = None,
    n: Optional[int] = None,
    name: Optional[str] = None,
    **kwargs,
):
    """Categorical color scale (DMA qualitative by default)."""
    return _discrete_scale(scale_color_manual, palette, n, name, **kwargs)


def scale_fill_dma(
    palette: Optional[str] = None,
    n: Optional[int] = None,
    name: Optional[str] = None,
    **kwargs,
):
    """Categorical fill scale (DMA qualitative by default)."""
    return _discrete_scale(scale_fill_manual, palette, n, name, **kwargs)


# R-spelling aliases
scale_colour_dma = scale_color_dma
scale_colour_dma.__doc__ = scale_color_dma.__doc__


def scale_color_dma_c(
    palette: str = "Cool",
    name: Optional[str] = None,
    **kwargs,
):
    """Continuous color gradient over a DMA sequential scheme."""
    anchors = (_anchors_seq(palette) if palette in dma.SEQUENTIAL_SCHEMES
               else dma.SEQUENTIAL_SCHEMES["Cool"])
    label = name or f"DMA {palette}"
    # anchors are light -> dark; plotnine maps first color to lowest value
    return scale_color_gradientn(colors=anchors, name=label, **kwargs)


def scale_fill_dma_c(
    palette: str = "Cool",
    name: Optional[str] = None,
    **kwargs,
):
    """Continuous fill gradient over a DMA sequential scheme."""
    anchors = (_anchors_seq(palette) if palette in dma.SEQUENTIAL_SCHEMES
               else dma.SEQUENTIAL_SCHEMES["Cool"])
    label = name or f"DMA {palette}"
    return scale_fill_gradientn(colors=anchors, name=label, **kwargs)


def _anchors_seq(scheme: str) -> list:
    if scheme in {"Blues", "Teals", "Turquoises", "Greens", "Oranges"}:
        alias = {
            "Blues": dma.BLUE, "Teals": dma.TEAL,
            "Turquoises": dma.TURQUOISE, "Greens": dma.GREEN,
            "Oranges": dma.WARNING,
        }
        keys = ("50", "100", "200", "300", "400",
                "500", "600", "700", "800", "900")
        return [alias[scheme][k] for k in keys]
    return dma.SEQUENTIAL_SCHEMES[scheme]


def scale_color_dma_b(
    palette: str = "Blues",
    n: int = 5,
    name: Optional[str] = None,
    **kwargs,
):
    """Binned color scale over a DMA sequential scheme."""
    values = dma.sequential(palette, n)
    label = name or f"DMA {palette}"
    return scale_color_steps(colors=values, name=label, **kwargs)


def scale_fill_dma_b(
    palette: str = "Blues",
    n: int = 5,
    name: Optional[str] = None,
    **kwargs,
):
    """Binned fill scale over a DMA sequential scheme."""
    values = dma.sequential(palette, n)
    label = name or f"DMA {palette}"
    return scale_fill_steps(colors=values, name=label, **kwargs)


# R-spelling aliases for continuous/binned
scale_colour_dma_c = scale_color_dma_c
scale_fill_dma_c = scale_fill_dma_c
scale_colour_dma_b = scale_color_dma_b
scale_fill_dma_b = scale_fill_dma_b
