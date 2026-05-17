#!/usr/bin/env python3
import argparse
import logging
from pathlib import Path
from instagram_scraper.config import OUTPUT_DIR, LOGS_DIR, TARGET_ACCOUNTS
from instagram_scraper.scrapers.ig_scraper_v2 import IgScraperV2
from instagram_scraper.scrapers.slug_crawler import SlugCrawler
from instagram_scraper.scrapers.zeeschuimer_scraper import ZeeschuimerScraper
from instagram_scraper.scrapers.osint_scraper import OSINTScraper
from instagram_scraper.scrapers.fb_scraper import IGFBScraper

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def run_scraper(scraper_name, account, format_type, **kwargs):
    scrapers = {
        "ig-scraper-v2": IgScraperV2,
        "slug": SlugCrawler,
        "zeeschuimer": ZeeschuimerScraper,
        "osint": OSINTScraper,
        "fb": IGFBScraper,
    }
    scraper_class = scrapers.get(scraper_name)
    if not scraper_class:
        return False
    if scraper_name == "osint":
        scraper = scraper_class(account, kwargs.get("output_dir"), use_proxies=kwargs.get("proxies"))
    else:
        scraper = scraper_class(account, kwargs.get("output_dir"))
    scraper.scrape()
    if format_type in ["json", "all"]:
        scraper.save_json()
    if format_type in ["html", "all"]:
        scraper.save_html_report()
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Instagram Scraper")
    parser.add_argument("--scraper", default="ig-scraper-v2")
    parser.add_argument("--account", type=str)
    parser.add_argument("--accounts", nargs="+")
    parser.add_argument("--format", default="json")
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--proxies", action="store_true")
    args = parser.parse_args()
    accounts = args.account and [args.account] or (args.accounts or TARGET_ACCOUNTS)
    scrapers = [args.scraper] if args.scraper != "all" else ["ig-scraper-v2", "slug", "zeeschuimer", "osint", "fb"]
    for account in accounts:
        for scraper in scrapers:
            run_scraper(scraper, account, args.format, output_dir=args.output_dir, proxies=args.proxies)
    print(f"\nOutput saved to: {args.output_dir}")
