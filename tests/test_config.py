import pytest
from pathlib import Path
from instagram_scraper.config import PROJECT_ROOT, OUTPUT_DIR, LOGS_DIR, TARGET_ACCOUNTS


class TestConfiguration:
    def test_project_root_exists(self):
        assert PROJECT_ROOT.exists()
        assert PROJECT_ROOT.is_dir()

    def test_output_dir_created(self):
        assert OUTPUT_DIR.exists()
        assert OUTPUT_DIR.is_dir()

    def test_logs_dir_created(self):
        assert LOGS_DIR.exists()
        assert LOGS_DIR.is_dir()

    def test_target_accounts_configured(self):
        assert isinstance(TARGET_ACCOUNTS, list)
        assert len(TARGET_ACCOUNTS) > 0

    def test_target_accounts_contain_strings(self):
        for account in TARGET_ACCOUNTS:
            assert isinstance(account, str)
            assert len(account) > 0
