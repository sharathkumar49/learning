"""
LeetCode 2252. Seven Day Average

Given an array cases, return the seven day average for each day after the sixth.

Example:
Input: cases = [1,2,3,4,5,6,7,8,9]
Output: [4,5,6]

Constraints:
- 7 <= cases.length <= 10^5
"""

def sevenDayAverage(cases):
    res = []
    for i in range(6, len(cases)):
        res.append(sum(cases[i-6:i+1])//7)
    return res

# Example usage:
# print(sevenDayAverage([1,2,3,4,5,6,7,8,9]))  # Output: [4,5,6]
