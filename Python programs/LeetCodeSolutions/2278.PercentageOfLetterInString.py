"""
LeetCode 2278. Percentage of Letter in String

Given s and letter, return the percentage of letter in s.

Example:
Input: s = "foobar", letter = "o"
Output: 33

Constraints:
- 1 <= s.length <= 100
- letter is a lowercase English letter
"""

def percentageLetter(s, letter):
    return int(s.count(letter) * 100 / len(s))

# Example usage:
# print(percentageLetter("foobar", "o"))  # Output: 33
