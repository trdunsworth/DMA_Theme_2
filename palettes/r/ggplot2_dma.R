#' DMA Theme - ggplot2 Integration
#'
#' Provides scale_colour_dma, scale_fill_dma, and theme_dma for ggplot2.
#' Compatible with ggplot2's scale_* and theme_* interface.
#'
#' @name ggplot2_dma
#' @docType package
NULL

#' Discrete color scale using DMA qualitative palettes
#'
#' @param palette Palette name: "bold", "light", "dark", "semantic"
#' @param ... Additional arguments passed to discrete_scale
#' @param na.value Color for NA/missing values
#' @param guide Guide type
#' @export
#' @examples
#' library(ggplot2)
#' ggplot(mpg, aes(displ, hwy, color = class)) +
#'   geom_point() +
#'   scale_colour_dma(palette = "bold")
scale_colour_dma <- function(
  palette = "bold",
  ...,
  na.value = "#6E89A0",
  guide = "legend"
) {
  palettes <- list(
    bold = dma_palettes$qualitative_bold,
    light = dma_palettes$qualitative_light,
    dark = dma_palettes$qualitative_dark,
    semantic = dma_palettes$qualitative_semantic
  )
  
  colors <- palettes[[palette]]
  if (is.null(colors)) {
    warning(sprintf("Unknown palette '%s', using 'bold'", palette))
    colors <- dma_palettes$qualitative_bold
  }
  
  ggplot2::discrete_scale(
    aesthetics = "colour",
    scale_name = "dma",
    palette = function(n) {
      if (n <= length(colors)) {
        colors[seq_len(n)]
      } else {
        rep(colors, length.out = n)
      }
    },
    na.value = na.value,
    guide = guide,
    ...
  )
}

#' @rdname scale_colour_dma
#' @export
scale_color_dma <- scale_colour_dma

#' Discrete fill scale using DMA qualitative palettes
#'
#' @param palette Palette name: "bold", "light", "dark", "semantic"
#' @param ... Additional arguments passed to discrete_scale
#' @param na.value Color for NA/missing values
#' @param guide Guide type
#' @export
#' @examples
#' library(ggplot2)
#' ggplot(mpg, aes(class, fill = class)) +
#'   geom_bar() +
#'   scale_fill_dma(palette = "semantic")
scale_fill_dma <- function(
  palette = "bold",
  ...,
  na.value = "#6E89A0",
  guide = "legend"
) {
  palettes <- list(
    bold = dma_palettes$qualitative_bold,
    light = dma_palettes$qualitative_light,
    dark = dma_palettes$qualitative_dark,
    semantic = dma_palettes$qualitative_semantic
  )
  
  colors <- palettes[[palette]]
  if (is.null(colors)) {
    warning(sprintf("Unknown palette '%s', using 'bold'", palette))
    colors <- dma_palettes$qualitative_bold
  }
  
  ggplot2::discrete_scale(
    aesthetics = "fill",
    scale_name = "dma",
    palette = function(n) {
      if (n <= length(colors)) {
        colors[seq_len(n)]
      } else {
        rep(colors, length.out = n)
      }
    },
    na.value = na.value,
    guide = guide,
    ...
  )
}

# =============================================================================
# Continuous (Sequential) Scales
# =============================================================================

#' Continuous color scale using DMA sequential palettes
#'
#' @param palette Palette name: "blue", "teal", "turquoise", "green", "gray_light", "gray_dark"
#' @param ... Additional arguments passed to continuous_scale
#' @param na.value Color for NA/missing values
#' @param guide Guide type
#' @export
#' @examples
#' library(ggplot2)
#' ggplot(faithfuld, aes(waiting, eruptions, fill = density)) +
#'   geom_raster() +
#'   scale_fill_dma_c(palette = "teal")
scale_colour_dma_c <- function(
  palette = "blue",
  ...,
  na.value = "#6E89A0",
  guide = "colourbar"
) {
  palettes <- list(
    blue = dma_palettes$sequential_blue,
    teal = dma_palettes$sequential_teal,
    turquoise = dma_palettes$sequential_turquoise,
    green = dma_palettes$sequential_green,
    gray_light = dma_palettes$sequential_gray_light,
    gray_dark = dma_palettes$sequential_gray_dark
  )
  
  colors <- palettes[[palette]]
  if (is.null(colors)) {
    warning(sprintf("Unknown palette '%s', using 'blue'", palette))
    colors <- dma_palettes$sequential_blue
  }
  
  ggplot2::continuous_scale(
    aesthetics = "colour",
    scale_name = "dma_c",
    palette = function(n) {
      # Interpolate if needed
      if (n <= length(colors)) {
        colors[seq_len(n)]
      } else {
        grDevices::colorRampPalette(colors)(n)
      }
    },
    na.value = na.value,
    guide = guide,
    ...
  )
}

#' @rdname scale_colour_dma_c
#' @export
scale_color_dma_c <- scale_colour_dma_c

#' Continuous fill scale using DMA sequential palettes
#'
#' @param palette Palette name: "blue", "teal", "turquoise", "green", "gray_light", "gray_dark"
#' @param ... Additional arguments passed to continuous_scale
#' @param na.value Color for NA/missing values
#' @param guide Guide type
#' @export
scale_fill_dma_c <- function(
  palette = "blue",
  ...,
  na.value = "#6E89A0",
  guide = "colourbar"
) {
  palettes <- list(
    blue = dma_palettes$sequential_blue,
    teal = dma_palettes$sequential_teal,
    turquoise = dma_palettes$sequential_turquoise,
    green = dma_palettes$sequential_green,
    gray_light = dma_palettes$sequential_gray_light,
    gray_dark = dma_palettes$sequential_gray_dark
  )
  
  colors <- palettes[[palette]]
  if (is.null(colors)) {
    warning(sprintf("Unknown palette '%s', using 'blue'", palette))
    colors <- dma_palettes$sequential_blue
  }
  
  ggplot2::continuous_scale(
    aesthetics = "fill",
    scale_name = "dma_c",
    palette = function(n) {
      if (n <= length(colors)) {
        colors[seq_len(n)]
      } else {
        grDevices::colorRampPalette(colors)(n)
      }
    },
    na.value = na.value,
    guide = guide,
    ...
  )
}

# =============================================================================
# Diverging Scales
# =============================================================================

#' Diverging color scale using DMA diverging palettes
#'
#' @param palette Palette name: "blue_orange", "teal_red", "green_warm"
#' @param ... Additional arguments passed to continuous_scale
#' @param na.value Color for NA/missing values
#' @param guide Guide type
#' @export
#' @examples
#' library(ggplot2)
#' ggplot(mtcars, aes(wt, mpg, color = hp)) +
#'   geom_point(size = 3) +
#'   scale_colour_dma_d(palette = "teal_red")
scale_colour_dma_d <- function(
  palette = "blue_orange",
  ...,
  na.value = "#6E89A0",
  guide = "colourbar"
) {
  palettes <- list(
    blue_orange = dma_palettes$diverging_blue_orange,
    teal_red = dma_palettes$diverging_teal_red,
    green_warm = dma_palettes$diverging_green_warm
  )
  
  colors <- palettes[[palette]]
  if (is.null(colors)) {
    warning(sprintf("Unknown palette '%s', using 'blue_orange'", palette))
    colors <- dma_palettes$diverging_blue_orange
  }
  
  ggplot2::continuous_scale(
    aesthetics = "colour",
    scale_name = "dma_d",
    palette = function(n) {
      if (n <= length(colors)) {
        colors[seq_len(n)]
      } else {
        grDevices::colorRampPalette(colors)(n)
      }
    },
    na.value = na.value,
    guide = guide,
    ...
  )
}

#' @rdname scale_colour_dma_d
#' @export
scale_color_dma_d <- scale_colour_dma_d

#' Diverging fill scale using DMA diverging palettes
#'
#' @param palette Palette name: "blue_orange", "teal_red", "green_warm"
#' @param ... Additional arguments passed to continuous_scale
#' @param na.value Color for NA/missing values
#' @param guide Guide type
#' @export
scale_fill_dma_d <- function(
  palette = "blue_orange",
  ...,
  na.value = "#6E89A0",
  guide = "colourbar"
) {
  palettes <- list(
    blue_orange = dma_palettes$diverging_blue_orange,
    teal_red = dma_palettes$diverging_teal_red,
    green_warm = dma_palettes$diverging_green_warm
  )
  
  colors <- palettes[[palette]]
  if (is.null(colors)) {
    warning(sprintf("Unknown palette '%s', using 'blue_orange'", palette))
    colors <- dma_palettes$diverging_blue_orange
  }
  
  ggplot2::continuous_scale(
    aesthetics = "fill",
    scale_name = "dma_d",
    palette = function(n) {
      if (n <= length(colors)) {
        colors[seq_len(n)]
      } else {
        grDevices::colorRampPalette(colors)(n)
      }
    },
    na.value = na.value,
    guide = guide,
    ...
  )
}

# =============================================================================
# Brewer-compatible 9-color Scales
# =============================================================================

#' Brewer-compatible discrete color scale
#'
#' @param palette Brewer palette name: "Blues", "Teals", "Turquoises", "Greens",
#'   "Reds", "Oranges", "Grays", "BuOr", "TealRed", "GreenWarm"
#' @param ... Additional arguments passed to discrete_scale
#' @export
#' @examples
#' library(ggplot2)
#' ggplot(mpg, aes(displ, hwy, color = class)) +
#'   geom_point() +
#'   scale_colour_dma_brewer(palette = "Blues")
scale_colour_dma_brewer <- function(palette = "Blues", ...) {
  brewer_palettes <- list(
    Blues = dma_palettes$Blues,
    Teals = dma_palettes$Teals,
    Turquoises = dma_palettes$Turquoises,
    Greens = dma_palettes$Greens,
    Reds = dma_palettes$Reds,
    Oranges = dma_palettes$Oranges,
    Grays = dma_palettes$Grays,
    BuOr = dma_palettes$BuOr,
    TealRed = dma_palettes$TealRed,
    GreenWarm = dma_palettes$GreenWarm
  )
  
  colors <- brewer_palettes[[palette]]
  if (is.null(colors)) {
    warning(sprintf("Unknown palette '%s', using 'Blues'", palette))
    colors <- dma_palettes$Blues
  }
  
  ggplot2::discrete_scale(
    aesthetics = "colour",
    scale_name = "dma_brewer",
    palette = function(n) {
      if (n <= length(colors)) {
        colors[seq_len(n)]
      } else {
        rep(colors, length.out = n)
      }
    },
    ...
  )
}

#' @rdname scale_colour_dma_brewer
#' @export
scale_color_dma_brewer <- scale_colour_dma_brewer

#' Brewer-compatible discrete fill scale
#'
#' @param palette Brewer palette name: "Blues", "Teals", "Turquoises", "Greens",
#'   "Reds", "Oranges", "Grays", "BuOr", "TealRed", "GreenWarm"
#' @param ... Additional arguments passed to discrete_scale
#' @export
scale_fill_dma_brewer <- function(palette = "Blues", ...) {
  brewer_palettes <- list(
    Blues = dma_palettes$Blues,
    Teals = dma_palettes$Teals,
    Turquoises = dma_palettes$Turquoises,
    Greens = dma_palettes$Greens,
    Reds = dma_palettes$Reds,
    Oranges = dma_palettes$Oranges,
    Grays = dma_palettes$Grays,
    BuOr = dma_palettes$BuOr,
    TealRed = dma_palettes$TealRed,
    GreenWarm = dma_palettes$GreenWarm
  )
  
  colors <- brewer_palettes[[palette]]
  if (is.null(colors)) {
    warning(sprintf("Unknown palette '%s', using 'Blues'", palette))
    colors <- dma_palettes$Blues
  }
  
  ggplot2::discrete_scale(
    aesthetics = "fill",
    scale_name = "dma_brewer",
    palette = function(n) {
      if (n <= length(colors)) {
        colors[seq_len(n)]
      } else {
        rep(colors, length.out = n)
      }
    },
    ...
  )
}

# =============================================================================
# Complete DMA Theme
# =============================================================================

#' DMA theme for ggplot2
#'
#' A complete ggplot2 theme matching the DMA visual language.
#'
#' @param base_size Base font size
#' @param base_family Base font family
#' @param base_color Base text color
#' @param background_color Plot background color
#' @param grid_color Grid line color
#' @param axis_color Axis line color
#' @export
#' @examples
#' library(ggplot2)
#' ggplot(mpg, aes(displ, hwy)) +
#'   geom_point() +
#'   theme_dma()
theme_dma <- function(
  base_size = 11,
  base_family = "",
  base_color = "#1E282D",
  background_color = "#F8FAFC",
  grid_color = "#C8D6E3",
  axis_color = "#6E89A0"
) {
  # Use theme_minimal as base
  theme <- ggplot2::theme_minimal(base_size = base_size, base_family = base_family)
  
  # Override with DMA settings
  theme + ggplot2::theme(
    # Text
    text = ggplot2::element_text(color = base_color, family = base_family),
    plot.title = ggplot2::element_text(
      size = base_size * 1.4, face = "bold", color = base_color,
      margin = ggplot2::margin(b = 8)
    ),
    plot.subtitle = ggplot2::element_text(
      size = base_size * 1.1, color = "#485C6E", margin = ggplot2::margin(b = 8)
    ),
    plot.caption = ggplot2::element_text(
      size = base_size * 0.8, color = "#6E89A0", margin = ggplot2::margin(t = 8)
    ),
    
    # Background
    plot.background = ggplot2::element_rect(fill = background_color, color = background_color),
    panel.background = ggplot2::element_rect(fill = background_color, color = background_color),
    panel.border = ggplot2::element_rect(fill = NA, color = axis_color, linewidth = 1),
    
    # Grid
    panel.grid.major = ggplot2::element_line(color = grid_color, linewidth = 0.5),
    panel.grid.minor = ggplot2::element_line(color = grid_color, linewidth = 0.25, linetype = "dotted"),
    panel.grid.major.x = ggplot2::element_line(color = grid_color, linewidth = 0.5),
    panel.grid.major.y = ggplot2::element_line(color = grid_color, linewidth = 0.5),
    panel.grid.minor.x = ggplot2::element_blank(),
    panel.grid.minor.y = ggplot2::element_blank(),
    
    # Axis
    axis.line = ggplot2::element_line(color = axis_color, linewidth = 0.75),
    axis.line.x = ggplot2::element_line(color = axis_color, linewidth = 0.75),
    axis.line.y = ggplot2::element_line(color = axis_color, linewidth = 0.75),
    axis.text = ggplot2::element_text(size = base_size * 0.9, color = base_color),
    axis.text.x = ggplot2::element_text(margin = ggplot2::margin(t = 4)),
    axis.text.y = ggplot2::element_text(margin = ggplot2::margin(r = 4)),
    axis.ticks = ggplot2::element_line(color = axis_color, linewidth = 0.5),
    axis.ticks.length = ggplot2::unit(4, "pt"),
    axis.title = ggplot2::element_text(size = base_size, color = base_color, face = "bold"),
    axis.title.x = ggplot2::element_text(margin = ggplot2::margin(t = 8)),
    axis.title.y = ggplot2::element_text(margin = ggplot2::margin(r = 8), angle = 90),
    
    # Legend
    legend.background = ggplot2::element_rect(fill = background_color, color = NA),
    legend.box.background = ggplot2::element_rect(fill = background_color, color = NA),
    legend.key = ggplot2::element_rect(fill = background_color, color = NA),
    legend.key.size = ggplot2::unit(16, "pt"),
    legend.text = ggplot2::element_text(size = base_size * 0.9, color = base_color),
    legend.title = ggplot2::element_text(size = base_size, color = base_color, face = "bold"),
    legend.margin = ggplot2::margin(4, 4, 4, 4),
    legend.box.margin = ggplot2::margin(0, 0, 0, 0),
    legend.position = "right",
    legend.direction = "vertical",
    legend.box = "vertical",
    
    # Strips (facets)
    strip.background = ggplot2::element_rect(fill = "#E0E8EF", color = axis_color, linewidth = 1),
    strip.text = ggplot2::element_text(size = base_size * 0.9, color = base_color, face = "bold"),
    strip.text.x = ggplot2::element_text(margin = ggplot2::margin(4, 4, 4, 4)),
    strip.text.y = ggplot2::element_text(margin = ggplot2::margin(4, 4, 4, 4), angle = -90),
    
    # Margins
    plot.margin = ggplot2::margin(12, 12, 12, 12),
    
    # Facets
    panel.spacing = ggplot2::unit(8, "pt"),
    panel.spacing.x = ggplot2::unit(8, "pt"),
    panel.spacing.y = ggplot2::unit(8, "pt"),
    
    complete = TRUE
  )
}

#' Dark DMA theme for ggplot2
#'
#' @param base_size Base font size
#' @param base_family Base font family
#' @param base_color Base text color
#' @param background_color Plot background color
#' @param grid_color Grid line color
#' @param axis_color Axis line color
#' @export
theme_dma_dark <- function(
  base_size = 11,
  base_family = "",
  base_color = "#E0E8EF",
  background_color = "#0A0F14",
  grid_color = "#2D4058",
  axis_color = "#6E89A0"
) {
  theme <- ggplot2::theme_minimal(base_size = base_size, base_family = base_family)
  
  theme + ggplot2::theme(
    text = ggplot2::element_text(color = base_color, family = base_family),
    plot.title = ggplot2::element_text(
      size = base_size * 1.4, face = "bold", color = base_color,
      margin = ggplot2::margin(b = 8)
    ),
    plot.subtitle = ggplot2::element_text(
      size = base_size * 1.1, color = "#93ABC3", margin = ggplot2::margin(b = 8)
    ),
    plot.caption = ggplot2::element_text(
      size = base_size * 0.8, color = "#6E89A0", margin = ggplot2::margin(t = 8)
    ),
    
    plot.background = ggplot2::element_rect(fill = background_color, color = background_color),
    panel.background = ggplot2::element_rect(fill = background_color, color = background_color),
    panel.border = ggplot2::element_rect(fill = NA, color = axis_color, linewidth = 1),
    
    panel.grid.major = ggplot2::element_line(color = grid_color, linewidth = 0.5),
    panel.grid.minor = ggplot2::element_line(color = grid_color, linewidth = 0.25, linetype = "dotted"),
    panel.grid.major.x = ggplot2::element_line(color = grid_color, linewidth = 0.5),
    panel.grid.major.y = ggplot2::element_line(color = grid_color, linewidth = 0.5),
    panel.grid.minor.x = ggplot2::element_blank(),
    panel.grid.minor.y = ggplot2::element_blank(),
    
    axis.line = ggplot2::element_line(color = axis_color, linewidth = 0.75),
    axis.line.x = ggplot2::element_line(color = axis_color, linewidth = 0.75),
    axis.line.y = ggplot2::element_line(color = axis_color, linewidth = 0.75),
    axis.text = ggplot2::element_text(size = base_size * 0.9, color = base_color),
    axis.text.x = ggplot2::element_text(margin = ggplot2::margin(t = 4)),
    axis.text.y = ggplot2::element_text(margin = ggplot2::margin(r = 4)),
    axis.ticks = ggplot2::element_line(color = axis_color, linewidth = 0.5),
    axis.ticks.length = ggplot2::unit(4, "pt"),
    axis.title = ggplot2::element_text(size = base_size, color = base_color, face = "bold"),
    axis.title.x = ggplot2::element_text(margin = ggplot2::margin(t = 8)),
    axis.title.y = ggplot2::element_text(margin = ggplot2::margin(r = 8), angle = 90),
    
    legend.background = ggplot2::element_rect(fill = background_color, color = NA),
    legend.box.background = ggplot2::element_rect(fill = background_color, color = NA),
    legend.key = ggplot2::element_rect(fill = background_color, color = NA),
    legend.key.size = ggplot2::unit(16, "pt"),
    legend.text = ggplot2::element_text(size = base_size * 0.9, color = base_color),
    legend.title = ggplot2::element_text(size = base_size, color = base_color, face = "bold"),
    legend.margin = ggplot2::margin(4, 4, 4, 4),
    legend.box.margin = ggplot2::margin(0, 0, 0, 0),
    legend.position = "right",
    legend.direction = "vertical",
    legend.box = "vertical",
    
    strip.background = ggplot2::element_rect(fill = "#101820", color = axis_color, linewidth = 1),
    strip.text = ggplot2::element_text(size = base_size * 0.9, color = base_color, face = "bold"),
    strip.text.x = ggplot2::element_text(margin = ggplot2::margin(4, 4, 4, 4)),
    strip.text.y = ggplot2::element_text(margin = ggplot2::margin(4, 4, 4, 4), angle = -90),
    
    plot.margin = ggplot2::margin(12, 12, 12, 12),
    panel.spacing = ggplot2::unit(8, "pt"),
    panel.spacing.x = ggplot2::unit(8, "pt"),
    panel.spacing.y = ggplot2::unit(8, "pt"),
    
    complete = TRUE
  )
}

# =============================================================================
# Package Export
# =============================================================================

# Export all functions
# (Already exported via roxygen2 @export tags)