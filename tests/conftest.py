import pytest
from pathlib import Path
from instagram_scraper.config import OUTPUT_DIR, LOGS_DIR
from instagram_scraper.scrapers.ig_scraper_v2 import IgScraperV2
from instagram_scraper.scrapers.slug_crawler import SlugCrawler
from instagram_scraper.scrapers.zeeschuimer_scraper import ZeeschuimerScraper
from instagram_scraper.scrapers.osint_scraper import OSINTScraper
from instagram_scraper.scrapers.fb_scraper import IGFBScraper


@pytest.fixture
def test_account():
    return "rajshamiofficial"


@pytest.fixture
def test_output_dir(tmp_path):
    output_dir = tmp_path / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


@pytest.fixture
def ig_scraper_v2(test_account, test_output_dir):
    return IgScraperV2(test_account, test_output_dir)


@pytest.fixture
def slug_crawler(test_account, test_output_dir):
    return SlugCrawler(test_account, test_output_dir)


@pytest.fixture
def zeeschuimer(test_account, test_output_dir):
    return ZeeschuimerScraper(test_account, test_output_dir)


@pytest.fixture
def osint_scraper(test_account, test_output_dir):
    return OSINTScraper(test_account, test_output_dir, use_proxies=False)


@pytest.fixture
def fb_scraper(test_account, test_output_dir):
    return IGFBScraper(test_account, test_output_dir)


@pytest.fixture(params=[IgScraperV2, SlugCrawler, ZeeschuimerScraper, OSINTScraper, IGFBScraper])
def all_scrapers(request, test_account, test_output_dir):
    scraper_class = request.param
    if scraper_class == OSINTScraper:
        return scraper_class(test_account, test_output_dir, use_proxies=False)
    return scraper_class(test_account, test_output_dir)
