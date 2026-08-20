"""
DMA Theme - plotnine Integration
=================================

plotnine-specific utilities and theme registration.

Author: Dunsworth-Mann Analytics LLC
https://dunsworth-mann.com
"""

from .ggplot2_dma import (
    scale_color_dma,
    scale_fill_dma,
    scale_color_dma_c,
    scale_fill_dma_c,
    scale_color_dma_d,
    scale_fill_dma_d,
    scale_color_dma_brewer,
    scale_fill_dma_brewer,
    theme_dma,
    theme_dma_dark,
)

# Alias for ggplot2 compatibility
scale_colour_dma = scale_color_dma
scale_colour_dma_c = scale_color_dma_c
scale_colour_dma_d = scale_color_dma_d
scale_colour_dma_brewer = scale_color_dma_brewer

__all__ = [
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
]


# Optional: Register scales with plotnine
def register_scales():
    """
    Register DMA scales with plotnine's scale registry.
    This allows using them as string names in aes().
    
    Example:
        aes(color='dma_bold')  # After registration
    """
    try:
        from plotnine.scales import scale_registry
        from plotnine.scales.scale_discrete import ScaleDiscrete
        from plotnine.scales.scale_continuous import ScaleContinuous
        
        # Register discrete scales
        scale_registry.register('dma_bold', scale_color_dma, 'color', {'palette': 'bold'})
        scale_registry.register('dma_bold', scale_fill_dma, 'fill', {'palette': 'bold'})
        scale_registry.register('dma_light', scale_color_dma, 'color', {'palette': 'light'})
        scale_registry.register('dma_light', scale_fill_dma, 'fill', {'palette': 'light'})
        scale_registry.register('dma_dark', scale_color_dma, 'color', {'palette': 'dark'})
        scale_registry.register('dma_dark', scale_fill_dma, 'fill', {'palette': 'dark'})
        scale_registry.register('dma_semantic', scale_color_dma, 'color', {'palette': 'semantic'})
        scale_registry.register('dma_semantic', scale_fill_dma, 'fill', {'palette': 'semantic'})
        
        # Register continuous scales
        scale_registry.register('dma_blue', scale_color_dma_c, 'color', {'palette': 'blue'})
        scale_registry.register('dma_blue', scale_fill_dma_c, 'fill', {'palette': 'blue'})
        scale_registry.register('dma_teal', scale_color_dma_c, 'color', {'palette': 'teal'})
        scale_registry.register('dma_teal', scale_fill_dma_c, 'fill', {'palette': 'teal'})
        scale_registry.register('dma_turquoise', scale_color_dma_c, 'color', {'palette': 'turquoise'})
        scale_registry.register('dma_turquoise', scale_fill_dma_c, 'fill', {'palette': 'turquoise'})
        scale_registry.register('dma_green', scale_color_dma_c, 'color', {'palette': 'green'})
        scale_registry.register('dma_green', scale_fill_dma_c, 'fill', {'palette': 'green'})
        
        # Register diverging scales
        scale_registry.register('dma_blue_orange', scale_color_dma_d, 'color', {'palette': 'blue_orange'})
        scale_registry.register('dma_blue_orange', scale_fill_dma_d, 'fill', {'palette': 'blue_orange'})
        scale_registry.register('dma_teal_red', scale_color_dma_d, 'color', {'palette': 'teal_red'})
        scale_registry.register('dma_teal_red', scale_fill_dma_d, 'fill', {'palette': 'teal_red'})
        
    except ImportError:
        pass  # plotnine not available


# Optional: Auto-register on import
# register_scales()