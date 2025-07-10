"""
LeetCode 1589. Maximum Sum Obtained of Any Permutation

Given an array nums and an array requests where requests[i] = [start, end], return the maximum total sum obtained by permuting nums and summing up requests. Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
Output: 19

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= requests.length <= 10^5
"""

def maxSumRangeQuery(nums, requests):
    mod = 10**9 + 7
    n = len(nums)
    freq = [0]*(n+1)
    for l, r in requests:
        freq[l] += 1
        freq[r+1] -= 1
    for i in range(1, n):
        freq[i] += freq[i-1]
    freq.pop()
    nums.sort(reverse=True)
    freq.sort(reverse=True)
    return sum(a*b for a, b in zip(nums, freq)) % mod

# Example usage:
# nums = [1,2,3,4,5]
# requests = [[1,3],[0,1]]
# print(maxSumRangeQuery(nums, requests))  # Output: 19
