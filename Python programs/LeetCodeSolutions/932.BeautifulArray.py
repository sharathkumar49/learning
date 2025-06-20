"""
932. Beautiful Array
https://leetcode.com/problems/beautiful-array/

For some fixed n, an array is beautiful if for every i < j, there is no k with i < k < j such that A[k] * 2 == A[i] + A[j].
Given n, return any beautiful array A of length n. (It is guaranteed that one exists.)

Constraints:
- 1 <= n <= 1000

Example:
Input: n = 4
Output: [2,1,4,3]
"""
from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        res = [1]
        while len(res) < n:
            res = [x*2-1 for x in res] + [x*2 for x in res]
            res = [x for x in res if x <= n]
        return res

# Example usage
if __name__ == "__main__":
    n = 4
    print(Solution().beautifulArray(n))  # Output: [1, 3, 2, 4] or any valid beautiful array
