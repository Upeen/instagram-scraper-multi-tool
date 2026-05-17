import streamlit as st
import pandas as pd
import json
from pathlib import Path
from datetime import datetime
from instagram_scraper.config import OUTPUT_DIR, TARGET_ACCOUNTS
from instagram_scraper.scrapers.ig_scraper_v2 import IgScraperV2
from instagram_scraper.scrapers.slug_crawler import SlugCrawler
from instagram_scraper.scrapers.zeeschuimer_scraper import ZeeschuimerScraper
from instagram_scraper.scrapers.osint_scraper import OSINTScraper
from instagram_scraper.scrapers.fb_scraper import IGFBScraper

st.set_page_config(page_title="Instagram Scraper", layout="wide")

def load_scraped_data():
    """Load previously scraped data from output directory"""
    data_files = list(OUTPUT_DIR.glob("*.json"))
    return sorted(data_files, key=lambda x: x.stat().st_mtime, reverse=True)

def main():
    st.title("📸 Instagram Scraper Multi-Tool")
    st.markdown("*Scrape Instagram data using multiple open-source tools*")
    
    tabs = st.tabs(["Scraper", "Results", "Comparison", "Documentation"])
    
    with tabs[0]:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("🔧 Scraper Configuration")
            
            scraper_type = st.selectbox(
                "Select Scraper Tool",
                ["ig-scraper-v2", "Slug-Ig-Crawler", "Zeeschuimer", "OSINT Tool", "IG-FB-Scraper", "All Tools"]
            )
            
            account = st.text_input(
                "Instagram Account",
                value="rajshamiofficial",
                help="Enter username without @ symbol"
            )
            
            export_format = st.multiselect(
                "Export Format",
                ["JSON", "HTML", "CSV"],
                default=["JSON"]
            )
        
        with col2:
            st.subheader("ℹ️ Tool Info")
            tool_info = {
                "ig-scraper-v2": "🟢 Selenium + BeautifulSoup. Recommended.",
                "Slug-Ig-Crawler": "🟡 Structured data. Advanced users.",
                "Zeeschuimer": "🔵 Firefox extension. No-code.",
                "OSINT Tool": "🔴 Proxy support. Advanced.",
                "IG-FB-Scraper": "🟣 HTML reports. Presentations."
            }
            st.info(tool_info.get(scraper_type, ""))
        
        if st.button("🚀 Start Scraping", use_container_width=True):
            with st.spinner("⏳ Scraping in progress..."):
                scrapers_to_run = [scraper_type] if scraper_type != "All Tools" else \
                                  ["ig-scraper-v2", "Slug-Ig-Crawler", "Zeeschuimer", "OSINT Tool", "IG-FB-Scraper"]
                
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for idx, scraper in enumerate(scrapers_to_run):
                    status_text.info(f"🔄 Running {scraper} for @{account}...")
                    
                    try:
                        scraper_map = {
                            "ig-scraper-v2": IgScraperV2,
                            "Slug-Ig-Crawler": SlugCrawler,
                            "Zeeschuimer": ZeeschuimerScraper,
                            "OSINT Tool": OSINTScraper,
                            "IG-FB-Scraper": IGFBScraper
                        }
                        
                        if scraper == "OSINT Tool":
                            scraper_obj = scraper_map[scraper](account, OUTPUT_DIR, use_proxies=False)
                        else:
                            scraper_obj = scraper_map[scraper](account, OUTPUT_DIR)
                        
                        data = scraper_obj.scrape()
                        
                        if "JSON" in export_format:
                            scraper_obj.save_json()
                        if "HTML" in export_format:
                            scraper_obj.save_html_report()
                        
                        st.success(f"✅ {scraper} completed successfully")
                    except Exception as e:
                        st.error(f"❌ {scraper} failed: {str(e)}")
                    
                    progress_bar.progress((idx + 1) / len(scrapers_to_run))
                
                status_text.success("✨ All scrapers completed!")
    
    with tabs[1]:
        st.subheader("📊 Scraped Data")
        
        data_files = load_scraped_data()
        if data_files:
            selected_file = st.selectbox(
                "Select scraped data file",
                options=[f.name for f in data_files]
            )
            
            if selected_file:
                file_path = OUTPUT_DIR / selected_file
                
                if file_path.suffix == ".json":
                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    
                    col1, col2 = st.columns([1, 2])
                    
                    with col1:
                        st.write("**Metadata**")
                        st.write(f"Scraper: {data.get('scraper', 'N/A')}")
                        st.write(f"Account: @{data.get('account', 'N/A')}")
                        st.write(f"Status: {data.get('status', 'N/A')}")
                    
                    with col2:
                        st.write("**Raw Data**")
                        st.json(data)
        else:
            st.info("No scraped data available. Run a scraper first.")
    
    with tabs[2]:
        st.subheader("📈 Tool Comparison")
        
        comparison_data = {
            "Tool": ["ig-scraper-v2", "Slug-Ig-Crawler", "Zeeschuimer", "OSINT Tool", "IG-FB-Scraper"],
            "Method": ["Selenium", "Selenium", "Extension", "API", "Selenium"],
            "Speed": ["⭐⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐"],
            "Ease": ["⭐⭐⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐⭐", "⭐⭐", "⭐⭐⭐"]
        }
        
        df = pd.DataFrame(comparison_data)
        st.dataframe(df, use_container_width=True)
    
    with tabs[3]:
        st.subheader("📚 Documentation")
        st.markdown("""
        ### Quick Start
        1. Select a tool
        2. Enter account name
        3. Click scrape
        4. View results
        """)

if __name__ == "__main__":
    main()
