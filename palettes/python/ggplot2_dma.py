"""
DMA Theme - plotnine / ggplot2 Integration for Python
======================================================

Provides scale_color_dma and scale_fill_dma functions for plotnine,
compatible with ggplot2's scale_color_* and scale_fill_* interface.

Author: Dunsworth-Mann Analytics LLC
https://dunsworth-mann.com
"""

from typing import List, Optional, Union
from plotnine import ggplot, aes, scale_color_manual, scale_fill_manual, discrete_scale
from plotnine.scales.scale_discrete import ScaleDiscrete
from plotnine.scales.scale_continuous import ScaleContinuous
from plotnine.scales.scale import scale_factory

from .dma_palette import (
    DMA_QUALITATIVE_BOLD,
    DMA_QUALITATIVE_LIGHT,
    DMA_QUALITATIVE_DARK,
    DMA_QUALITATIVE_SEMANTIC,
    DMA_SEQUENTIAL_BLUE,
    DMA_SEQUENTIAL_TEAL,
    DMA_SEQUENTIAL_TURQUOISE,
    DMA_SEQUENTIAL_GREEN,
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
)


# =============================================================================
# Discrete Color Scales
# =============================================================================

def scale_color_dma(
    palette: str = "bold",
    na_value: str = "#6E89A0",
    guide: str = "legend",
    **kwargs
):
    """
    DMA color scale for discrete data (plotnine/ggplot2 compatible).
    
    Parameters
    ----------
    palette : str
        Palette name. Options: 'bold', 'light', 'dark', 'semantic'
    na_value : str
        Color for NA/missing values
    guide : str
        Guide type ('legend' or 'none')
    **kwargs : 
        Additional arguments passed to scale_color_manual
    
    Returns
    -------
    ScaleDiscrete
        A plotnine discrete color scale
    
    Examples
    --------
    >>> from plotnine import ggplot, aes, geom_point
    >>> from dma_palette import scale_color_dma
    >>> (ggplot(data, aes(x='x', y='y', color='category'))
    ...  + geom_point()
    ...  + scale_color_dma(palette='bold'))
    """
    palettes = {
        "bold": DMA_QUALITATIVE_BOLD,
        "light": DMA_QUALITATIVE_LIGHT,
        "dark": DMA_QUALITATIVE_DARK,
        "semantic": DMA_QUALITATIVE_SEMANTIC,
    }
    colors = palettes.get(palette, DMA_QUALITATIVE_BOLD)
    
    return scale_color_manual(values=colors, na_value=na_value, guide=guide, **kwargs)


def scale_fill_dma(
    palette: str = "bold",
    na_value: str = "#6E89A0",
    guide: str = "legend",
    **kwargs
):
    """
    DMA fill scale for discrete data (plotnine/ggplot2 compatible).
    
    Parameters
    ----------
    palette : str
        Palette name. Options: 'bold', 'light', 'dark', 'semantic'
    na_value : str
        Color for NA/missing values
    guide : str
        Guide type ('legend' or 'none')
    **kwargs : 
        Additional arguments passed to scale_fill_manual
    
    Returns
    -------
    ScaleDiscrete
        A plotnine discrete fill scale
    
    Examples
    --------
    >>> from plotnine import ggplot, aes, geom_bar
    >>> from dma_palette import scale_fill_dma
    >>> (ggplot(data, aes(x='category', fill='category'))
    ...  + geom_bar()
    ...  + scale_fill_dma(palette='semantic'))
    """
    palettes = {
        "bold": DMA_QUALITATIVE_BOLD,
        "light": DMA_QUALITATIVE_LIGHT,
        "dark": DMA_QUALITATIVE_DARK,
        "semantic": DMA_QUALITATIVE_SEMANTIC,
    }
    colors = palettes.get(palette, DMA_QUALITATIVE_BOLD)
    
    return scale_fill_manual(values=colors, na_value=na_value, guide=guide, **kwargs)


# =============================================================================
# Continuous Color Scales (Sequential)
# =============================================================================

class scale_color_dma_continuous(ScaleContinuous):
    """Continuous color scale using DMA sequential palettes."""
    
    def __init__(
        self,
        palette: str = "blue",
        na_value: str = "#6E89A0",
        guide: str = "colorbar",
        **kwargs
    ):
        palettes = {
            "blue": DMA_SEQUENTIAL_BLUE,
            "teal": DMA_SEQUENTIAL_TEAL,
            "turquoise": DMA_SEQUENTIAL_TURQUOISE,
            "green": DMA_SEQUENTIAL_GREEN,
            "gray_light": [c for c in reversed(DMA_GRAYS_9)],
            "gray_dark": DMA_GRAYS_9,
        }
        colors = palettes.get(palette, DMA_SEQUENTIAL_BLUE)
        
        from matplotlib.colors import LinearSegmentedColormap
        cmap = LinearSegmentedColormap.from_list(f"dma_{palette}", colors)
        
        super().__init__(
            palette=cmap,
            na_value=na_value,
            guide=guide,
            **kwargs
        )


class scale_fill_dma_continuous(ScaleContinuous):
    """Continuous fill scale using DMA sequential palettes."""
    
    def __init__(
        self,
        palette: str = "blue",
        na_value: str = "#6E89A0",
        guide: str = "colorbar",
        **kwargs
    ):
        palettes = {
            "blue": DMA_SEQUENTIAL_BLUE,
            "teal": DMA_SEQUENTIAL_TEAL,
            "turquoise": DMA_SEQUENTIAL_TURQUOISE,
            "green": DMA_SEQUENTIAL_GREEN,
            "gray_light": [c for c in reversed(DMA_GRAYS_9)],
            "gray_dark": DMA_GRAYS_9,
        }
        colors = palettes.get(palette, DMA_SEQUENTIAL_BLUE)
        
        from matplotlib.colors import LinearSegmentedColormap
        cmap = LinearSegmentedColormap.from_list(f"dma_{palette}", colors)
        
        super().__init__(
            palette=cmap,
            na_value=na_value,
            guide=guide,
            **kwargs
        )


# Factory functions for continuous scales
def scale_color_dma_c(
    palette: str = "blue",
    na_value: str = "#6E89A0",
    guide: str = "colorbar",
    **kwargs
):
    """
    DMA continuous color scale (sequential).
    
    Parameters
    ----------
    palette : str
        Palette name. Options: 'blue', 'teal', 'turquoise', 'green', 'gray_light', 'gray_dark'
    na_value : str
        Color for NA/missing values
    guide : str
        Guide type ('colorbar' or 'legend')
    **kwargs : 
        Additional arguments passed to the scale
    
    Returns
    -------
    ScaleContinuous
        A plotnine continuous color scale
    
    Examples
    --------
    >>> from plotnine import ggplot, aes, geom_point
    >>> from dma_palette import scale_color_dma_c
    >>> (ggplot(data, aes(x='x', y='y', color='value'))
    ...  + geom_point()
    ...  + scale_color_dma_c(palette='teal'))
    """
    return scale_color_dma_continuous(palette=palette, na_value=na_value, guide=guide, **kwargs)


def scale_fill_dma_c(
    palette: str = "blue",
    na_value: str = "#6E89A0",
    guide: str = "colorbar",
    **kwargs
):
    """
    DMA continuous fill scale (sequential).
    
    Parameters
    ----------
    palette : str
        Palette name. Options: 'blue', 'teal', 'turquoise', 'green', 'gray_light', 'gray_dark'
    na_value : str
        Color for NA/missing values
    guide : str
        Guide type ('colorbar' or 'legend')
    **kwargs : 
        Additional arguments passed to the scale
    
    Returns
    -------
    ScaleContinuous
        A plotnine continuous fill scale
    """
    return scale_fill_dma_continuous(palette=palette, na_value=na_value, guide=guide, **kwargs)


# =============================================================================
# Diverging Color Scales
# =============================================================================

class scale_color_dma_diverging(ScaleContinuous):
    """Diverging color scale using DMA diverging palettes."""
    
    def __init__(
        self,
        palette: str = "blue_orange",
        na_value: str = "#6E89A0",
        guide: str = "colorbar",
        **kwargs
    ):
        palettes = {
            "blue_orange": DMA_DIVERGING_BLUE_ORANGE,
            "teal_red": DMA_DIVERGING_TEAL_RED,
            "green_warm": DMA_DIVERGING_GREEN_PURPLE,
        }
        colors = palettes.get(palette, DMA_DIVERGING_BLUE_ORANGE)
        
        from matplotlib.colors import LinearSegmentedColormap
        cmap = LinearSegmentedColormap.from_list(f"dma_{palette}", colors)
        
        super().__init__(
            palette=cmap,
            na_value=na_value,
            guide=guide,
            **kwargs
        )


class scale_fill_dma_diverging(ScaleContinuous):
    """Diverging fill scale using DMA diverging palettes."""
    
    def __init__(
        self,
        palette: str = "blue_orange",
        na_value: str = "#6E89A0",
        guide: str = "colorbar",
        **kwargs
    ):
        palettes = {
            "blue_orange": DMA_DIVERGING_BLUE_ORANGE,
            "teal_red": DMA_DIVERGING_TEAL_RED,
            "green_warm": DMA_DIVERGING_GREEN_PURPLE,
        }
        colors = palettes.get(palette, DMA_DIVERGING_BLUE_ORANGE)
        
        from matplotlib.colors import LinearSegmentedColormap
        cmap = LinearSegmentedColormap.from_list(f"dma_{palette}", colors)
        
        super().__init__(
            palette=cmap,
            na_value=na_value,
            guide=guide,
            **kwargs
        )


def scale_color_dma_d(
    palette: str = "blue_orange",
    na_value: str = "#6E89A0",
    guide: str = "colorbar",
    **kwargs
):
    """
    DMA diverging color scale.
    
    Parameters
    ----------
    palette : str
        Palette name. Options: 'blue_orange', 'teal_red', 'green_warm'
    na_value : str
        Color for NA/missing values
    guide : str
        Guide type ('colorbar' or 'legend')
    **kwargs : 
        Additional arguments passed to the scale
    
    Returns
    -------
    ScaleContinuous
        A plotnine diverging color scale
    
    Examples
    --------
    >>> from plotnine import ggplot, aes, geom_tile
    >>> from dma_palette import scale_color_dma_d
    >>> (ggplot(data, aes(x='x', y='y', fill='score'))
    ...  + geom_tile()
    ...  + scale_fill_dma_d(palette='teal_red'))
    """
    return scale_color_dma_diverging(palette=palette, na_value=na_value, guide=guide, **kwargs)


def scale_fill_dma_d(
    palette: str = "blue_orange",
    na_value: str = "#6E89A0",
    guide: str = "colorbar",
    **kwargs
):
    """
    DMA diverging fill scale.
    
    Parameters
    ----------
    palette : str
        Palette name. Options: 'blue_orange', 'teal_red', 'green_warm'
    na_value : str
        Color for NA/missing values
    guide : str
        Guide type ('colorbar' or 'legend')
    **kwargs : 
        Additional arguments passed to the scale
    
    Returns
    -------
    ScaleContinuous
        A plotnine diverging fill scale
    """
    return scale_fill_dma_diverging(palette=palette, na_value=na_value, guide=guide, **kwargs)


# =============================================================================
# Brewer-compatible 9-color scales
# =============================================================================

def scale_color_dma_brewer(palette: str = "Blues", **kwargs):
    """
    DMA color scale compatible with RColorBrewer palette names.
    
    Parameters
    ----------
    palette : str
        Brewer palette name. Options: 'Blues', 'Teals', 'Turquoises', 'Greens',
        'Reds', 'Oranges', 'Grays', 'BuOr', 'TealRed', 'GreenWarm'
    **kwargs : 
        Additional arguments passed to scale_color_manual
    
    Returns
    -------
    ScaleDiscrete
        A plotnine discrete color scale with 9 colors
    """
    palettes = {
        "Blues": DMA_BLUES_9,
        "Teals": DMA_TEALS_9,
        "Turquoises": DMA_TURQUOISES_9,
        "Greens": DMA_GREENS_9,
        "Reds": DMA_REDS_9,
        "Oranges": DMA_ORANGES_9,
        "Grays": DMA_GRAYS_9,
        "BuOr": DMA_DIVERGING_BLUE_ORANGE[:9],
        "TealRed": DMA_DIVERGING_TEAL_RED[:9],
        "GreenWarm": DMA_DIVERGING_GREEN_PURPLE[:9],
    }
    colors = palettes.get(palette, DMA_BLUES_9)
    return scale_color_manual(values=colors, **kwargs)


def scale_fill_dma_brewer(palette: str = "Blues", **kwargs):
    """
    DMA fill scale compatible with RColorBrewer palette names.
    
    Parameters
    ----------
    palette : str
        Brewer palette name. Options: 'Blues', 'Teals', 'Turquoises', 'Greens',
        'Reds', 'Oranges', 'Grays', 'BuOr', 'TealRed', 'GreenWarm'
    **kwargs : 
        Additional arguments passed to scale_fill_manual
    
    Returns
    -------
    ScaleDiscrete
        A plotnine discrete fill scale with 9 colors
    """
    palettes = {
        "Blues": DMA_BLUES_9,
        "Teals": DMA_TEALS_9,
        "Turquoises": DMA_TURQUOISES_9,
        "Greens": DMA_GREENS_9,
        "Reds": DMA_REDS_9,
        "Oranges": DMA_ORANGES_9,
        "Grays": DMA_GRAYS_9,
        "BuOr": DMA_DIVERGING_BLUE_ORANGE[:9],
        "TealRed": DMA_DIVERGING_TEAL_RED[:9],
        "GreenWarm": DMA_DIVERGING_GREEN_PURPLE[:9],
    }
    colors = palettes.get(palette, DMA_BLUES_9)
    return scale_fill_manual(values=colors, **kwargs)


# =============================================================================
# Theme Elements
# =============================================================================

def theme_dma(
    base_size: int = 11,
    base_family: str = "DejaVu Sans",
    base_color: str = "#1E282D",
    background_color: str = "#F8FAFC",
    grid_color: str = "#C8D6E3",
    axis_color: str = "#6E89A0",
) -> "theme":
    """
    Create a complete DMA theme for plotnine.
    
    Parameters
    ----------
    base_size : int
        Base font size
    base_family : str
        Base font family
    base_color : str
        Base text color
    background_color : str
        Plot background color
    grid_color : str
        Grid line color
    axis_color : str
        Axis line color
    
    Returns
    -------
    theme
        A plotnine theme object
    
    Examples
    --------
    >>> from plotnine import ggplot, aes, geom_point
    >>> from dma_palette import theme_dma
    >>> (ggplot(data, aes(x='x', y='y'))
    ...  + geom_point()
    ...  + theme_dma())
    """
    from plotnine import theme, element_text, element_rect, element_line, element_blank, margin
    
    return theme(
        # Base
        text=element_text(size=base_size, family=base_family, color=base_color),
        title=element_text(size=base_size * 1.2, family=base_family, color=base_color, weight='bold'),
        
        # Background
        plot_background=element_rect(fill=background_color, color=background_color),
        panel_background=element_rect(fill=background_color, color=background_color),
        panel_border=element_rect(fill='none', color=axis_color, size=1),
        
        # Grid
        panel_grid_major=element_line(color=grid_color, size=0.5),
        panel_grid_minor=element_line(color=grid_color, size=0.25, linetype='dotted'),
        panel_grid_major_x=element_line(color=grid_color, size=0.5),
        panel_grid_major_y=element_line(color=grid_color, size=0.5),
        panel_grid_minor_x=element_blank(),
        panel_grid_minor_y=element_blank(),
        
        # Axis
        axis_line=element_line(color=axis_color, size=0.75),
        axis_line_x=element_line(color=axis_color, size=0.75),
        axis_line_y=element_line(color=axis_color, size=0.75),
        axis_text=element_text(size=base_size * 0.9, color=base_color),
        axis_text_x=element_text(size=base_size * 0.9, color=base_color, margin=margin(t=4)),
        axis_text_y=element_text(size=base_size * 0.9, color=base_color, margin=margin(r=4)),
        axis_ticks=element_line(color=axis_color, size=0.5),
        axis_ticks_length=4,
        axis_title=element_text(size=base_size, color=base_color, weight='bold'),
        axis_title_x=element_text(margin=margin(t=8)),
        axis_title_y=element_text(margin=margin(r=8), angle=90),
        
        # Legend
        legend_background=element_rect(fill=background_color, color='none'),
        legend_box_background=element_rect(fill=background_color, color='none'),
        legend_key=element_rect(fill=background_color, color='none'),
        legend_key_size=16,
        legend_text=element_text(size=base_size * 0.9, color=base_color),
        legend_title=element_text(size=base_size, color=base_color, weight='bold'),
        legend_margin=margin(4, 4, 4, 4),
        legend_box_margin=margin(0, 0, 0, 0),
        legend_position='right',
        legend_direction='vertical',
        legend_box='vertical',
        
        # Strips (facets)
        strip_background=element_rect(fill="#E0E8EF", color=axis_color, size=1),
        strip_text=element_text(size=base_size * 0.9, color=base_color, weight='bold'),
        strip_text_x=element_text(margin=margin(4, 4, 4, 4)),
        strip_text_y=element_text(margin=margin(4, 4, 4, 4), angle=-90),
        
        # Plot margins
        plot_margin=margin(12, 12, 12, 12),
        plot_title=element_text(size=base_size * 1.4, weight='bold', margin=margin(b=8)),
        plot_subtitle=element_text(size=base_size * 1.1, color="#485C6E", margin=margin(b=8)),
        plot_caption=element_text(size=base_size * 0.8, color="#6E89A0", margin=margin(t=8)),
        
        # Facets
        panel_spacing=8,
        panel_spacing_x=8,
        panel_spacing_y=8,
        
        # Complete
        complete=True
    )


def theme_dma_dark(
    base_size: int = 11,
    base_family: str = "DejaVu Sans",
    base_color: str = "#E0E8EF",
    background_color: str = "#0A0F14",
    grid_color: str = "#2D4058",
    axis_color: str = "#6E89A0",
) -> "theme":
    """
    Create a dark DMA theme for plotnine.
    """
    from plotnine import theme, element_text, element_rect, element_line, element_blank, margin
    
    return theme(
        text=element_text(size=base_size, family=base_family, color=base_color),
        title=element_text(size=base_size * 1.2, family=base_family, color=base_color, weight='bold'),
        
        plot_background=element_rect(fill=background_color, color=background_color),
        panel_background=element_rect(fill=background_color, color=background_color),
        panel_border=element_rect(fill='none', color=axis_color, size=1),
        
        panel_grid_major=element_line(color=grid_color, size=0.5),
        panel_grid_minor=element_line(color=grid_color, size=0.25, linetype='dotted'),
        panel_grid_major_x=element_line(color=grid_color, size=0.5),
        panel_grid_major_y=element_line(color=grid_color, size=0.5),
        panel_grid_minor_x=element_blank(),
        panel_grid_minor_y=element_blank(),
        
        axis_line=element_line(color=axis_color, size=0.75),
        axis_line_x=element_line(color=axis_color, size=0.75),
        axis_line_y=element_line(color=axis_color, size=0.75),
        axis_text=element_text(size=base_size * 0.9, color=base_color),
        axis_text_x=element_text(size=base_size * 0.9, color=base_color, margin=margin(t=4)),
        axis_text_y=element_text(size=base_size * 0.9, color=base_color, margin=margin(r=4)),
        axis_ticks=element_line(color=axis_color, size=0.5),
        axis_ticks_length=4,
        axis_title=element_text(size=base_size, color=base_color, weight='bold'),
        axis_title_x=element_text(margin=margin(t=8)),
        axis_title_y=element_text(margin=margin(r=8), angle=90),
        
        legend_background=element_rect(fill=background_color, color='none'),
        legend_box_background=element_rect(fill=background_color, color='none'),
        legend_key=element_rect(fill=background_color, color='none'),
        legend_key_size=16,
        legend_text=element_text(size=base_size * 0.9, color=base_color),
        legend_title=element_text(size=base_size, color=base_color, weight='bold'),
        legend_margin=margin(4, 4, 4, 4),
        legend_box_margin=margin(0, 0, 0, 0),
        legend_position='right',
        legend_direction='vertical',
        legend_box='vertical',
        
        strip_background=element_rect(fill="#101820", color=axis_color, size=1),
        strip_text=element_text(size=base_size * 0.9, color=base_color, weight='bold'),
        strip_text_x=element_text(margin=margin(4, 4, 4, 4)),
        strip_text_y=element_text(margin=margin(4, 4, 4, 4), angle=-90),
        
        plot_margin=margin(12, 12, 12, 12),
        plot_title=element_text(size=base_size * 1.4, weight='bold', margin=margin(b=8)),
        plot_subtitle=element_text(size=base_size * 1.1, color="#93ABC3", margin=margin(b=8)),
        plot_caption=element_text(size=base_size * 0.8, color="#6E89A0", margin=margin(t=8)),
        
        panel_spacing=8,
        panel_spacing_x=8,
        panel_spacing_y=8,
        
        complete=True
    )


# =============================================================================
# Register with plotnine (optional)
# =============================================================================

# Allow using as: + scale_color_dma(palette='bold')
# The functions are already compatible with plotnine's scale interface

__all__ = [
    # Discrete
    "scale_color_dma",
    "scale_fill_dma",
    # Continuous (sequential)
    "scale_color_dma_c",
    "scale_fill_dma_c",
    # Diverging
    "scale_color_dma_d",
    "scale_fill_dma_d",
    # Brewer-compatible
    "scale_color_dma_brewer",
    "scale_fill_dma_brewer",
    # Themes
    "theme_dma",
    "theme_dma_dark",
]