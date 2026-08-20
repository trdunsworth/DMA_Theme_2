# Changelog

All notable changes to DMA Theme will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-08-20

### Added
- Initial release of DMA Theme
- Core semantic color palette (blue, teal, turquoise, green + error, warning, info, success)
- Light and dark theme variants (light is default)
- Editor themes:
  - VS Code / Positron (full semantic highlighting)
  - Emacs (complete with org, magit, lsp, package support)
  - Neovim (Lua-based with TreeSitter, LSP, plugin integrations)
  - Kakoune (light and dark)
  - Helix (light and dark)
  - Zed (light and dark)
  - Notepad++ (light and dark)
- Terminal themes:
  - Ghostty (light and dark)
  - WezTerm (light and dark)
  - Cosmic Terminal (light and dark)
  - Yen (light and dark)
  - Warp (light and dark)
  - tmux (light and dark with status line)
- Obsidian CSS theme (light and dark with CSS variables)
- Python palettes for matplotlib, seaborn, plotnine/ggplot2
- R palettes for ggplot2 and plotly
- Comprehensive documentation (README, GUIDELINES, TODO)

### Design Decisions
- Default to light theme (black text on softer white background)
- Bold, saturated colors (no pastels)
- Semantic color system (colors have meaning)
- Blue/teal/turquoise/green primary palette
- Warm red/orange for errors and warnings

## [Unreleased]

### Planned
- VS Code Marketplace publication
- Sublime Text theme
- Nova theme
- Lapce theme
- Additional language-specific optimizations
- Web-based theme preview
- WCAG contrast compliance report