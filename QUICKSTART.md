# Quick Start Guide

## 🎯 Get Started in 5 Minutes

### Step 1: Clone & Setup (2 min)

```bash
# Clone repository
git clone https://github.com/Upeen/instagram-scraper-multi-tool.git
cd instagram-scraper-multi-tool

# Create virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Run Web UI (1 min)

```bash
streamlit run app.py
```

Then open: **http://localhost:8501** in your browser

### Step 3: Scrape an Account (1 min)

1. Select **ig-scraper-v2** (recommended)
2. Enter account: **rajshamiofficial**
3. Select format: **JSON**
4. Click **🚀 Start Scraping**
5. View results in **Results** tab

### Step 4: Run Tests (1 min)

```bash
pytest tests/ -v
```

---

## 🖥️ Web UI Guide

### Tabs Overview

#### 1️⃣ Scraper Tab
- **Select Tool:** Choose from 5 scrapers
- **Account Name:** Enter Instagram username
- **Export Format:** JSON, HTML, or both
- **Start Button:** Begin scraping

```
Select Tool:        Tool Info:
✅ ig-scraper-v2   🟢 Recommended
□ Slug-Ig-Crawler  For beginners
□ Zeeschuimer      
□ OSINT Tool       
□ IG-FB-Scraper    
□ All Tools        
```

#### 2️⃣ Results Tab
- **View** scraped data in JSON
- **Download** files
- **Browse** previous results

#### 3️⃣ Comparison Tab
- **Side-by-side** tool comparison
- **Speed & Ease** ratings
- **Use case** recommendations

#### 4️⃣ Documentation Tab
- **Quick Start**
- **Tool Information**
- **Tips & Tricks**

---

## 💻 CLI Commands

### Basic Scraping
```bash
python main.py --account rajshamiofficial --format json
```

### Multiple Accounts
```bash
python main.py --accounts account1 account2 account3 --format json
```

### Use Specific Tool
```bash
python main.py --scraper slug --account username --format json
```

### Use All Tools
```bash
python main.py --scraper all --account username
```

### With HTML Report
```bash
python main.py --account username --format html
```

### With Proxies (OSINT only)
```bash
python main.py --scraper osint --account username --proxies
```

---

## 🧪 Testing

### Run All Tests
```bash
pytest tests/
```

### Verbose Output
```bash
pytest tests/ -v
```

### With Coverage Report
```bash
pytest --cov=instagram_scraper tests/
```

### Run Specific Test
```bash
pytest tests/test_scrapers.py::TestIgScraperV2 -v
```

### Quick Test
```bash
pytest tests/ -q
```

---

## 📊 Available Scrapers

| Tool | Best For | Command |
|------|----------|---------|
| **ig-scraper-v2** | Beginners ⭐⭐⭐⭐⭐ | `--scraper ig-scraper-v2` |
| **Slug-Ig-Crawler** | Advanced 🟡🟡🟡 | `--scraper slug` |
| **Zeeschuimer** | Researchers 🔵🔵🔵🔵 | `--scraper zeeschuimer` |
| **OSINT Tool** | Investigators 🔴🔴🔴🔴 | `--scraper osint --proxies` |
| **IG-FB-Scraper** | Reports 🟣🟣🟣 | `--scraper fb --format html` |

---

## 📁 Output Files

After scraping, files are saved to:

```
output/scraped_data/
├── rajshamiofficial_IgScraperV2_20260517_153000.json
├── rajshamiofficial_IgScraperV2_20260517_153000.html
├── rajshamiofficial_SlugCrawler_20260517_153015.json
└── ...
```

### JSON Structure
```json
{
  "scraper": "ig-scraper-v2",
  "account": "rajshamiofficial",
  "account_info": {
    "username": "rajshamiofficial",
    "full_name": "Raj Shami",
    "follower_count": 150000,
    ...
  },
  "status": "success"
}
```

---

## ⚙️ Configuration

Edit `instagram_scraper/config.py`:

```python
TARGET_ACCOUNTS = ["rajshamiofficial", "other_account"]
REQUEST_DELAY = 2              # Seconds between requests
PAGE_LOAD_TIMEOUT = 30         # Browser timeout
```

---

## 🔧 Troubleshooting

### Issue: Module not found
```bash
pip install -r requirements.txt
```

### Issue: Chrome driver not found
```bash
python -c "from webdriver_manager.chrome import ChromeDriverManager; ChromeDriverManager().install()"
```

### Issue: Streamlit not opening
```bash
streamlit run app.py --logger.level=debug
```

### Issue: Tests failing
```bash
pytest tests/ -v --tb=short
```

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| [README.md](README.md) | Project overview |
| [SETUP_GUIDE.md](SETUP_GUIDE.md) | Detailed setup |
| [TESTING.md](TESTING.md) | Test guide |
| [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) | Completion summary |
| [TEST_DOCUMENTATION.md](TEST_DOCUMENTATION.md) | Test details |

---

## 🎯 Common Tasks

### Task 1: Scrape Account Profile
```bash
# Web UI
streamlit run app.py
# Then select ig-scraper-v2, enter account, click scrape

# CLI
python main.py --account rajshamiofficial --format json
```

### Task 2: Compare Multiple Tools
```bash
# Web UI
streamlit run app.py
# Then select "All Tools" and click scrape

# CLI
python main.py --scraper all --account username
```

### Task 3: Generate HTML Report
```bash
# Web UI
streamlit run app.py
# Select any tool, choose HTML format

# CLI
python main.py --scraper fb --account username --format html
```

### Task 4: Run Tests
```bash
pytest tests/ -v
```

### Task 5: Check Test Coverage
```bash
pytest --cov=instagram_scraper tests/
```

---

## 🚀 Performance Tips

1. **Use delays** - Increase REQUEST_DELAY to avoid rate limiting
2. **Use proxies** - Enable for multiple account scraping
3. **Start small** - Test with one account first
4. **Monitor logs** - Check `logs/scraper.log` for issues
5. **Export frequently** - Save results often

---

## ⚠️ Important Notes

- ✅ Always check **Instagram's Terms of Service**
- ✅ Verify scraping is **legal in your jurisdiction**
- ✅ Use **rate limiting** to avoid detection
- ✅ Handle **personal data responsibly**
- ✅ Consider **ethics** of data collection

---

## 📞 Help & Support

### Check Logs
```bash
cat logs/scraper.log
```

### Enable Debug Mode
```bash
streamlit run app.py --logger.level=debug
```

### Test Configuration
```bash
pytest tests/test_config.py -v
```

### View Available Options
```bash
python main.py --help
```

---

## 🎓 Learn More

- [Streamlit Docs](https://docs.streamlit.io/)
- [Pytest Docs](https://docs.pytest.org/)
- [Selenium Docs](https://selenium.dev/)
- [BeautifulSoup Guide](https://www.crummy.com/software/BeautifulSoup/)

---

## 🎉 You're Ready!

```
✅ Installation complete
✅ Dependencies installed
✅ Tests passing
✅ Web UI ready
✅ CLI configured

Happy scraping! 🚀
```

Start with: `streamlit run app.py`

---

**Need Help?**
1. Check this guide
2. Read SETUP_GUIDE.md
3. Review TEST_DOCUMENTATION.md
4. Check logs/scraper.log
5. Create GitHub issue

**Questions?** See PROJECT_SUMMARY.md for detailed info.
