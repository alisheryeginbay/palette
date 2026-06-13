# palette

Personal color palette and matplotlib style. Colors are defined once in
[`palette.toml`](palette.toml) — the single source of truth — and consumed by
both Python figures and the website's CSS, so they can never drift.

## Python (figures)

Install from GitHub:

```bash
uv pip install "git+https://github.com/alisheryeginbay/palette.git"
```

Use:

```python
import yeginbay_palette as yp

p = yp.apply_style()          # activates the mplstyle + categorical color cycle
ax.bar(x, y, color=p.accent("primary"))
ink   = p.neutral("ink")
cats  = p.categorical()       # colorblind-safe sequence, led by ink + mauve
```

`apply_style()` sets the matplotlib style and derives the color cycle from
`palette.toml` at runtime (the cycle is **not** duplicated in the style file).

## Website (CSS)

```bash
python generate_css.py > palette.css
```

Emits `:root` custom properties (light + dark) matching the site's existing
`--foreground` / `--background` / `--foreground-secondary` names, plus `--accent`.

## Structure

- `neutral` — ink, paper, gray, gray_light (light mode)
- `neutral_dark` — dark-mode equivalents (used by the CSS generator)
- `accent.primary` — dusty mauve, the "look here" color
- `categorical.colors` — N-category sequence; ink + mauve first, then Bang
  Wong's colorblind-safe palette

## Note on duplication

The neutral hexes (ink/gray) also appear in `mystyle.mplstyle` because a
matplotlib style file can't read TOML. These are stable site colors; if you
change them, update both. Categorical/accent colors live only in the TOML.
