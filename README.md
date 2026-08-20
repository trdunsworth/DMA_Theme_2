# DMA Theme

A semantic color theme for editors, terminals, and Obsidian focused on blues, teals, turquoises, and greens with warm error/warning colors. Created by [Dunsworth, Mann, and Associates LLC](https://dunsworth-mann.com).

## Overview

DMA Theme provides a consistent visual language across different development environments. It features:

- **Semantic color system** — Colors have meaning (error, warning, info, success) rather than just syntax roles
- **Light and dark variants** — Defaults to light theme with softer white backgrounds and black text
- **Bold, non-pastel palette** — Deep, saturated colors for better readability and reduced eye strain
- **Cross-platform support** — VS Code, Positron, Emacs, Neovim, Kakoune, Helix, Zed, Notepad++, Ghostty, WezTerm, Cosmic Terminal, Yen, Warp, tmux, Obsidian

## Color Palette

### Primary Colors

| Color | 900 | 800 | 700 | 600 | 500 | 400 | 300 | 200 | 100 | 50 |
|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| **Blue** | `#002B5C` | `#003D7A` | `#00529E` | `#0069C0` | `#007BDB` | `#1A91E6` | `#4DA8EE` | `#8FC3F5` | `#C5DEF9` | `#E8F4FC` |
| **Teal** | `#004D4D` | `#006666` | `#007F7F` | `#009999` | `#00B3B3` | `#1ACCCC` | `#4DE5E5` | `#99F0F0` | `#CCF7F7` | `#E6FBFB` |
| **Turquoise** | `#005C5C` | `#007373` | `#008A8A` | `#00A1A1` | `#00B8B8` | `#1ACECE` | `#4DDDDD` | `#99EDED` | `#CCF6F6` | `#E6FBFB` |
| **Green** | `#004D1A` | `#006622` | `#007F2A` | `#009933` | `#00B33B` | `#1ACC4D` | `#4DD966` | `#99E599` | `#CCF0CC` | `#E6F8E6` |

### Semantic Colors

| Role | 900 | 800 | 700 | 600 | 500 (Base) | 400 | 300 | 200 | 100 | 50 |
|------|-----|-----|-----|-----|------------|-----|-----|-----|-----|-----|
| **Error** | `#7A0000` | `#9E0000` | `#C40000` | `#E80000` | `#FF1A1A` | `#FF4D4D` | `#FF7A7A` | `#FFA8A8` | `#FFD4D4` | `#FFEAEA` |
| **Warning** | `#7A4A00` | `#9E5E00` | `#C47300` | `#E88800` | `#FF9F00` | `#FFAD33` | `#FFC466` | `#FFDB99` | `#FFF0CC` | `#FFF8E6` |
| **Info** | `#003D7A` | `#00529E` | `#0069C0` | `#007BDB` | `#0091E6` | `#33A8EE` | `#66BFFF` | `#99D4FF` | `#CCE9FF` | `#E6F4FF` |
| **Success** | `#004D1A` | `#006622` | `#007F2A` | `#009933` | `#00B33B` | `#33CC5A` | `#66D97A` | `#99E599` | `#CCF0CC` | `#E6F8E6` |

### Neutral Colors

**Light Theme (Default)**
- Background: `#F8FAFC`
- Background Alt: `#F0F4F8`
- Background Elevated: `#FFFFFF`
- Foreground: `#1E282D` (near black)
- Foreground Muted: `#485C6E`
- Foreground Subtle: `#6E89A0`
- Border: `#C8D6E3`

**Dark Theme**
- Background: `#0A0F14`
- Background Alt: `#101820`
- Background Elevated: `#182430`
- Foreground: `#E0E8EF`
- Foreground Muted: `#93ABC3`
- Foreground Subtle: `#6E89A0`
- Border: `#2D4058`

## Supported Environments

### Editors
- **VS Code / Positron** — Full semantic highlighting with semanticTokenColors
- **Emacs** — Complete theme with org-mode, magit, lsp, and package support
- **Neovim** — Lua-based theme with TreeSitter, LSP, and plugin integrations
- **Kakoune** — kakrc configuration
- **Helix** — TOML theme configuration
- **Zed** — JSON theme configuration
- **Notepad++** — XML theme file

### Terminals
- **Ghostty** — Config file with full 256-color palette
- **WezTerm** — TOML theme with indexed colors
- **Cosmic Terminal** — Theme configuration
- **Yen** — Theme configuration
- **Warp** — Theme configuration
- **tmux** — Configuration with status line

### Other
- **Obsidian** — CSS theme with light/dark variants

## Installation

### VS Code / Positron
1. Open Extensions (`Ctrl+Shift+X`)
2. Search for "DMA Theme"
3. Click Install

Or install from VSIX:
```bash
code --install-extension dma-theme-1.0.0.vsix
```

### Emacs
```elisp
(add-to-list 'custom-theme-load-path "~/.emacs.d/themes/dma-theme")
(load-theme 'dma-theme-light t)  ; or 'dma-theme-dark
```

For Doom Emacs:
```elisp
(package! dma-theme :recipe (:host github :repo "dunsworth-mann-analytics/dma-theme"))
(setq doom-theme 'dma-theme-light)
```

For Spacemacs:
```elisp
dotspacemacs-themes '(dma-theme-light)
```

### Neovim
Using lazy.nvim:
```lua
{
  "dunsworth-mann-analytics/dma-theme",
  priority = 1000,
  config = function()
    require("dma_theme").setup({ variant = "light" }) -- or "dark"
  end
}
```

Using packer.nvim:
```lua
use {
  "dunsworth-mann-analytics/dma-theme",
  config = function()
    require("dma_theme").setup({ variant = "light" })
  end
}
```

### Ghostty
Copy `dma-theme-light` (or `dma-theme-dark`) to your Ghostty config directory:
```bash
cp themes/ghostty/dma-theme-light ~/.config/ghostty/themes/
```
Then add to your config:
```
theme = dma-theme-light
```

### WezTerm
Copy the theme file to your WezTerm config:
```lua
-- In wezterm.lua
local dma_theme = require('dma-theme-light') -- or dma-theme-dark
return dma_theme
```

### Obsidian
1. Copy `dma-theme.css` to your vault's `.obsidian/themes/` folder
2. Enable in Settings → Appearance → Themes → DMA Theme

### tmux
Add to your `~/.tmux.conf`:
```bash
source-file ~/.config/tmux/dma-theme-light.conf
```

## Language Support

Full semantic support for:
- Python, R, Julia, Rust, Go
- Markdown, Typst, LaTeX, Quarto
- SQL, C#, HTML, CSS, JavaScript, TypeScript
- Node, Deno, Bun, YAML, JSON, TOML

## Palettes for Data Visualization

See `palettes/python/` and `palettes/r/` for ggplot2, plotnine, and matplotlib color palettes.

## Contributing

See [GUIDELINES.md](GUIDELINES.md) for design principles and contribution guidelines.

## License

MIT License — see [LICENSE](LICENSE) for details.

## Links

- [Website](https://dunsworth-mann.com)
- [GitHub Repository](https://github.com/dunsworth-mann-analytics/dma-theme)
- [Issues](https://github.com/dunsworth-mann-analytics/dma-theme/issues)
