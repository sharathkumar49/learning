"""
295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/

The MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

Constraints:
- -10^5 <= num <= 10^5
- There will be at least one element before calling findMedian.
- At most 5 * 10^4 calls will be made to addNum and findMedian.

Example:
Input
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]
Output
[null,null,null,1.5,null,2.0]
"""
import heapq
class MedianFinder:
    def __init__(self):
        self.small = []  # max heap
        self.large = []  # min heap
    def addNum(self, num):
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2

# Example usage:
if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # Output: 1.5
    mf.addNum(3)
    print(mf.findMedian())  # Output: 2.0
