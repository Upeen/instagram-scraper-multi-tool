# Instagram Scraper - Multi-Tool Implementation

A comprehensive Instagram scraper with **5 scraping tools**, **Streamlit web UI**, and **25+ test cases**.

## ✨ Features

### 🎯 5 Scraping Tools
1. **ig-scraper-v2** (Recommended) - Selenium + BeautifulSoup
2. **Slug-Ig-Crawler** - Structured JSON output
3. **Zeeschuimer** - Firefox browser extension
4. **Instagram OSINT Tool** - Advanced analysis & proxies
5. **IG-FB-Scraper** - Visual HTML reports

### 🖥️ Web Interface
- **Streamlit UI** for easy scraping
- **Real-time progress** tracking
- **Tool comparison** dashboard
- **Results viewer** with export
- **Built-in documentation**

### 🧪 Testing
- **25+ test cases** covering all functionality
- **Unit tests** for each scraper
- **Integration tests** for workflows
- **Configuration tests**
- **Pytest fixtures** utilities

## 🚀 Quick Start

### Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Using Streamlit Web UI

```bash
streamlit run app.py
```

Open http://localhost:8501

### Using CLI

```bash
python main.py --account rajshamiofficial --format json
```

### Running Tests

```bash
pytest tests/                              # Run all tests
pytest --cov=instagram_scraper tests/      # With coverage
pytest -v tests/                           # Verbose output
```

## 📊 Test Results

✅ **25+ test cases**
- TestIgScraperV2 (5 tests)
- TestSlugCrawler (3 tests)
- TestZeeschuimer (2 tests)
- TestOSINTScraper (2 tests)
- TestIGFBScraper (2 tests)
- TestAllScrapers (4 tests)
- TestIntegration (4 tests)
- TestConfiguration (5 tests)

All tests passing ✓

## 📁 Project Structure

```
instagram_scraper/
├── config.py
├── scrapers/
│   ├── base_scraper.py
│   ├── ig_scraper_v2.py
│   ├── slug_crawler.py
│   ├── zeeschuimer_scraper.py
│   ├── osint_scraper.py
│   └── fb_scraper.py

tests/
├── conftest.py          # Fixtures
├── test_scrapers.py     # Unit tests
├── test_integration.py  # Integration tests
└── test_config.py       # Config tests

app.py                   # Streamlit UI
main.py                  # CLI
```

## 🖥️ Streamlit Web UI

**Features:**
- ✅ Tool selection (ig-scraper-v2, Slug, Zeeschuimer, OSINT, IG-FB)
- ✅ Account input and configuration
- ✅ Multi-format export (JSON, HTML)
- ✅ Real-time progress tracking
- ✅ Results viewer and downloader
- ✅ Tool comparison table
- ✅ Built-in documentation

**Usage:**
```bash
streamlit run app.py
```

## 🧪 Test Coverage

### Unit Tests
```
✅ Scraper initialization
✅ Scrape method functionality
✅ JSON export
✅ HTML report generation
✅ Scraper identification
```

### Integration Tests
```
✅ Multiple scrapers on same account
✅ Multiple accounts scraping
✅ Export format validation
✅ Complete workflows
```

### Configuration Tests
```
✅ Project directories exist
✅ Target accounts configured
✅ Configuration values valid
```

## 📊 Export Formats

- **JSON** - Structured data export
- **HTML** - Visual reports with styling
- **CSV** - Spreadsheet compatible (ready)

## 🔧 Configuration

Edit `instagram_scraper/config.py`:

```python
TARGET_ACCOUNTS = ["rajshamiofficial"]
REQUEST_DELAY = 2
PAGE_LOAD_TIMEOUT = 30
```

## 📚 Documentation

- [SETUP_GUIDE.md](SETUP_GUIDE.md) - Detailed setup
- [TESTING.md](TESTING.md) - Test running guide
- [app.py](app.py) - UI source code
- [main.py](main.py) - CLI source code

## 🔒 Legal & Ethical

⚠️ **Important:**
- Scraping may violate Instagram ToS
- Check local laws
- Use responsibly
- Respect rate limits
- Handle data ethically

## 🎯 Usage Examples

### Web UI
```bash
streamlit run app.py
# Select tool → Enter account → Export → View results
```

### CLI - Single Tool
```bash
python main.py --account rajshamiofficial --format json
```

### CLI - All Tools
```bash
python main.py --scraper all --account rajshamiofficial --format json
```

### Tests
```bash
pytest tests/test_scrapers.py -v           # Unit tests
pytest tests/test_integration.py -v        # Integration
pytest --cov=instagram_scraper tests/      # Coverage
```

## 🚀 Deployment

### Local
```bash
streamlit run app.py --server.port 8501
```

### Production
```bash
streamlit run app.py --logger.level=info
```

## 📝 Notes

- ✅ All 5 scrapers implemented
- ✅ Comprehensive test suite
- ✅ Streamlit web interface
- ✅ CLI tool included
- ✅ Full documentation
- ✅ Export capabilities

## 📄 License

Educational and research purposes only.

---

**Status:** ✅ Active & Tested  
**Tests:** 25+ passing  
**UI:** Streamlit web interface  
**Last Updated:** 2026-05-17
