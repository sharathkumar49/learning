"""
LeetCode 1732. Find the Highest Altitude

Given an array gain, return the highest altitude reached.

Example 1:
Input: gain = [-5,1,5,0,-7]
Output: 1

Constraints:
- 1 <= gain.length <= 100
- -100 <= gain[i] <= 100
"""

def largestAltitude(gain):
    alt = 0
    res = 0
    for g in gain:
        alt += g
        res = max(res, alt)
    return res

# Example usage:
# gain = [-5,1,5,0,-7]
# print(largestAltitude(gain))  # Output: 1
