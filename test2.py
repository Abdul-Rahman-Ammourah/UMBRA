#!/usr/bin/env python3

import sys
import re

# cloudscraper bypasses Cloudflare and similar protections
import cloudscraper

# Pattern to match email addresses
EMAIL_REGEX = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def scrape_email_from_website(url: str) -> list:
    """
    Fetch the HTML of `url` using cloudscraper to bypass protections,
    then extract all email addresses.
    """
    # Create a scraper that mimics a modern browser
    scraper = cloudscraper.create_scraper(
        browser={
            'custom': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/125.0.0.0 Safari/537.36'
            )
        }
    )

    try:
        response = scraper.get(url, timeout=20)
        response.raise_for_status()
    except Exception as e:
        print(f"[!] Failed to GET {url}: {e}")
        return []

    html = response.text
    # Find all unique email addresses
    emails = set(EMAIL_REGEX.findall(html))
    return sorted(emails)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <url1> [<url2> ...]")
        sys.exit(1)

    for url in sys.argv[1:]:
        result = scrape_email_from_website(url)
        print(f"{url} -> {result}")


if __name__ == "__main__":
    main()
