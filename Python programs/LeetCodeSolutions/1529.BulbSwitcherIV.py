"""
LeetCode 1529. Bulb Switcher IV

Given a string target consisting of only '0' and '1', return the minimum number of flips required to make all bulbs equal to target.

Constraints:
- 1 <= target.length <= 10^5
- target consists of only '0' and '1'.

Example:
Input: target = "10111"
Output: 3
"""
def minFlips(target):
    flips = 0
    curr = '0'
    for c in target:
        if c != curr:
            flips += 1
            curr = c
    return flips

# Example usage:
target = "10111"
print(minFlips(target))  # Output: 3
