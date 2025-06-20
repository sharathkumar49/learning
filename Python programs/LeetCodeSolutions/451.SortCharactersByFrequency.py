"""
451. Sort Characters By Frequency

Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

Constraints:
- 1 <= s.length <= 5 * 10^5
- s consists of uppercase and lowercase English letters and digits.

Example:
Input: s = "tree"
Output: "eetr"
"""

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        return ''.join([char * freq for char, freq in count.most_common()])

# Example usage:
sol = Solution()
print(sol.frequencySort("tree"))  # Output: "eetr"
