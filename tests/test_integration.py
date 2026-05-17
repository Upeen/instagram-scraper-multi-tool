import pytest
import json
from pathlib import Path
from instagram_scraper.scrapers.ig_scraper_v2 import IgScraperV2
from instagram_scraper.scrapers.slug_crawler import SlugCrawler
from instagram_scraper.scrapers.osint_scraper import OSINTScraper


class TestScrappersIntegration:
    def test_multiple_scrapers_same_account(self, test_account, test_output_dir):
        scrapers = [
            IgScraperV2(test_account, test_output_dir),
            SlugCrawler(test_account, test_output_dir),
            OSINTScraper(test_account, test_output_dir),
        ]
        
        results = []
        for scraper in scrapers:
            result = scraper.scrape()
            results.append(result)
            assert result["account"] == test_account
        
        assert len(results) == 3

    def test_export_all_formats(self, ig_scraper_v2):
        ig_scraper_v2.scrape()
        json_path = ig_scraper_v2.save_json()
        html_path = ig_scraper_v2.save_html_report()
        
        assert json_path.exists()
        assert html_path.exists()


class TestWorkflow:
    def test_complete_scraping_workflow(self, test_account, test_output_dir):
        scraper = IgScraperV2(test_account, test_output_dir)
        
        result = scraper.scrape()
        assert result["status"] == "success"
        
        json_path = scraper.save_json()
        assert json_path.exists()
        
        html_path = scraper.save_html_report()
        assert html_path.exists()
