"""
LeetCode 2178. Maximum Split of Positive Even Integers

Given an integer finalSum, split it into the maximum number of unique positive even integers. Return the result as a list. If not possible, return an empty list.

Example:
Input: finalSum = 12
Output: [2,4,6]

Constraints:
- 1 <= finalSum <= 10^{10}
"""

def maximumEvenSplit(finalSum):
    if finalSum % 2:
        return []
    res, x = [], 2
    while finalSum >= x:
        res.append(x)
        finalSum -= x
        x += 2
    if finalSum:
        res[-1] += finalSum
    return res

# Example usage:
# print(maximumEvenSplit(12))  # Output: [2,4,6]
