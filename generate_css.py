"""Generate CSS custom properties from palette.toml.

Run:  python generate_css.py > palette.css
Then @import or paste the variables into the site's stylesheet so the
website and the Python figures share one color definition.
"""

import tomllib
from pathlib import Path

toml_path = Path(__file__).resolve().parent / "palette.toml"
with open(toml_path, "rb") as f:
    p = tomllib.load(f)

light = p["neutral"]
dark = p["neutral_dark"]
accent = p["accent"]["primary"]

lines = [":root {"]
lines.append(f"    --background: {light['paper']};")
lines.append(f"    --foreground: {light['ink']};")
lines.append(f"    --foreground-secondary: {light['gray']};")
lines.append(f"    --accent: {accent};")
lines.append("}")
lines.append("")
lines.append("@media (prefers-color-scheme: dark) {")
lines.append("    :root {")
lines.append(f"        --background: {dark['paper']};")
lines.append(f"        --foreground: {dark['ink']};")
lines.append(f"        --foreground-secondary: {dark['gray']};")
lines.append(f"        --accent: {accent};")
lines.append("    }")
lines.append("}")

print("\n".join(lines))
