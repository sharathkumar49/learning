"""
967. Numbers With Same Consecutive Differences
https://leetcode.com/problems/numbers-with-same-consecutive-differences/

Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k. You may return the answer in any order.

Constraints:
- 2 <= n <= 9
- 0 <= k <= 9

Example:
Input: n = 3, k = 7
Output: [181,292,707,818,929]
"""
from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = list(range(1, 10))
        for _ in range(n-1):
            temp = []
            for x in res:
                d = x % 10
                if d + k < 10:
                    temp.append(x * 10 + d + k)
                if k > 0 and d - k >= 0:
                    temp.append(x * 10 + d - k)
            res = temp
        return res

# Example usage
if __name__ == "__main__":
    n = 3
    k = 7
    print(Solution().numsSameConsecDiff(n, k))  # Output: [181,292,707,818,929]
