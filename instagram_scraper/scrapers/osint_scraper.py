from .base_scraper import BaseScraper

class OSINTScraper(BaseScraper):
    def __init__(self, account: str, output_dir, use_proxies: bool = False):
        super().__init__(account, output_dir)
        self.use_proxies = use_proxies

    def scrape(self):
        self.logger.info(f"OSINT scraper for: {self.account}")
        self.data = {"scraper": "Instagram OSINT", "account": self.account, "proxies": self.use_proxies}
        return self.data