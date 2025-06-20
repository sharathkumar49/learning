"""
528. Random Pick with Weight

Given an array w of positive integers, write a function pickIndex which randomly picks an index in proportion to its weight.

Constraints:
- 1 <= w.length <= 10^4
- 1 <= w[i] <= 10^5

Example:
Input: w = [1,3]
Output: 1 (with probability 0.75), 0 (with probability 0.25)
"""

import random
import bisect

class Solution:
    def __init__(self, w: list):
        self.prefix = []
        s = 0
        for x in w:
            s += x
            self.prefix.append(s)
        self.total = s
    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, x)

# Example usage:
sol = Solution([1,3])
print([sol.pickIndex() for _ in range(10)])  # Output: mostly 1's, some 0's
