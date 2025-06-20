"""
796. Rotate String

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s. A shift on s consists of moving the leftmost character to the rightmost position.

Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false

Constraints:
- 1 <= s.length, goal.length <= 100
- s and goal consist of lowercase English letters.
"""
def rotateString(s, goal):
    return len(s) == len(goal) and goal in (s + s)

# Example usage:
print(rotateString("abcde", "cdeab"))  # Output: True
print(rotateString("abcde", "abced"))  # Output: False
