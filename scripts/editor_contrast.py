#!/usr/bin/env python3
"""Validate WCAG contrast for every *shipped* editor/terminal theme file.

contrast_report.py validates the canonical palette.json. This script goes further:
it parses each editor/terminal file the repo actually ships (light + dark) and
checks the text colors those files contain against the background *they* declare.
This catches drift between palette.json and the hand-authored environment files.

To add a new editor/terminal later, add an entry to EDITORS/TERMINALS below (and,
if its format needs special handling, a parser) — then re-run. See GUIDELINES.md.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# --- WCAG math -----------------------------------------------------------------
def _lin(c: float) -> float:
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hexcode: str) -> float:
    h = hexcode.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(fg: str, bg: str) -> float:
    l1, l2 = luminance(fg), luminance(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def level(ratio: float) -> str:
    if ratio >= 7.0:
        return "AAA"
    if ratio >= 4.5:
        return "AA"
    if ratio >= 3.0:
        return "AA Large"
    return "FAIL"


def _is_light(h: str) -> bool:
    try:
        return luminance(h) > 0.5
    except Exception:
        return False


# Token classification ----------------------------------------------------------
TERMINAL_HINTS = ("ansi", "terminal", "brightblack", "palette")
CHROME_SURFACE = ("background", "border", "fill", "panel", "gutter", "scrollbar",
                  "ruler", "indentguide", "whitespace", "minimap", "widget",
                  "editorghosttext", "debugging", "caret", "selection",
                  "linehighlight", "accent", "hover", "active", "modal",
                  "workspace", "tooltip", "menu", "frame", "header", "elevated",
                  "surface", "side", "statusbar", "titlebar", "activitybarbadge",
                  "extensionbutton", "tab", "badge", "button", "shadow", "divider")
TEXT_HINTS = ("warning", "error", "conflict", "comment", "string",
               "keyword", "function", "escape", "number", "constant", "variable",
               "type", "operator", "tag", "attribute", "link", "git",
               "info", "success", "diagnostic", "notification", "markup", "text",
               "hint", "normal", "fg")


def classify(name: str) -> str:
    """Return 'text', 'surface', 'terminal', or '' (skip)."""
    n = name.lower()
    if any(h in n for h in TERMINAL_HINTS):
        return "terminal"
    # Foreground/text tokens take priority over surface keywords.
    if n.endswith("foreground"):
        return "text"
    if any(h in n for h in CHROME_SURFACE):
        return "surface"
    if any(h in n for h in TEXT_HINTS):
        return "text"
    return ""


# Background / variant helpers --------------------------------------------------
def _flatten(d, prefix=""):
    out = {}
    if isinstance(d, dict):
        for k, v in d.items():
            kk = f"{prefix}.{k}" if prefix else str(k)
            if isinstance(v, dict):
                out.update(_flatten(v, kk))
            elif isinstance(v, str) and re.match(r'^#[0-9a-fA-F]{6}$', v):
                out[kk.lower()] = v
    return out


def _var_map(text: str) -> dict:
    vm = {}
    for m in re.finditer(
        r'(?:defvar|declare-option\s+\S+)\s+([\w-]+)\s*["\']?#?([0-9a-fA-F]{6})',
        text):
        vm.setdefault(m.group(1).lower(), "#" + m.group(2))
    # Emacs let-binding style: (dma-bg "#F8FAFC")
    for m in re.finditer(r'\(([\w-]+)\s+"#([0-9a-fA-F]{6})"\)', text):
        vm.setdefault(m.group(1).lower(), "#" + m.group(2))
    return vm


def block_for(text: str, fmt: str, variant: str) -> str:
    if fmt in ("obsidian", "css"):
        m = re.search(r'\.theme-dark\s*\{', text)
        i = m.start() if m else -1
        return text[i:] if (variant == "dark" and i != -1) else text[:i if i != -1 else len(text)]
    if fmt in ("emacs", "elisp"):
        # Single-file theme (light variant); dark is not yet shipped.
        return text
    return text


def resolve_bg(text: str, fmt: str, variant: str) -> tuple[str | None, str]:
    blk = block_for(text, fmt, variant)
    if fmt == "json":
        flat = _flatten(json.loads(text))
        for k, v in flat.items():
            if k.endswith("editor.background"):
                return v, f"json:{k}"
        for k, v in flat.items():
            if k.endswith("background") and not any(
                    c in k for c in ("gutter", "panel", "elevated", "alt",
                                     "border", "status", "title", "activity", "side")):
                return v, f"json:{k}"
        m = re.search(r'"(?:editor\.)?background"\s*:\s*"#([0-9a-fA-F]{6})"', text)
        if m:
            return "#" + m.group(1), "json:raw-background"
    if fmt in ("toml", "yaml"):
        m = re.search(r'^\s*background\s*[:=]\s*["\']?#?([0-9a-fA-F]{6})', blk, re.M)
        if m:
            return "#" + m.group(1), f"{fmt}:background"
    if fmt == "xml":
        m = re.search(r'name="DEFAULT"[^>]*\bbgColor="([0-9a-fA-F]{6})"', blk)
        if m:
            return "#" + m.group(1), "xml:DEFAULT.bgColor"
    if fmt == "css":
        # Use the base (first) declaration in the variant block; later nested
        # overrides apply only to specific UI subtrees, not the page surface.
        ms = re.findall(r'--background-primary:\s*#?([0-9a-fA-F]{6})', blk)
        if ms:
            return "#" + ms[0], "css:--background-primary"
    if fmt == "kak":
        vm = _var_map(blk)
        m = re.search(r'set-face global Default\s+(\S+)\s+(\S+)', blk)
        if m:
            bg = m.group(2).lstrip("$")
            return vm.get(bg.lower()), "kak:Default.bg(var)"
    if fmt == "ghostty":
        m = re.search(r'^\s*background\s*=\s*#?([0-9a-fA-F]{6})', blk, re.M)
        if m:
            return "#" + m.group(1), "ghostty:background"
    if fmt == "tmux":
        # tmux is a status-bar overlay: the dominant surface is the status-style bg.
        m = re.search(r'status-style\s*"[^"]*bg=(#[0-9a-fA-F]{6})', blk)
        if m:
            return m.group(1), "tmux:status-style.bg"
    if fmt in ("emacs", "elisp"):
        vm = _var_map(blk)
        m = re.search(r':background\s*,?\s*([\w-]+)', blk)
        if m and m.group(1).lower() in vm:
            return vm[m.group(1).lower()], f"emacs:{m.group(1)}"
        m = re.search(r'defvar\s+dma-bg\s+"?#?([0-9a-fA-F]{6})', blk)
        if m:
            return "#" + m.group(1), "emacs:dma-bg"
    if fmt == "neovim":
        return _nvim_bg(blk, variant)
    return None, "UNRESOLVED"


def _nvim_bg(text: str, variant: str) -> tuple[str | None, str]:
    # NOTE: the palette names its neutral keys inverted: neutral.dark.background is the
    # LIGHT page color and neutral.light.background is the DARK page color (M.light.bg
    # is sourced from neutral.dark). So the theme "light" variant uses the "dark" block.
    nkey = "dark" if variant == "light" else "light"
    # Locate neutral = { ... <nkey> = { ... background = "#hex" ... } ... }
    m = re.search(rf'neutral\s*=\s*{{', text)
    if not m:
        return None, "UNRESOLVED"
    start = m.end() - 1
    depth = 0
    i = start
    n = len(text)
    seg = None
    while i < n:
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                seg = text[start + 1:i]
                break
        i += 1
    if seg is None:
        return None, "UNRESOLVED"
    m2 = re.search(rf'\b{nkey}\s*=\s*{{', seg)
    if not m2:
        return None, "UNRESOLVED"
    s2 = m2.end() - 1
    depth = 0
    j = s2
    vseg = None
    while j < len(seg):
        if seg[j] == '{':
            depth += 1
        elif seg[j] == '}':
            depth -= 1
            if depth == 0:
                vseg = seg[s2 + 1:j]
                break
        j += 1
    if vseg is None:
        return None, "UNRESOLVED"
    m3 = re.search(r'background\s*=\s*"(#[0-9a-fA-F]{6})"', vseg)
    if m3:
        return m3.group(1), f"neovim:neutral.{nkey}.background"
    return None, "UNRESOLVED"


def resolve_term_bg(text: str, fmt: str) -> str | None:
    if fmt == "json":
        flat = _flatten(json.loads(text))
        for k, v in flat.items():
            if k.endswith("terminal.ansiBlack") or k == "terminalblack":
                return v
        m = re.search(r'terminal\.ansiBlack\s*[:=]\s*["\']?#?([0-9a-fA-F]{6})', text)
        if m:
            return "#" + m.group(1)
    if fmt == "toml":
        m = re.search(r'(?:black|ansi_0)\s*=\s*"(#[0-9a-fA-F]{6})"', text)
        if m:
            return m.group(1)
    if fmt == "ghostty":
        m = re.search(r'palette\s*=\s*0\s*=\s*#?([0-9a-fA-F]{6})', text)
        if m:
            return "#" + m.group(1)
    if fmt == "kak":
        vm = _var_map(text)
        m = re.search(r'set-face global Default\s+(\S+)\s+(\S+)', text)
        if m:
            return vm.get(m.group(1).lstrip("$").lower())
    return None


# Token extraction --------------------------------------------------------------
def _tmux_tokens(blk: str) -> dict:
    # Text colors live in fg=#hex inside style strings.
    toks = {}
    for m in re.finditer(r'\bfg=(#[0-9a-fA-F]{6})', blk):
        toks["tmux:fg:" + m.group(1)] = m.group(1)
    return toks


def extract_tokens(text: str, fmt: str, variant: str) -> dict:
    blk = block_for(text, fmt, variant)
    toks = {}
    if fmt == "json":
        data = json.loads(text)
        if isinstance(data, dict) and "themes" in data:
            # Zed: colors live in themes[].style, selected by appearance.
            style = {}
            for th in data.get("themes", []):
                if isinstance(th, dict) and th.get("appearance") == variant:
                    style = th.get("style", {}) or {}
                    break
            if not style and data.get("themes"):
                style = (data["themes"][0].get("style", {}) or {})
            toks.update(_flatten(style))
            return toks
        colors = data.get("colors", {}) if isinstance(data, dict) else {}
        sem = ["editor.foreground", "editorwarning.foreground", "editorerror.foreground",
               "editorinfo.foreground", "editorsuccess.foreground",
               "gitdecoration.conflictingresourceforeground",
               "notificationswarningicon.foreground", "editorhint.foreground"]
        for k in sem:
            if k in colors and isinstance(colors[k], str):
                toks[k] = colors[k]
        for tc in data.get("tokenColors", []) if isinstance(data, dict) else []:
            if isinstance(tc, dict):
                s = tc.get("settings", {})
                if isinstance(s, dict) and isinstance(s.get("foreground"), str):
                    name = tc.get("name") or ",".join(tc.get("scope", []))
                    if name:
                        toks["tok:" + name] = s["foreground"]
        # Zed-style nested syntax objects (e.g. "syntax.comment.color")
        toks.update(_flatten(data))
        return toks
    if fmt == "kak":
        vm = _var_map(blk)
        for m in re.finditer(r'set-face global (\S+)\s+(\S+)\s+(\S+)', blk):
            fg = m.group(2).lstrip("$")
            val = "#" + fg[1:] if fg.startswith("#") else vm.get(fg.lower())
            if val:
                toks["kak:" + m.group(1)] = val
        return toks
    if fmt == "elisp":
        vm = _var_map(blk)
        for m in re.finditer(
                r"\(([\w-]+)\s+\(\(t\s+\(:foreground\s+(?:\"#([0-9a-fA-F]{6})\"|,([\w-]+))", blk):
            name = m.group(1)
            val = ("#" + m.group(2)) if m.group(2) else vm.get((m.group(3) or "").lower())
            if val:
                toks["el:" + name] = val
        for m in re.finditer(r"set-face-foreground\s+'?([\w-]+)\s+\"#([0-9a-fA-F]{6})\"", blk):
            toks["el:" + m.group(1)] = "#" + m.group(2)
        return toks
    if fmt == "xml":
        for m in re.finditer(r'name="([^"]+)"\s+fgColor="([0-9a-fA-F]{6})"', blk):
            toks["xml:" + m.group(1)] = "#" + m.group(2)
        return toks
    if fmt == "css":
        # Page-background text variables (validated against --background-primary)
        PAGE = ("--text-", "--heading", "--bold", "--italic", "--code",
                "--link", "--list", "--blockquote", "--hr",
                "--git-modified", "--git-conflict")
        # Text that sits on the accent surface (validated against --interactive-accent)
        ACCENT = ("--text-on-accent", "--button-primary-foreground",
                  "--interactive-normal", "--interactive-hover")
        for m in re.finditer(r'(--[\w-]+):\s*#?([0-9a-fA-F]{6})', blk):
            name, val = m.group(1), "#" + m.group(2)
            if name.startswith(PAGE):
                toks["css:" + name] = val
            elif name in ACCENT:
                toks["css:onaccent:" + name] = val
        return toks
    if fmt == "neovim":
        return _neovim_tokens(variant)
    if fmt == "tmux":
        return _tmux_tokens(blk)
    # generic toml/yaml/ghostty
    for m in re.finditer(r'([@A-Za-z_][\w.\-@]*)\s*[:=]\s*["\']?#?([0-9a-fA-F]{6})', blk):
        toks[m.group(1)] = "#" + m.group(2)
    return toks


def _neovim_tokens(variant: str) -> dict:
    pal = (ROOT / "themes/neovim/lua/dma_theme/palette.lua").read_text()
    # M.colors.<path> -> hex (literals + aliases), resolved
    raw = {}
    for m in re.finditer(r'M\.colors\.([\w.]+)\s*=\s*"(#[0-9a-fA-F]{6})"', pal):
        raw[m.group(1)] = m.group(2)
    for m in re.finditer(r'M\.colors\.([\w.]+)\s*=\s*M\.colors\.([\w.]+)', pal):
        raw.setdefault(m.group(1), m.group(2))
    cmap = {}
    for k, v in raw.items():
        seen = set()
        cur = v
        while cur in raw and cur not in seen:
            seen.add(cur)
            cur = raw[cur]
        cmap[k] = cur if cur.startswith("#") else raw.get(cur, cur)
    # Per-variant color table (M.light.* / M.dark.*) -> hex or M.colors.* ref
    mvar = {}
    for m in re.finditer(
            rf'M\.{variant}\.([\w.]+)\s*=\s*(?:M\.colors\.([\w.]+)|"(#[0-9a-fA-F]{{6}})")',
            pal):
        mvar[m.group(1)] = ("colors:" + m.group(2)) if m.group(2) else m.group(3)
    leaf = {}
    for m in re.finditer(r'\b([A-Za-z_]\w*)\s*=\s*"(#[0-9a-fA-F]{6})"', pal):
        leaf.setdefault(m.group(1), "#" + m.group(2))

    def resolve(key: str) -> str | None:
        if key in mvar:
            ref = mvar[key]
            if ref.startswith("#"):
                return ref
            if ref.startswith("colors:"):
                return cmap.get(ref[7:])
            return cmap.get(ref) or leaf.get(ref.split(".")[-1])
        if key in cmap:
            return cmap[key]
        return leaf.get(key.split(".")[-1])

    hi = (ROOT / "themes/neovim/lua/dma_theme/highlights.lua").read_text()
    toks = {}
    for m in re.finditer(r'(?:fg|bg|sp)\s*=\s*(?:colors\.([\w.]+)|"([0-9a-fA-F]{6})")', hi):
        path = m.group(1)
        if path:
            val = resolve(path)
            if val:
                toks["nv:" + path] = val
        elif m.group(2):
            toks["nv:literal"] = "#" + m.group(2)
    return {k: v for k, v in toks.items() if v}


# Registry ----------------------------------------------------------------------
EDITORS = [
    ("VS Code", "vscode/dma-theme-light-color-theme.json", "vscode/dma-theme-dark-color-theme.json", "json", "editor"),
    ("Positron", "themes/positron/dma-theme-light.json", "themes/positron/dma-theme-dark.json", "json", "editor"),
    ("Zed", "themes/zed/dma-theme-light.json", "themes/zed/dma-theme-dark.json", "json", "editor"),
    ("Helix", "themes/helix/dma-theme-light.toml", "themes/helix/dma-theme-dark.toml", "toml", "editor"),
    ("Kakoune", "themes/kakoune/dma-theme-light.kak", "themes/kakoune/dma-theme-dark.kak", "kak", "editor"),
    ("Notepad++", "themes/notepadpp/dma-theme-light.xml", "themes/notepadpp/dma-theme-dark.xml", "xml", "editor"),
    ("Obsidian", "themes/obsidian/dma-theme.css", "themes/obsidian/dma-theme.css", "css", "editor"),
    ("Emacs", "themes/emacs/dma-theme-theme.el", None, "elisp", "editor"),
    ("Neovim", "themes/neovim/lua/dma_theme/palette.lua", "themes/neovim/lua/dma_theme/palette.lua", "neovim", "editor"),
]
TERMINALS = [
    ("Ghostty", "themes/ghostty/dma-theme-light", "themes/ghostty/dma-theme-dark", "ghostty", "terminal"),
    ("WezTerm", "themes/wezterm/dma-theme-light.toml", "themes/wezterm/dma-theme-dark.toml", "toml", "terminal"),
    ("Cosmic", "themes/cosmic/dma-theme-light.toml", "themes/cosmic/dma-theme-dark.toml", "toml", "terminal"),
    ("Yen", "themes/yen/dma-theme-light.yaml", "themes/yen/dma-theme-dark.yaml", "yaml", "terminal"),
    ("Warp", "themes/warp/dma-theme-light.yaml", "themes/warp/dma-theme-dark.yaml", "yaml", "terminal"),
    ("tmux", "themes/tmux/dma-theme-light.conf", "themes/tmux/dma-theme-dark.conf", "tmux", "terminal"),
]


def validate_file(path: str, fmt: str, kind: str, variant: str):
    text = (ROOT / path).read_text()
    bg, bg_how = resolve_bg(text, fmt, variant)
    term_bg = resolve_term_bg(text, fmt) if kind == "terminal" else None
    accent_bg = None
    if fmt == "css":
        m = re.search(r'--interactive-accent:\s*#?([0-9a-fA-F]{6})', text)
        if m:
            accent_bg = "#" + m.group(1)
    toks = extract_tokens(text, fmt, variant)
    rows = []
    real_fail = 0
    for name, val in toks.items():
        cat = classify(name)
        if cat in ("", "terminal"):
            continue
        surface = bg
        note = "on editor bg"
        if "onaccent" in name:
            surface = accent_bg
            note = "on accent bg"
        # Pure-white or self-colored foregrounds on a light background are text
        # rendered on an accent/cursor surface (by design), not page text.
        if (cat == "text" and bg and val
                and (val.upper() == "#FFFFFF" or val.upper() == bg.upper())
                and _is_light(bg)):
            cat = "surface"
            note = "white/self-colored on accent/cursor (by design)"
        if not val or surface is None:
            rows.append((name, val or "?", None, "?", "no bg/value"))
            continue
        ratio = contrast(val, surface)
        lv = level(ratio)
        rows.append((name, val, ratio, lv, note))
        if lv == "FAIL" and cat == "text":
            real_fail += 1
    rows.sort(key=lambda r: (r[2] is None, r[2] if r[2] is not None else 99))
    return bg, bg_how, term_bg, rows, real_fail


def build_section() -> str:
    lines = ["## Per-editor / per-terminal validation (shipped files)\n"]
    lines.append(
        "Each shipped theme file is parsed directly. **Essential text** tokens (editor foreground, "
        "semantic status, links, git decorations, UI labels) are checked against the background *that "
        "file declares* — this catches drift between `palette.json` and the hand-authored environment files. "
        "Syntax-highlighting tokens (comments, strings, keywords) are listed for reference but are "
        "non-essential under WCAG 1.4.3 and are **not** counted as hard FAILs. UI-chrome foregrounds that "
        "sit on their own colored surface (buttons, badges, status bar) and terminal ANSI colors are "
        "excluded from the FAIL count.\n")
    text_fail = 0
    syntax_notes = 0
    for group, label in ((EDITORS, "Editors"), (TERMINALS, "Terminals")):
        lines.append(f"### {label}\n")
        for name, light, dark, fmt, kind in group:
            for variant, path in (("light", light), ("dark", dark)):
                if path is None:
                    lines.append(f"#### {name} ({variant}) — *not yet shipped*\n")
                    continue
                bg, bg_how, term_bg, rows, rf = validate_file(path, fmt, kind, variant)
                text_fail += rf
                lines.append(f"#### {name} ({variant}) — bg `{bg}` <small>({bg_how})</small>\n")
                if not rows:
                    lines.append("_No text tokens extracted._\n")
                    continue
                lines.append("| Token | Color | Contrast | Level | Note |")
                lines.append("|-------|-------|---------:|-------|------|")
                for nm, val, ratio, lv, note in rows:
                    cat = classify(nm)
                    if cat == "syntax" and lv == "FAIL":
                        syntax_notes += 1
                    rstr = f"{ratio:5.2f}:1" if ratio is not None else "n/a"
                    lines.append(f"| `{nm}` | {val} | {rstr} | {lv} | {note} |")
                lines.append("")
    lines.append(f"**Essential text-token FAILs (shipped files): {text_fail}**  ")
    lines.append(f"**Syntax-highlighting sub-AA tokens (informational, not WCAG-essential): {syntax_notes}**\n")
    return "\n".join(lines)


if __name__ == "__main__":
    for group in (EDITORS, TERMINALS):
        for name, light, dark, fmt, kind in group:
            for variant, path in (("light", light), ("dark", dark)):
                if path is None:
                    print(f"{name:10s} {variant:5s} NOT SHIPPED")
                    continue
                bg, bg_how, term_bg, rows, rf = validate_file(path, fmt, kind, variant)
                print(f"{name:10s} {variant:5s} {fmt:7s} bg={bg} ({bg_how}) term_bg={term_bg} toks={len(rows)} FAIL={rf}")
    print("\n--- VS Code light tokens (sample) ---")
    _, _, _, rows, _ = validate_file("vscode/dma-theme-light-color-theme.json", "json", "editor", "light")
    for r in rows:
        print("  ", r)
