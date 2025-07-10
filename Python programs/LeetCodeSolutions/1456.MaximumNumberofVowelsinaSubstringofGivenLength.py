"""
LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length

Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= s.length

Example:
Input: s = "abciiidef", k = 3
Output: 3
"""
def maxVowels(s, k):
    vowels = set('aeiou')
    count = max_count = sum(1 for c in s[:k] if c in vowels)
    for i in range(k, len(s)):
        if s[i] in vowels:
            count += 1
        if s[i - k] in vowels:
            count -= 1
        max_count = max(max_count, count)
    return max_count

# Example usage:
s = "abciiidef"
k = 3
print(maxVowels(s, k))  # Output: 3
