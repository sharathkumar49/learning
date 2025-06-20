"""
276. Paint Fence
https://leetcode.com/problems/paint-fence/

You are painting a fence of n posts with k different colors. You must paint the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.

Constraints:
- 1 <= n <= 50
- 1 <= k <= 100

Example 1:
Input: n = 3, k = 2
Output: 6

Example 2:
Input: n = 1, k = 1
Output: 1
"""
def numWays(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k
    same, diff = 0, k
    for i in range(2, n+1):
        same, diff = diff, (same + diff) * (k - 1)
    return same + diff

# Example usage:
if __name__ == "__main__":
    print(numWays(3, 2))  # Output: 6
    print(numWays(1, 1))  # Output: 1
