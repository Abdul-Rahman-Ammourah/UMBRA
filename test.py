#!/usr/bin/env python3
"""
Enhanced asynchronous email scraper using Playwright with optional domain-limited crawling,
concurrency control, custom user-agent, and improved error handling.
"""
import sys
import re
import argparse
import asyncio
from urllib.parse import urlparse
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

EMAIL_REGEX = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    re.IGNORECASE
)

async def extract_emails_from_response(response, emails):
    try:
        content_type = response.headers.get('content-type', '')
        if 'application/json' in content_type or 'javascript' in content_type:
            text = await response.text()
            emails.update(EMAIL_REGEX.findall(text))
    except Exception:
        pass

async def scrape_page(page, url, emails, visited, to_visit, base_netloc, timeout):
    try:
        await page.goto(url, wait_until='networkidle', timeout=timeout)  # Increased timeout
    except PlaywrightTimeoutError:
        print(f"[!] Timeout loading {url}", file=sys.stderr)
        return
    except Exception as e:
        print(f"[!] Error loading {url}: {e}", file=sys.stderr)
        return

    try:
        # Wait for email links or some other indicator if needed
        await page.wait_for_selector('a[href^="mailto:"]', timeout=timeout)
        html = await page.content()
        emails.update(EMAIL_REGEX.findall(html))
    except Exception as e:
        print(f"[!] Failed to get content for {url}: {e}", file=sys.stderr)

    try:
        # Extract all anchor tags
        anchors = await page.eval_on_selector_all('a[href]', 'elements => elements.map(e => e.href)')
        for link in anchors:
            parsed = urlparse(link)
            if parsed.netloc == base_netloc:
                normalized = parsed.scheme + '://' + parsed.netloc + parsed.path
                if normalized not in visited:
                    to_visit.append(normalized)
    except Exception as e:
        print(f"[!] Failed to extract links from {url}: {e}", file=sys.stderr)

async def crawl(start_url, depth, concurrency, timeout, user_agent, headless):
    emails = set()
    parsed_start = urlparse(start_url)
    base_netloc = parsed_start.netloc

    visited = set()
    to_visit = [start_url]

    sem = asyncio.Semaphore(concurrency)

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=headless)
        context = await browser.new_context(
            user_agent=user_agent,
            ignore_https_errors=True
        )
        page = await context.new_page()
        page.on('response', lambda resp: asyncio.create_task(extract_emails_from_response(resp, emails)))

        current_depth = 0
        while to_visit and current_depth <= depth:
            tasks = []
            for _ in range(len(to_visit)):
                url = to_visit.pop(0)
                if url in visited:
                    continue
                visited.add(url)
                tasks.append(scrape_page(page, url, emails, visited, to_visit, base_netloc, timeout))

            if tasks:
                await asyncio.gather(*tasks)
            current_depth += 1

        await browser.close()
    return sorted(emails)

async def main():
    parser = argparse.ArgumentParser(description='Asynchronous email scraper with crawling')
    parser.add_argument('urls', nargs='+', help='Starting URL(s) to scrape')
    parser.add_argument('--depth', type=int, default=0, help='Crawl depth (0 = only the start page)')
    parser.add_argument('--concurrency', type=int, default=3, help='Max concurrent page loads')
    parser.add_argument('--timeout', type=int, default=60000, help='Navigation timeout in ms')
    parser.add_argument('--headless', action='store_true', help='Run browser in headless mode')
    parser.add_argument('--user-agent', type=str,
                        default=('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'),
                        help='Custom User-Agent string')
    args = parser.parse_args()

    tasks = [
        crawl(url, args.depth, args.concurrency, args.timeout, args.user_agent, args.headless)
        for url in args.urls
    ]
    results = await asyncio.gather(*tasks)

    for url, emails in zip(args.urls, results):
        print(f"\n{url} ->")
        for email in emails:
            print(f"  [✓] {email}")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("[!] Interrupted by user", file=sys.stderr)
