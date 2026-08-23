# DMA Theme data-visualization palettes ----------------------------------
#
# Brewer-style schemes (qualitative / sequential / diverging) built from
# DMA Theme brand colors. Inspired by the ColorBrewer *taxonomy*; no
# ColorBrewer colors are used.
#
# Usage:
#   source("dma_palette.R")
#   dma_qualitative(4)
#   dma_sequential("Teals", 7)
#   dma_diverging("Red-Green", 9)
#
# Author: Dunsworth-Mann Analytics LLC   |   License: MIT

# Full 10-stop brand scales (900 dark -> 50 light), from palette.json ----

.dma_scales <- list(
  blue = c(
    "900" = "#002B5C", "800" = "#003D7A", "700" = "#00529E",
    "600" = "#0069C0", "500" = "#0077CC", "400" = "#1A91E6",
    "300" = "#4DA8EE", "200" = "#8FC3F5", "100" = "#C5DEF9",
    "50"  = "#E8F4FC"
  ),
  teal = c(
    "900" = "#004D4D", "800" = "#006666", "700" = "#007F7F",
    "600" = "#009999", "500" = "#00B3B3", "400" = "#1ACCCC",
    "300" = "#4DE5E5", "200" = "#99F0F0", "100" = "#CCF7F7",
    "50"  = "#E6FBFB"
  ),
  turquoise = c(
    "900" = "#005C5C", "800" = "#007373", "700" = "#008A8A",
    "600" = "#00A1A1", "500" = "#00B8B8", "400" = "#1ACECE",
    "300" = "#4DDDDD", "200" = "#99EDED", "100" = "#CCF6F6",
    "50"  = "#E6FBFB"
  ),
  green = c(
    "900" = "#004D1A", "800" = "#006622", "700" = "#007F2A",
    "600" = "#009933", "500" = "#00B33B", "400" = "#1ACC4D",
    "300" = "#4DD966", "200" = "#99E599", "100" = "#CCF0CC",
    "50"  = "#E6F8E6"
  ),
  error = c(
    "900" = "#7A0000", "800" = "#9E0000", "700" = "#C40000",
    "600" = "#E80000", "500" = "#FF1A1A", "400" = "#FF4D4D",
    "300" = "#FF7A7A", "200" = "#FFA8A8", "100" = "#FFD4D4",
    "50"  = "#FFEAEA"
  ),
  warning = c(
    "900" = "#7A4A00", "800" = "#9E5E00", "700" = "#C47300",
    "600" = "#E88800", "500" = "#FF9F00", "400" = "#FFAD33",
    "300" = "#FFC466", "200" = "#FFDB99", "100" = "#FFF0CC",
    "50"  = "#FFF8E6"
  ),
  info = c(
    "900" = "#003D7A", "800" = "#00529E", "700" = "#0069C0",
    "600" = "#007BDB", "500" = "#0091E6", "400" = "#33A8EE",
    "300" = "#66BFFF", "200" = "#99D4FF", "100" = "#CCE9FF",
    "50"  = "#E6F4FF"
  ),
  success = c(
    "900" = "#004D1A", "800" = "#006622", "700" = "#007F2A",
    "600" = "#009933", "500" = "#00B33B", "400" = "#33CC5A",
    "300" = "#66D97A", "200" = "#99E599", "100" = "#CCF0CC",
    "50"  = "#E6F8E6"
  )
)

.dma_neutral_light <- "#F0F4F8"

# Qualitative (categorical); ordered to alternate hue family/lightness ---

dma_qualitative_colors <- c(
  "#0077CC",  # blue
  "#E88800",  # orange   (warning 600)
  "#009933",  # green
  "#C40000",  # red      (error 700)
  "#00A1A1",  # turquoise
  "#9E5E00",  # bronze   (warning 800)
  "#4DA8EE",  # light blue
  "#66D97A"   # light green
)

# Sequential scheme registry ---------------------------------------------

.dma_seq_single <- c(
  Blues      = "blue",
  Teals      = "teal",
  Turquoises = "turquoise",
  Greens     = "green",
  Oranges    = "warning"
)

.dma_seq_multi <- list(
  Cool = c(   # green -> teal -> blue (GnBu-like)
    "#E6F8E6", "#4DD966", "#00B3B3", "#0077CC", "#002B5C"
  ),
  Ocean = c(  # pale aqua -> deep navy
    "#CCF6F6", "#4DDDDD", "#009999", "#00529E", "#002B5C"
  ),
  Forest = c( # pale mint -> dark forest
    "#E6F8E6", "#99E599", "#00B33B", "#006622", "#004D1A"
  )
)

# Diverging scheme registry: end -> mid -> neutral -> mid -> end ---------

.dma_diverging <- list(
  "Red-Blue" = c(
    "#9E0000", "#FF7A7A", .dma_neutral_light, "#66BFFF", "#003D7A"
  ),
  "Red-Green" = c(
    "#9E0000", "#FF7A7A", .dma_neutral_light, "#66D97A", "#004D1A"
  ),
  "Brown-Teal" = c(
    "#7A4A00", "#FFAD33", "#FFFFFF", "#1ACCCC", "#004D4D"
  )
)

# Semantic status colors (all >= 4.5:1 on white) --------------------------

dma_semantic <- c(
  error   = "#C40000",
  warning = "#9E5E00",
  info    = "#0069C0",
  success = "#007F2A"
)

# Public functions ---------------------------------------------------------

#' Categorical DMA palette
#' @param n number of colors (recycles beyond 8)
dma_qualitative <- function(n = 8) {
  stopifnot(n >= 1)
  rep_len(dma_qualitative_colors, n)
}

#' Sequential DMA ramp, lightest first
#' @param scheme one of Blues/Teals/Turquoises/Greens/Oranges/Cool/Ocean/Forest
#' @param n number of colors (>= 2)
dma_sequential <- function(scheme = "Blues", n = 9) {
  stopifnot(n >= 2)
  if (scheme %in% names(.dma_seq_single)) {
    scale <- .dma_scales[[.dma_seq_single[[scheme]]]]
    anchors <- rev(unname(scale))          # 50 -> 900, light to dark
    colorRampPalette(anchors)(n)
  } else if (scheme %in% names(.dma_seq_multi)) {
    colorRampPalette(.dma_seq_multi[[scheme]])(n)
  } else {
    stop("Unknown scheme '", scheme,
         "'. Choose from: ",
         paste(c(names(.dma_seq_single), names(.dma_seq_multi)),
               collapse = ", "))
  }
}

#' Diverging DMA ramp, end -> neutral center -> other end
dma_diverging <- function(scheme = "Red-Blue", n = 11) {
  stopifnot(n >= 3)
  if (!scheme %in% names(.dma_diverging)) {
    stop("Unknown scheme '", scheme,
         "'. Choose from: ", paste(names(.dma_diverging), collapse = ", "))
  }
  anchors <- .dma_diverging[[scheme]]
  left  <- anchors[1:3]                    # end, mid, neutral
  right <- anchors[3:5]                    # neutral, mid, end
  half <- n %/% 2
  if (n %% 2 == 1) {
    c(colorRampPalette(left)(half + 1),
      tail(colorRampPalette(right)(half + 1), -1))
  } else {
    c(head(colorRampPalette(left)(half + 1), -1),
      tail(colorRampPalette(right)(half + 1), -1))
  }
}

#' Named semantic status colors
dma_status_colors <- function() dma_semantic

# Convenience alias matching README example
dma_colors <- dma_qualitative_colors
