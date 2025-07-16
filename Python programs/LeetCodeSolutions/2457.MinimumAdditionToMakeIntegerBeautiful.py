"""
LeetCode 2457. Minimum Addition to Make Integer Beautiful

Given n and target, return the minimum addition to make n beautiful.

Constraints:
- 1 <= n, target <= 10^12
"""

def makeIntegerBeautiful(n, target):
    add = 0
    while sum(map(int,str(n+add))) > target:
        p = 10**len(str(n+add))-((n+add)%10**len(str(n+add)))
        add += p
    return add

# Example usage:
# print(makeIntegerBeautiful(16,6))  # Output: 4
