from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output" / "scraped_data"
LOGS_DIR = PROJECT_ROOT / "logs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

TARGET_ACCOUNTS = ["rajshamiofficial"]
REQUEST_DELAY = 2
PAGE_LOAD_TIMEOUT = 30