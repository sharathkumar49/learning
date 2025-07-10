"""
LeetCode 1879. Minimum XOR Sum of Two Arrays

You are given two integer arrays nums1 and nums2 of length n. Rearrange nums2 to minimize the sum of nums1[i] XOR nums2[i] for all i.

Example:
Input: nums1 = [1,2], nums2 = [2,3]
Output: 2

Constraints:
- 1 <= n <= 14
- 0 <= nums1[i], nums2[i] <= 10^9
"""

def minimumXORSum(nums1, nums2):
    n = len(nums1)
    dp = [float('inf')] * (1 << n)
    dp[0] = 0
    for mask in range(1 << n):
        i = bin(mask).count('1')
        if i > n: continue
        for j in range(n):
            if not (mask & (1 << j)):
                dp[mask | (1 << j)] = min(dp[mask | (1 << j)], dp[mask] + (nums1[i] ^ nums2[j]))
    return dp[-1]

# Example usage:
# print(minimumXORSum([1,2],[2,3]))  # Output: 2
