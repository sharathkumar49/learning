"""
LeetCode 2059. Minimum Operations to Convert Number

Given two integers start and goal, and an array nums, return the minimum number of operations to convert start to goal using +, -, or ^ with any element in nums.

Example:
Input: nums = [2,4,12], start = 2, goal = 12
Output: 2

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i], start, goal <= 1000
"""

def minimumOperations(nums, start, goal):
    from collections import deque
    visited = set()
    q = deque([(start, 0)])
    while q:
        x, steps = q.popleft()
        if x == goal:
            return steps
        if x < 0 or x > 1000 or x in visited:
            continue
        visited.add(x)
        for n in nums:
            for op in (x+n, x-n, x^n):
                q.append((op, steps+1))
    return -1

# Example usage:
# print(minimumOperations([2,4,12], 2, 12))  # Output: 2
