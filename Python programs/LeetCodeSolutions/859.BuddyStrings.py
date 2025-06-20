"""
859. Buddy Strings

Given two strings s and goal, return true if you can swap two letters in s so the result equals goal.

Example 1:
Input: s = "ab", goal = "ba"
Output: true

Example 2:
Input: s = "ab", goal = "ab"
Output: false

Constraints:
- 1 <= s.length, goal.length <= 2 * 10^4
- s and goal consist of lowercase letters.
"""
def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False
    if s == goal:
        return len(set(s)) < len(s)
    pairs = [(a, b) for a, b in zip(s, goal) if a != b]
    return len(pairs) == 2 and pairs[0] == pairs[1][::-1]

# Example usage:
print(buddyStrings("ab", "ba"))  # Output: True
print(buddyStrings("ab", "ab"))  # Output: False
