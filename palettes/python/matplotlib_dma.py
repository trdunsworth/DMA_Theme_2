"""
DMA Theme - Matplotlib Integration
===================================

Matplotlib colormaps, cyclers, and style sheets.

Author: Dunsworth-Mann Analytics LLC
https://dunsworth-mann.com
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from cycler import cycler

from .dma_palette import (
    DMA_SEQUENTIAL_BLUE,
    DMA_SEQUENTIAL_TEAL,
    DMA_SEQUENTIAL_TURQUOISE,
    DMA_SEQUENTIAL_GREEN,
    DMA_SEQUENTIAL_GRAY_LIGHT,
    DMA_SEQUENTIAL_GRAY_DARK,
    DMA_DIVERGING_BLUE_ORANGE,
    DMA_DIVERGING_TEAL_RED,
    DMA_DIVERGING_GREEN_PURPLE,
    DMA_QUALITATIVE_BOLD,
    DMA_QUALITATIVE_LIGHT,
    DMA_QUALITATIVE_DARK,
    DMA_QUALITATIVE_SEMANTIC,
    DMA_BLUES_9,
    DMA_TEALS_9,
    DMA_TURQUOISES_9,
    DMA_GREENS_9,
    DMA_REDS_9,
    DMA_ORANGES_9,
    DMA_GRAYS_9,
)


# =============================================================================
# Colormap Registration
# =============================================================================

def _register_cmap(name: str, colors: list, n_colors: int = 256) -> LinearSegmentedColormap:
    """Register a colormap with matplotlib."""
    cmap = LinearSegmentedColormap.from_list(f"dma_{name}", colors, N=n_colors)
    if name not in mpl.colormaps:
        mpl.colormaps.register(cmap, name=name)
    rev_name = f"{name}_r"
    if rev_name not in mpl.colormaps:
        mpl.colormaps.register(cmap.reversed(), name=rev_name)
    return cmap


def _register_listed_cmap(name: str, colors: list) -> ListedColormap:
    """Register a listed colormap with matplotlib."""
    cmap = ListedColormap(colors, name=f"dma_{name}")
    if name not in mpl.colormaps:
        mpl.colormaps.register(cmap, name=name)
    return cmap


# Register all colormaps
DMA_CMAPS = {}

# Sequential
DMA_CMAPS['blue'] = _register_cmap('blue', DMA_SEQUENTIAL_BLUE)
DMA_CMAPS['teal'] = _register_cmap('teal', DMA_SEQUENTIAL_TEAL)
DMA_CMAPS['turquoise'] = _register_cmap('turquoise', DMA_SEQUENTIAL_TURQUOISE)
DMA_CMAPS['green'] = _register_cmap('green', DMA_SEQUENTIAL_GREEN)
DMA_CMAPS['gray_light'] = _register_cmap('gray_light', DMA_SEQUENTIAL_GRAY_LIGHT)
DMA_CMAPS['gray_dark'] = _register_cmap('gray_dark', DMA_SEQUENTIAL_GRAY_DARK)

# Diverging
DMA_CMAPS['blue_orange'] = _register_cmap('blue_orange', DMA_DIVERGING_BLUE_ORANGE)
DMA_CMAPS['teal_red'] = _register_cmap('teal_red', DMA_DIVERGING_TEAL_RED)
DMA_CMAPS['green_warm'] = _register_cmap('green_warm', DMA_DIVERGING_GREEN_PURPLE)

# Qualitative (listed)
DMA_CMAPS['bold'] = _register_listed_cmap('bold', DMA_QUALITATIVE_BOLD)
DMA_CMAPS['light'] = _register_listed_cmap('light', DMA_QUALITATIVE_LIGHT)
DMA_CMAPS['dark'] = _register_listed_cmap('dark', DMA_QUALITATIVE_DARK)
DMA_CMAPS['semantic'] = _register_listed_cmap('semantic', DMA_QUALITATIVE_SEMANTIC)

# Brewer-style (9 colors)
DMA_CMAPS['Blues'] = _register_listed_cmap('Blues', DMA_BLUES_9)
DMA_CMAPS['Teals'] = _register_listed_cmap('Teals', DMA_TEALS_9)
DMA_CMAPS['Turquoises'] = _register_listed_cmap('Turquoises', DMA_TURQUOISES_9)
DMA_CMAPS['Greens'] = _register_listed_cmap('Greens', DMA_GREENS_9)
DMA_CMAPS['Reds'] = _register_listed_cmap('Reds', DMA_REDS_9)
DMA_CMAPS['Oranges'] = _register_listed_cmap('Oranges', DMA_ORANGES_9)
DMA_CMAPS['Grays'] = _register_listed_cmap('Grays', DMA_GRAYS_9)
DMA_CMAPS['BuOr'] = _register_listed_cmap('BuOr', DMA_DIVERGING_BLUE_ORANGE[:9])
DMA_CMAPS['TealRed'] = _register_listed_cmap('TealRed', DMA_DIVERGING_TEAL_RED[:9])
DMA_CMAPS['GreenWarm'] = _register_listed_cmap('GreenWarm', DMA_DIVERGING_GREEN_PURPLE[:9])


def get_cmap(name: str):
    """Get a registered colormap by name."""
    return mpl.colormaps.get_cmap(f"dma_{name}")


def list_cmaps() -> list:
    """List all registered DMA colormaps."""
    return [name for name in mpl.colormaps if name.startswith('dma_')]


# =============================================================================
# Color Cyclers
# =============================================================================

def get_cycler(palette: str = "bold"):
    """Get a cycler for the given palette."""
    palettes = {
        "bold": DMA_QUALITATIVE_BOLD,
        "light": DMA_QUALITATIVE_LIGHT,
        "dark": DMA_QUALITATIVE_DARK,
        "semantic": DMA_QUALITATIVE_SEMANTIC,
        "blue": DMA_SEQUENTIAL_BLUE,
        "teal": DMA_SEQUENTIAL_TEAL,
        "turquoise": DMA_SEQUENTIAL_TURQUOISE,
        "green": DMA_SEQUENTIAL_GREEN,
    }
    colors = palettes.get(palette, DMA_QUALITATIVE_BOLD)
    return cycler(color=colors)


def set_default_cycler(palette: str = "bold") -> None:
    """Set the default matplotlib color cycler."""
    mpl.rcParams['axes.prop_cycle'] = get_cycler(palette)


# =============================================================================
# Style Sheets
# =============================================================================

DMA_STYLE_LIGHT = {
    # Figure
    'figure.facecolor': '#F8FAFC',
    'figure.edgecolor': '#F8FAFC',
    'figure.titlesize': 14,
    'figure.titleweight': 'bold',
    
    # Axes
    'axes.facecolor': '#F8FAFC',
    'axes.edgecolor': '#6E89A0',
    'axes.linewidth': 1.0,
    'axes.grid': True,
    'axes.grid.axis': 'both',
    'axes.grid.which': 'major',
    'axes.axisbelow': True,
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
    'axes.titlecolor': '#1E282D',
    'axes.labelsize': 11,
    'axes.labelweight': 'bold',
    'axes.labelcolor': '#1E282D',
    'axes.edgecolor': '#6E89A0',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.spines.left': True,
    'axes.spines.bottom': True,
    
    # Grid
    'grid.color': '#C8D6E3',
    'grid.linewidth': 0.5,
    'grid.linestyle': '-',
    'grid.alpha': 1.0,
    
    # Ticks
    'xtick.color': '#1E282D',
    'ytick.color': '#1E282D',
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    'xtick.major.size': 4,
    'ytick.major.size': 4,
    'xtick.minor.size': 2,
    'ytick.minor.size': 2,
    'xtick.major.width': 0.75,
    'ytick.major.width': 0.75,
    'xtick.minor.width': 0.5,
    'ytick.minor.width': 0.5,
    
    # Lines
    'lines.linewidth': 2.0,
    'lines.markersize': 6.0,
    'lines.markeredgewidth': 0.0,
    
    # Patch
    'patch.edgecolor': '#1E282D',
    'patch.linewidth': 0.5,
    'patch.force_edgecolor': False,
    
    # Text
    'text.color': '#1E282D',
    'font.size': 11,
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica', 'sans-serif'],
    
    # Legend
    'legend.frameon': True,
    'legend.framealpha': 0.95,
    'legend.facecolor': '#FFFFFF',
    'legend.edgecolor': '#C8D6E3',
    'legend.fancybox': True,
    'legend.fontsize': 10,
    'legend.title_fontsize': 11,
    'legend.borderpad': 0.5,
    'legend.labelspacing': 0.5,
    'legend.handlelength': 2.0,
    'legend.handleheight': 0.7,
    'legend.handletextpad': 0.8,
    'legend.borderaxespad': 0.5,
    'legend.columnspacing': 2.0,
    
    # Color cycle
    'axes.prop_cycle': get_cycler('bold'),
    
    # Image
    'image.cmap': 'dma_blue',
    'image.aspect': 'auto',
    'image.interpolation': 'antialiased',
    
    # Contour
    'contour.negative_linestyle': 'dashed',
    'contour.corner_mask': True,
    
    # Errorbar
    'errorbar.capsize': 3.0,
    
    # Hist
    'hist.bins': 'auto',
    
    # Scatter
    'scatter.edgecolors': 'face',
    
    # Savefig
    'savefig.facecolor': '#F8FAFC',
    'savefig.edgecolor': '#F8FAFC',
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
    'savefig.transparent': False,
}

DMA_STYLE_DARK = {
    # Figure
    'figure.facecolor': '#0A0F14',
    'figure.edgecolor': '#0A0F14',
    'figure.titlesize': 14,
    'figure.titleweight': 'bold',
    
    # Axes
    'axes.facecolor': '#0A0F14',
    'axes.edgecolor': '#6E89A0',
    'axes.linewidth': 1.0,
    'axes.grid': True,
    'axes.grid.axis': 'both',
    'axes.grid.which': 'major',
    'axes.axisbelow': True,
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
    'axes.titlecolor': '#E0E8EF',
    'axes.labelsize': 11,
    'axes.labelweight': 'bold',
    'axes.labelcolor': '#E0E8EF',
    'axes.edgecolor': '#6E89A0',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.spines.left': True,
    'axes.spines.bottom': True,
    
    # Grid
    'grid.color': '#2D4058',
    'grid.linewidth': 0.5,
    'grid.linestyle': '-',
    'grid.alpha': 1.0,
    
    # Ticks
    'xtick.color': '#E0E8EF',
    'ytick.color': '#E0E8EF',
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    'xtick.major.size': 4,
    'ytick.major.size': 4,
    'xtick.minor.size': 2,
    'ytick.minor.size': 2,
    'xtick.major.width': 0.75,
    'ytick.major.width': 0.75,
    'xtick.minor.width': 0.5,
    'ytick.minor.width': 0.5,
    
    # Lines
    'lines.linewidth': 2.0,
    'lines.markersize': 6.0,
    'lines.markeredgewidth': 0.0,
    
    # Patch
    'patch.edgecolor': '#E0E8EF',
    'patch.linewidth': 0.5,
    'patch.force_edgecolor': False,
    
    # Text
    'text.color': '#E0E8EF',
    'font.size': 11,
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Helvetica', 'sans-serif'],
    
    # Legend
    'legend.frameon': True,
    'legend.framealpha': 0.95,
    'legend.facecolor': '#101820',
    'legend.edgecolor': '#2D4058',
    'legend.fancybox': True,
    'legend.fontsize': 10,
    'legend.title_fontsize': 11,
    'legend.borderpad': 0.5,
    'legend.labelspacing': 0.5,
    'legend.handlelength': 2.0,
    'legend.handleheight': 0.7,
    'legend.handletextpad': 0.8,
    'legend.borderaxespad': 0.5,
    'legend.columnspacing': 2.0,
    
    # Color cycle
    'axes.prop_cycle': get_cycler('dark'),
    
    # Image
    'image.cmap': 'dma_blue',
    'image.aspect': 'auto',
    'image.interpolation': 'antialiased',
    
    # Contour
    'contour.negative_linestyle': 'dashed',
    'contour.corner_mask': True,
    
    # Errorbar
    'errorbar.capsize': 3.0,
    
    # Hist
    'hist.bins': 'auto',
    
    # Scatter
    'scatter.edgecolors': 'face',
    
    # Savefig
    'savefig.facecolor': '#0A0F14',
    'savefig.edgecolor': '#0A0F14',
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
    'savefig.transparent': False,
}


def apply_style(theme: str = "light") -> None:
    """Apply DMA style to matplotlib."""
    if theme == "dark":
        mpl.rcParams.update(DMA_STYLE_DARK)
    else:
        mpl.rcParams.update(DMA_STYLE_LIGHT)


def style_context(theme: str = "light"):
    """Context manager for temporary style application."""
    return mpl.rc_context(DMA_STYLE_DARK if theme == "dark" else DMA_STYLE_LIGHT)


# =============================================================================
# Demo Functions
# =============================================================================

def demo_colormaps() -> None:
    """Display all registered colormaps."""
    import numpy as np
    
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    gradient = np.vstack([gradient] * 10)
    
    sequential = ['blue', 'teal', 'turquoise', 'green', 'gray_light', 'gray_dark']
    diverging = ['blue_orange', 'teal_red', 'green_warm']
    qualitative = ['bold', 'light', 'dark', 'semantic']
    brewer = ['Blues', 'Teals', 'Turquoises', 'Greens', 'Reds', 'Oranges', 'Grays', 'BuOr', 'TealRed', 'GreenWarm']
    
    all_cmaps = sequential + diverging + qualitative + brewer
    n = len(all_cmaps)
    
    fig, axes = plt.subplots(n, 1, figsize=(10, 0.5 * n))
    fig.suptitle("DMA Theme Colormaps", fontsize=14, fontweight='bold', color='#1E282D')
    
    for ax, name in zip(axes, all_cmaps):
        cmap = get_cmap(name)
        ax.imshow(gradient, aspect='auto', cmap=cmap)
        ax.set_yticks([])
        ax.set_xticks([])
        ax.set_ylabel(name, rotation=0, ha='right', va='center', fontsize=10)
        for spine in ax.spines.values():
            spine.set_visible(False)
    
    plt.tight_layout()
    plt.show()


def demo_color_cycle(palette: str = "bold", n_lines: int = 10) -> None:
    """Demo the color cycle with sample lines."""
    import numpy as np
    
    with style_context("light"):
        cycler_obj = get_cycler(palette)
        colors = [c['color'] for c in cycler_obj()][:n_lines]
        
        x = np.linspace(0, 10, 100)
        fig, ax = plt.subplots(figsize=(10, 6))
        
        for i, color in enumerate(colors):
            y = np.sin(x + i * 0.5) * (1 + i * 0.1)
            ax.plot(x, y, color=color, label=f'Line {i+1}', linewidth=2)
        
        ax.set_title(f"DMA Color Cycle: {palette}", fontweight='bold')
        ax.legend(ncol=2, fontsize=9)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        plt.tight_layout()
        plt.show()


# =============================================================================
# Style sheet files (for mpl.style.use)
# =============================================================================

def write_style_sheets(output_dir: str = ".") -> None:
    """Write .mplstyle files for use with matplotlib.style.use()."""
    import os
    
    os.makedirs(output_dir, exist_ok=True)
    
    # Light style
    with open(os.path.join(output_dir, 'dma-light.mplstyle'), 'w') as f:
        f.write("# DMA Theme Light Style\n")
        f.write("# Use with: plt.style.use('dma-light')\n\n")
        for key, value in DMA_STYLE_LIGHT.items():
            if isinstance(value, str) and ('#' in value or value.startswith('dma_')):
                f.write(f"{key}: {value}\n")
            elif isinstance(value, (list, tuple)):
                f.write(f"{key}: {', '.join(str(v) for v in value)}\n")
            elif isinstance(value, cycler):
                colors = [c['color'] for c in value()]
                f.write(f"{key}: cycler('color', {colors})\n")
            else:
                f.write(f"{key}: {value}\n")
    
    # Dark style
    with open(os.path.join(output_dir, 'dma-dark.mplstyle'), 'w') as f:
        f.write("# DMA Theme Dark Style\n")
        f.write("# Use with: plt.style.use('dma-dark')\n\n")
        for key, value in DMA_STYLE_DARK.items():
            if isinstance(value, str) and ('#' in value or value.startswith('dma_')):
                f.write(f"{key}: {value}\n")
            elif isinstance(value, (list, tuple)):
                f.write(f"{key}: {', '.join(str(v) for v in value)}\n")
            elif isinstance(value, cycler):
                colors = [c['color'] for c in value()]
                f.write(f"{key}: cycler('color', {colors})\n")
            else:
                f.write(f"{key}: {value}\n")


__all__ = [
    "DMA_CMAPS",
    "get_cmap",
    "list_cmaps",
    "get_cycler",
    "set_default_cycler",
    "apply_style",
    "style_context",
    "DMA_STYLE_LIGHT",
    "DMA_STYLE_DARK",
    "demo_colormaps",
    "demo_color_cycle",
    "write_style_sheets",
]