"""
159. Longest Substring with At Most Two Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

Given a string s, return the length of the longest substring that contains at most two distinct characters.

Constraints:
- 1 <= s.length <= 10^5
- s consists of English letters.

Example:
Input: s = "eceba"
Output: 3
"""
def lengthOfLongestSubstringTwoDistinct(s: str) -> int:
    left = 0
    count = {}
    max_len = 0
    for right, c in enumerate(s):
        count[c] = count.get(c, 0) + 1
        while len(count) > 2:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# Example usage:
if __name__ == "__main__":
    print(lengthOfLongestSubstringTwoDistinct("eceba"))  # Output: 3
    print(lengthOfLongestSubstringTwoDistinct("ccaabbb"))  # Output: 5
