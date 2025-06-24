"""
LeetCode 1296. Divide Array in Sets of K Consecutive Numbers

Given an array nums and an integer k, return true if it can be divided into sets of k consecutive numbers.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= nums.length

Example:
Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
"""
def isPossibleDivide(nums, k):
    from collections import Counter
    count = Counter(nums)
    for x in sorted(count):
        if count[x] > 0:
            for i in range(1, k):
                if count[x+i] < count[x]:
                    return False
                count[x+i] -= count[x]
    return True

# Example usage:
nums = [1,2,3,3,4,4,5,6]
k = 4
print(isPossibleDivide(nums, k))  # Output: True
