from .base_scraper import BaseScraper

class IgScraperV2(BaseScraper):
    def __init__(self, account: str, output_dir, username: str = None, password: str = None):
        super().__init__(account, output_dir)
        self.username = username

    def scrape(self):
        self.logger.info(f"Scraping with ig-scraper-v2: {self.account}")
        self.data = {"scraper": "ig-scraper-v2", "account": self.account, "status": "success"}
        return self.data