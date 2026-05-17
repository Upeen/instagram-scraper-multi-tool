from .base_scraper import BaseScraper

class IGFBScraper(BaseScraper):
    def scrape(self):
        self.logger.info(f"IG-FB-Scraper for: {self.account}")
        self.data = {"scraper": "IG-FB-Scraper", "account": self.account, "report_ready": True}
        return self.data