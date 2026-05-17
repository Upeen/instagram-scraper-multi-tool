from .base_scraper import BaseScraper

class ZeeschuimerScraper(BaseScraper):
    def scrape(self):
        self.logger.info(f"Zeeschuimer browser extension for: {self.account}")
        self.data = {"scraper": "Zeeschuimer", "account": self.account, "method": "Browser Extension"}
        return self.data