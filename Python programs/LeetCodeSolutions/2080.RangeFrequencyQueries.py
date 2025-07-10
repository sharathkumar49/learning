"""
LeetCode 2080. Range Frequency Queries

Design a data structure to find the frequency of a value in a subarray.

Example:
Input: ["RangeFreqQuery","query","query"], [[[12,33,4,56,22,2,34,33,22,12,34,56]],[1,2,4],[0,11,33]]
Output: [null,1,2]

Constraints:
- 2 <= arr.length <= 10^5
- 1 <= value, left, right <= 10^9
"""

class RangeFreqQuery:
    def __init__(self, arr):
        from collections import defaultdict
        self.pos = defaultdict(list)
        for i, v in enumerate(arr):
            self.pos[v].append(i)
    def query(self, left, right, value):
        import bisect
        idxs = self.pos.get(value, [])
        l = bisect.bisect_left(idxs, left)
        r = bisect.bisect_right(idxs, right)
        return r - l

# Example usage:
# rfq = RangeFreqQuery([12,33,4,56,22,2,34,33,22,12,34,56])
# print(rfq.query(1,2,4))  # Output: 1
# print(rfq.query(0,11,33))  # Output: 2
