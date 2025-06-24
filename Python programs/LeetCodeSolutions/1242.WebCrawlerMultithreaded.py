"""
1242. Web Crawler Multithreaded

Given a startUrl and a HtmlParser interface, return all URLs reachable from startUrl with the same hostname using multiple threads.

Constraints:
- 1 <= urls.length <= 1000
- 1 <= url.length <= 300
- startUrl is a valid URL

Note: The HtmlParser interface is not implemented here.

Example:
Input: startUrl = "http://news.yahoo.com/news/topics/", HtmlParser = ...
Output: [urls...]

"""
# Note: HtmlParser API is not implemented here.
import threading
from urllib.parse import urlparse

def crawl(startUrl, htmlParser):
    hostname = urlparse(startUrl).hostname
    seen = set()
    lock = threading.Lock()
    def worker(url):
        with lock:
            if url in seen or urlparse(url).hostname != hostname:
                return
            seen.add(url)
        for next_url in htmlParser.getUrls(url):
            worker(next_url)
    worker(startUrl)
    return list(seen)

# Example usage
# Not executable without HtmlParser API
