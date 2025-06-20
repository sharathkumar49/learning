"""
996. Number of Squareful Arrays
https://leetcode.com/problems/number-of-squareful-arrays/

Given an array nums, a permutation of the array is squareful if the sum of every pair of adjacent elements is a perfect square. Return the number of squareful permutations.

Constraints:
- 1 <= nums.length <= 12
- 0 <= nums[i] <= 10^9

Example:
Input: nums = [1,17,8]
Output: 2
"""
from typing import List
from math import isqrt
from collections import Counter

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_square(n):
            r = isqrt(n)
            return r * r == n
        def dfs(x, left):
            if left == 0:
                return 1
            res = 0
            for y in graph[x]:
                if count[y]:
                    count[y] -= 1
                    res += dfs(y, left-1)
                    count[y] += 1
            return res
        count = Counter(nums)
        graph = {x: [] for x in count}
        for x in count:
            for y in count:
                if is_square(x + y):
                    graph[x].append(y)
        res = 0
        for x in count:
            count[x] -= 1
            res += dfs(x, len(nums)-1)
            count[x] += 1
        return res

# Example usage
if __name__ == "__main__":
    nums = [1,17,8]
    print(Solution().numSquarefulPerms(nums))  # Output: 2
