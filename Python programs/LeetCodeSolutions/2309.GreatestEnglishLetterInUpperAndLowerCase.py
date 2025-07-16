"""
LeetCode 2309. Greatest English Letter in Upper and Lower Case

Given s, return the greatest English letter present in both cases.

Example:
Input: s = "lEeTcOdE"
Output: "E"

Constraints:
- 1 <= s.length <= 1000
"""

def greatestLetter(s):
    return max([c for c in set(s) if c.isupper() and c.lower() in s], default='')

# Example usage:
# print(greatestLetter("lEeTcOdE"))  # Output: "E"
