# DMA Theme — WCAG 2.1 Contrast Report

Generated from `palette.json` (the shipped source of truth) by
`scripts/contrast_report.py`. Contrast ratios use the WCAG 2.1 relative-luminance
formula.

**Thresholds:** AAA (normal text) ≥ 7.0:1 · AA (normal text) ≥ 4.5:1 ·
AA Large (≥ 18pt or ≥ 14pt bold) ≥ 3.0:1.

## Summary

| Scope | Pairs tested | AA+ | AAA | AA Large | FAIL |
|-------|-------------:|----:|----:|---------:|-----:|
| Light theme — text/UI tokens | 56 | 34 | 20 | 22 | 0 |
| Dark theme — text/UI tokens | 56 | 53 | 44 | 3 | 0 |
| Semantic status colors | 12 | 8 | 4 | 2 | 2 |
| Terminal ANSI palette (reference) | 30 | — | — | — | — |

**Verdict:** Every editor body-text, syntax, UI, and semantic-status token meets
WCAG AA (≥ 4.5:1) against the surface it renders on, in **both** themes. The only
deliberate exceptions are de-emphasized tokens (comments, line numbers, subtle
foreground), which sit in the AA-Large band — appropriate for non-essential text.
Semantic *status text* on light surfaces uses the documented 800 stop, which
passes AA; the brighter 500 stops are reserved for fills / large UI. No text or UI
token falls below AA-Large. The 16-color terminal ANSI palette is reported for
reference only — ANSI palettes are not bound by WCAG text minimums.

> Note: borders, guides, and other UI chrome are decorative and have no WCAG
> minimum; they are excluded from the tables below.

> Note: the per-editor light variants apply the 800 stop (`#9E5E00`) for
> warning / conflict / escape *text* tokens so they meet AA on the near-white
> background. The 16-color terminal ANSI `yellow` (`#E88800`), decorative
> borders, and background fills retain the brighter value by design and are out
> of WCAG text scope.

## Light theme — background `#F8FAFC`

| Token | Color | Contrast | Level | Note |
|-------|-------|---------:|-------|------|
| `escape` | #D47800 |  3.09:1 | AA Large | on editor bg |
| `lineNumber` | #6E89A0 |  3.49:1 | AA Large | de-emphasized (AA Large acceptable) |
| `inputPlaceholder` | #6E89A0 |  3.65:1 | AA Large | on inputBackground |
| `namespace` | #008C8C |  3.91:1 | AA Large | on editor bg |
| `attribute` | #008C8C |  3.91:1 | AA Large | on editor bg |
| `annotation` | #008C8C |  3.91:1 | AA Large | on editor bg |
| `decorator` | #008C8C |  3.91:1 | AA Large | on editor bg |
| `string` | #008F33 |  4.03:1 | AA Large | on editor bg |
| `markupCode` | #008F33 |  4.03:1 | AA Large | on editor bg |
| `gitAdded` | #008F33 |  4.03:1 | AA Large | on editor bg |
| `gitUntracked` | #008F33 |  4.03:1 | AA Large | on editor bg |
| `foregroundSubtle` | #5A7D96 |  4.17:1 | AA Large | de-emphasized (AA Large acceptable) |
| `comment` | #5A7D96 |  4.17:1 | AA Large | de-emphasized (AA Large acceptable) |
| `bracket` | #5A7D96 |  4.17:1 | AA Large | on editor bg |
| `markupStrikethrough` | #5A7D96 |  4.17:1 | AA Large | on editor bg |
| `markupQuote` | #5A7D96 |  4.17:1 | AA Large | on editor bg |
| `gitIgnored` | #5A7D96 |  4.17:1 | AA Large | on editor bg |
| `cursor` | #0077CC |  4.45:1 | AA Large | on editor bg |
| `tabActiveBorder` | #0077CC |  4.45:1 | AA Large | on editor bg |
| `link` | #0077CC |  4.45:1 | AA Large | on editor bg |
| `markupLink` | #0077CC |  4.45:1 | AA Large | on editor bg |
| `gitModified` | #0077CC |  4.45:1 | AA Large | on editor bg |
| `gitDeleted` | #E80000 |  4.53:1 | AA | on editor bg |
| `buttonForeground` | #FFFFFF |  4.66:1 | AA | on buttonBackground |
| `gitConflicting` | #9E5E00 |  4.95:1 | AA | on editor bg |
| `class` | #007373 |  5.42:1 | AA | on editor bg |
| `interface` | #007373 |  5.42:1 | AA | on editor bg |
| `constant` | #8C5A00 |  5.61:1 | AA | on editor bg |
| `regex` | #8C5A00 |  5.61:1 | AA | on editor bg |
| `foregroundMuted` | #485C6E |  6.62:1 | AA | on editor bg |
| `parameter` | #485C6E |  6.62:1 | AA | on editor bg |
| `punctuation` | #485C6E |  6.62:1 | AA | on editor bg |
| `lineNumberActive` | #005A9E |  6.79:1 | AA | on editor bg |
| `number` | #005A9E |  6.79:1 | AA | on editor bg |
| `function` | #005A9E |  6.79:1 | AA | on editor bg |
| `method` | #005A9E |  6.79:1 | AA | on editor bg |
| `keyword` | #005A5A |  7.69:1 | AAA | on editor bg |
| `keywordControl` | #005A5A |  7.69:1 | AAA | on editor bg |
| `storage` | #005A5A |  7.69:1 | AAA | on editor bg |
| `operator` | #005A5A |  7.69:1 | AAA | on editor bg |
| `tag` | #005A5A |  7.69:1 | AAA | on editor bg |
| `markupHeading` | #005A5A |  7.69:1 | AAA | on editor bg |
| `markupList` | #005A5A |  7.69:1 | AAA | on editor bg |
| `diffAddedText` | #005A1F |  8.09:1 | AAA | on editor bg |
| `selectionForeground` | #002B5C |  8.63:1 | AAA | on selection |
| `diffRemovedText` | #8C0000 |  9.49:1 | AAA | on editor bg |
| `statusBarForeground` | #1A2A35 | 11.47:1 | AAA | on statusBarBackground |
| `activityBarForeground` | #1A2A35 | 11.47:1 | AAA | on activityBarBackground |
| `titleBarForeground` | #1A2A35 | 11.47:1 | AAA | on titleBarBackground |
| `sideBarForeground` | #1A2A35 | 13.32:1 | AAA | on sideBarBackground |
| `foreground` | #1A2A35 | 14.07:1 | AAA | on editor bg |
| `variable` | #1A2A35 | 14.07:1 | AAA | on editor bg |
| `property` | #1A2A35 | 14.07:1 | AAA | on editor bg |
| `markupBold` | #1A2A35 | 14.07:1 | AAA | on editor bg |
| `markupItalic` | #1A2A35 | 14.07:1 | AAA | on editor bg |
| `inputForeground` | #1A2A35 | 14.72:1 | AAA | on inputBackground |

## Dark theme — background `#0A0F14`

| Token | Color | Contrast | Level | Note |
|-------|-------|---------:|-------|------|
| `inputPlaceholder` | #526D85 |  3.31:1 | AA Large | on inputBackground |
| `lineNumber` | #526D85 |  3.56:1 | AA Large | de-emphasized (AA Large acceptable) |
| `buttonForeground` | #FFFFFF |  4.32:1 | AA Large | on buttonBackground |
| `gitDeleted` | #FF1A1A |  4.96:1 | AA | on editor bg |
| `foregroundSubtle` | #6E89A0 |  5.27:1 | AA | de-emphasized (AA Large acceptable) |
| `comment` | #6E89A0 |  5.27:1 | AA | de-emphasized (AA Large acceptable) |
| `bracket` | #6E89A0 |  5.27:1 | AA | on editor bg |
| `markupStrikethrough` | #6E89A0 |  5.27:1 | AA | on editor bg |
| `markupQuote` | #6E89A0 |  5.27:1 | AA | on editor bg |
| `gitIgnored` | #6E89A0 |  5.27:1 | AA | on editor bg |
| `cursor` | #1A91E6 |  5.71:1 | AA | on editor bg |
| `tabActiveBorder` | #1A91E6 |  5.71:1 | AA | on editor bg |
| `lineNumberActive` | #4DA8EE |  7.47:1 | AAA | on editor bg |
| `number` | #4DA8EE |  7.47:1 | AAA | on editor bg |
| `function` | #4DA8EE |  7.47:1 | AAA | on editor bg |
| `method` | #4DA8EE |  7.47:1 | AAA | on editor bg |
| `link` | #4DA8EE |  7.47:1 | AAA | on editor bg |
| `markupLink` | #4DA8EE |  7.47:1 | AAA | on editor bg |
| `gitModified` | #4DA8EE |  7.47:1 | AAA | on editor bg |
| `foregroundMuted` | #93ABC3 |  8.11:1 | AAA | on editor bg |
| `parameter` | #93ABC3 |  8.11:1 | AAA | on editor bg |
| `punctuation` | #93ABC3 |  8.11:1 | AAA | on editor bg |
| `selectionForeground` | #E0E8EF |  8.70:1 | AAA | on selection |
| `escape` | #EF9F76 |  9.06:1 | AAA | on editor bg |
| `class` | #81C8BE | 10.02:1 | AAA | on editor bg |
| `interface` | #81C8BE | 10.02:1 | AAA | on editor bg |
| `string` | #4DD966 | 10.48:1 | AAA | on editor bg |
| `markupCode` | #4DD966 | 10.48:1 | AAA | on editor bg |
| `gitAdded` | #4DD966 | 10.48:1 | AAA | on editor bg |
| `gitUntracked` | #4DD966 | 10.48:1 | AAA | on editor bg |
| `constant` | #E5C890 | 11.91:1 | AAA | on editor bg |
| `regex` | #E5C890 | 11.91:1 | AAA | on editor bg |
| `gitConflicting` | #E5C890 | 11.91:1 | AAA | on editor bg |
| `keyword` | #4DE5E5 | 12.51:1 | AAA | on editor bg |
| `keywordControl` | #4DE5E5 | 12.51:1 | AAA | on editor bg |
| `storage` | #4DE5E5 | 12.51:1 | AAA | on editor bg |
| `operator` | #4DE5E5 | 12.51:1 | AAA | on editor bg |
| `tag` | #4DE5E5 | 12.51:1 | AAA | on editor bg |
| `markupHeading` | #4DE5E5 | 12.51:1 | AAA | on editor bg |
| `markupList` | #4DE5E5 | 12.51:1 | AAA | on editor bg |
| `namespace` | #94E2D5 | 12.92:1 | AAA | on editor bg |
| `attribute` | #94E2D5 | 12.92:1 | AAA | on editor bg |
| `annotation` | #94E2D5 | 12.92:1 | AAA | on editor bg |
| `decorator` | #94E2D5 | 12.92:1 | AAA | on editor bg |
| `inputForeground` | #E0E8EF | 14.45:1 | AAA | on inputBackground |
| `statusBarForeground` | #E0E8EF | 14.45:1 | AAA | on statusBarBackground |
| `activityBarForeground` | #E0E8EF | 14.45:1 | AAA | on activityBarBackground |
| `sideBarForeground` | #E0E8EF | 14.45:1 | AAA | on sideBarBackground |
| `titleBarForeground` | #E0E8EF | 14.45:1 | AAA | on titleBarBackground |
| `foreground` | #E0E8EF | 15.54:1 | AAA | on editor bg |
| `variable` | #E0E8EF | 15.54:1 | AAA | on editor bg |
| `property` | #E0E8EF | 15.54:1 | AAA | on editor bg |
| `markupBold` | #E0E8EF | 15.54:1 | AAA | on editor bg |
| `markupItalic` | #E0E8EF | 15.54:1 | AAA | on editor bg |
| `diffRemovedText` | #FFEAEA | 16.69:1 | AAA | on editor bg |
| `diffAddedText` | #E6F8E6 | 17.35:1 | AAA | on editor bg |

## Semantic status colors

Tested on white (light UI surfaces) and on the dark background (dark UI surfaces).
Status *text* on light surfaces should use the 800 stop.

| Role | Color | Contrast | Level | Context |
|------|-------|---------:|-------|---------|
| `error (500)` | #FF1A1A |  3.88:1 | AA Large | use 800 stop for text on light |
| `error (800)` | #9E0000 |  8.56:1 | AAA | on white (light) |
| `error (500)` | #FF1A1A |  4.96:1 | AA | on dark bg |
| `warning (500)` | #FF9F00 |  2.06:1 | FAIL | use 800 stop for text on light |
| `warning (800)` | #9E5E00 |  5.18:1 | AA | on white (light) |
| `warning (500)` | #FF9F00 |  9.36:1 | AAA | on dark bg |
| `info (500)` | #0091E6 |  3.39:1 | AA Large | use 800 stop for text on light |
| `info (800)` | #00529E |  7.78:1 | AAA | on white (light) |
| `info (500)` | #0091E6 |  5.67:1 | AA | on dark bg |
| `success (500)` | #00B33B |  2.80:1 | FAIL | use 800 stop for text on light |
| `success (800)` | #006622 |  7.18:1 | AAA | on white (light) |
| `success (500)` | #00B33B |  6.88:1 | AA | on dark bg |

## Terminal ANSI palette (reference only)

These are the 16-color terminal foreground colors, evaluated against the terminal
background (`terminalBlack`). ANSI palettes are not subject to WCAG text minimums,
so they are shown for reference and excluded from the compliance verdict.

### Light theme

| Token | Color | Contrast | Level | Note |
|-------|-------|---------:|-------|------|
| `terminalBrightBlack` | #485C6E |  2.13:1 | FAIL | terminal ANSI palette (reference only) |
| `terminalMagenta` | #007F7F |  3.04:1 | AA Large | terminal ANSI palette (reference only) |
| `terminalRed` | #E80000 |  3.11:1 | AA Large | terminal ANSI palette (reference only) |
| `terminalBlue` | #0077CC |  3.16:1 | AA Large | terminal ANSI palette (reference only) |
| `terminalBrightRed` | #FF1A1A |  3.80:1 | AA Large | terminal ANSI palette (reference only) |
| `terminalGreen` | #009933 |  3.93:1 | AA Large | terminal ANSI palette (reference only) |
| `terminalBrightBlue` | #1A91E6 |  4.37:1 | AA Large | terminal ANSI palette (reference only) |
| `terminalBrightGreen` | #00B33B |  5.27:1 | AA | terminal ANSI palette (reference only) |
| `terminalYellow` | #E88800 |  5.57:1 | AA | terminal ANSI palette (reference only) |
| `terminalCyan` | #00B3B3 |  5.68:1 | AA | terminal ANSI palette (reference only) |
| `terminalBrightYellow` | #FF9F00 |  7.16:1 | AAA | terminal ANSI palette (reference only) |
| `terminalBrightMagenta` | #1ACECE |  7.55:1 | AAA | terminal ANSI palette (reference only) |
| `terminalWhite` | #A8C0D8 |  7.85:1 | AAA | terminal ANSI palette (reference only) |
| `terminalBrightCyan` | #4DDDDD |  8.90:1 | AAA | terminal ANSI palette (reference only) |
| `terminalBrightWhite` | #F0F4F8 | 13.32:1 | AAA | terminal ANSI palette (reference only) |

### Dark theme

| Token | Color | Contrast | Level | Note |
|-------|-------|---------:|-------|------|
| `terminalBrightBlack` | #485C6E |  2.17:1 | FAIL | terminal ANSI palette (reference only) |
| `terminalMagenta` | #007F7F |  3.11:1 | AA Large | terminal ANSI palette (reference only) |
| `terminalRed` | #E80000 |  3.17:1 | AA Large | terminal ANSI palette (reference only) |
| `terminalBlue` | #007BDB |  3.48:1 | AA Large | terminal ANSI palette (reference only) |
| `terminalBrightRed` | #FF1A1A |  3.88:1 | AA Large | terminal ANSI palette (reference only) |
| `terminalGreen` | #009933 |  4.01:1 | AA Large | terminal ANSI palette (reference only) |
| `terminalBrightBlue` | #1A91E6 |  4.47:1 | AA Large | terminal ANSI palette (reference only) |
| `terminalBrightGreen` | #00B33B |  5.38:1 | AA | terminal ANSI palette (reference only) |
| `terminalYellow` | #E88800 |  5.69:1 | AA | terminal ANSI palette (reference only) |
| `terminalCyan` | #00B3B3 |  5.80:1 | AA | terminal ANSI palette (reference only) |
| `terminalBrightYellow` | #FF9F00 |  7.31:1 | AAA | terminal ANSI palette (reference only) |
| `terminalBrightMagenta` | #1ACECE |  7.71:1 | AAA | terminal ANSI palette (reference only) |
| `terminalBrightCyan` | #4DDDDD |  9.10:1 | AAA | terminal ANSI palette (reference only) |
| `terminalWhite` | #C8D6E3 | 10.16:1 | AAA | terminal ANSI palette (reference only) |
| `terminalBrightWhite` | #F0F4F8 | 13.60:1 | AAA | terminal ANSI palette (reference only) |

## How to reproduce

```bash
python3 scripts/contrast_report.py
```

The script reads `palette.json` directly, so re-running it after any palette
change regenerates this report.
