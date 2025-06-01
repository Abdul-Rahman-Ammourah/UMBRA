import requests
from bs4 import BeautifulSoup
import re
import time
import random
import json
import pandas as pd
from urllib.parse import urljoin, urlparse

class SpiderFootLite:
    def __init__(self, target, use_proxy=False):
        self.target = target
        self.domain = self.extract_domain(target)
        self.visited = set()
        self.emails = set()
        self.links = set()
        self.subdomains = set()
        self.use_proxy = use_proxy

        # Random User-Agent list to mimic different browsers
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/113.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Gecko/20100101 Firefox/112.0",
            "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 Chrome/110.0 Mobile Safari/537.36"
        ]

    # Extract domain from full URL or raw domain input
    def extract_domain(self, url):
        parsed = urlparse(url)
        return parsed.netloc if parsed.netloc else url

    # Fetch a page with optional proxy and random user-agent
    def fetch_page(self, url):
        headers = {
            "User-Agent": random.choice(self.user_agents)
        }
        try:
            if self.use_proxy:
                response = requests.get(url, headers=headers, proxies=self.proxies, timeout=10)
            else:
                response = requests.get(url, headers=headers, timeout=10)

            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"[!] Failed to fetch {url}: {e}")
            return ""

    # Extract email addresses using regex
    def extract_emails(self, text):
        return set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text))

    # Extract internal links (same domain)
    def extract_links(self, soup, current_url):
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            absolute = urljoin(current_url, href)
            if self.domain in absolute:
                self.links.add(absolute)

    # Crawl for emails and links with a limited depth
    def crawl_for_emails_links(self, url, depth=2):
        if depth == 0 or url in self.visited:
            return

        print(f"[+] Crawling: {url}")
        self.visited.add(url)

        html = self.fetch_page(url)
        if not html:
            return

        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()

        # Find and store emails
        found_emails = self.extract_emails(text)
        self.emails.update(found_emails)

        # Find and store internal links
        self.extract_links(soup, url)

        # Recursively follow internal links
        for link in self.links.copy():
            time.sleep(1)  # Politeness delay
            self.crawl_for_emails_links(link, depth - 1)

    # Get subdomains from crt.sh
    def get_subdomains_crtsh(self):
        print("[*] Fetching subdomains from crt.sh...")
        url = f"https://crt.sh/?q=%25.{self.domain}&output=json"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                entries = response.json()
                for entry in entries:
                    name = entry.get("name_value", "")
                    for sub in name.split("\n"):
                        if self.domain in sub:
                            self.subdomains.add(sub.strip())
            else:
                print("[!] Failed to fetch from crt.sh")
        except Exception as e:
            print(f"[!] Error fetching subdomains: {e}")

    # Save all results to TXT, JSON, and Excel
    def save_results(self):
        # Emails
        with open("emails.txt", "w") as f:
            for email in sorted(self.emails):
                f.write(email + "\n")

        with open("emails.json", "w") as f:
            json.dump(sorted(list(self.emails)), f, indent=4)

        pd.DataFrame(sorted(self.emails), columns=["Email"]).to_excel("emails.xlsx", index=False)

        # Links
        with open("links.txt", "w") as f:
            for link in sorted(self.links):
                f.write(link + "\n")

        with open("links.json", "w") as f:
            json.dump(sorted(list(self.links)), f, indent=4)

        pd.DataFrame(sorted(self.links), columns=["Link"]).to_excel("links.xlsx", index=False)

        # Subdomains
        with open("subdomains.txt", "w") as f:
            for sub in sorted(self.subdomains):
                f.write(sub + "\n")

        with open("subdomains.json", "w") as f:
            json.dump(sorted(list(self.subdomains)), f, indent=4)

        pd.DataFrame(sorted(self.subdomains), columns=["Subdomain"]).to_excel("subdomains.xlsx", index=False)

        print("[✔] Results saved to TXT, JSON, and Excel formats.")

    # Main method to execute all data collection
    def run(self):
        print("[*] Starting SpiderFootLite OSINT scan...\n")
        self.get_subdomains_crtsh()
        self.crawl_for_emails_links("http://" + self.domain)
        self.save_results()

        print(f"\n[+] Emails found: {len(self.emails)}")
        print(f"[+] Links found: {len(self.links)}")
        print(f"[+] Subdomains found: {len(self.subdomains)}")

# Program entry point
if __name__ == "__main__":
    target_input = input("Enter target domain or IP (e.g. example.com): ").strip()
    proxy_choice = input("Use proxy? (y/n): ").strip().lower()
    use_proxy = proxy_choice == "y"

    scanner = SpiderFootLite(target=target_input, use_proxy=use_proxy)
    scanner.run()
