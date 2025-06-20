"""
952. Largest Component Size by Common Factor
https://leetcode.com/problems/largest-component-size-by-common-factor/

You are given an integer array of unique positive integers nums. Consider the following graph:
- There are nums.length nodes, labeled nums[0] to nums[nums.length - 1]
- There is an edge between nums[i] and nums[j] if gcd(nums[i], nums[j]) > 1
Return the size of the largest connected component in the graph.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i] <= 10^5
- All the values of nums are unique.

Example:
Input: nums = [4,6,15,35]
Output: 4
"""
from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        parent = {}
        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)
        for x in nums:
            for f in range(2, int(x ** 0.5) + 1):
                if x % f == 0:
                    union(x, f)
                    union(x, x // f)
        count = defaultdict(int)
        for x in nums:
            count[find(x)] += 1
        return max(count.values())

# Example usage
if __name__ == "__main__":
    nums = [4,6,15,35]
    print(Solution().largestComponentSize(nums))  # Output: 4
