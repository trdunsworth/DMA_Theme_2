"""
DMA Theme - Python Color Palettes
==================================

A semantic color palette for data visualization in Python.
Compatible with matplotlib, seaborn, plotnine, and ggplot2 (via plotnine).

Author: Dunsworth-Mann Analytics LLC
https://dunsworth-mann.com
"""

from typing import Dict, List, Tuple
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from cycler import cycler


# =============================================================================
# Core Color Definitions
# =============================================================================

# Primary Colors
DMA_BLUE = {
    900: "#002B5C",
    800: "#003D7A",
    700: "#00529E",
    600: "#0069C0",
    500: "#007BDB",
    400: "#1A91E6",
    300: "#4DA8EE",
    200: "#8FC3F5",
    100: "#C5DEF9",
    50:  "#E8F4FC",
}

DMA_TEAL = {
    900: "#004D4D",
    800: "#006666",
    700: "#007F7F",
    600: "#009999",
    500: "#00B3B3",
    400: "#1ACCCC",
    300: "#4DE5E5",
    200: "#99F0F0",
    100: "#CCF7F7",
    50:  "#E6FBFB",
}

DMA_TURQUOISE = {
    900: "#005C5C",
    800: "#007373",
    700: "#008A8A",
    600: "#00A1A1",
    500: "#00B8B8",
    400: "#1ACECE",
    300: "#4DDDDD",
    200: "#99EDED",
    100: "#CCF6F6",
    50:  "#E6FBFB",
}

DMA_GREEN = {
    900: "#004D1A",
    800: "#006622",
    700: "#007F2A",
    600: "#009933",
    500: "#00B33B",
    400: "#1ACC4D",
    300: "#4DD966",
    200: "#99E599",
    100: "#CCF0CC",
    50:  "#E6F8E6",
}

# Semantic Colors
DMA_ERROR = {
    900: "#7A0000",
    800: "#9E0000",
    700: "#C40000",
    600: "#E80000",
    500: "#FF1A1A",
    400: "#FF4D4D",
    300: "#FF7A7A",
    200: "#FFA8A8",
    100: "#FFD4D4",
    50:  "#FFEAEA",
}

DMA_WARNING = {
    900: "#7A4A00",
    800: "#9E5E00",
    700: "#C47300",
    600: "#E88800",
    500: "#FF9F00",
    400: "#FFAD33",
    300: "#FFC466",
    200: "#FFDB99",
    100: "#FFF0CC",
    50:  "#FFF8E6",
}

DMA_INFO = {
    900: "#003D7A",
    800: "#00529E",
    700: "#0069C0",
    600: "#007BDB",
    500: "#0091E6",
    400: "#33A8EE",
    300: "#66BFFF",
    200: "#99D4FF",
    100: "#CCE9FF",
    50:  "#E6F4FF",
}

DMA_SUCCESS = {
    900: "#004D1A",
    800: "#006622",
    700: "#007F2A",
    600: "#009933",
    500: "#00B33B",
    400: "#33CC5A",
    300: "#66D97A",
    200: "#99E599",
    100: "#CCF0CC",
    50:  "#E6F8E6",
}

# Neutral Colors
DMA_NEUTRAL_LIGHT = {
    950: "#F0F4F8",
    900: "#E0E8EF",
    800: "#C8D6E3",
    700: "#A8BED1",
    600: "#8AA3BC",
    500: "#708BA0",
    400: "#5A7287",
    300: "#485C6E",
    200: "#384854",
    100: "#2A363E",
    50:  "#1E282D",
}

DMA_NEUTRAL_DARK = {
    950: "#0A0F14",
    900: "#101820",
    800: "#182430",
    700: "#203040",
    600: "#2D4058",
    500: "#3D526E",
    400: "#526D85",
    300: "#6E89A0",
    200: "#93ABC3",
    100: "#B8CDE0",
    50:  "#DCE8F0",
}


# =============================================================================
# Predefined Palettes
# =============================================================================

# Qualitative palettes (for categorical data)
DMA_QUALITATIVE_BOLD = [
    DMA_BLUE[500],      # Blue
    DMA_TEAL[500],      # Teal
    DMA_GREEN[500],     # Green
    DMA_TURQUOISE[500], # Turquoise
    DMA_WARNING[500],   # Warning Orange
    DMA_ERROR[500],     # Error Red
    DMA_BLUE[700],      # Dark Blue
    DMA_TEAL[700],      # Dark Teal
    DMA_GREEN[700],     # Dark Green
    DMA_TURQUOISE[700], # Dark Turquoise
]

DMA_QUALITATIVE_LIGHT = [
    DMA_BLUE[300],
    DMA_TEAL[300],
    DMA_GREEN[300],
    DMA_TURQUOISE[300],
    DMA_WARNING[300],
    DMA_ERROR[300],
    DMA_BLUE[400],
    DMA_TEAL[400],
    DMA_GREEN[400],
    DMA_TURQUOISE[400],
]

DMA_QUALITATIVE_DARK = [
    DMA_BLUE[700],
    DMA_TEAL[700],
    DMA_GREEN[700],
    DMA_TURQUOISE[700],
    DMA_WARNING[700],
    DMA_ERROR[700],
    DMA_BLUE[800],
    DMA_TEAL[800],
    DMA_GREEN[800],
    DMA_TURQUOISE[800],
]

# Semantic qualitative palette
DMA_QUALITATIVE_SEMANTIC = [
    DMA_INFO[500],     # Info
    DMA_SUCCESS[500],  # Success
    DMA_WARNING[500],  # Warning
    DMA_ERROR[500],    # Error
    DMA_BLUE[500],     # Primary
    DMA_TEAL[500],     # Secondary
]

# Sequential palettes (for ordered data)
DMA_SEQUENTIAL_BLUE = [DMA_BLUE[i] for i in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]]
DMA_SEQUENTIAL_TEAL = [DMA_TEAL[i] for i in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]]
DMA_SEQUENTIAL_TURQUOISE = [DMA_TURQUOISE[i] for i in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]]
DMA_SEQUENTIAL_GREEN = [DMA_GREEN[i] for i in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]]
DMA_SEQUENTIAL_GRAY_LIGHT = [DMA_NEUTRAL_LIGHT[i] for i in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]]
DMA_SEQUENTIAL_GRAY_DARK = [DMA_NEUTRAL_DARK[i] for i in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]]

# Diverging palettes (for data with meaningful midpoint)
DMA_DIVERGING_BLUE_ORANGE = [
    DMA_BLUE[900], DMA_BLUE[700], DMA_BLUE[500], DMA_BLUE[300], DMA_BLUE[100],
    DMA_NEUTRAL_LIGHT[50],
    DMA_WARNING[100], DMA_WARNING[300], DMA_WARNING[500], DMA_WARNING[700], DMA_WARNING[900]
]

DMA_DIVERGING_TEAL_RED = [
    DMA_TEAL[900], DMA_TEAL[700], DMA_TEAL[500], DMA_TEAL[300], DMA_TEAL[100],
    DMA_NEUTRAL_LIGHT[50],
    DMA_ERROR[100], DMA_ERROR[300], DMA_ERROR[500], DMA_ERROR[700], DMA_ERROR[900]
]

DMA_DIVERGING_GREEN_PURPLE = [
    DMA_GREEN[900], DMA_GREEN[700], DMA_GREEN[500], DMA_GREEN[300], DMA_GREEN[100],
    DMA_NEUTRAL_LIGHT[50],
    "#7A4A00", "#C47300", "#E88800", "#FF9F00", "#FFAD33"  # Warm variants
]

# Single-hue sequential (9 steps for ggplot2 compatibility)
DMA_BLUES_9 = [DMA_BLUE[i] for i in [50, 100, 200, 300, 400, 500, 600, 700, 800]]
DMA_TEALS_9 = [DMA_TEAL[i] for i in [50, 100, 200, 300, 400, 500, 600, 700, 800]]
DMA_TURQUOISES_9 = [DMA_TURQUOISE[i] for i in [50, 100, 200, 300, 400, 500, 600, 700, 800]]
DMA_GREENS_9 = [DMA_GREEN[i] for i in [50, 100, 200, 300, 400, 500, 600, 700, 800]]
DMA_REDS_9 = [DMA_ERROR[i] for i in [50, 100, 200, 300, 400, 500, 600, 700, 800]]
DMA_ORANGES_9 = [DMA_WARNING[i] for i in [50, 100, 200, 300, 400, 500, 600, 700, 800]]
DMA_GRAYS_9 = [DMA_NEUTRAL_LIGHT[i] for i in [50, 100, 200, 300, 400, 500, 600, 700, 800]]


# =============================================================================
# Matplotlib Colormaps
# =============================================================================

def get_sequential_cmap(name: str = "blue", n_colors: int = 256) -> LinearSegmentedColormap:
    """Get a sequential colormap."""
    palettes = {
        "blue": DMA_SEQUENTIAL_BLUE,
        "teal": DMA_SEQUENTIAL_TEAL,
        "turquoise": DMA_SEQUENTIAL_TURQUOISE,
        "green": DMA_SEQUENTIAL_GREEN,
        "gray_light": DMA_SEQUENTIAL_GRAY_LIGHT,
        "gray_dark": DMA_SEQUENTIAL_GRAY_DARK,
    }
    colors = palettes.get(name, DMA_SEQUENTIAL_BLUE)
    return LinearSegmentedColormap.from_list(f"dma_{name}", colors, N=n_colors)


def get_diverging_cmap(name: str = "blue_orange", n_colors: int = 256) -> LinearSegmentedColormap:
    """Get a diverging colormap."""
    palettes = {
        "blue_orange": DMA_DIVERGING_BLUE_ORANGE,
        "teal_red": DMA_DIVERGING_TEAL_RED,
        "green_warm": DMA_DIVERGING_GREEN_PURPLE,
    }
    colors = palettes.get(name, DMA_DIVERGING_BLUE_ORANGE)
    return LinearSegmentedColormap.from_list(f"dma_{name}", colors, N=n_colors)


def get_qualitative_cmap(name: str = "bold", n_colors: int = None) -> ListedColormap:
    """Get a qualitative colormap."""
    palettes = {
        "bold": DMA_QUALITATIVE_BOLD,
        "light": DMA_QUALITATIVE_LIGHT,
        "dark": DMA_QUALITATIVE_DARK,
        "semantic": DMA_QUALITATIVE_SEMANTIC,
    }
    colors = palettes.get(name, DMA_QUALITATIVE_BOLD)
    if n_colors is None:
        n_colors = len(colors)
    return ListedColormap(colors[:n_colors], name=f"dma_{name}")


# Pre-register colormaps
DMA_CMAPS = {
    # Sequential
    "dma_blue": get_sequential_cmap("blue"),
    "dma_teal": get_sequential_cmap("teal"),
    "dma_turquoise": get_sequential_cmap("turquoise"),
    "dma_green": get_sequential_cmap("green"),
    "dma_gray_light": get_sequential_cmap("gray_light"),
    "dma_gray_dark": get_sequential_cmap("gray_dark"),
    # Diverging
    "dma_blue_orange": get_diverging_cmap("blue_orange"),
    "dma_teal_red": get_diverging_cmap("teal_red"),
    "dma_green_warm": get_diverging_cmap("green_warm"),
    # Qualitative
    "dma_bold": get_qualitative_cmap("bold"),
    "dma_light": get_qualitative_cmap("light"),
    "dma_dark": get_qualitative_cmap("dark"),
    "dma_semantic": get_qualitative_cmap("semantic"),
}


def register_cmaps() -> None:
    """Register all DMA colormaps with matplotlib."""
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    
    for name, cmap in DMA_CMAPS.items():
        if name not in mpl.colormaps:
            mpl.colormaps.register(cmap, name=name)
        # Also register reversed versions
        rev_name = f"{name}_r"
        if rev_name not in mpl.colormaps:
            mpl.colormaps.register(cmap.reversed(), name=rev_name)


# =============================================================================
# Cycler for matplotlib
# =============================================================================

def get_color_cycler(palette: str = "bold") -> cycler:
    """Get a matplotlib cycler for the given palette."""
    palettes = {
        "bold": DMA_QUALITATIVE_BOLD,
        "light": DMA_QUALITATIVE_LIGHT,
        "dark": DMA_QUALITATIVE_DARK,
        "semantic": DMA_QUALITATIVE_SEMANTIC,
        "blue": DMA_SEQUENTIAL_BLUE,
        "teal": DMA_SEQUENTIAL_TEAL,
        "green": DMA_SEQUENTIAL_GREEN,
    }
    colors = palettes.get(palette, DMA_QUALITATIVE_BOLD)
    return cycler(color=colors)


def set_default_cycler(palette: str = "bold") -> None:
    """Set the default matplotlib color cycler."""
    import matplotlib as mpl
    mpl.rcParams['axes.prop_cycle'] = get_color_cycler(palette)


# =============================================================================
# Helper Functions
# =============================================================================

def get_palette(name: str) -> List[str]:
    """Get a palette by name."""
    palettes = {
        "qualitative_bold": DMA_QUALITATIVE_BOLD,
        "qualitative_light": DMA_QUALITATIVE_LIGHT,
        "qualitative_dark": DMA_QUALITATIVE_DARK,
        "qualitative_semantic": DMA_QUALITATIVE_SEMANTIC,
        "sequential_blue": DMA_SEQUENTIAL_BLUE,
        "sequential_teal": DMA_SEQUENTIAL_TEAL,
        "sequential_turquoise": DMA_SEQUENTIAL_TURQUOISE,
        "sequential_green": DMA_SEQUENTIAL_GREEN,
        "sequential_gray_light": DMA_SEQUENTIAL_GRAY_LIGHT,
        "sequential_gray_dark": DMA_SEQUENTIAL_GRAY_DARK,
        "diverging_blue_orange": DMA_DIVERGING_BLUE_ORANGE,
        "diverging_teal_red": DMA_DIVERGING_TEAL_RED,
        "diverging_green_warm": DMA_DIVERGING_GREEN_PURPLE,
        "blues_9": DMA_BLUES_9,
        "teals_9": DMA_TEALS_9,
        "turquoises_9": DMA_TURQUOISES_9,
        "greens_9": DMA_GREENS_9,
        "reds_9": DMA_REDS_9,
        "oranges_9": DMA_ORANGES_9,
        "grays_9": DMA_GRAYS_9,
    }
    return palettes.get(name, [])


def list_palettes() -> Dict[str, int]:
    """List all available palettes with their color counts."""
    return {name: len(get_palette(name)) for name in [
        "qualitative_bold", "qualitative_light", "qualitative_dark", "qualitative_semantic",
        "sequential_blue", "sequential_teal", "sequential_turquoise", "sequential_green",
        "sequential_gray_light", "sequential_gray_dark",
        "diverging_blue_orange", "diverging_teal_red", "diverging_green_warm",
        "blues_9", "teals_9", "turquoises_9", "greens_9", "reds_9", "oranges_9", "grays_9",
    ]}


def demo_palettes() -> None:
    """Display all palettes using matplotlib."""
    import matplotlib.pyplot as plt
    import numpy as np
    
    palettes = {
        "Qualitative Bold": DMA_QUALITATIVE_BOLD,
        "Qualitative Light": DMA_QUALITATIVE_LIGHT,
        "Qualitative Dark": DMA_QUALITATIVE_DARK,
        "Qualitative Semantic": DMA_QUALITATIVE_SEMANTIC,
        "Sequential Blue": DMA_SEQUENTIAL_BLUE,
        "Sequential Teal": DMA_SEQUENTIAL_TEAL,
        "Sequential Turquoise": DMA_SEQUENTIAL_TURQUOISE,
        "Sequential Green": DMA_SEQUENTIAL_GREEN,
        "Sequential Gray (Light)": DMA_SEQUENTIAL_GRAY_LIGHT,
        "Sequential Gray (Dark)": DMA_SEQUENTIAL_GRAY_DARK,
        "Diverging Blue-Orange": DMA_DIVERGING_BLUE_ORANGE,
        "Diverging Teal-Red": DMA_DIVERGING_TEAL_RED,
        "Diverging Green-Warm": DMA_DIVERGING_GREEN_PURPLE,
    }
    
    n = len(palettes)
    fig, axes = plt.subplots(n, 1, figsize=(12, 2 * n))
    fig.suptitle("DMA Theme Color Palettes", fontsize=16, fontweight='bold')
    
    for ax, (name, colors) in zip(axes, palettes.items()):
        n_colors = len(colors)
        x = np.arange(n_colors)
        ax.barh(0, 1, color=colors, edgecolor='white', linewidth=0.5, width=1/n_colors, left=x/n_colors)
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.5, 0.5)
        ax.set_yticks([])
        ax.set_xticks([])
        ax.set_title(name, loc='left', fontsize=12, fontweight='bold')
        for spine in ax.spines.values():
            spine.set_visible(False)
    
    plt.tight_layout()
    plt.show()


# =============================================================================
# Color Conversion Utilities
# =============================================================================

def hex_to_rgb(hex_color: str) -> Tuple[float, float, float]:
    """Convert hex color to RGB tuple (0-1 range)."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))


def hex_to_rgb255(hex_color: str) -> Tuple[int, int, int]:
    """Convert hex color to RGB tuple (0-255 range)."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(r: float, g: float, b: float) -> str:
    """Convert RGB tuple (0-1 range) to hex color."""
    return "#{:02x}{:02x}{:02x}".format(
        int(r * 255), int(g * 255), int(b * 255)
    )


# =============================================================================
# Export all colors as flat dictionary
# =============================================================================

ALL_COLORS = {
    **{f"blue_{k}": v for k, v in DMA_BLUE.items()},
    **{f"teal_{k}": v for k, v in DMA_TEAL.items()},
    **{f"turquoise_{k}": v for k, v in DMA_TURQUOISE.items()},
    **{f"green_{k}": v for k, v in DMA_GREEN.items()},
    **{f"error_{k}": v for k, v in DMA_ERROR.items()},
    **{f"warning_{k}": v for k, v in DMA_WARNING.items()},
    **{f"info_{k}": v for k, v in DMA_INFO.items()},
    **{f"success_{k}": v for k, v in DMA_SUCCESS.items()},
    **{f"neutral_light_{k}": v for k, v in DMA_NEUTRAL_LIGHT.items()},
    **{f"neutral_dark_{k}": v for k, v in DMA_NEUTRAL_DARK.items()},
}

__all__ = [
    # Core colors
    "DMA_BLUE", "DMA_TEAL", "DMA_TURQUOISE", "DMA_GREEN",
    "DMA_ERROR", "DMA_WARNING", "DMA_INFO", "DMA_SUCCESS",
    "DMA_NEUTRAL_LIGHT", "DMA_NEUTRAL_DARK",
    # Palettes
    "DMA_QUALITATIVE_BOLD", "DMA_QUALITATIVE_LIGHT", "DMA_QUALITATIVE_DARK",
    "DMA_QUALITATIVE_SEMANTIC",
    "DMA_SEQUENTIAL_BLUE", "DMA_SEQUENTIAL_TEAL", "DMA_SEQUENTIAL_TURQUOISE",
    "DMA_SEQUENTIAL_GREEN", "DMA_SEQUENTIAL_GRAY_LIGHT", "DMA_SEQUENTIAL_GRAY_DARK",
    "DMA_DIVERGING_BLUE_ORANGE", "DMA_DIVERGING_TEAL_RED", "DMA_DIVERGING_GREEN_PURPLE",
    "DMA_BLUES_9", "DMA_TEALS_9", "DMA_TURQUOISES_9", "DMA_GREENS_9",
    "DMA_REDS_9", "DMA_ORANGES_9", "DMA_GRAYS_9",
    # Colormaps
    "DMA_CMAPS", "register_cmaps", "get_sequential_cmap", "get_diverging_cmap", "get_qualitative_cmap",
    # Cyclers
    "get_color_cycler", "set_default_cycler",
    # Helpers
    "get_palette", "list_palettes", "demo_palettes",
    # Conversion
    "hex_to_rgb", "hex_to_rgb255", "rgb_to_hex",
    # All colors
    "ALL_COLORS",
]