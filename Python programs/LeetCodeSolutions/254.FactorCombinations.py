"""
254. Factor Combinations
https://leetcode.com/problems/factor-combinations/

Numbers can be regarded as the product of their factors. Return all possible combinations of its factors.

Constraints:
- 1 <= n <= 10^7

Example 1:
Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]

Example 2:
Input: n = 37
Output: []
"""
def getFactors(n):
    res = []
    def backtrack(start, n, path):
        for i in range(start, int(n ** 0.5) + 1):
            if n % i == 0:
                res.append(path + [i, n // i])
                backtrack(i, n // i, path + [i])
    backtrack(2, n, [])
    return res

# Example usage:
if __name__ == "__main__":
    print(getFactors(12))  # Output: [[2,6],[3,4],[2,2,3]]
    print(getFactors(37))  # Output: []
