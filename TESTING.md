# Running Tests

## Run all tests
pytest tests/

## Run specific test file
pytest tests/test_scrapers.py

## Run with coverage
pytest --cov=instagram_scraper tests/

## Run with verbose output
pytest -v tests/

## Run a specific test
pytest tests/test_scrapers.py::TestIgScraperV2::test_scrape_returns_dict

## Run tests matching a pattern
pytest -k "test_save" tests/

## Run with markers
pytest -m unit tests/
