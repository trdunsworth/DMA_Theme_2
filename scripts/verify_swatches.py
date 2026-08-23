#!/usr/bin/env python3
"""Pixel-level sanity checks for the generated swatch images.

This model cannot view images, so we verify them by inspecting pixel data
instead of relying on visual inspection.
"""
import json
from pathlib import Path

import matplotlib.image as mpimg
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
P = json.loads((ROOT / "palette.json").read_text())
L = P["themes"]["light"]
D = P["themes"]["dark"]


def lum(rgb):
    return float(rgb @ np.array([0.2126, 0.7152, 0.0722]))


def load(name):
    img = mpimg.imread(ASSETS / name)
    return (img[..., :3] * 255).astype(np.uint8)  # undo matplotlib's 0-1 float


def surface_region(img):
    """Central editor surface, avoiding window chrome."""
    h, w, _ = img.shape
    y0, y1 = int(h * 0.20), int(h * 0.92)
    x0, x1 = int(w * 0.10), int(w * 0.96)
    return img[y0:y1, x0:x1]


print("=== Editor previews ===")
for name, theme in (("preview-light.png", L), ("preview-dark.png", D)):
    img = load(name)
    h, w, _ = img.shape
    hexbg = theme["background"].lstrip("#")
    bg_rgb = np.array([int(hexbg[i:i + 2], 16) for i in (0, 2, 4)])
    bg = lum(bg_rgb)
    surf = surface_region(img)
    mean = lum(surf.reshape(-1, 3).mean(axis=0))
    # variation across surface => multiple syntax colors present
    per_channel_std = surf.reshape(-1, 3).std(axis=0).mean()
    print(f"{name:20s} {w}x{h}  theme_bg_mean_lum={bg:5.1f}  "
          f"surface_mean_lum={mean:5.1f}  syntax_variation={per_channel_std:5.1f}")
    assert per_channel_std > 8, f"{name}: looks flat, no syntax colors?"

print("\n=== Color scale strips (whole-image distinct color count) ===")
# Layouts have title/label bands, so sample the whole image (strided) rather
# than a single mid-row, which can land on a white label band.
for name in ("palette-primary.png", "palette-semantic.png",
             "ansi-light.png", "ansi-dark.png",
             "dv-qualitative.png", "dv-sequential.png", "dv-diverging.png"):
    img = load(name)
    h, w, _ = img.shape
    s = img[::3, ::3].reshape(-1, 3)
    uniq = len(np.unique(s, axis=0))
    print(f"{name:22s} {w}x{h}  distinct colors (strided): {uniq}")
    assert uniq >= 15, f"{name}: too uniform"

print("\nALL PIXEL CHECKS PASSED")
