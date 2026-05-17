# Instagram Scraper - Multi-Tool Implementation

Comprehensive Instagram scraper supporting 5 open-source tools.

## Tools

1. **ig-scraper-v2** (Recommended) - Selenium + BeautifulSoup
2. **Slug-Ig-Crawler** - Structured JSON
3. **Zeeschuimer** - Browser extension
4. **Instagram OSINT Tool** - Advanced analysis
5. **IG-FB-Scraper** - HTML reports

## Quick Start

```bash
pip install -r requirements.txt
python main.py --account rajshamiofficial --format json
```

## Usage

```bash
# Basic scraping
python main.py --account username --format json

# Generate HTML report
python main.py --scraper fb --account username --format html

# Multiple accounts
python main.py --accounts account1 account2 --format json

# All tools
python main.py --scraper all --account username
```

## Output

Scraped data saved to `output/scraped_data/`

## Configuration

Edit `instagram_scraper/config.py`:

```python
TARGET_ACCOUNTS = ["rajshamiofficial"]
REQUEST_DELAY = 2
PAGE_LOAD_TIMEOUT = 30
```

## ⚠️ Legal Notice

Scraping may violate Instagram's Terms of Service. Use responsibly and check local laws.

---

For detailed setup, see SETUP_GUIDE.md