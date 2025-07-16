"""
LeetCode 2274. Maximum Consecutive Floors Without Special Floors

Given bottom, top, and special, return the maximum number of consecutive floors without special floors.

Example:
Input: bottom = 2, top = 9, special = [4,6]
Output: 3

Constraints:
- 1 <= bottom <= top <= 10^9
- 1 <= special.length <= 10^5
"""

def maxConsecutive(bottom, top, special):
    special = sorted(set(special))
    res = max(special[0]-bottom, top-special[-1])
    for i in range(1, len(special)):
        res = max(res, special[i]-special[i-1]-1)
    return res

# Example usage:
# print(maxConsecutive(2, 9, [4,6]))  # Output: 3
