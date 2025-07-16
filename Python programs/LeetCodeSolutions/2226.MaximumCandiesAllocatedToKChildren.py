"""
LeetCode 2226. Maximum Candies Allocated to K Children

Given candies and k, return the maximum number of candies each child can get.

Example:
Input: candies = [5,8,6], k = 3
Output: 5

Constraints:
- 1 <= candies.length <= 10^5
- 1 <= candies[i] <= 10^7
- 1 <= k <= 10^12
"""

def maximumCandies(candies, k):
    left, right = 1, max(candies)
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if sum(c // mid for c in candies) >= k:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

# Example usage:
# print(maximumCandies([5,8,6], 3))  # Output: 5
