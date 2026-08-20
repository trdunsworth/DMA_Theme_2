# DMA Theme - Task Tracker

## Project Status: In Development

---

## ✅ Completed

### Core Palette & Theme Definition
- [x] Define primary color palette (blue, teal, turquoise, green) with 10 shades each
- [x] Define semantic colors (error, warning, info, success) with 10 shades each
- [x] Define neutral colors for light and dark themes
- [x] Create semantic theme mappings for light variant
- [x] Create semantic theme mappings for dark variant
- [x] Create master `palette.json` with all colors and theme definitions

### VS Code / Positron
- [x] Light theme (`dma-theme-light-color-theme.json`)
- [x] Dark theme (`dma-theme-dark-color-theme.json`)
- [x] Package.json with metadata and publishing config
- [x] Semantic highlighting support
- [x] Full tokenColors for TextMate grammars

### Emacs
- [x] Complete theme file (`dma-theme-theme.el`) with light variant
- [x] Support for core faces, mode line, minibuffer, completion
- [x] Font-lock faces for syntax highlighting
- [x] Tree-sitter faces
- [x] Org mode, Markdown, Magit support
- [x] LSP/Flycheck/Company/Ivy/Helm/Consult/Corfu/Vertico/Marginalia support
- [x] Language-specific faces (Python, Rust, Go, C/C++, Java, SQL, R, Julia, Typescript, Web)
- [x] ANSI terminal colors

### Ghostty
- [x] Light theme (`dma-theme-light`)
- [x] Full 256-color palette with semantic color extensions

### WezTerm
- [x] Light theme (`dma-theme-light.toml`)
- [x] Dark theme (`dma-theme-dark.toml`)
- [x] Full indexed color palette (16-255)
- [x] UI colors (scrollbar, split, copy mode, quick select, launcher)

### Neovim
- [x] Lua-based theme structure
- [x] Palette module with light/dark variants
- [x] Comprehensive highlights module (500+ highlight groups)
- [x] TreeSitter/LSP/Diagnostic highlights
- [x] Plugin integrations (Telescope, NvimTree, WhichKey, Lazy, Mason, Noice, Notify, Snacks, Gitsigns, IndentBlankline, Mini, Leap, Flash, Cmp, BlinkCmp, RainbowDelimiter)

---

## 🔄 In Progress

### Documentation
- [x] README.md
- [ ] TODO.md (this file)
- [ ] GUIDELINES.md
- [ ] CHANGELOG.md
- [ ] LICENSE

---

## 📋 Pending - High Priority

### Editor Themes (Missing)

#### Helix
- [ ] `dma-theme-light.toml` — Light theme
- [ ] `dma-theme-dark.toml` — Dark theme

#### Kakoune
- [ ] `dma-theme-light.kak` — Light theme
- [ ] `dma-theme-dark.kak` — Dark theme

#### Notepad++
- [ ] `dma-theme-light.xml` — Light theme
- [ ] `dma-theme-dark.xml` — Dark theme

#### Obsidian
- [ ] `dma-theme.css` — CSS theme with light/dark variants using CSS variables

#### Positron
- [ ] `dma-theme-light.json` — Light theme (VS Code compatible)
- [ ] `dma-theme-dark.json` — Dark theme (VS Code compatible)

#### Zed
- [ ] `dma-theme-light.json` — Light theme
- [ ] `dma-theme-dark.json` — Dark theme

### Terminal Themes (Missing)

#### Cosmic Terminal
- [ ] `dma-theme-light.toml` — Light theme
- [ ] `dma-theme-dark.toml` — Dark theme

#### Yen
- [ ] `dma-theme-light.yaml` — Light theme
- [ ] `dma-theme-dark.yaml` — Dark theme

#### Warp
- [ ] `dma-theme-light.yaml` — Light theme
- [ ] `dma-theme-dark.yaml` — Dark theme

#### tmux
- [ ] `dma-theme-light.conf` — Light theme with status line
- [ ] `dma-theme-dark.conf` — Dark theme with status line

### Existing Themes - Missing Variants

#### Ghostty
- [ ] `dma-theme-dark` — Dark theme variant

---

## 📋 Pending - Medium Priority

### Data Visualization Palettes

#### Python (`palettes/python/`)
- [ ] `dma_palette.py` — Core palette module with color constants
- [ ] `ggplot2_dma.py` — ggplot2 scale functions (`scale_color_dma`, `scale_fill_dma`)
- [ ] `plotnine_dma.py` — plotnine integration
- [ ] `matplotlib_dma.py` — Matplotlib colormaps and cyclers
- [ ] `seaborn_dma.py` — Seaborn palette registration
- [ ] `demo_python.ipynb` — Jupyter notebook demonstrating palettes

#### R (`palettes/r/`)
- [ ] `dma_palette.R` — Core palette vectors and functions
- [ ] `ggplot2_dma.R` — ggplot2 scale functions (`scale_colour_dma`, `scale_fill_dma`)
- [ ] `plotly_dma.R` — Plotly color sequences
- [ ] `demo_r.Rmd` — R Markdown demo document

---

## 📋 Pending - Low Priority

### VS Code Extension
- [ ] Create extension icon (`icon.png`)
- [ ] Publish to VS Code Marketplace
- [ ] Add to Open VSX Registry

### Repository Setup
- [ ] Initialize git repository
- [ ] Create GitHub repository
- [ ] Set up GitHub Actions for CI/CD
- [ ] Configure dependabot
- [ ] Add contribution templates (issue, PR)

### Additional Features
- [ ] Create theme preview images for each editor
- [ ] Add support for more editors (Sublime Text, Nova, Lapce, etc.)
- [ ] Create web-based theme preview
- [ ] Generate color contrast report (WCAG compliance)
- [ ] Create npm package for web/CSS variables

---

## 🎨 Design Decisions Tracked

| Decision | Date | Rationale |
|----------|------|-----------|
| Default to light theme | 2024-08-20 | Per requirements: "Text should be black, background a softer white" |
| No pastels | 2024-08-20 | Per requirements: "bolder and darker colours where practical" |
| Semantic color system | 2024-08-20 | Per requirements: "semantic theme, using other semantic themes as examples" |
| Blue/teal/turquoise/green primary | 2024-08-20 | Per requirements: "focus on blues, teals, turquoises, and greens" |
| Warm red/orange for errors/warnings | 2024-08-20 | Per requirements: "Warm colours like reds and oranges should be used for errors and warnings" |

---

## 📝 Notes

- All themes should use the exact colors from `palette.json` for consistency
- When creating new themes, reference existing implementations (VS Code, Emacs, Neovim) for semantic mapping patterns
- Test each theme in its target environment before marking complete
- Update CHANGELOG.md with each release