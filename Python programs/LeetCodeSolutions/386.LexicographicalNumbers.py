"""
386. Lexicographical Numbers

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

Constraints:
- 1 <= n <= 5 * 10^4
"""
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(curr):
            if curr > n:
                return
            res.append(curr)
            for i in range(10):
                if curr * 10 + i > n:
                    break
                if curr * 10 + i != 0:
                    dfs(curr * 10 + i)
        for i in range(1, 10):
            dfs(i)
        return res

# Example usage:
n = 13
print(Solution().lexicalOrder(n))  # Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
