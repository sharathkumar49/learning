"""
900. RLE Iterator
https://leetcode.com/problems/rle-iterator/

Write an iterator that iterates through a run-length encoded sequence.
Implement the RLEIterator class:
- RLEIterator(int[] encoding) Initializes the object with the encoded array encoding.
- int next(int n) Exhausts the next n elements and returns the last element exhausted. If there is no element left to exhaust, return -1 instead.

Constraints:
- 2 <= encoding.length <= 10000
- encoding.length is even.
- 0 <= encoding[i] <= 10^9
- 1 <= n <= 10^9

Example:
Input: ["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
Output: [null,8,8,5,-1]
"""
from typing import List

class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.idx = 0

    def next(self, n: int) -> int:
        while self.idx < len(self.encoding) and n > 0:
            if self.encoding[self.idx] >= n:
                self.encoding[self.idx] -= n
                return self.encoding[self.idx+1]
            n -= self.encoding[self.idx]
            self.idx += 2
        return -1

# Example usage
if __name__ == "__main__":
    rle = RLEIterator([3,8,0,9,2,5])
    print(rle.next(2))  # Output: 8
    print(rle.next(1))  # Output: 8
    print(rle.next(1))  # Output: 5
    print(rle.next(2))  # Output: -1
