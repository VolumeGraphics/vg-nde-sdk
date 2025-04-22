"""Run security audit."""

import configparser
import logging
import sys

from pip_audit._cli import audit

logging.basicConfig()
logger = logging.getLogger("pip-audit")


def main():
    """Main entry point."""
    config = configparser.ConfigParser()
    config["Config"] = {"Ignore": ""}
    config.read(".sec-audit")

    cfg_ignored_vulns = config["Config"]["Ignore"]
    ignored_vulns = []
    if cfg_ignored_vulns:
        ignored_vulns = cfg_ignored_vulns.split(",")
        for vuln in ignored_vulns:
            vuln = vuln.strip()
            if vuln == "":
                continue

            logger.warning(f"(Config) Ignoring vulnerability: {vuln}")

            # hack to not have to re-implement argument parsing from pip-audit
            sys.argv.append("--ignore-vuln")
            sys.argv.append(vuln)

    # audit calls sys.exit() with the right exit code
    # thus no need to return anything here
    audit()


if __name__ == "__main__":
    main()
