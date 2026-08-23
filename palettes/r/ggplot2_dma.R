# ggplot2 scales for DMA Theme palettes -----------------------------------
#
# Usage:
#   source("dma_palette.R"); source("ggplot2_dma.R")
#   library(ggplot2)
#
#   ggplot(df, aes(x, y, colour = grp)) + geom_point() +
#     scale_colour_dma()
#
#   ggplot(df, aes(x, y, fill = value)) + geom_raster() +
#     scale_fill_dma_continuous("Cool")
#
# Requires: ggplot2 >= 3.4

# Discrete (categorical) --------------------------------------------------

#' Categorical colour scale using DMA qualitative palette
scale_colour_dma <- function(palette = "qualitative", n = NULL,
                             name = waiver_name(palette), ...) {
  if (!requireNamespace("ggplot2", quietly = TRUE)) {
    stop("ggplot2 is required for scale_colour_dma()")
  }
  values <- .dma_discrete_values(palette, n)
  ggplot2::discrete_scale(
    aesthetics = "colour", scale_name = "dma",
    palette = function(n_req) {
      if (!is.null(n) && n_req > length(values)) {
        stop("Need ", n_req, " colors; palette provides ", length(values))
      }
      values
    },
    name = name, ...
  )
}

#' Categorical fill scale using DMA qualitative palette
scale_fill_dma <- function(palette = "qualitative", n = NULL,
                           name = waiver_name(palette), ...) {
  if (!requireNamespace("ggplot2", quietly = TRUE)) {
    stop("ggplot2 is required for scale_fill_dma()")
  }
  values <- .dma_discrete_values(palette, n)
  ggplot2::discrete_scale(
    aesthetics = "fill", scale_name = "dma",
    palette = function(n_req) {
      if (!is.null(n) && n_req > length(values)) {
        stop("Need ", n_req, " colors; palette provides ", length(values))
      }
      values
    },
    name = name, ...
  )
}

# R-spelling compatibility is native; add US spelling aliases
scale_color_dma <- scale_colour_dma
scale_color_fill_dma <- scale_fill_dma

.dma_discrete_values <- function(palette = "qualitative", n = NULL) {
  if (palette == "qualitative") {
    return(dma_qualitative(if (is.null(n)) 8 else n))
  }
  if (palette %in% names(.dma_seq_single) ||
      palette %in% names(.dma_seq_multi)) {
    return(dma_sequential(palette, if (is.null(n)) 5 else n))
  }
  if (palette %in% names(.dma_diverging)) {
    return(dma_diverging(palette, if (is.null(n)) 7 else n))
  }
  stop("Unknown DMA palette '", palette, "'")
}

waiver_name <- function(palette) {
  if (palette == "qualitative") "DMA" else paste("DMA", palette)
}

# Continuous --------------------------------------------------------------

#' Continuous gradient over a DMA sequential scheme
scale_colour_dma_continuous <- function(palette = "Cool",
                                        name = waiver_name(palette), ...) {
  ggplot2::scale_colour_gradientn(
    colours = .dma_seq_anchors(palette),       # light -> dark
    name = name, ...
  )
}

#' Continuous fill gradient over a DMA sequential scheme
scale_fill_dma_continuous <- function(palette = "Cool",
                                      name = waiver_name(palette), ...) {
  ggplot2::scale_fill_gradientn(
    colours = .dma_seq_anchors(palette),       # light -> dark
    name = name, ...
  )
}

scale_color_dma_continuous <- scale_colour_dma_continuous

.dma_seq_anchors <- function(scheme) {
  if (scheme %in% names(.dma_seq_single)) {
    scale <- .dma_scales[[.dma_seq_single[[scheme]]]]
    return(rev(unname(scale)))                 # light -> dark
  }
  if (scheme %in% names(.dma_seq_multi)) {
    return(.dma_seq_multi[[scheme]])
  }
  stop("Unknown sequential scheme '", scheme, "'")
}

# Binned ------------------------------------------------------------------

#' Binned colour scale over a DMA sequential scheme
scale_colour_dma_binned <- function(palette = "Blues", n = 5,
                                    name = waiver_name(palette), ...) {
  ggplot2::scale_colour_stepsn(
    colours = dma_sequential(palette, n), name = name, ...
  )
}

#' Binned fill scale over a DMA sequential scheme
scale_fill_dma_binned <- function(palette = "Blues", n = 5,
                                  name = waiver_name(palette), ...) {
  ggplot2::scale_fill_stepsn(
    colours = dma_sequential(palette, n), name = name, ...
  )
}

scale_color_dma_binned <- scale_colour_dma_binned

# Diverging continuous ----------------------------------------------------

#' Diverging continuous colour gradient
scale_colour_dma_diverging <- function(palette = "Red-Blue",
                                       name = waiver_name(palette), ...) {
  ggplot2::scale_colour_gradient2(
    low = .dma_diverging[[palette]][1],
    mid = .dma_diverging[[palette]][3],
    high = .dma_diverging[[palette]][5],
    midpoint = 0,
    name = name, ...
  )
}

#' Diverging continuous fill gradient
scale_fill_dma_diverging <- function(palette = "Red-Blue",
                                     name = waiver_name(palette), ...) {
  ggplot2::scale_fill_gradient2(
    low = .dma_diverging[[palette]][1],
    mid = .dma_diverging[[palette]][3],
    high = .dma_diverging[[palette]][5],
    midpoint = 0,
    name = name, ...
  )
}

scale_color_dma_diverging <- scale_colour_dma_diverging
