"""
1088. Confusing Number II

Return the total number of confusing numbers between 1 and N inclusive.
A confusing number is a number that when rotated 180 degrees becomes a different valid number.

Constraints:
- 1 <= N <= 10^9

Example:
Input: N = 20
Output: 6
"""
def confusingNumberII(N: int) -> int:
    mapping = {0:0, 1:1, 6:9, 8:8, 9:6}
    res = 0
    def dfs(num, rotated, base):
        nonlocal res
        if num > N:
            return
        if num != rotated:
            res += 1
        for d in mapping:
            if num * 10 + d > N or num * 10 + d == 0:
                continue
            dfs(num * 10 + d, mapping[d] * base + rotated, base * 10)
    for d in [1,6,8,9]:
        dfs(d, mapping[d], 10)
    return res

# Example usage:
N = 20
print(confusingNumberII(N))  # Output: 6
