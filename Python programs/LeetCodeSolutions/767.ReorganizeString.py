"""
767. Reorganize String

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or the empty string if not possible.

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""

Constraints:
- 1 <= s.length <= 500
- s consists of lowercase English letters.
"""
import heapq
from collections import Counter

def reorganizeString(s):
    count = Counter(s)
    max_heap = [(-freq, char) for char, freq in count.items()]
    heapq.heapify(max_heap)
    prev = (0, '')
    result = []
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result.append(char)
        if prev[0] < 0:
            heapq.heappush(max_heap, prev)
        freq += 1
        prev = (freq, char)
    res = ''.join(result)
    for i in range(1, len(res)):
        if res[i] == res[i-1]:
            return ""
    return res

# Example usage:
print(reorganizeString("aab"))  # Output: "aba"
print(reorganizeString("aaab")) # Output: ""
