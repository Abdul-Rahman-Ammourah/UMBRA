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
            # Choose a random User-Agent for each request
            headers = {
                "User-Agent": random.choice(self.user_agents)
            }

            # Apply proxy if enabled
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
            time.sleep(1)  # polite delay to avoid being blocked
            self.crawl(link, depth - 1)

    def run(self):
        print("[*] Starting harvesting...")
        self.crawl(self.base_url, self.max_depth)

        if self.emails:
            print(f"\n📬 Total unique emails found: {len(self.emails)}")
            for email in self.emails:
                print(" -", email)
            with open("emails.txt", "w") as f:
                for email in self.emails:
                    f.write(email + "\n")
            print("[+] Saved to emails.txt")
        else:
            print("[-] No emails found.")

if __name__ == "__main__":
    target_url = input("Enter the target URL (e.g. https://example.com): ").strip()
    depth = input("Enter crawl depth (default 2): ").strip()
    depth = int(depth) if depth.isdigit() else 2

    use_proxy_input = input("Use proxy? (y/n): ").strip().lower()
    use_proxy = use_proxy_input == 'y'

    harvester = Harvester(base_url=target_url, max_depth=depth, use_proxy=use_proxy)
    harvester.run()
