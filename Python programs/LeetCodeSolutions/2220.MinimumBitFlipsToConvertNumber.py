"""
LeetCode 2220. Minimum Bit Flips to Convert Number

Given start and goal, return the minimum number of bit flips to convert start to goal.

Example:
Input: start = 10, goal = 7
Output: 3

Constraints:
- 0 <= start, goal <= 10^9
"""

def minBitFlips(start, goal):
    return bin(start ^ goal).count('1')

# Example usage:
# print(minBitFlips(10, 7))  # Output: 3
