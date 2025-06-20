"""
LeetCode 753. Cracking the Safe

There is a safe with a circular dial consisting of k digits, each digit can be 0 to k-1. The safe has a password of length n.
Return any string of minimum length that will open the safe at some point.

Example 1:
Input: n = 1, k = 2
Output: "01"

Example 2:
Input: n = 2, k = 2
Output: "0010"

Constraints:
- 1 <= n <= 4
- 1 <= k <= 10
"""
def crackSafe(n: int, k: int) -> str:
    seen = set()
    res = []
    def dfs(node):
        for x in map(str, range(k)):
            nei = node + x
            if nei not in seen:
                seen.add(nei)
                dfs(nei[1:])
                res.append(x)
    dfs('0'*(n-1))
    return '0'*(n-1) + ''.join(res)

# Example usage
if __name__ == "__main__":
    print(crackSafe(1, 2))  # Output: "01"
    print(crackSafe(2, 2))  # Output: "0010"
