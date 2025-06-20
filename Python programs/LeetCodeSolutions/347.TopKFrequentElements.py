"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in nums]
- It is guaranteed that the answer is unique.
"""
from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]

# Example usage:
nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums, k))  # Output: [1,2]
