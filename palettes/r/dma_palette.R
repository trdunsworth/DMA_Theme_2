#' DMA Theme - R Color Palettes
#'
#' A semantic color palette for data visualization in R.
#' Compatible with ggplot2, plotly, and base R graphics.
#'
#' @name dma_palette
#' @docType package
#' @author Dunsworth-Mann Analytics LLC
#' @references https://dunsworth-mann.com
NULL

# =============================================================================
# Core Color Definitions
# =============================================================================

#' @export
dma_colors <- list(
  # Primary Colors
  blue = c(
    "900" = "#002B5C",
    "800" = "#003D7A",
    "700" = "#00529E",
    "600" = "#0069C0",
    "500" = "#007BDB",
    "400" = "#1A91E6",
    "300" = "#4DA8EE",
    "200" = "#8FC3F5",
    "100" = "#C5DEF9",
    "50"  = "#E8F4FC"
  ),
  
  teal = c(
    "900" = "#004D4D",
    "800" = "#006666",
    "700" = "#007F7F",
    "600" = "#009999",
    "500" = "#00B3B3",
    "400" = "#1ACCCC",
    "300" = "#4DE5E5",
    "200" = "#99F0F0",
    "100" = "#CCF7F7",
    "50"  = "#E6FBFB"
  ),
  
  turquoise = c(
    "900" = "#005C5C",
    "800" = "#007373",
    "700" = "#008A8A",
    "600" = "#00A1A1",
    "500" = "#00B8B8",
    "400" = "#1ACECE",
    "300" = "#4DDDDD",
    "200" = "#99EDED",
    "100" = "#CCF6F6",
    "50"  = "#E6FBFB"
  ),
  
  green = c(
    "900" = "#004D1A",
    "800" = "#006622",
    "700" = "#007F2A",
    "600" = "#009933",
    "500" = "#00B33B",
    "400" = "#1ACC4D",
    "300" = "#4DD966",
    "200" = "#99E599",
    "100" = "#CCF0CC",
    "50"  = "#E6F8E6"
  ),
  
  # Semantic Colors
  error = c(
    "900" = "#7A0000",
    "800" = "#9E0000",
    "700" = "#C40000",
    "600" = "#E80000",
    "500" = "#FF1A1A",
    "400" = "#FF4D4D",
    "300" = "#FF7A7A",
    "200" = "#FFA8A8",
    "100" = "#FFD4D4",
    "50"  = "#FFEAEA"
  ),
  
  warning = c(
    "900" = "#7A4A00",
    "800" = "#9E5E00",
    "700" = "#C47300",
    "600" = "#E88800",
    "500" = "#FF9F00",
    "400" = "#FFAD33",
    "300" = "#FFC466",
    "200" = "#FFDB99",
    "100" = "#FFF0CC",
    "50"  = "#FFF8E6"
  ),
  
  info = c(
    "900" = "#003D7A",
    "800" = "#00529E",
    "700" = "#0069C0",
    "600" = "#007BDB",
    "500" = "#0091E6",
    "400" = "#33A8EE",
    "300" = "#66BFFF",
    "200" = "#99D4FF",
    "100" = "#CCE9FF",
    "50"  = "#E6F4FF"
  ),
  
  success = c(
    "900" = "#004D1A",
    "800" = "#006622",
    "700" = "#007F2A",
    "600" = "#009933",
    "500" = "#00B33B",
    "400" = "#33CC5A",
    "300" = "#66D97A",
    "200" = "#99E599",
    "100" = "#CCF0CC",
    "50"  = "#E6F8E6"
  ),
  
  # Neutral Colors
  neutral_light = c(
    "950" = "#F0F4F8",
    "900" = "#E0E8EF",
    "800" = "#C8D6E3",
    "700" = "#A8BED1",
    "600" = "#8AA3BC",
    "500" = "#708BA0",
    "400" = "#5A7287",
    "300" = "#485C6E",
    "200" = "#384854",
    "100" = "#2A363E",
    "50"  = "#1E282D"
  ),
  
  neutral_dark = c(
    "950" = "#0A0F14",
    "900" = "#101820",
    "800" = "#182430",
    "700" = "#203040",
    "600" = "#2D4058",
    "500" = "#3D526E",
    "400" = "#526D85",
    "300" = "#6E89A0",
    "200" = "#93ABC3",
    "100" = "#B8CDE0",
    "50"  = "#DCE8F0"
  )
)

# =============================================================================
# Predefined Palettes
# =============================================================================

#' @export
dma_palettes <- list(
  # Qualitative palettes (for categorical data)
  qualitative_bold = unname(c(
    dma_colors$blue["500"],
    dma_colors$teal["500"],
    dma_colors$green["500"],
    dma_colors$turquoise["500"],
    dma_colors$warning["500"],
    dma_colors$error["500"],
    dma_colors$blue["700"],
    dma_colors$teal["700"],
    dma_colors$green["700"],
    dma_colors$turquoise["700"]
  )),
  
  qualitative_light = unname(c(
    dma_colors$blue["300"],
    dma_colors$teal["300"],
    dma_colors$green["300"],
    dma_colors$turquoise["300"],
    dma_colors$warning["300"],
    dma_colors$error["300"],
    dma_colors$blue["400"],
    dma_colors$teal["400"],
    dma_colors$green["400"],
    dma_colors$turquoise["400"]
  )),
  
  qualitative_dark = unname(c(
    dma_colors$blue["700"],
    dma_colors$teal["700"],
    dma_colors$green["700"],
    dma_colors$turquoise["700"],
    dma_colors$warning["700"],
    dma_colors$error["700"],
    dma_colors$blue["800"],
    dma_colors$teal["800"],
    dma_colors$green["800"],
    dma_colors$turquoise["800"]
  )),
  
  qualitative_semantic = unname(c(
    dma_colors$info["500"],
    dma_colors$success["500"],
    dma_colors$warning["500"],
    dma_colors$error["500"],
    dma_colors$blue["500"],
    dma_colors$teal["500"]
  )),
  
  # Sequential palettes (for ordered data)
  sequential_blue = unname(dma_colors$blue[c("50", "100", "200", "300", "400", "500", "600", "700", "800", "900")]),
  sequential_teal = unname(dma_colors$teal[c("50", "100", "200", "300", "400", "500", "600", "700", "800", "900")]),
  sequential_turquoise = unname(dma_colors$turquoise[c("50", "100", "200", "300", "400", "500", "600", "700", "800", "900")]),
  sequential_green = unname(dma_colors$green[c("50", "100", "200", "300", "400", "500", "600", "700", "800", "900")]),
  sequential_gray_light = unname(dma_colors$neutral_light[c("50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950")]),
  sequential_gray_dark = unname(dma_colors$neutral_dark[c("50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950")]),
  
  # Diverging palettes (for data with meaningful midpoint)
  diverging_blue_orange = unname(c(
    dma_colors$blue["900"],
    dma_colors$blue["700"],
    dma_colors$blue["500"],
    dma_colors$blue["300"],
    dma_colors$blue["100"],
    dma_colors$neutral_light["50"],
    dma_colors$warning["100"],
    dma_colors$warning["300"],
    dma_colors$warning["500"],
    dma_colors$warning["700"],
    dma_colors$warning["900"]
  )),
  
  diverging_teal_red = unname(c(
    dma_colors$teal["900"],
    dma_colors$teal["700"],
    dma_colors$teal["500"],
    dma_colors$teal["300"],
    dma_colors$teal["100"],
    dma_colors$neutral_light["50"],
    dma_colors$error["100"],
    dma_colors$error["300"],
    dma_colors$error["500"],
    dma_colors$error["700"],
    dma_colors$error["900"]
  )),
  
  diverging_green_warm = unname(c(
    dma_colors$green["900"],
    dma_colors$green["700"],
    dma_colors$green["500"],
    dma_colors$green["300"],
    dma_colors$green["100"],
    dma_colors$neutral_light["50"],
    dma_colors$warning["900"],
    dma_colors$warning["700"],
    dma_colors$warning["500"],
    dma_colors$warning["300"],
    dma_colors$warning["100"]
  )),
  
  # Brewer-style 9-color palettes
  Blues = unname(dma_colors$blue[c("50", "100", "200", "300", "400", "500", "600", "700", "800")]),
  Teals = unname(dma_colors$teal[c("50", "100", "200", "300", "400", "500", "600", "700", "800")]),
  Turquoises = unname(dma_colors$turquoise[c("50", "100", "200", "300", "400", "500", "600", "700", "800")]),
  Greens = unname(dma_colors$green[c("50", "100", "200", "300", "400", "500", "600", "700", "800")]),
  Reds = unname(dma_colors$error[c("50", "100", "200", "300", "400", "500", "600", "700", "800")]),
  Oranges = unname(dma_colors$warning[c("50", "100", "200", "300", "400", "500", "600", "700", "800")]),
  Grays = unname(dma_colors$neutral_light[c("50", "100", "200", "300", "400", "500", "600", "700", "800")]),
  
  # Diverging brewer-style (9 colors)
  BuOr = unname(c(
    dma_colors$blue["900"],
    dma_colors$blue["700"],
    dma_colors$blue["500"],
    dma_colors$blue["300"],
    dma_colors$blue["100"],
    dma_colors$neutral_light["50"],
    dma_colors$warning["100"],
    dma_colors$warning["300"],
    dma_colors$warning["500"]
  )),
  
  TealRed = unname(c(
    dma_colors$teal["900"],
    dma_colors$teal["700"],
    dma_colors$teal["500"],
    dma_colors$teal["300"],
    dma_colors$teal["100"],
    dma_colors$neutral_light["50"],
    dma_colors$error["100"],
    dma_colors$error["300"],
    dma_colors$error["500"]
  )),
  
  GreenWarm = unname(c(
    dma_colors$green["900"],
    dma_colors$green["700"],
    dma_colors$green["500"],
    dma_colors$green["300"],
    dma_colors$green["100"],
    dma_colors$neutral_light["50"],
    dma_colors$warning["900"],
    dma_colors$warning["700"],
    dma_colors$warning["500"]
  ))
)

# =============================================================================
# Helper Functions
# =============================================================================

#' Get a DMA palette by name
#'
#' @param name Palette name (see \code{names(dma_palettes)})
#' @param n Number of colors to return (optional)
#' @return Character vector of hex colors
#' @export
get_dma_palette <- function(name, n = NULL) {
  if (!name %in% names(dma_palettes)) {
    stop(sprintf("Palette '%s' not found. Available: %s", 
                 name, paste(names(dma_palettes), collapse = ", ")))
  }
  
  palette <- dma_palettes[[name]]
  
  if (!is.null(n)) {
    if (n > length(palette)) {
      warning(sprintf("Requested %d colors but palette '%s' only has %d. Recycling.", 
                      n, name, length(palette)))
      palette <- rep(palette, length.out = n)
    } else {
      palette <- palette[seq_len(n)]
    }
  }
  
  return(palette)
}

#' List all available DMA palettes
#'
#' @return Data frame with palette names and color counts
#' @export
list_dma_palettes <- function() {
  data.frame(
    palette = names(dma_palettes),
    n_colors = vapply(dma_palettes, length, integer(1)),
    stringsAsFactors = FALSE
  )
}

#' Demo all DMA palettes
#'
#' @param ncol Number of columns in the plot
#' @export
demo_dma_palettes <- function(ncol = 2) {
  if (!requireNamespace("ggplot2", quietly = TRUE)) {
    stop("ggplot2 is required for demo_dma_palettes()")
  }
  
  # Create demo data
  palette_data <- do.call(rbind, lapply(names(dma_palettes), function(name) {
    colors <- dma_palettes[[name]]
    data.frame(
      palette = name,
      color = colors,
      index = seq_along(colors),
      stringsAsFactors = FALSE
    )
  }))
  
  # Plot
  ggplot2::ggplot(palette_data, ggplot2::aes(x = index, y = palette, fill = color)) +
    ggplot2::geom_tile(color = "white", linewidth = 0.5) +
    ggplot2::scale_fill_identity() +
    ggplot2::scale_x_continuous(expand = c(0, 0), breaks = NULL) +
    ggplot2::scale_y_discrete(limits = rev(unique(palette_data$palette))) +
    ggplot2::labs(
      title = "DMA Theme Color Palettes",
      subtitle = "All available qualitative, sequential, diverging, and brewer-style palettes",
      x = NULL, y = NULL
    ) +
    ggplot2::theme_minimal(base_size = 11) +
    ggplot2::theme(
      panel.grid = ggplot2::element_blank(),
      axis.text.x = ggplot2::element_blank(),
      plot.title = ggplot2::element_text(face = "bold", size = 14),
      plot.subtitle = ggplot2::element_text(color = "#6E89A0")
    )
}

# =============================================================================
# Color Conversion Utilities
# =============================================================================

#' Convert hex color to RGB
#'
#' @param hex Character vector of hex colors
#' @param scale Output scale: "0-1" or "0-255"
#' @return Matrix with RGB values
#' @export
hex_to_rgb <- function(hex, scale = c("0-1", "0-255")) {
  scale <- match.arg(scale)
  hex <- gsub("^#", "", hex)
  
  if (nchar(hex[1]) == 3) {
    hex <- gsub("(.)(.)(.)", "\\1\\1\\2\\2\\3\\3", hex)
  }
  
  r <- as.integer(substr(hex, 1, 2), 16)
  g <- as.integer(substr(hex, 3, 4), 16)
  b <- as.integer(substr(hex, 5, 6), 16)
  
  if (scale == "0-1") {
    return(cbind(r = r / 255, g = g / 255, b = b / 255))
  } else {
    return(cbind(r = r, g = g, b = b))
  }
}

#' Convert RGB to hex
#'
#' @param r,g,b Red, green, blue values (0-1 or 0-255)
#' @param scale Input scale: "0-1" or "0-255"
#' @return Hex color string
#' @export
rgb_to_hex <- function(r, g, b, scale = c("0-1", "0-255")) {
  scale <- match.arg(scale)
  
  if (scale == "0-1") {
    r <- round(r * 255)
    g <- round(g * 255)
    b <- round(b * 255)
  }
  
  sprintf("#%02X%02X%02X", r, g, b)
}

# =============================================================================
# Package Initialization
# =============================================================================

.onLoad <- function(libname, pkgname) {
  # Register with ggplot2 if available
  if (requireNamespace("ggplot2", quietly = TRUE)) {
    # The scales will be registered when ggplot2_dma is loaded
  }
  
  # Register with plotly if available
  if (requireNamespace("plotly", quietly = TRUE)) {
    # Plotly color sequences will be available via dma_palettes
  }
  
  invisible()
}