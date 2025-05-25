# Multithreaded Downloader
import threading
import requests

def download(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)
    print(f"Downloaded {filename}")

if __name__ == "__main__":
    urls = [
        # Add your URLs here
        # ("https://example.com/file1", "file1"),
        # ("https://example.com/file2", "file2"),
    ]
    threads = []
    for url, filename in urls:
        t = threading.Thread(target=download, args=(url, filename))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print("All downloads complete.")
