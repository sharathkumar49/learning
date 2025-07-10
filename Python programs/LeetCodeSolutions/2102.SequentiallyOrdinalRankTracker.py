"""
LeetCode 2102. Sequentially Ordinal Rank Tracker

Design a data structure to track the k-th largest element in a stream.

Example:
Input: ["KthLargest","add","add","add","add","add"], [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
Output: [null,4,5,5,8,8]

Constraints:
- 1 <= k <= 10^4
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
"""

import heapq
class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Example usage:
# kth = KthLargest(3, [4,5,8,2])
# print(kth.add(3))  # Output: 4
# print(kth.add(5))  # Output: 5
# print(kth.add(10)) # Output: 5
# print(kth.add(9))  # Output: 8
# print(kth.add(4))  # Output: 8
