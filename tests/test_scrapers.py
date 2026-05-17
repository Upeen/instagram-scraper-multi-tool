import pytest
import json
from pathlib import Path
from instagram_scraper.scrapers.ig_scraper_v2 import IgScraperV2
from instagram_scraper.scrapers.slug_crawler import SlugCrawler
from instagram_scraper.scrapers.zeeschuimer_scraper import ZeeschuimerScraper
from instagram_scraper.scrapers.osint_scraper import OSINTScraper
from instagram_scraper.scrapers.fb_scraper import IGFBScraper


class TestIgScraperV2:
    def test_initialization(self, ig_scraper_v2):
        assert ig_scraper_v2.account == "rajshamiofficial"
        assert ig_scraper_v2.output_dir.exists()
        assert ig_scraper_v2.logger is not None

    def test_scrape_returns_dict(self, ig_scraper_v2):
        result = ig_scraper_v2.scrape()
        assert isinstance(result, dict)
        assert "scraper" in result
        assert "account" in result
        assert "status" in result

    def test_scraper_name(self, ig_scraper_v2):
        result = ig_scraper_v2.scrape()
        assert result["scraper"] == "ig-scraper-v2"

    def test_save_json(self, ig_scraper_v2):
        ig_scraper_v2.scrape()
        json_path = ig_scraper_v2.save_json()
        assert json_path.exists()
        assert json_path.suffix == ".json"
        with open(json_path, "r") as f:
            data = json.load(f)
        assert "scraper" in data

    def test_save_html_report(self, ig_scraper_v2):
        ig_scraper_v2.scrape()
        html_path = ig_scraper_v2.save_html_report()
        assert html_path.exists()
        assert html_path.suffix == ".html"


class TestSlugCrawler:
    def test_initialization(self, slug_crawler):
        assert slug_crawler.account == "rajshamiofficial"
        assert slug_crawler.output_dir.exists()

    def test_scrape_returns_dict(self, slug_crawler):
        result = slug_crawler.scrape()
        assert isinstance(result, dict)
        assert result["scraper"] == "Slug-Ig-Crawler"

    def test_json_export(self, slug_crawler):
        slug_crawler.scrape()
        json_path = slug_crawler.save_json()
        assert json_path.exists()


class TestZeeschuimer:
    def test_initialization(self, zeeschuimer):
        assert zeeschuimer.account == "rajshamiofficial"

    def test_scrape_returns_dict(self, zeeschuimer):
        result = zeeschuimer.scrape()
        assert isinstance(result, dict)
        assert result["scraper"] == "Zeeschuimer"

    def test_manual_setup_status(self, zeeschuimer):
        result = zeeschuimer.scrape()
        assert result["status"] == "manual_setup_required"


class TestOSINTScraper:
    def test_initialization(self, osint_scraper):
        assert osint_scraper.account == "rajshamiofficial"
        assert osint_scraper.use_proxies == False

    def test_scrape_returns_dict(self, osint_scraper):
        result = osint_scraper.scrape()
        assert isinstance(result, dict)
        assert result["scraper"] == "Instagram OSINT Tool"


class TestIGFBScraper:
    def test_initialization(self, fb_scraper):
        assert fb_scraper.account == "rajshamiofficial"

    def test_scrape_returns_dict(self, fb_scraper):
        result = fb_scraper.scrape()
        assert isinstance(result, dict)
        assert result["scraper"] == "IG-FB-Scraper"


class TestAllScrapers:
    def test_all_scrapers_have_logger(self, all_scrapers):
        assert all_scrapers.logger is not None
        assert all_scrapers.logger.name == all_scrapers.__class__.__name__

    def test_all_scrapers_scrape_method(self, all_scrapers):
        result = all_scrapers.scrape()
        assert isinstance(result, dict)
        assert "account" in result

    def test_all_scrapers_save_json(self, all_scrapers):
        all_scrapers.scrape()
        json_path = all_scrapers.save_json()
        assert json_path.exists()
        assert json_path.suffix == ".json"

    def test_all_scrapers_save_html(self, all_scrapers):
        all_scrapers.scrape()
        html_path = all_scrapers.save_html_report()
        assert html_path.exists()
        assert html_path.suffix == ".html"
