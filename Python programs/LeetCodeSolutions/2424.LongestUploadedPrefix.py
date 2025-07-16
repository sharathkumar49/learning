"""
LeetCode 2424. Longest Uploaded Prefix

Design a data structure to track the longest uploaded prefix.

Constraints:
- 1 <= n <= 10^5
"""

class LUPrefix:
    def __init__(self, n):
        self.uploaded = set()
        self.longest = 0
    def upload(self, video):
        self.uploaded.add(video)
        while self.longest+1 in self.uploaded:
            self.longest += 1
    def longest(self):
        return self.longest

# Example usage:
# obj = LUPrefix(4)
# obj.upload(3)
# obj.upload(1)
# obj.longest()  # Output: 1
# obj.upload(2)
# obj.longest()  # Output: 3
# obj.upload(4)
# obj.longest()  # Output: 4
