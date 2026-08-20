#' DMA Theme - Plotly Integration
#'
#' Provides DMA color sequences and templates for plotly.
#'
#' @name plotly_dma
#' @docType package
NULL

#' DMA color sequences for plotly
#'
#' @export
dma_plotly_colors <- list(
  # Qualitative sequences
  qualitative_bold = dma_palettes$qualitative_bold,
  qualitative_light = dma_palettes$qualitative_light,
  qualitative_dark = dma_palettes$qualitative_dark,
  qualitative_semantic = dma_palettes$qualitative_semantic,
  
  # Sequential sequences
  sequential_blue = dma_palettes$sequential_blue,
  sequential_teal = dma_palettes$sequential_teal,
  sequential_turquoise = dma_palettes$sequential_turquoise,
  sequential_green = dma_palettes$sequential_green,
  
  # Diverging sequences
  diverging_blue_orange = dma_palettes$diverging_blue_orange,
  diverging_teal_red = dma_palettes$diverging_teal_red,
  diverging_green_warm = dma_palettes$diverging_green_warm,
  
  # Brewer-style
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

#' Get a DMA color sequence for plotly
#'
#' @param name Sequence name (see \code{names(dma_plotly_colors)})
#' @return Character vector of hex colors
#' @export
get_dma_plotly_colors <- function(name) {
  if (!name %in% names(dma_plotly_colors)) {
    stop(sprintf("Color sequence '%s' not found. Available: %s",
                 name, paste(names(dma_plotly_colors), collapse = ", ")))
  }
  dma_plotly_colors[[name]]
}

#' List all DMA plotly color sequences
#'
#' @return Data frame with sequence names and lengths
#' @export
list_dma_plotly_colors <- function() {
  data.frame(
    sequence = names(dma_plotly_colors),
    n_colors = vapply(dma_plotly_colors, length, integer(1)),
    stringsAsFactors = FALSE
  )
}

# =============================================================================
# Plotly Templates
# =============================================================================

#' DMA plotly template (light)
#'
#' @export
dma_plotly_template_light <- list(
  layout = list(
    # Font
    font = list(
      family = "DejaVu Sans, Arial, Helvetica, sans-serif",
      color = "#1E282D",
      size = 12
    ),
    
    # Title
    title = list(
      font = list(
        family = "DejaVu Sans, Arial, Helvetica, sans-serif",
        color = "#1E282D",
        size = 16
      ),
      x = 0.5,
      xanchor = "center"
    ),
    
    # Background
    paper_bgcolor = "#F8FAFC",
    plot_bgcolor = "#F8FAFC",
    
    # Axes
    xaxis = list(
      gridcolor = "#C8D6E3",
      zerolinecolor = "#C8D6E3",
      linecolor = "#6E89A0",
      linewidth = 1,
      tickcolor = "#1E282D",
      tickfont = list(color = "#1E282D", size = 11),
      titlefont = list(color = "#1E282D", size = 13)
    ),
    yaxis = list(
      gridcolor = "#C8D6E3",
      zerolinecolor = "#C8D6E3",
      linecolor = "#6E89A0",
      linewidth = 1,
      tickcolor = "#1E282D",
      tickfont = list(color = "#1E282D", size = 11),
      titlefont = list(color = "#1E282D", size = 13)
    ),
    
    # Legend
    legend = list(
      bgcolor = "rgba(248,250,252,0.95)",
      bordercolor = "#C8D6E3",
      borderwidth = 1,
      font = list(color = "#1E282D", size = 11)
    ),
    
    # Colorway (default discrete color sequence)
    colorway = dma_palettes$qualitative_bold,
    
    # Colorscale (default continuous color scale)
    colorscale = list(
      sequential = dma_palettes$sequential_blue,
      sequentialminus = rev(dma_palettes$sequential_blue),
      diverging = dma_palettes$diverging_blue_orange
    ),
    
    # Hover
    hoverlabel = list(
      bgcolor = "#FFFFFF",
      bordercolor = "#C8D6E3",
      font = list(color = "#1E282D", size = 11)
    ),
    
    # Modebar
    modebar = list(
      bgcolor = "rgba(248,250,252,0.8)",
      color = "#6E89A0",
      activecolor = "#007BDB"
    ),
    
    # Margin
    margin = list(l = 60, r = 40, t = 60, b = 60, pad = 4)
  )
)

#' DMA plotly template (dark)
#'
#' @export
dma_plotly_template_dark <- list(
  layout = list(
    # Font
    font = list(
      family = "DejaVu Sans, Arial, Helvetica, sans-serif",
      color = "#E0E8EF",
      size = 12
    ),
    
    # Title
    title = list(
      font = list(
        family = "DejaVu Sans, Arial, Helvetica, sans-serif",
        color = "#E0E8EF",
        size = 16
      ),
      x = 0.5,
      xanchor = "center"
    ),
    
    # Background
    paper_bgcolor = "#0A0F14",
    plot_bgcolor = "#0A0F14",
    
    # Axes
    xaxis = list(
      gridcolor = "#2D4058",
      zerolinecolor = "#2D4058",
      linecolor = "#6E89A0",
      linewidth = 1,
      tickcolor = "#E0E8EF",
      tickfont = list(color = "#E0E8EF", size = 11),
      titlefont = list(color = "#E0E8EF", size = 13)
    ),
    yaxis = list(
      gridcolor = "#2D4058",
      zerolinecolor = "#2D4058",
      linecolor = "#6E89A0",
      linewidth = 1,
      tickcolor = "#E0E8EF",
      tickfont = list(color = "#E0E8EF", size = 11),
      titlefont = list(color = "#E0E8EF", size = 13)
    ),
    
    # Legend
    legend = list(
      bgcolor = "rgba(16,24,32,0.95)",
      bordercolor = "#2D4058",
      borderwidth = 1,
      font = list(color = "#E0E8EF", size = 11)
    ),
    
    # Colorway (default discrete color sequence)
    colorway = dma_palettes$qualitative_dark,
    
    # Colorscale (default continuous color scale)
    colorscale = list(
      sequential = dma_palettes$sequential_blue,
      sequentialminus = rev(dma_palettes$sequential_blue),
      diverging = dma_palettes$diverging_blue_orange
    ),
    
    # Hover
    hoverlabel = list(
      bgcolor = "#101820",
      bordercolor = "#2D4058",
      font = list(color = "#E0E8EF", size = 11)
    ),
    
    # Modebar
    modebar = list(
      bgcolor = "rgba(16,24,32,0.8)",
      color = "#6E89A0",
      activecolor = "#1A91E6"
    ),
    
    # Margin
    margin = list(l = 60, r = 40, t = 60, b = 60, pad = 4)
  )
)

#' Register DMA templates with plotly
#'
#' @param theme "light" or "dark"
#' @export
register_dma_plotly_template <- function(theme = "light") {
  if (!requireNamespace("plotly", quietly = TRUE)) {
    stop("plotly package is required")
  }
  
  template_name <- sprintf("dma_%s", theme)
  template <- if (theme == "dark") dma_plotly_template_dark else dma_plotly_template_light
  
  plotly::register_template(template_name, template)
  
  # Set as default if requested
  if (getOption("plotly_default_template", "") == "") {
    options(plotly_default_template = template_name)
  }
  
  invisible(template_name)
}

#' Create a plotly figure with DMA styling
#'
#' @param p A plotly figure object
#' @param theme "light" or "dark"
#' @return Styled plotly figure
#' @export
style_plotly_dma <- function(p, theme = "light") {
  if (!requireNamespace("plotly", quietly = TRUE)) {
    stop("plotly package is required")
  }
  
  template <- if (theme == "dark") dma_plotly_template_dark else dma_plotly_template_light
  
  # Apply template layout
  p <- plotly::layout(p, template$layout)
  
  # Update traces to use DMA colorway if they don't have explicit colors
  trace_names <- vapply(p$x$data, function(tr) tr$type %in% c("scatter", "bar", "box", "violin", "histogram"), logical(1))
  
  p
}

# =============================================================================
# Color Scale Helpers for Plotly
# =============================================================================

#' Create a plotly colorscale from DMA palette
#'
#' @param palette Palette name (see \code{names(dma_plotly_colors)})
#' @return List suitable for plotly colorscale
#' @export
dma_plotly_colorscale <- function(palette = "sequential_blue") {
  colors <- get_dma_plotly_colors(palette)
  
  # Convert to plotly colorscale format: list of [normalized_position, color]
  n <- length(colors)
  positions <- seq(0, 1, length.out = n)
  
  Map(function(pos, col) list(pos, col), positions, colors)
}

#' Get all available DMA colorscales for plotly
#'
#' @return Named list of colorscales
#' @export
get_dma_plotly_colorscales <- function() {
  scales <- list()
  for (name in names(dma_plotly_colors)) {
    scales[[name]] <- dma_plotly_colorscale(name)
  }
  scales
}

# =============================================================================
# Demo Functions
# =============================================================================

#' Demo DMA plotly color sequences
#'
#' @export
demo_dma_plotly_colors <- function() {
  if (!requireNamespace("plotly", quietly = TRUE)) {
    stop("plotly package is required")
  }
  
  # Create a simple bar chart for each palette
  plots <- list()
  
  for (name in names(dma_plotly_colors)) {
    colors <- dma_plotly_colors[[name]]
    n <- length(colors)
    
    p <- plotly::plot_ly(
      x = seq_len(n),
      y = rep(1, n),
      type = "bar",
      marker = list(color = colors),
      showlegend = FALSE,
      hoverinfo = "text",
      hovertext = sprintf("%s: %s", name, colors)
    ) %>%
      plotly::layout(
        title = name,
        xaxis = list(showticklabels = FALSE, showgrid = FALSE, zeroline = FALSE),
        yaxis = list(showticklabels = FALSE, showgrid = FALSE, zeroline = FALSE),
        margin = list(l = 20, r = 20, t = 40, b = 20),
        height = 100
      )
    
    plots[[name]] <- p
  }
  
  # Subplot all palettes
  plotly::subplot(plots, nrows = length(plots), shareX = TRUE, titleY = FALSE) %>%
    plotly::layout(
      title = "DMA Theme Plotly Color Sequences",
      margin = list(l = 20, r = 20, t = 60, b = 20)
    )
}

#' Demo DMA plotly templates
#'
#' @export
demo_dma_plotly_templates <- function() {
  if (!requireNamespace("plotly", quietly = TRUE)) {
    stop("plotly package is required")
  }
  
  # Sample data
  df <- data.frame(
    x = rep(1:10, 3),
    y = c(rnorm(10, 5, 1), rnorm(10, 3, 1), rnorm(10, 7, 1)),
    group = rep(c("A", "B", "C"), each = 10)
  )
  
  # Light theme
  p1 <- plotly::plot_ly(df, x = ~x, y = ~y, color = ~group, type = "scatter", mode = "lines+markers") %>%
    plotly::layout(template = "dma_light", title = "DMA Light Template")
  
  # Dark theme
  p2 <- plotly::plot_ly(df, x = ~x, y = ~y, color = ~group, type = "scatter", mode = "lines+markers") %>%
    plotly::layout(template = "dma_dark", title = "DMA Dark Template")
  
  # Side by side
  plotly::subplot(p1, p2, nrows = 1, shareY = TRUE, titleX = FALSE, titleY = FALSE) %>%
    plotly::layout(title = "DMA Plotly Templates Comparison")
}

# Register templates on load
.onLoad <- function(libname, pkgname) {
  if (requireNamespace("plotly", quietly = TRUE)) {
    tryCatch({
      plotly::register_template("dma_light", dma_plotly_template_light)
      plotly::register_template("dma_dark", dma_plotly_template_dark)
    }, error = function(e) {
      # Ignore registration errors
    })
  }
  invisible()
}

# Export
# (Already exported via roxygen2 @export tags)