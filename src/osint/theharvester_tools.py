import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import time
import random

class Harvester:
    def __init__(self, base_url, max_depth=2, use_proxy=False):
        self.base_url = base_url
        self.max_depth = max_depth
        self.use_proxy = use_proxy
        self.visited = set()
        self.emails = set()
        self.domain = urlparse(base_url).netloc

        # Random User-Agent list
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/113.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Gecko/20100101 Firefox/112.0",
            "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 Chrome/110.0 Mobile Safari/537.36",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0"
        ]

        # Optional proxy configuration
        self.proxies = {
            "http": "http://your-proxy-ip:port",
            "https": "http://your-proxy-ip:port"
        }

    def fetch_page(self, url):
        try:
            headers = {
                "User-Agent": random.choice(self.user_agents)
            }

            if self.use_proxy:
                response = requests.get(url, headers=headers, proxies=self.proxies, timeout=10)
            else:
                response = requests.get(url, headers=headers, timeout=10)

            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"[!] Failed to fetch {url}: {e}")
            return ""

    def extract_emails(self, text):
        email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
        found = re.findall(email_regex, text)
        return set(found)

    def extract_links(self, soup, current_url):
        links = set()
        for a_tag in soup.find_all("a", href=True):
            href = a_tag.get("href")
            absolute = urljoin(current_url, href)
            parsed = urlparse(absolute)
            if parsed.netloc == self.domain:
                cleaned = parsed.scheme + "://" + parsed.netloc + parsed.path
                links.add(cleaned)
        return links

    def crawl(self, url, depth):
        if depth == 0 or url in self.visited:
            return

        print(f"[+] Crawling: {url}")
        self.visited.add(url)

        html = self.fetch_page(url)
        if not html:
            return

        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        page_emails = self.extract_emails(text)

        if page_emails:
            print(f"[✔] Found {len(page_emails)} emails on {url}")
            self.emails.update(page_emails)

        links = self.extract_links(soup, url)
        for link in links:
            time.sleep(1)  # polite delay
            self.crawl(link, depth - 1)

    def run(self):
        print("[*] Starting harvesting...")
        self.crawl(self.base_url, self.max_depth)

# ✅ دالة جاهزة للـ GUI
def run(url="https://www.uiowa.edu/about/contact-us", depth=2, use_proxy=False):
    harvester = Harvester(base_url=url, max_depth=depth, use_proxy=use_proxy)
    harvester.run()
    if harvester.emails:
        return f"[+] Found {len(harvester.emails)} emails:\n" + "\n".join(harvester.emails)
    else:
        return "[-] No emails found."

# ✅ اختبار يدوي
if __name__ == "__main__":
    print(run())
