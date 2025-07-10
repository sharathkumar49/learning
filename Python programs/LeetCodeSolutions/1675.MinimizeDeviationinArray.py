"""
LeetCode 1675. Minimize Deviation in Array

Given an array nums, return the minimum deviation possible after performing any number of operations (multiply odd by 2, divide even by 2).

Example 1:
Input: nums = [1,2,3,4]
Output: 1

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

def minimumDeviation(nums):
    import heapq
    nums = [x*2 if x%2 else x for x in nums]
    heap = [-x for x in nums]
    heapq.heapify(heap)
    res = float('inf')
    mi = min(nums)
    while True:
        mx = -heapq.heappop(heap)
        res = min(res, mx - mi)
        if mx % 2:
            break
        mi = min(mi, mx//2)
        heapq.heappush(heap, -mx//2)
    return res

# Example usage:
# nums = [1,2,3,4]
# print(minimumDeviation(nums))  # Output: 1
