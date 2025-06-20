"""
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window, return the empty string "".

Constraints:
- 1 <= s.length, t.length <= 10^5
- s and t consist of English letters.

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
"""
def minWindow(s: str, t: str) -> str:
    from collections import Counter
    if not t or not s:
        return ""
    dict_t = Counter(t)
    required = len(dict_t)
    l, r, formed = 0, 0, 0
    window_counts = {}
    ans = float("inf"), None, None
    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        while l <= r and formed == required:
            character = s[l]
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            l += 1
        r += 1
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]

# Example usage:
if __name__ == "__main__":
    print(minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
    print(minWindow("a", "a"))  # Output: "a"
