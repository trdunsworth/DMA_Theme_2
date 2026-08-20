#' @keywords internal
.onLoad <- function(libname, pkgname) {
  # Register plotly templates
  if (requireNamespace("plotly", quietly = TRUE)) {
    tryCatch({
      plotly::register_template("dma_light", dma_plotly_template_light)
      plotly::register_template("dma_dark", dma_plotly_template_dark)
    }, error = function(e) {
      # Ignore registration errors
    })
  }
  
  # Set default ggplot2 theme options
  options(
    dma_theme.default_palette = "bold",
    dma_theme.default_continuous = "blue",
    dma_theme.default_diverging = "blue_orange"
  )
  
  invisible()
}

#' @keywords internal
.onAttach <- function(libname, pkgname) {
  packageStartupMessage(
    "DMA Theme v", utils::packageVersion("dmaTheme"),
    "\nSemantic color palettes for data visualization",
    "\nhttps://dunsworth-mann.com"
  )
}