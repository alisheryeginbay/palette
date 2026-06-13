"""yeginbay_palette — personal color palette and matplotlib style.

Colors are defined once in palette.toml (the single source of truth) and
read at runtime here, so Python figures and the website CSS never drift.

Typical use:

    import yeginbay_palette as yp
    yp.apply_style()                 # activates mplstyle + categorical cycle
    p = yp.load()
    ax.bar(x, y, color=p.accent("primary"))
"""

from __future__ import annotations

import tomllib
from pathlib import Path
from dataclasses import dataclass

_HERE = Path(__file__).resolve().parent
_TOML = _HERE / "palette.toml"
_STYLE = _HERE / "mystyle.mplstyle"


@dataclass
class Palette:
    """Loaded palette. Access colors by group + name, or get the raw dict."""

    data: dict

    def neutral(self, name: str) -> str:
        return self.data["neutral"][name]

    def accent(self, name: str = "primary") -> str:
        return self.data["accent"][name]

    def categorical(self) -> list[str]:
        return list(self.data["categorical"]["colors"])

    def __getitem__(self, key: str):
        return self.data[key]


def load() -> Palette:
    """Read palette.toml and return a Palette object."""
    with open(_TOML, "rb") as f:
        return Palette(tomllib.load(f))


def apply_style() -> Palette:
    """Activate the mplstyle and set matplotlib's color cycle from the
    categorical palette. Returns the loaded Palette for convenience."""
    import matplotlib.pyplot as plt
    from cycler import cycler

    p = load()
    plt.style.use(_STYLE)
    plt.rcParams["axes.prop_cycle"] = cycler(color=p.categorical())
    plt.rcParams["mathtext.fontset"] = "cm"
    return p
