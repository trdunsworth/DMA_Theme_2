"""
DMA Theme - Python Palette Package
===================================

A semantic color palette for data visualization in Python.
Compatible with matplotlib, seaborn, plotnine, and ggplot2 (via plotnine).

Author: Dunsworth-Mann Analytics LLC
https://dunsworth-mann.com

Installation:
    pip install -e .

Usage:
    from dma_palette import (
        DMA_BLUE, DMA_TEAL, DMA_TURQUOISE, DMA_GREEN,
        DMA_ERROR, DMA_WARNING, DMA_INFO, DMA_SUCCESS,
        scale_color_dma, scale_fill_dma, theme_dma,
        get_cmap, set_theme, register_palettes
    )
"""

# Core palette
from .dma_palette import (
    # Primary colors
    DMA_BLUE,
    DMA_TEAL,
    DMA_TURQUOISE,
    DMA_GREEN,
    # Semantic colors
    DMA_ERROR,
    DMA_WARNING,
    DMA_INFO,
    DMA_SUCCESS,
    # Neutral colors
    DMA_NEUTRAL_LIGHT,
    DMA_NEUTRAL_DARK,
    # Predefined palettes
    DMA_QUALITATIVE_BOLD,
    DMA_QUALITATIVE_LIGHT,
    DMA_QUALITATIVE_DARK,
    DMA_QUALITATIVE_SEMANTIC,
    DMA_SEQUENTIAL_BLUE,
    DMA_SEQUENTIAL_TEAL,
    DMA_SEQUENTIAL_TURQUOISE,
    DMA_SEQUENTIAL_GREEN,
    DMA_SEQUENTIAL_GRAY_LIGHT,
    DMA_SEQUENTIAL_GRAY_DARK,
    DMA_DIVERGING_BLUE_ORANGE,
    DMA_DIVERGING_TEAL_RED,
    DMA_DIVERGING_GREEN_PURPLE,
    DMA_BLUES_9,
    DMA_TEALS_9,
    DMA_TURQUOISES_9,
    DMA_GREENS_9,
    DMA_REDS_9,
    DMA_ORANGES_9,
    DMA_GRAYS_9,
    # Colormaps
    DMA_CMAPS,
    # Functions
    register_cmaps,
    get_sequential_cmap,
    get_diverging_cmap,
    get_qualitative_cmap,
    get_color_cycler,
    set_default_cycler,
    get_palette,
    list_palettes,
    demo_palettes,
    hex_to_rgb,
    hex_to_rgb255,
    rgb_to_hex,
    ALL_COLORS,
)

# plotnine / ggplot2 integration
from .ggplot2_dma import (
    scale_color_dma,
    scale_fill_dma,
    scale_color_dma_c,
    scale_fill_dma_c,
    scale_color_dma_d,
    scale_fill_dma_d,
    scale_color_dma_brewer,
    scale_fill_dma_brewer,
    scale_colour_dma,
    scale_colour_dma_c,
    scale_colour_dma_d,
    scale_colour_dma_brewer,
    theme_dma,
    theme_dma_dark,
)

# plotnine specific
from .plotnine_dma import register_scales

# Matplotlib integration
from .matplotlib_dma import (
    DMA_CMAPS as MPL_DMA_CMAPS,
    get_cmap,
    list_cmaps,
    get_cycler as mpl_get_cycler,
    set_default_cycler as mpl_set_default_cycler,
    apply_style,
    style_context,
    DMA_STYLE_LIGHT,
    DMA_STYLE_DARK,
    demo_colormaps,
    demo_color_cycle,
    write_style_sheets,
)

# Seaborn integration
from .seaborn_dma import (
    register_palettes,
    register_cmaps as seaborn_register_cmaps,
    get_palette as sb_get_palette,
    set_palette,
    set_theme,
    axes_style,
    plotting_context,
    color_palette,
    diverging_palette,
    cubehelix_palette,
    demo_palettes as sb_demo_palettes,
    demo_heatmap,
    DMA_SEABORN_THEME_LIGHT,
    DMA_SEABORN_THEME_DARK,
)

__version__ = "1.0.0"
__author__ = "Dunsworth-Mann Analytics LLC"
__email__ = "contact@dunsworth-mann.com"
__url__ = "https://github.com/dunsworth-mann-analytics/dma-theme"

# Auto-register on import
try:
    register_cmaps()
except Exception:
    pass

try:
    register_palettes()
except Exception:
    pass

try:
    register_scales()
except Exception:
    pass

__all__ = [
    # Version info
    "__version__",
    "__author__",
    "__email__",
    "__url__",
    
    # Core colors
    "DMA_BLUE",
    "DMA_TEAL",
    "DMA_TURQUOISE",
    "DMA_GREEN",
    "DMA_ERROR",
    "DMA_WARNING",
    "DMA_INFO",
    "DMA_SUCCESS",
    "DMA_NEUTRAL_LIGHT",
    "DMA_NEUTRAL_DARK",
    
    # Palettes
    "DMA_QUALITATIVE_BOLD",
    "DMA_QUALITATIVE_LIGHT",
    "DMA_QUALITATIVE_DARK",
    "DMA_QUALITATIVE_SEMANTIC",
    "DMA_SEQUENTIAL_BLUE",
    "DMA_SEQUENTIAL_TEAL",
    "DMA_SEQUENTIAL_TURQUOISE",
    "DMA_SEQUENTIAL_GREEN",
    "DMA_SEQUENTIAL_GRAY_LIGHT",
    "DMA_SEQUENTIAL_GRAY_DARK",
    "DMA_DIVERGING_BLUE_ORANGE",
    "DMA_DIVERGING_TEAL_RED",
    "DMA_DIVERGING_GREEN_PURPLE",
    "DMA_BLUES_9",
    "DMA_TEALS_9",
    "DMA_TURQUOISES_9",
    "DMA_GREENS_9",
    "DMA_REDS_9",
    "DMA_ORANGES_9",
    "DMA_GRAYS_9",
    
    # Colormaps
    "DMA_CMAPS",
    "MPL_DMA_CMAPS",
    
    # Core functions
    "register_cmaps",
    "get_sequential_cmap",
    "get_diverging_cmap",
    "get_qualitative_cmap",
    "get_color_cycler",
    "set_default_cycler",
    "get_palette",
    "list_palettes",
    "demo_palettes",
    "hex_to_rgb",
    "hex_to_rgb255",
    "rgb_to_hex",
    "ALL_COLORS",
    
    # plotnine / ggplot2
    "scale_color_dma",
    "scale_fill_dma",
    "scale_color_dma_c",
    "scale_fill_dma_c",
    "scale_color_dma_d",
    "scale_fill_dma_d",
    "scale_color_dma_brewer",
    "scale_fill_dma_brewer",
    "scale_colour_dma",
    "scale_colour_dma_c",
    "scale_colour_dma_d",
    "scale_colour_dma_brewer",
    "theme_dma",
    "theme_dma_dark",
    "register_scales",
    
    # Matplotlib
    "get_cmap",
    "list_cmaps",
    "mpl_get_cycler",
    "mpl_set_default_cycler",
    "apply_style",
    "style_context",
    "DMA_STYLE_LIGHT",
    "DMA_STYLE_DARK",
    "demo_colormaps",
    "demo_color_cycle",
    "write_style_sheets",
    
    # Seaborn
    "register_palettes",
    "seaborn_register_cmaps",
    "sb_get_palette",
    "set_palette",
    "set_theme",
    "axes_style",
    "plotting_context",
    "color_palette",
    "diverging_palette",
    "cubehelix_palette",
    "sb_demo_palettes",
    "demo_heatmap",
    "DMA_SEABORN_THEME_LIGHT",
    "DMA_SEABORN_THEME_DARK",
]