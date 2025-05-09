from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re

def extract_emails_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

def run_playwright_tool(target_url):
    emails = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(target_url, timeout=20000)

            # انتظر ظهور عنصر فيه class="email"
            page.wait_for_selector(".email", timeout=10000)

            # استخرج النصوص من كل العناصر اللي فيها class="email"
            email_elements = page.locator(".email").all()
            for elem in email_elements:
                text = elem.inner_text()
                if "@" in text:
                    emails.append(text)

            emails = list(set(emails))  # remove duplicates
        except Exception as e:
            print(f"[!] Error with Playwright: {e}")
        finally:
            browser.close()

    return emails


