"""
LeetCode 2600. K Items With the Maximum Sum

Given numOnes, numZeros, numNegOnes, k, return the maximum sum of k items.

Constraints:
- 0 <= numOnes, numZeros, numNegOnes, k <= 50
"""

def kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):
    res = 0
    if k <= numOnes:
        return k
    res += numOnes
    k -= numOnes
    if k <= numZeros:
        return res
    k -= numZeros
    return res - k
# Example usage:
# print(kItemsWithMaximumSum(3,2,0,2))  # Output: 2
