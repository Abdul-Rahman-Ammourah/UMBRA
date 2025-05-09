#!/usr/bin/env python3

import re
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

EMAIL_REGEX = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')

def extract_emails_from_text(text: str) -> set:
    return set(EMAIL_REGEX.findall(text))

def extract_emails_from_mailto(page) -> set:
    emails = set()
    for element in page.query_selector_all("a[href^='mailto:']"):
        href = element.get_attribute("href")
        if href:
            emails.add(href.replace("mailto:", "").strip())
    return emails

def scrape_emails(url: str) -> list:
    found_emails = set()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0.0.0 Safari/537.36"
            ),
            ignore_https_errors=True,
            locale='en-US'
        )

        page = context.new_page()

        # Block images, fonts, etc. for performance
        page.route("**/*", lambda route, request: (
            route.abort() if request.resource_type in ["image", "stylesheet", "font"] else route.continue_()
        ))

        # Intercept JSON/JS responses for emails
        network_emails = set()
        def on_response(response):
            try:
                if any(t in response.headers.get("content-type", "") for t in ['json', 'javascript']):
                    text = response.text()
                    network_emails.update(extract_emails_from_text(text))
            except:
                pass

        page.on("response", on_response)

        try:
            page.goto(url, wait_until="networkidle", timeout=60000)
        except PlaywrightTimeoutError:
            print(f"[!] Timeout loading {url}")
            return []

        # Extract from page content
        html = page.content()
        found_emails.update(extract_emails_from_text(html))

        # Extract from mailto: links
        found_emails.update(extract_emails_from_mailto(page))

        # Also include network-captured emails
        found_emails.update(network_emails)

        browser.close()

    return sorted(found_emails)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <url>")
        sys.exit(1)

    for target_url in sys.argv[1:]:
        results = scrape_emails(target_url)
        print(f"{target_url} -> {results}")
د