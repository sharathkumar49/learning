"""
LeetCode 2213. Longest Substring of One Repeating Character

Given a string s and queries, return the length of the longest substring of one repeating character after each query.

Example:
Input: s = "babacc", queries = [[1,'b'],[3,'a'],[0,'c']]
Output: [3,3,3]

Constraints:
- 1 <= s.length, queries.length <= 10^5
- queries[i] = [index, ch]
"""

def longestRepeating(s, queries):
    res = []
    s = list(s)
    for idx, ch in queries:
        s[idx] = ch
        max_len = 1
        curr = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
                max_len = max(max_len, curr)
            else:
                curr = 1
        res.append(max_len)
    return res

# Example usage:
# print(longestRepeating("babacc", [[1,'b'],[3,'a'],[0,'c']]))  # Output: [3,3,3]
