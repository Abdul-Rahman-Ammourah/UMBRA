#Take all the Osint data and combine them into one list

#def compiner(osint_data):
    #Implement the code here
  #  pass

import sys, os
from pathlib import Path

# نضيف مجلد 'src/osint' إلى sys.path لكي تُعامَل 'playwright/' داخله كحزمة علوية
project_root = Path(__file__).resolve().parent.parent  # .../UMBRA/src
sys.path.insert(0, str(project_root / "osint"))

import re
from playwright.sync_api import sync_playwright   # الآن سيجد الحزمة تحت osint/playwright

def run_playwright_scraper(target_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_default_navigation_timeout(0)
        page.set_default_timeout(0)

        page.goto(target_url, wait_until="networkidle")
        page.wait_for_timeout(5000)
        html = page.content()
        browser.close()

    text = re.sub(r'<[^>]+>', '', html)
    return list(set(re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Compiner.py <URL>")
        sys.exit(1)
    url = sys.argv[1]
    results = run_playwright_scraper(url)

    print(f"[✓] Found {len(results)} emails:")
    for e in results:
        print(" -", e)
