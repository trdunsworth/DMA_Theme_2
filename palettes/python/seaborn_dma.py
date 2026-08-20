"""
DMA Theme - Seaborn Integration
================================

Seaborn palette registration and theme settings.

Author: Dunsworth-Mann Analytics LLC
https://dunsworth-mann.com
"""

import seaborn as sns
import matplotlib as mpl
from matplotlib.colors import ListedColormap

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
# Palette Registration
# =============================================================================

def register_palettes() -> None:
    """Register all DMA palettes with seaborn."""
    
    # Qualitative palettes
    sns.palettes.SEABORN_PALETTES['dma_bold'] = DMA_QUALITATIVE_BOLD
    sns.palettes.SEABORN_PALETTES['dma_light'] = DMA_QUALITATIVE_LIGHT
    sns.palettes.SEABORN_PALETTES['dma_dark'] = DMA_QUALITATIVE_DARK
    sns.palettes.SEABORN_PALETTES['dma_semantic'] = DMA_QUALITATIVE_SEMANTIC
    
    # Sequential palettes
    sns.palettes.SEABORN_PALETTES['dma_blue'] = DMA_SEQUENTIAL_BLUE
    sns.palettes.SEABORN_PALETTES['dma_teal'] = DMA_SEQUENTIAL_TEAL
    sns.palettes.SEABORN_PALETTES['dma_turquoise'] = DMA_SEQUENTIAL_TURQUOISE
    sns.palettes.SEABORN_PALETTES['dma_green'] = DMA_SEQUENTIAL_GREEN
    
    # Diverging palettes
    sns.palettes.SEABORN_PALETTES['dma_blue_orange'] = DMA_DIVERGING_BLUE_ORANGE
    sns.palettes.SEABORN_PALETTES['dma_teal_red'] = DMA_DIVERGING_TEAL_RED
    sns.palettes.SEABORN_PALETTES['dma_green_warm'] = DMA_DIVERGING_GREEN_PURPLE
    
    # Brewer-style (9 colors)
    sns.palettes.SEABORN_PALETTES['dma_Blues'] = DMA_BLUES_9
    sns.palettes.SEABORN_PALETTES['dma_Teals'] = DMA_TEALS_9
    sns.palettes.SEABORN_PALETTES['dma_Turquoises'] = DMA_TURQUOISES_9
    sns.palettes.SEABORN_PALETTES['dma_Greens'] = DMA_GREENS_9
    sns.palettes.SEABORN_PALETTES['dma_Reds'] = DMA_REDS_9
    sns.palettes.SEABORN_PALETTES['dma_Oranges'] = DMA_ORANGES_9
    sns.palettes.SEABORN_PALETTES['dma_Grays'] = DMA_GRAYS_9
    sns.palettes.SEABORN_PALETTES['dma_BuOr'] = DMA_DIVERGING_BLUE_ORANGE[:9]
    sns.palettes.SEABORN_PALETTES['dma_TealRed'] = DMA_DIVERGING_TEAL_RED[:9]
    sns.palettes.SEABORN_PALETTES['dma_GreenWarm'] = DMA_DIVERGING_GREEN_PURPLE[:9]


def get_palette(name: str, n_colors: int = None, desat: float = None) -> list:
    """Get a seaborn color palette by name."""
    # Ensure palettes are registered
    if name not in sns.palettes.SEABORN_PALETTES:
        register_palettes()
    
    return sns.color_palette(name, n_colors=n_colors, desat=desat)


def set_palette(name: str = "dma_bold", n_colors: int = None, desat: float = None) -> None:
    """Set the default seaborn color palette."""
    palette = get_palette(name, n_colors=n_colors, desat=desat)
    sns.set_palette(palette)


# =============================================================================
# Colormap Registration
# =============================================================================

def register_cmaps() -> dict:
    """Register DMA colormaps for seaborn heatmap/clustermap."""
    from matplotlib.colors import LinearSegmentedColormap
    
    cmaps = {}
    
    # Sequential
    cmaps['dma_blue'] = LinearSegmentedColormap.from_list('dma_blue', DMA_SEQUENTIAL_BLUE)
    cmaps['dma_teal'] = LinearSegmentedColormap.from_list('dma_teal', DMA_SEQUENTIAL_TEAL)
    cmaps['dma_turquoise'] = LinearSegmentedColormap.from_list('dma_turquoise', DMA_SEQUENTIAL_TURQUOISE)
    cmaps['dma_green'] = LinearSegmentedColormap.from_list('dma_green', DMA_SEQUENTIAL_GREEN)
    
    # Diverging
    cmaps['dma_blue_orange'] = LinearSegmentedColormap.from_list('dma_blue_orange', DMA_DIVERGING_BLUE_ORANGE)
    cmaps['dma_teal_red'] = LinearSegmentedColormap.from_list('dma_teal_red', DMA_DIVERGING_TEAL_RED)
    cmaps['dma_green_warm'] = LinearSegmentedColormap.from_list('dma_green_warm', DMA_DIVERGING_GREEN_PURPLE)
    
    # Register with matplotlib
    for name, cmap in cmaps.items():
        if name not in mpl.colormaps:
            mpl.colormaps.register(cmap, name=name)
        if f"{name}_r" not in mpl.colormaps:
            mpl.colormaps.register(cmap.reversed(), name=f"{name}_r")
    
    return cmaps


# =============================================================================
# Seaborn Theme Settings
# =============================================================================

DMA_SEABORN_THEME_LIGHT = {
    # Figure
    'figure.facecolor': '#F8FAFC',
    'figure.edgecolor': '#F8FAFC',
    
    # Axes
    'axes.facecolor': '#F8FAFC',
    'axes.edgecolor': '#6E89A0',
    'axes.linewidth': 1.0,
    'axes.grid': True,
    'axes.axisbelow': True,
    'axes.labelcolor': '#1E282D',
    'axes.titlecolor': '#1E282D',
    
    # Grid
    'grid.color': '#C8D6E3',
    'grid.linewidth': 0.5,
    'grid.linestyle': '-',
    
    # Ticks
    'xtick.color': '#1E282D',
    'ytick.color': '#1E282D',
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    
    # Text
    'text.color': '#1E282D',
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica', 'sans-serif'],
    
    # Legend
    'legend.frameon': True,
    'legend.facecolor': '#FFFFFF',
    'legend.edgecolor': '#C8D6E3',
    
    # Color palette
    'axes.prop_cycle': 'cycler("color", ["#007BDB", "#00B3B3", "#00B33B", "#00B8B8", "#FF9F00", "#FF1A1A", "#00529E", "#007F7F", "#007F2A", "#008A8A"])',
}


DMA_SEABORN_THEME_DARK = {
    # Figure
    'figure.facecolor': '#0A0F14',
    'figure.edgecolor': '#0A0F14',
    
    # Axes
    'axes.facecolor': '#0A0F14',
    'axes.edgecolor': '#6E89A0',
    'axes.linewidth': 1.0,
    'axes.grid': True,
    'axes.axisbelow': True,
    'axes.labelcolor': '#E0E8EF',
    'axes.titlecolor': '#E0E8EF',
    
    # Grid
    'grid.color': '#2D4058',
    'grid.linewidth': 0.5,
    'grid.linestyle': '-',
    
    # Ticks
    'xtick.color': '#E0E8EF',
    'ytick.color': '#E0E8EF',
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    
    # Text
    'text.color': '#E0E8EF',
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica', 'sans-serif'],
    
    # Legend
    'legend.frameon': True,
    'legend.facecolor': '#101820',
    'legend.edgecolor': '#2D4058',
    
    # Color palette
    'axes.prop_cycle': 'cycler("color", ["#1A91E6", "#1ACECE", "#4DD966", "#4DDDDD", "#FF9F00", "#FF1A1A", "#4DA8EE", "#4DE5E5", "#4DD966", "#4DDDDD"])',
}


def set_theme(theme: str = "light", style: str = "whitegrid", **kwargs) -> None:
    """
    Set the DMA seaborn theme.
    
    Parameters
    ----------
    theme : str
        'light' or 'dark'
    style : str
        Seaborn style: 'whitegrid', 'darkgrid', 'white', 'dark', 'ticks'
    **kwargs :
        Additional arguments passed to sns.set_theme()
    """
    # Register palettes and colormaps
    register_palettes()
    register_cmaps()
    
    # Get theme settings
    theme_settings = DMA_SEABORN_THEME_DARK if theme == "dark" else DMA_SEABORN_THEME_LIGHT
    
    # Apply seaborn theme
    sns.set_theme(style=style, rc=theme_settings, **kwargs)
    
    # Set default palette
    set_palette('dma_bold' if theme == "light" else 'dma_dark')


def axes_style(theme: str = "light") -> dict:
    """Return the axes style dictionary for the given theme."""
    return DMA_SEABORN_THEME_DARK if theme == "dark" else DMA_SEABORN_THEME_LIGHT


def plotting_context(context: str = "notebook", font_scale: float = 1.0, rc: dict = None) -> dict:
    """Return plotting context parameters."""
    base_rc = axes_style("light")  # Default to light
    if rc:
        base_rc.update(rc)
    return base_rc


# =============================================================================
# Convenience Functions
# =============================================================================

def color_palette(palette: str = "dma_bold", n_colors: int = None, **kwargs) -> list:
    """Return a color palette as a list of colors."""
    return get_palette(palette, n_colors=n_colors, **kwargs)


def diverging_palette(h_neg: int = 200, h_pos: int = 30, s: int = 75, l: int = 50, 
                      sep: int = 1, n: int = 9, center: str = "light", as_cmap: bool = False):
    """
    Create a diverging palette (seaborn compatible).
    
    Note: This is a wrapper that returns DMA's predefined diverging palettes
    instead of generating them from HSL values.
    """
    # Map common HSL combinations to DMA palettes
    if h_neg >= 180 and h_neg <= 220 and h_pos >= 20 and h_pos <= 40:
        # Blue-Orange
        palette = DMA_DIVERGING_BLUE_ORANGE
    elif h_neg >= 160 and h_neg <= 190 and h_pos >= 0 and h_pos <= 20:
        # Teal-Red
        palette = DMA_DIVERGING_TEAL_RED
    elif h_neg >= 120 and h_neg <= 150 and h_pos >= 20 and h_pos <= 40:
        # Green-Warm
        palette = DMA_DIVERGING_GREEN_PURPLE
    else:
        # Default to blue-orange
        palette = DMA_DIVERGING_BLUE_ORANGE
    
    if n <= len(palette):
        return palette[:n] if not as_cmap else ListedColormap(palette[:n])
    
    # Interpolate if more colors needed
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list('dma_diverging', palette)
    if as_cmap:
        return cmap
    return [cmap(i / (n - 1)) for i in range(n)]


def cubehelix_palette(start: float = 0.5, rot: float = -0.5, gamma: float = 1.0,
                      hue: float = 0.8, light: float = 0.85, dark: float = 0.15,
                      reverse: bool = False, as_cmap: bool = False, n: int = 9):
    """
    Cubehelix palette (seaborn compatible).
    
    Returns DMA sequential palettes instead.
    """
    # Map to closest DMA sequential palette
    if hue >= 0.55 and hue <= 0.65:  # Blue region
        palette = DMA_SEQUENTIAL_BLUE
    elif hue >= 0.45 and hue <= 0.55:  # Teal region
        palette = DMA_SEQUENTIAL_TEAL
    elif hue >= 0.35 and hue <= 0.45:  # Turquoise region
        palette = DMA_SEQUENTIAL_TURQUOISE
    elif hue >= 0.25 and hue <= 0.35:  # Green region
        palette = DMA_SEQUENTIAL_GREEN
    else:
        palette = DMA_SEQUENTIAL_BLUE
    
    if reverse:
        palette = palette[::-1]
    
    if n <= len(palette):
        return palette[:n] if not as_cmap else ListedColormap(palette[:n])
    
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list('dma_cubehelix', palette)
    if as_cmap:
        return cmap
    return [cmap(i / (n - 1)) for i in range(n)]


# =============================================================================
# Demo Functions
# =============================================================================

def demo_palettes() -> None:
    """Display all registered seaborn palettes."""
    import matplotlib.pyplot as plt
    import numpy as np
    
    register_palettes()
    
    palettes = {
        'dma_bold': 'Qualitative Bold',
        'dma_light': 'Qualitative Light',
        'dma_dark': 'Qualitative Dark',
        'dma_semantic': 'Qualitative Semantic',
        'dma_blue': 'Sequential Blue',
        'dma_teal': 'Sequential Teal',
        'dma_turquoise': 'Sequential Turquoise',
        'dma_green': 'Sequential Green',
        'dma_blue_orange': 'Diverging Blue-Orange',
        'dma_teal_red': 'Diverging Teal-Red',
        'dma_green_warm': 'Diverging Green-Warm',
    }
    
    n = len(palettes)
    fig, axes = plt.subplots(n, 1, figsize=(12, 0.6 * n))
    fig.suptitle("DMA Theme Seaborn Palettes", fontsize=14, fontweight='bold')
    
    for ax, (name, title) in zip(axes, palettes.items()):
        colors = get_palette(name)
        n_colors = len(colors)
        x = np.arange(n_colors)
        ax.barh(0, 1, color=colors, edgecolor='white', linewidth=0.5, 
                width=1/n_colors, left=x/n_colors)
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.5, 0.5)
        ax.set_yticks([])
        ax.set_xticks([])
        ax.set_title(title, loc='left', fontsize=11, fontweight='bold')
        for spine in ax.spines.values():
            spine.set_visible(False)
    
    plt.tight_layout()
    plt.show()


def demo_heatmap() -> None:
    """Demo heatmap with DMA diverging colormap."""
    import numpy as np
    import matplotlib.pyplot as plt
    
    register_cmaps()
    
    # Create sample correlation matrix
    np.random.seed(42)
    data = np.random.randn(10, 10)
    corr = np.corrcoef(data)
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    for ax, cmap_name in zip(axes, ['dma_blue_orange', 'dma_teal_red', 'dma_green_warm']):
        im = ax.imshow(corr, cmap=cmap_name, vmin=-1, vmax=1, aspect='auto')
        ax.set_title(f"cmap='{cmap_name}'", fontweight='bold')
        ax.set_xticks([])
        ax.set_yticks([])
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    
    plt.suptitle("DMA Diverging Colormaps for Heatmaps", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()


# Register on import
register_palettes()
register_cmaps()

__all__ = [
    "register_palettes",
    "register_cmaps",
    "get_palette",
    "set_palette",
    "set_theme",
    "axes_style",
    "plotting_context",
    "color_palette",
    "diverging_palette",
    "cubehelix_palette",
    "demo_palettes",
    "demo_heatmap",
    "DMA_SEABORN_THEME_LIGHT",
    "DMA_SEABORN_THEME_DARK",
]