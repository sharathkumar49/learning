"""
LeetCode 703. Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement the KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example 1:
Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4,5,8,2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Constraints:
- 1 <= k <= 10^4
- 0 <= nums.length <= 10^4
- -10^4 <= nums[i], val <= 10^4
- At most 10^4 calls will be made to add.
"""
from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

# Example usage
if __name__ == "__main__":
    kth = KthLargest(3, [4,5,8,2])
    print(kth.add(3))  # Output: 4
    print(kth.add(5))  # Output: 5
    print(kth.add(10)) # Output: 5
    print(kth.add(9))  # Output: 8
    print(kth.add(4))  # Output: 8
