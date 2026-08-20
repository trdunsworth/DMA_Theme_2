# DMA Theme - Design Guidelines & Contribution Guide

## Design Philosophy

### Core Principles

1. **Semantic First** — Colors convey meaning (error, warning, info, success) not just syntax categories. A user should understand code semantics at a glance.

2. **Consistency Across Environments** — The same semantic color means the same thing whether in VS Code, Neovim, terminal, or Obsidian.

3. **Bold, Not Pastel** — Colors are saturated and purposeful. Light variants exist for backgrounds/subtle elements, but UI chrome uses strong colors.

4. **Light Theme Default** — Per requirements: black text on softer white backgrounds. Dark theme is a first-class citizen but not default.

5. **Accessibility** — All foreground/background combinations meet WCAG AA contrast ratios (4.5:1 for text, 3:1 for UI elements).

### Color Theory

#### Primary Palette: Blue-Turquoise-Green Spectrum

The primary palette spans a contiguous region of color space from blue (220°) through teal (180°) to green (140°). This creates natural harmony:

- **Blue** (`#007BDB` base) — Primary actions, links, keywords, functions
- **Teal** (`#00B3B3` base) — Types, classes, interfaces, namespaces
- **Turquoise** (`#00B8B8` base) — Attributes, decorators, annotations
- **Green** (`#00B33B` base) — Strings, success states, git additions

#### Semantic Palette: Warm for Alerts

Error/warning use warm hues (0°-30°) for maximum visual distinction from the cool primary palette:

- **Error** (`#FF1A1A` base) — Errors, deletions, critical failures
- **Warning** (`#FF9F00` base) — Warnings, modifications, deprecations
- **Info** (`#0091E6` base) — Information, hints, incoming changes
- **Success** (`#00B33B` base) — Success, additions, confirmations

#### Neutral Scale

Two neutral scales (light/dark) with 11 steps each (950-50), designed for:
- Text hierarchy (fg, fg_muted, fg_subtle)
- Background layering (bg, bg_alt, bg_elevated)
- Borders and dividers
- Selection and highlight states

### Semantic Mapping Rules

| Semantic Role | Light Theme | Dark Theme | Usage |
|---------------|-------------|------------|-------|
| Primary Action | Blue 500 | Blue 400 | Buttons, links, focus rings |
| Error | Error 600 | Error 500 | Errors, deletions, invalid |
| Warning | Warning 600 | Warning 500 | Warnings, deprecations |
| Info | Info 600 | Info 500 | Info, hints, incoming |
| Success | Success 600 | Success 500 | Success, additions |
| Background | Neutral Light 50 | Neutral Dark 950 | Main editor background |
| Surface | Neutral Light 100 | Neutral Dark 900 | Panels, sidebars |
| Elevated | White | Neutral Dark 800 | Dropdowns, modals |
| Text Primary | Neutral Dark 950 | Neutral Light 50 | Main text |
| Text Muted | Neutral Dark 500 | Neutral Light 400 | Secondary text |
| Text Subtle | Neutral Dark 300 | Neutral Light 300 | Placeholders, line numbers |
| Border | Neutral Dark 200 | Neutral Dark 600 | Dividers, input borders |

### Syntax Highlighting Semantics

| Scope | Color | Rationale |
|-------|-------|-----------|
| Comments | Neutral Subtle | Recede, italic for distinction |
| Strings | Green Dark | Data content, success-adjacent |
| Numbers | Blue Dark | Constants, precision |
| Keywords | Teal Darkest | Control flow, structure |
| Functions | Blue Dark | Actions, callable |
| Types/Classes | Teal Darker | Definitions, contracts |
| Variables | Text Primary | Default, readable |
| Parameters | Text Muted | Distinct from variables |
| Constants | Warning Darker | Immutable, attention |
| Operators | Teal Darkest | Structural |
| Punctuation | Text Muted | Structural, low emphasis |
| Tags | Teal Darkest | Markup structure |
| Attributes | Teal Dark | HTML/XML attributes |
| Regex | Warning Darker | Complex, error-prone |
| Escape | Warning Dark | Special sequences |

---

## Creating New Themes

### Process

1. **Reference `palette.json`** — Use exact color values from the master palette
2. **Map Semantically** — Don't map syntax scopes to raw colors; map to semantic roles
3. **Test Both Variants** — Ensure light and dark work in the target environment
4. **Follow Environment Conventions** — Use the target's native theme format and patterns
5. **Document Installation** — Add to README.md with clear instructions

### Required Semantic Coverage

Every theme must define colors for:

**UI Chrome**
- Background, backgroundAlt, backgroundElevated
- Foreground, foregroundMuted, foregroundSubtle
- Border, borderFocus
- Selection, selectionForeground
- Cursor
- Line numbers (active/inactive)
- Indent guides (active/inactive)
- Scrollbar (thumb, hover)
- Buttons (primary, secondary, hover)
- Inputs (background, border, foreground, placeholder)
- Dropdowns, tabs, status bar, activity bar, sidebar, title bar

**Syntax (Minimum)**
- Comment, string, number, keyword, keywordControl, storage
- Function, method, variable, parameter, property
- Type, class, interface, namespace, constant, operator, punctuation
- Bracket, tag, attribute, regex, escape, annotation, decorator
- Link, markup (heading, bold, italic, strikethrough, code, link, quote, list)

**Diff/Git**
- Added, removed, context (bg and fg)
- Git status colors (added, modified, deleted, untracked, ignored, conflicting)

**Terminal ANSI**
- 16 base colors + bright variants
- Should match semantic colors where applicable

---

## Adding Editor/Terminal Support

### File Naming Convention

```
themes/{editor}/
  dma-theme-light.{ext}    # Light variant
  dma-theme-dark.{ext}     # Dark variant
```

### VS Code / Positron / Zed (JSON)
- Use VS Code color theme schema
- Include `semanticHighlighting: true`
- Provide both `tokenColors` (TextMate) and `semanticTokenColors` (LSP)

### Emacs (Elisp)
- Use `deftheme` with `custom-theme-set-faces`
- Include `custom-theme-set-variables` for ANSI colors
- Support major packages (magit, org, lsp, company, etc.)

### Neovim (Lua)
- Structure: `palette.lua` → `highlights.lua` → `init.lua`
- Return theme table from `colors/dma_theme.lua`
- Support TreeSitter, LSP, and popular plugins

### Terminal (Ghostty, WezTerm, etc.)
- Define 16 ANSI colors + 256-color indexed palette
- Include semantic color ranges in indexed palette (indices 32-255)
- Define UI colors (scrollbar, selection, cursor, copy mode)

### Obsidian (CSS)
- Use CSS custom properties for light/dark switching
- Target `.theme-light` and `.theme-dark` classes
- Style markdown elements, code blocks, UI chrome

---

## Data Visualization Palettes

### Python (`palettes/python/`)

Structure:
```
palettes/python/
  dma_palette.py          # Core colors, exports
  ggplot2_dma.py          # scale_colour_dma(), scale_fill_dma()
  plotnine_dma.py         # plotnine integration
  matplotlib_dma.py       # ListedColormap, cycler
  seaborn_dma.py          # sns.color_palette registration
  __init__.py             # Package exports
```

### R (`palettes/r/`)

Structure:
```
palettes/r/
  dma_palette.R           # dma_colors, dma_palettes list
  ggplot2_dma.R           # scale_colour_dma(), scale_fill_dma()
  plotly_dma.R            # plotly color sequences
  zzz.R                   # .onLoad registration
```

### Palette Categories

Each palette set should include:
- **Qualitative** — Categorical data (8-12 colors, max discrimination)
- **Sequential** — Ordered data (light to dark, 9 steps)
- **Diverging** — Two-ended data (neutral center, 11 steps)
- **Semantic** — Error/Warning/Info/Success for status charts

---

## Quality Checklist

Before submitting a theme:

- [ ] Colors match `palette.json` exactly (no approximations)
- [ ] Light and dark variants both implemented
- [ ] All required semantic roles covered
- [ ] Tested in target environment
- [ ] Installation instructions added to README
- [ ] No pastel colors used for UI chrome
- [ ] Contrast ratios verified (WCAG AA minimum)
- [ ] File follows target environment conventions
- [ ] No hardcoded colors outside palette references

---

## Versioning & Releases

- Follow Semantic Versioning (MAJOR.MINOR.PATCH)
- MAJOR: Breaking color changes or semantic remapping
- MINOR: New editor/terminal support, new palette additions
- PATCH: Bug fixes, minor adjustments, documentation

### Release Process

1. Update version in `palette.json`, `package.json`, theme files
2. Update `CHANGELOG.md`
3. Create git tag `v{version}`
4. Build VS Code extension: `npm run package`
5. Publish to marketplace: `npm run publish`
6. Create GitHub release with artifacts

---

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Credit inspiration sources
- No plagiarism — reference, don't copy

---

## Resources

- [WCAG Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- [VS Code Theme Color Reference](https://code.visualstudio.com/api/references/theme-color)
- [Neovim Highlight Groups](https://neovim.io/doc/user/syntax.html#highlight-groups)
- [Emacs Face Attributes](https://www.gnu.org/software/emacs/manual/html_node/elisp/Face-Attributes.html)
- [WezTerm Color Scheme](https://wezfurlong.org/wezterm/config/lua/config/color_schemes.html)