"""
LeetCode 1718. Construct the Lexicographically Largest Valid Sequence

Given an integer n, construct a sequence of length 2n-1 such that each integer from 1 to n appears exactly twice, except for 1 which appears once, and the two occurrences of k are k apart. Return the lexicographically largest sequence.

Example 1:
Input: n = 3
Output: [3,1,2,3,2]

Constraints:
- 1 <= n <= 20
"""

def constructDistancedSequence(n):
    res = [0] * (2 * n - 1)
    used = [False] * (n + 1)
    def dfs(i):
        if i == len(res):
            return True
        if res[i]:
            return dfs(i+1)
        for k in range(n, 0, -1):
            if used[k]:
                continue
            if k == 1:
                res[i] = 1
                used[1] = True
                if dfs(i+1):
                    return True
                res[i] = 0
                used[1] = False
            elif i + k < len(res) and not res[i] and not res[i+k]:
                res[i] = res[i+k] = k
                used[k] = True
                if dfs(i+1):
                    return True
                res[i] = res[i+k] = 0
                used[k] = False
        return False
    dfs(0)
    return res

# Example usage:
# n = 3
# print(constructDistancedSequence(3))  # Output: [3,1,2,3,2]
