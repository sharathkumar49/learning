"""
854. K-Similar Strings

Given two anagrams s1 and s2, return the minimum number of adjacent swaps to transform s1 into s2.

Example 1:
Input: s1 = "ab", s2 = "ba"
Output: 1

Example 2:
Input: s1 = "abc", s2 = "bca"
Output: 2

Constraints:
- 1 <= s1.length <= 20
- s2.length == s1.length
- s1 and s2 are anagrams.
"""
def kSimilarity(s1, s2):
    from collections import deque
    queue = deque([(s1, 0)])
    visited = set([s1])
    while queue:
        s, k = queue.popleft()
        if s == s2:
            return k
        i = 0
        while s[i] == s2[i]:
            i += 1
        for j in range(i+1, len(s)):
            if s[j] == s2[i] and s[j] != s2[j]:
                ns = list(s)
                ns[i], ns[j] = ns[j], ns[i]
                ns = ''.join(ns)
                if ns not in visited:
                    visited.add(ns)
                    queue.append((ns, k+1))
    return -1

# Example usage:
print(kSimilarity("ab", "ba"))  # Output: 1
print(kSimilarity("abc", "bca"))  # Output: 2
