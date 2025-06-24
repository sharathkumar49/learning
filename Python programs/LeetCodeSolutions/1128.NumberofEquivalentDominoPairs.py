"""
1128. Number of Equivalent Domino Pairs

Given a list of dominoes, return the number of pairs of equivalent dominoes. Two dominoes [a, b] and [c, d] are equivalent if a == c and b == d, or a == d and b == c.

Constraints:
- 1 <= dominoes.length <= 40000
- 1 <= dominoes[i][j] <= 9

Example:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
"""
from typing import List
from collections import Counter

def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    count = Counter()
    res = 0
    for a, b in dominoes:
        key = tuple(sorted((a, b)))
        res += count[key]
        count[key] += 1
    return res

# Example usage:
dominoes = [[1,2],[2,1],[3,4],[5,6]]
print(numEquivDominoPairs(dominoes))  # Output: 1
