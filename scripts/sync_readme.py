# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "jinja2>=3.1.6",
# ]
# ///

import argparse
import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined


def main() -> None:
    parser = argparse.ArgumentParser(description="Render README.md from a Jinja2 template and projects JSON.")
    parser.add_argument("--json", required=True, type=Path, help="Path to projects.json")
    parser.add_argument("--template", required=True, type=Path, help="Path to README.md.j2")
    parser.add_argument("--output", default=Path("README.md"), type=Path, help="Output path (default: README.md)")
    args = parser.parse_args()

    data = json.loads(args.json.read_text())

    env = Environment(
        loader=FileSystemLoader(str(args.template.parent)),
        undefined=StrictUndefined,
        keep_trailing_newline=True,
    )
    template = env.get_template(args.template.name)
    rendered = template.render(**data)

    args.output.write_text(rendered)
    print(f"Written to {args.output}")


if __name__ == "__main__":
    main()
