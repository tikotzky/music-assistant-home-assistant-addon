#!/usr/bin/env python3
"""
Turn a checkout of the upstream add-on repository into the 24six add-on repository.

The 24six repository is upstream's content with the identity from ``24six/overlay.json``
written over it: the add-on's name, slug, panel title and container image, the repository
name and URL, a fork notice in the README, and the upstream add-ons this fork does not ship
removed. The add-on version is kept as it is unless ``--version`` says otherwise, because
it names a container image that only exists once the server repository has released it.

Running the script twice is a no-op the second time, so it is safe on an already converted
tree as well as on a fresh upstream one.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path
from urllib.parse import quote

OVERLAY_FILE = Path(__file__).with_name("overlay.json")
FORK_NOTICE_MARKER = "24six fork"


class OverlayError(RuntimeError):
    """Report an upstream layout the overlay does not know how to handle."""


def apply_overlay(root: Path, overlay: dict[str, object], version: str | None) -> None:
    """
    Rewrite the repository at ``root`` so it carries the 24six identity.

    :param root: Repository working directory holding upstream's content.
    :param overlay: Parsed ``overlay.json``.
    :param version: Add-on version to write, or ``None`` to keep the current one.
    """
    addon_folder = root / str(overlay["addon_folder"])
    _rewrite_addon_config(addon_folder / "config.yaml", _mapping(overlay["addon"]), version)
    _rewrite_repository(root / "repository.json", _mapping(overlay["repository"]))
    _rewrite_readme(root / "README.md", overlay)
    for folder in _sequence(overlay["dropped_folders"]):
        shutil.rmtree(root / folder, ignore_errors=True)


def main() -> int:
    """Run the command-line interface."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=OVERLAY_FILE.parents[1])
    parser.add_argument("--overlay", type=Path, default=OVERLAY_FILE)
    parser.add_argument("--version", help="add-on version to write; defaults to the current one")
    args = parser.parse_args()
    overlay = json.loads(args.overlay.read_text(encoding="utf-8"))
    try:
        apply_overlay(args.root, overlay, args.version)
    except OverlayError as err:
        print(err, file=sys.stderr)
        return 1
    return 0


def _rewrite_addon_config(config_path: Path, addon: dict[str, str], version: str | None) -> None:
    config = config_path.read_text(encoding="utf-8")
    fields = dict(addon)
    if version is not None:
        fields["version"] = version
    for key, value in fields.items():
        config = _replace_yaml_field(config, key, value, config_path)
    config_path.write_text(config, encoding="utf-8")


def _replace_yaml_field(config: str, key: str, value: str, config_path: Path) -> str:
    # a duplicate key would leave the stale one in effect, so rewrite nothing unless it is unique
    config, replacements = re.subn(
        rf"^{re.escape(key)}: .+$",
        f"{key}: {value}",
        config,
        flags=re.MULTILINE,
    )
    if replacements != 1:
        raise OverlayError(f"Expected exactly one top-level '{key}' field in {config_path}")
    return config


def _rewrite_repository(repository_path: Path, repository: dict[str, str]) -> None:
    current = json.loads(repository_path.read_text(encoding="utf-8"))
    repository_path.write_text(
        json.dumps({**current, **repository}, indent=4) + "\n",
        encoding="utf-8",
    )


def _rewrite_readme(readme_path: Path, overlay: dict[str, object]) -> None:
    upstream_url = str(overlay["upstream_repository_url"])
    fork_url = str(_mapping(overlay["repository"])["url"])
    readme = readme_path.read_text(encoding="utf-8")
    readme = readme.replace(quote(upstream_url, safe=""), quote(fork_url, safe=""))
    readme = readme.replace(upstream_url, fork_url)
    if FORK_NOTICE_MARKER not in readme:
        readme = _insert_fork_notice(readme, overlay, readme_path)
    readme_path.write_text(readme, encoding="utf-8")


def _insert_fork_notice(readme: str, overlay: dict[str, object], readme_path: Path) -> str:
    addon_name = _mapping(overlay["addon"])["name"]
    notice = (
        f"> **{FORK_NOTICE_MARKER}.** This repository is the 24six fork of the official\n"
        f"> [Music Assistant add-on repository]({overlay['upstream_repository_url']}).\n"
        f"> It ships *{addon_name}*, built from\n"
        f"> [the 24six fork of the server]({overlay['server_repository_url']}) which adds the\n"
        "> 24six music provider. Versions follow upstream with a `-24six.N` suffix.\n"
    )
    lines = readme.splitlines(keepends=True)
    for index, line in enumerate(lines):
        # the title is a setext heading: the notice goes right below its underline
        if re.fullmatch(r"=+\s*", line):
            if index > 0 and lines[index - 1].strip() == "Music Assistant":
                lines[index - 1] = f"{addon_name}\n"
            return "".join([*lines[: index + 1], "\n", notice, *lines[index + 1 :]])
    raise OverlayError(f"No setext title found in {readme_path} to place the fork notice under")


def _mapping(value: object) -> dict[str, str]:
    if not isinstance(value, dict):
        raise OverlayError(f"Expected a mapping in overlay.json, got {type(value).__name__}")
    return {str(key): str(item) for key, item in value.items()}


def _sequence(value: object) -> list[str]:
    if not isinstance(value, list):
        raise OverlayError(f"Expected a list in overlay.json, got {type(value).__name__}")
    return [str(item) for item in value]


if __name__ == "__main__":
    sys.exit(main())
