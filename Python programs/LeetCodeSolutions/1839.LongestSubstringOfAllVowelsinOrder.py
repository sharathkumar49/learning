"""
LeetCode 1839. Longest Substring Of All Vowels in Order

Given a string word, return the length of the longest substring where all five vowels are in order.

Example 1:
Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
Output: 13

Constraints:
- 1 <= word.length <= 5 * 10^5
- word consists only of lowercase English letters
"""

def longestBeautifulSubstring(word):
    vowels = 'aeiou'
    res = cnt = 0
    last = ''
    unique = 0
    for c in word:
        if c < last:
            cnt = 0
            unique = 0
        if c != last:
            unique += 1
        if c == vowels[unique-1]:
            cnt += 1
            if unique == 5:
                res = max(res, cnt)
        else:
            cnt = 1
            unique = 1 if c == 'a' else 0
        last = c
    return res

# Example usage:
# word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
# print(longestBeautifulSubstring(word))  # Output: 13
