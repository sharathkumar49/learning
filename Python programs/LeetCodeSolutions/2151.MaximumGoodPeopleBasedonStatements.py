"""
LeetCode 2151. Maximum Good People Based on Statements

There are n people. Each person makes statements about others, where statements[i][j] is 0 (bad), 1 (good), or 2 (no statement). Return the maximum number of good people possible such that all statements made by good people are true.

Example:
Input: statements = [[2,1,2],[1,2,2],[2,0,2]]
Output: 2

Constraints:
- 2 <= n <= 15
- statements[i][j] in {0,1,2}
"""

def maximumGood(statements):
    n = len(statements)
    res = 0
    for mask in range(1<<n):
        valid = True
        for i in range(n):
            if not (mask & (1<<i)):
                continue
            for j in range(n):
                if statements[i][j] == 2:
                    continue
                if ((mask & (1<<j)) > 0) != (statements[i][j] == 1):
                    valid = False
        if valid:
            res = max(res, bin(mask).count('1'))
    return res

# Example usage:
# print(maximumGood([[2,1,2],[1,2,2],[2,0,2]]))  # Output: 2
