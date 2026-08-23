# Plotly integration for DMA Theme palettes -------------------------------
#
# Usage:
#   source("dma_palette.R"); source("plotly_dma.R")
#   library(plotly)
#
#   # Categorical trace colors
#   plot_ly(df, x = ~x, y = ~y, color = ~grp,
#           colors = dma_qualitative_colors)
#
#   # Continuous colorbar
#   plot_ly(df, x = ~x, y = ~y, color = ~z,
#           colorscale = dma_colorscale("Cool"),
#           showscale = TRUE)

#' Named categorical sequences (plotly 'colors' argument)
dma_plotly_qualitative <- list(
  `DMA`        = dma_qualitative_colors,
  `DMA Blue`   = c("#0077CC", "#4DA8EE", "#8FC3F5"),
  `DMA Green`  = c("#004D1A", "#009933", "#66D97A")
)

#' Named sequential sequences (plotly 'colors' argument, discrete sampling)
dma_plotly_sequential <- function(scheme = "Blues", n = 9) {
  dma_sequential(scheme, n)
}

#' Continuous colorscale matrix for plotly (0-1 positions + hex colors)
dma_colorscale <- function(scheme = "Cool") {
  anchors <- if (scheme %in% names(.dma_seq_single)) {
    scale <- .dma_scales[[.dma_seq_single[[scheme]]]]
    rev(unname(scale))                       # light -> dark
  } else if (scheme %in% names(.dma_seq_multi)) {
    .dma_seq_multi[[scheme]]
  } else if (scheme %in% names(.dma_diverging)) {
    .dma_diverging[[scheme]]
  } else {
    stop("Unknown scheme '", scheme, "'")
  }
  k <- length(anchors)
  pos <- seq(0, 1, length.out = k)
  matrix(c(pos, anchors), ncol = 2L)
}

#' Register DMA scales as plotly defaults for a figure
#'
#' Returns a list suitable for spreading into layout()/add_trace():
#' \code{do.call(layout, c(p = fig, dma_layout_defaults()))}
dma_layout_defaults <- function() {
  list(
    colorway = dma_qualitative_colors,
    font = list(color = "#1A2A35"),
    paper_bgcolor = "#F8FAFC",
    plot_bgcolor = "#FFFFFF",
    xaxis = list(gridcolor = "#DCE4ED", zerolinecolor = "#A8C0D8"),
    yaxis = list(gridcolor = "#DCE4ED", zerolinecolor = "#A8C0D8")
  )
}
