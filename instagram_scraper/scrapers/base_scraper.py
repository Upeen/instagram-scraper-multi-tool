import logging
import json
from abc import ABC, abstractmethod
from pathlib import Path
from datetime import datetime

class BaseScraper(ABC):
    def __init__(self, account: str, output_dir: Path):
        self.account = account
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.logger = self._setup_logger()
        self.data = {}

    def _setup_logger(self):
        logger = logging.getLogger(self.__class__.__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger

    @abstractmethod
    def scrape(self):
        pass

    def save_json(self, filename: str = None) -> Path:
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{self.account}_{self.__class__.__name__}_{timestamp}.json"
        filepath = self.output_dir / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
        self.logger.info(f"JSON saved to {filepath}")
        return filepath

    def save_html_report(self, filename: str = None) -> Path:
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{self.account}_{self.__class__.__name__}_{timestamp}.html"
        filepath = self.output_dir / filename
        html = f"""<!DOCTYPE html><html><head><title>Report</title></head><body><h1>@{self.account}</h1></body></html>"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        self.logger.info(f"HTML saved to {filepath}")
        return filepath