"""
LeetCode 2354. Number of Excellent Pairs

Given nums and k, return the number of excellent pairs.

Example:
Input: nums = [1,2,3,1], k = 3
Output: 5

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

def countExcellentPairs(nums, k):
    nums = set(nums)
    bits = [bin(x).count('1') for x in nums]
    bits.sort()
    res = 0
    n = len(bits)
    for i in range(n):
        l = 0
        r = n-1
        while l <= r:
            m = (l+r)//2
            if bits[i]+bits[m] >= k:
                r = m-1
            else:
                l = m+1
        res += n-l
    return res

# Example usage:
# print(countExcellentPairs([1,2,3,1], 3))  # Output: 5
