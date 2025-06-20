"""
LeetCode 668. Kth Smallest Number in Multiplication Table

Nearly every one have used the Multiplication Table. But could you find the k-th smallest number in the m x n multiplication table?

Given the height m and the length n of a m x n multiplication table, and a positive integer k, return the k-th smallest number in the m x n multiplication table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The multiplication table is:
1 2 3
2 4 6
3 6 9
The 5th smallest number is 3.

Example 2:
Input: m = 2, n = 3, k = 6
Output: 6

Constraints:
- 1 <= m, n <= 3 * 10^4
- 1 <= k <= m * n
"""

def findKthNumber(m: int, n: int, k: int) -> int:
    def count(x):
        return sum(min(x // i, n) for i in range(1, m+1))
    left, right = 1, m * n
    while left < right:
        mid = (left + right) // 2
        if count(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left

# Example usage
if __name__ == "__main__":
    print(findKthNumber(3, 3, 5))  # Output: 3
    print(findKthNumber(2, 3, 6))  # Output: 6
