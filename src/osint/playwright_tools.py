from playwright.sync_api import sync_playwright
import re

def extract_emails(text):
    """Extract emails from given text using regex"""
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

def run_scraper(target_url):
    with sync_playwright() as p:
        print(f"[+] Launching browser for {target_url} ...")
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            page.goto(target_url, timeout=15000)
            page.wait_for_timeout(3000)  # Wait 3 seconds for JS
            text = page.inner_text("body")

            emails = extract_emails(text)
            emails = list(set(emails))  # remove duplicates

            print("\n📧 Emails found:" if emails else "\n❌ No emails found.")
            for email in emails:
                print(f" - {email}")
        
        except Exception as e:
            print(f"[!] Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    url = input("Enter full target URL (e.g. https://www.just.edu.jo): ").strip()
    run_scraper(url)