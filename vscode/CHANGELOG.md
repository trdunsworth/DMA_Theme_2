# Changelog

All notable changes to the **DMA Theme** VS Code extension are documented in this
file. The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [1.2.0] - 2026-08-22

### Changed
- **Light theme — WCAG AA for text.** Syntax and warning *text* colors that
  previously used the 500 stops (teal `#00B3B3`, turquoise `#00B8B8`, green
  `#00B33B`, warning `#FF9F00` / `#E88800`) now use the 700/800 stops on the
  `#F8FAFC` background (e.g. warning text → `#9E5E00`). This brings every
  essential text token to ≥ 4.5:1 contrast; the brighter 500 stops remain
  reserved for fills and large UI.
- Regenerated the packaged extension from the updated theme files.

### Fixed
- Light-theme editor-warning / git-conflict / escape *text* drift corrected to
  the warning 800 stop (`#9E5E00`).

## [1.1.0] - 2026-08-21

### Added
- Dark variant (`DMA Theme Dark`) shipped alongside the light variant.
- Brand-consistent semantic palette across both themes.

### Changed
- Softened light background to `#F8FAFC` with black body text.
- Blues/teals/turquoises/greens as the base; warm reds/oranges reserved for
  errors and warnings.

## [1.0.0] - 2026-08-21

### Added
- Initial release: `DMA Theme Light`, a semantic color theme focused on blues,
  teals, turquoises, and greens with warm error/warning colors.
