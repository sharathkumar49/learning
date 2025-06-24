"""
1246. Palindrome Removal

Given an array arr, return the minimum number of steps to remove all elements by removing palindromic subarrays.

Constraints:
- 1 <= arr.length <= 100
- 1 <= arr[i] <= 20

Example:
Input: arr = [1,2,3,2,1]
Output: 1

"""
def minimumMoves(arr):
    n = len(arr)
    dp = [[0]*n for _ in range(n)]
    for l in range(n-1, -1, -1):
        for r in range(l, n):
            if l == r:
                dp[l][r] = 1
            else:
                dp[l][r] = 1 + dp[l+1][r]
                for k in range(l+1, r+1):
                    if arr[l] == arr[k]:
                        dp[l][r] = min(dp[l][r], (dp[l+1][k-1] if k-1 >= l+1 else 0) + dp[k][r])
    return dp[0][n-1]

# Example usage
if __name__ == "__main__":
    print(minimumMoves([1,2,3,2,1]))  # Output: 1
