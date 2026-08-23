"""ggplot2-style DMA scales for Python.

This module is a convenience alias for :mod:`plotnine_dma`. ggplot2 itself is
an R library — in Python the equivalent grammar of graphics is plotnine, and
that's where these scale functions are implemented.

Usage (identical API to plotnine_dma)::

    from ggplot2_dma import scale_color_dma, scale_fill_dma_c
"""

from plotnine_dma import (  # noqa: F401
    scale_color_dma,
    scale_color_dma_b,
    scale_color_dma_c,
    scale_fill_dma,
    scale_fill_dma_b,
    scale_fill_dma_c,
    scale_colour_dma,
    scale_colour_dma_b,
    scale_colour_dma_c,
)

__all__ = [
    "scale_color_dma", "scale_fill_dma",
    "scale_color_dma_b", "scale_fill_dma_b",
    "scale_color_dma_c", "scale_fill_dma_c",
    "scale_colour_dma", "scale_colour_dma_b", "scale_colour_dma_c",
]
