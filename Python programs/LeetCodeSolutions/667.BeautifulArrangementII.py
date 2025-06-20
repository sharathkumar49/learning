"""
LeetCode 667. Beautiful Arrangement II

Given two integers n and k, construct a list answer that contains n different positive integers ranging from 1 to n and obeys the following requirement:

Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, ... , |an-1 - an|] has exactly k distinct integers.

Return the list answer. If there are multiple valid answers, return any of them.

Example 1:
Input: n = 3, k = 1
Output: [1,2,3]
Explanation: The [1,2,3] has [1,1] with only 1 distinct value: 1.

Example 2:
Input: n = 3, k = 2
Output: [1,3,2]
Explanation: The [1,3,2] has [2,1] with 2 distinct values: 1 and 2.

Constraints:
- 1 <= k < n <= 10^4
"""
from typing import List

def constructArray(n: int, k: int) -> List[int]:
    res = []
    l, r = 1, n
    for i in range(k):
        if i % 2 == 0:
            res.append(l)
            l += 1
        else:
            res.append(r)
            r -= 1
    if k % 2 == 0:
        res += list(range(r, l-1, -1))
    else:
        res += list(range(l, r+1))
    return res

# Example usage
if __name__ == "__main__":
    print(constructArray(3, 1))  # Output: [1,2,3]
    print(constructArray(3, 2))  # Output: [1,3,2]
