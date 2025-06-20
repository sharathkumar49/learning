"""
372. Super Pow

Your task is to calculate a^b mod 1337 where a is a positive integer and b is a very large positive integer represented as an array.

Constraints:
- 1 <= a <= 2^31 - 1
- 1 <= b.length <= 2000
- 0 <= b[i] <= 9
"""
from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def mod_pow(a, k):
            res = 1
            a %= 1337
            for _ in range(k):
                res = (res * a) % 1337
            return res
        if not b:
            return 1
        last = b.pop()
        part1 = mod_pow(self.superPow(a, b), 10)
        part2 = mod_pow(a, last)
        return (part1 * part2) % 1337

# Example usage:
a = 2
b = [3]
print(Solution().superPow(a, b))  # Output: 8
