"""
LeetCode 2131. Longest Palindrome by Concatenating Two Letter Words

Given an array of two-letter words, return the length of the longest palindrome that can be built.

Example:
Input: words = ["lc","cl","gg"]
Output: 6

Constraints:
- 1 <= words.length <= 10^5
- words[i].length == 2
"""

def longestPalindrome(words):
    from collections import Counter
    count = Counter(words)
    res = 0
    center = False
    for w in count:
        if w[0] == w[1]:
            pairs = count[w] // 2
            res += pairs * 4
            if count[w] % 2:
                center = True
        else:
            rev = w[::-1]
            if rev in count:
                pairs = min(count[w], count[rev])
                res += pairs * 4
                count[w] -= pairs
                count[rev] -= pairs
    if center:
        res += 2
    return res

# Example usage:
# print(longestPalindrome(["lc","cl","gg"]))  # Output: 6
