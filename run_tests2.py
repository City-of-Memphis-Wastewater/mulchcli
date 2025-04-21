import pytest
import os
import webbrowser
from datetime import datetime
from pathlib import Path

# Logging configuration
import logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.FileHandler("tests/logs/pytest.log"),  # Store raw logs in this file for debugging
        logging.StreamHandler()  # Output to console as well
    ]
)

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = f"tests/logs/pytest_{timestamp}.md"

    # Run pytest with logging
    logging.info(f"Running pytest. Logs will be saved to {log_path}")
    
    result = pytest.main([
        "-v",  # Verbose output
        "--capture=tee-sys",  # Capture output
        "--log-cli-level=INFO",  # Capture logs
        "--log-file={}".format(log_path),  # Save to file
        "--log-file-level=INFO"  # Minimum log level for the log file
    ])

    if result == 0:
        logging.info("Tests passed.")
    else:
        logging.error("Some tests failed.")

    # Open coverage report if successful
    html_cov_index = Path("tests/coverage/index.html").resolve()
    if html_cov_index.exists():
        webbrowser.open(html_cov_index.as_uri())

if __name__ == "__main__":
    main()
