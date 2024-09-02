from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup


class PageParser:

    def parse(self, html: str, base_url: str) -> tuple[str, list[str]]:
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string if soup.title.string else "No title"
        links = (urljoin(base_url,
                         a.get("href")) for a in soup.find_all("a", href=True))
        full_links = [link for link in links if self.is_valid_url(link)]
        return title, full_links

    @staticmethod
    def is_valid_url(url: str) -> bool:
        parsed = urlparse(url)
        return parsed.scheme in ["http", "https"]
