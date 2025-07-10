"""
LeetCode 2042. Check if Numbers Are Ascending in a Sentence

Given a string s containing numbers and words, return true if the numbers are strictly increasing.

Example:
Input: s = "1 box has 3 blue 4 red 6 green and 12 yellow balls"
Output: true

Constraints:
- 3 <= s.length <= 200
- s contains only lowercase English letters, spaces, and digits.
"""

def areNumbersAscending(s):
    prev = -1
    for word in s.split():
        if word.isdigit():
            num = int(word)
            if num <= prev:
                return False
            prev = num
    return True

# Example usage:
# print(areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow balls"))  # Output: True
