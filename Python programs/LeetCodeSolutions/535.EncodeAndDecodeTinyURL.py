"""
535. Encode and Decode TinyURL

Design a TinyURL system that encodes a URL to a shortened URL and decodes a shortened URL to its original URL.

Constraints:
- There is no restriction on how your encode/decode algorithm should work.

Example:
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"
"""

class Codec:
    def __init__(self):
        self.url2code = {}
        self.code2url = {}
        self.counter = 0
    def encode(self, longUrl: str) -> str:
        if longUrl in self.url2code:
            return self.url2code[longUrl]
        code = f"http://tinyurl.com/{self.counter}"
        self.url2code[longUrl] = code
        self.code2url[code] = longUrl
        self.counter += 1
        return code
    def decode(self, shortUrl: str) -> str:
        return self.code2url.get(shortUrl, "")

# Example usage:
codec = Codec()
url = "https://leetcode.com/problems/design-tinyurl"
short = codec.encode(url)
print(short)
print(codec.decode(short))
