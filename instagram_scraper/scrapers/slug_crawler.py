from .base_scraper import BaseScraper

class SlugCrawler(BaseScraper):
    def scrape(self):
        self.logger.info(f"Scraping with Slug-Ig-Crawler: {self.account}")
        self.data = {"scraper": "Slug-Ig-Crawler", "account": self.account, "status": "success"}
        return self.data