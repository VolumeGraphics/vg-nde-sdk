"""Code formatting."""

import os
import sys

from isort.main import main as isort_main


def run_black(check_only: bool = False) -> None:
    """Run black."""
    print("Running black ...")
    check = "--check" if check_only else ""
    os.system("black " + check + " .")  # noqa


def run_isort(check_only: bool = False) -> None:
    """Run isort to sort the imports."""
    print("Running isort ...")
    args = ["--check-only", "."] if check_only else ["."]
    isort_main(args)


def execute_formatters(check_only: bool = False):
    """Call all formatters."""
    formatters = [run_isort, run_black]
    for formatter in formatters:
        formatter(check_only)
        sys.stdout.flush()
        sys.stderr.flush()


def main_check():
    """Format-check entry point."""
    execute_formatters(check_only=True)


def main():
    """Main entry point."""
    execute_formatters(check_only=False)
