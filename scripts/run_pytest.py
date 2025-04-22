"""Run pytest."""

import pytest


def main():
    """Main entry point."""
    pytest.main(
        [
            "--junitxml=reports/pytest-report.xml",
            "--cov=vg_nde_sdk",
            "--cov-report=xml:reports/coverage.xml",
            "--cov-report=html:reports/htmlcov",
            "--cov-report=term-missing",
            "--typeguard-packages=vg_nde_sdk",
            "tests",
        ]
    )
