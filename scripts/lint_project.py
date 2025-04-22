"""Project linting."""

import sys
from pathlib import Path

import flake8.main.application as flake
import toml
from mypy.main import main as mypy


def run_flake8() -> None:
    """Execute flake8 linter on the project."""
    print("Running flake8 ...")
    app = flake.Application()
    app.run(".")


def run_mypy() -> None:
    """Execute type checking on the project."""
    print("Running mypy ...")
    mypy(args=["."], stdout=sys.stdout, stderr=sys.stderr, clean_exit=True)


def run_version_check() -> None:
    """Execute version consistency check."""
    print("Running version consistency check ...")

    from vg_nde_sdk import __version__ as vg_nde_sdk_version

    print(" * vg_nde_sdk.__version__ = ", vg_nde_sdk_version)

    pyproject_toml = Path(__file__).parent.parent / "pyproject.toml"
    pkg_version = toml.load(pyproject_toml)["project"]["version"]
    print(" * project.version = ", pkg_version)

    if str(vg_nde_sdk_version) != str(pkg_version):
        print("ERROR: Version numbers do not match!")
        sys.exit(1)


def main():
    """Main entry point."""
    # Important: Run mypy as last because it does sys.exit() and would
    # prevent the other linters from running.
    linters = [run_version_check, run_flake8, run_mypy]
    for linter in linters:
        linter()
        sys.stdout.flush()
        sys.stderr.flush()
