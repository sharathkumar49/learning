"""
1157. Online Majority Element In Subarray

Implement a MajorityChecker class that can efficiently answer queries for the majority element in a subarray.

Constraints:
- 1 <= arr.length <= 2 * 10^4
- 1 <= arr[i] <= 2 * 10^4
- 1 <= threshold <= right - left + 1
- 0 <= left <= right < arr.length
- At most 2 * 10^4 queries.

Example:
Input: ["MajorityChecker","query","query","query"], [[[1,1,2,2,1,1]],[0,5,4],[0,3,3],[2,3,2]]
Output: [null,1,-1,2]

"""
import random
from collections import defaultdict

class MajorityChecker:
    def __init__(self, arr):
        self.arr = arr
        self.pos = defaultdict(list)
        for i, v in enumerate(arr):
            self.pos[v].append(i)
    def query(self, left, right, threshold):
        for _ in range(20):
            x = self.arr[random.randint(left, right)]
            idxs = self.pos[x]
            l = self._left(idxs, left)
            r = self._right(idxs, right)
            if r - l >= threshold:
                return x
        return -1
    def _left(self, idxs, left):
        lo, hi = 0, len(idxs)
        while lo < hi:
            mid = (lo + hi) // 2
            if idxs[mid] < left:
                lo = mid + 1
            else:
                hi = mid
        return lo
    def _right(self, idxs, right):
        lo, hi = 0, len(idxs)
        while lo < hi:
            mid = (lo + hi) // 2
            if idxs[mid] <= right:
                lo = mid + 1
            else:
                hi = mid
        return lo

# Example usage
if __name__ == "__main__":
    checker = MajorityChecker([1,1,2,2,1,1])
    print(checker.query(0,5,4))  # Output: 1
    print(checker.query(0,3,3))  # Output: -1
    print(checker.query(2,3,2))  # Output: 2
