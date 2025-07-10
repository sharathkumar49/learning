"""
LeetCode 1891. Cutting Ribbons

Given an integer array ribbons and an integer k, return the maximum length of ribbon you can obtain such that you can cut at least k ribbons of that length.

Example:
Input: ribbons = [9,7,5], k = 3
Output: 5

Constraints:
- 1 <= ribbons.length <= 10^5
- 1 <= ribbons[i] <= 10^5
- 1 <= k <= 10^9
"""

def maxLength(ribbons, k):
    left, right = 1, max(ribbons)
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if sum(r // mid for r in ribbons) >= k:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

# Example usage:
# print(maxLength([9,7,5], 3))  # Output: 5
