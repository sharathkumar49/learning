"""
LeetCode 2208. Minimum Operations to Halve Array Sum

Given an array nums, in one operation you can pick any number from nums and reduce it to exactly half. Return the minimum number of operations to reduce the sum of nums by at least half.

Example:
Input: nums = [5,19,8,1]
Output: 3

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^7
"""

def halveArray(nums):
    import heapq
    total = sum(nums)
    target = total / 2
    reduced = 0
    operations = 0
    heap = [-num for num in nums]
    heapq.heapify(heap)
    
    while reduced < target:
        largest = -heapq.heappop(heap)
        reduced += largest / 2
        heapq.heappush(heap, -(largest / 2))
        operations += 1
    
    return operations

# Example usage:
# print(halveArray([5,19,8,1]))  # Output: 3
