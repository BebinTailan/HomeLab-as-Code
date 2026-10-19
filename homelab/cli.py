"""Command-line interface for HomeLab-as-Code."""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from homelab import __version__


def build_parser() -> argparse.ArgumentParser:
    """Create the top-level argument parser."""
    parser = argparse.ArgumentParser(prog="homelab", description="Describe a lab network once and generate its documentation, router, firewall and VPN configs.")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point. Returns a process exit code."""
    parser = build_parser()
    parser.parse_args(argv)
    parser.print_help()
    return 0
