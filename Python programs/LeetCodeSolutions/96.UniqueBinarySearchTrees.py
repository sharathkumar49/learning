"""
96. Unique Binary Search Trees
https://leetcode.com/problems/unique-binary-search-trees/

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Constraints:
- 1 <= n <= 19

Example:
Input: n = 3
Output: 5
"""
def numTrees(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1
    for nodes in range(1, n + 1):
        for root in range(1, nodes + 1):
            dp[nodes] += dp[root - 1] * dp[nodes - root]
    return dp[n]

# Example usage:
if __name__ == "__main__":
    print(numTrees(3))  # Output: 5
    print(numTrees(1))  # Output: 1
