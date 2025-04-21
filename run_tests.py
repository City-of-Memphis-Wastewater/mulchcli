#!/usr/bin/env python
"""
Run Tests Script

This script runs all the tests in the project using pytest, generates a code coverage report, 
and opens an HTML coverage report in the default web browser. It also saves the logs in markdown 
format under the 'tests/logs/' directory.

Usage:
1. By default, running this script will execute the tests, generate the report, and open it in the browser.
2. To run the tests in "headless" mode (without opening the HTML report automatically in the browser),
   set the environment variable `HEADLESS=true` before running the script. This can be done by running:

   For Windows:
   set HEADLESS=true && python run_tests.py

   For Mac/Linux:
   HEADLESS=true python run_tests.py

Created: 2025-04-21
Author: George Bennett, with AI assistance
"""

import subprocess
from datetime import datetime
from pathlib import Path
import webbrowser
import os

def prepend_frontmatter(log_file: Path, date_str: str):
    frontmatter = f"""---
title: Test Log
date: {date_str}
tags: [tests, pytest, coverage]
---

# Test Log - {date_str}

"""
    original_content = log_file.read_text(encoding="utf-8")
    log_file.write_text(frontmatter + original_content, encoding="utf-8")

def main():
    # Prepare paths and timestamps
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    date_str = datetime.now().strftime("%Y-%m-%d")
    log_dir = Path("tests/logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"pytest_{timestamp}.md"

    # Pytest command
    command = [
        "poetry", "run", "pytest",
        "--capture=tee-sys",
        "--log-cli-level=INFO",
        f"--log-file={log_file}",
        "--cov=mulchcli",  # adjust this to match your actual source package
        "--cov-report=term-missing",
        "--cov-report=html",  # HTML report
        "tests",
    ]

    print(f"Running pytest. Logs will be saved to {log_file}")
    subprocess.run(command)

    # Prepend Obsidian-friendly frontmatter
    prepend_frontmatter(log_file, date_str)

    # Optionally open HTML coverage report (unless headless mode is on)
    html_cov_index = Path("htmlcov/index.html")
    if html_cov_index.exists():
        html_cov_index_abs = html_cov_index.resolve()  # Convert to absolute path
        print(f"Opening coverage report: {html_cov_index_abs}")
        
        # Check if headless mode is enabled
        if not os.environ.get("HEADLESS", "False").lower() in ("true", "1", "t", "y", "yes"):
            webbrowser.open(html_cov_index_abs.as_uri())

if __name__ == "__main__":
    main()
