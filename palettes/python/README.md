# DMA Theme - Python Palettes

Semantic color palettes for data visualization in Python. Compatible with matplotlib, seaborn, plotnine, and ggplot2 (via plotnine).

## Installation

```bash
pip install dma-palette
# With optional dependencies
pip install dma-palette[seaborn]
pip install dma-palette[plotnine]
pip install dma-palette[all]
```

## Quick Start

```python
from dma_palette import (
    DMA_BLUE, DMA_TEAL, DMA_TURQUOISE, DMA_GREEN,
    DMA_ERROR, DMA_WARNING, DMA_INFO, DMA_SUCCESS,
    get_cmap, set_default_cycler, theme_dma,
    scale_color_dma, scale_fill_dma
)

# Matplotlib
import matplotlib.pyplot as plt
set_default_cycler('bold')  # or 'light', 'dark', 'semantic'
plt.style.use('dma-light')  # or 'dma-dark'

# Seaborn
import seaborn as sns
from dma_palette import set_theme
set_theme('light')  # or 'dark'

# plotnine / ggplot2
from plotnine import ggplot, aes, geom_point
from dma_palette import scale_color_dma, theme_dma

(ggplot(data, aes(x='x', y='y', color='category'))
 + geom_point()
 + scale_color_dma(palette='bold')
 + theme_dma())
```

## Color Palettes

### Primary Colors
- **Blue**: 900-50 (10 shades)
- **Teal**: 900-50
- **Turquoise**: 900-50
- **Green**: 900-50

### Semantic Colors
- **Error**: Red shades
- **Warning**: Orange shades
- **Info**: Blue shades
- **Success**: Green shades

### Predefined Palettes
- Qualitative: `bold`, `light`, `dark`, `semantic`
- Sequential: `blue`, `teal`, `turquoise`, `green`, `gray_light`, `gray_dark`
- Diverging: `blue_orange`, `teal_red`, `green_warm`
- Brewer-compatible: `Blues`, `Teals`, `Turquoises`, `Greens`, `Reds`, `Oranges`, `Grays`, `BuOr`, `TealRed`, `GreenWarm`

## Colormaps

All palettes are registered as matplotlib colormaps:
```python
from dma_palette import get_cmap
cmap = get_cmap('blue')        # Sequential
cmap = get_cmap('blue_orange') # Diverging
cmap = get_cmap('bold')        # Qualitative
```

## Themes

```python
from dma_palette import theme_dma, theme_dma_dark
# For matplotlib
plt.style.use('dma-light')
# For plotnine
theme_dma()
theme_dma_dark()
```