"""
LeetCode 2157. Groups of Strings

Given a list of strings words, return the number of groups of similar strings and the size of the largest group. Two strings are similar if you can swap two letters (in different positions) to make them equal, or if they are already equal.

Example:
Input: words = ["abc","acb","bac","xyz","yxz"]
Output: [2,3]

Constraints:
- 1 <= words.length <= 10^5
- 1 <= words[i].length <= 26
- words[i] consists of lowercase English letters only.
"""

def groupStrings(words):
    from collections import defaultdict
    def mask(word):
        m = 0
        for c in set(word):
            m |= 1 << (ord(c) - ord('a'))
        return m
    parent = {}
    size = defaultdict(int)
    def find(x):
        if parent.setdefault(x, x) != x:
            parent[x] = find(parent[x])
        return parent[x]
    for w in words:
        m = mask(w)
        size[find(m)] += 1
        for i in range(26):
            m2 = m ^ (1 << i)
            if m2 in parent:
                parent[find(m)] = find(m2)
    group_count = len(set(find(x) for x in parent))
    max_size = max(size.values())
    return [group_count, max_size]

# Example usage:
# print(groupStrings(["abc","acb","bac","xyz","yxz"]))  # Output: [2,3]
