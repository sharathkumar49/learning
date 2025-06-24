"""
LeetCode 1340. Jump Game V

Given an array arr and an integer d, you can jump to any index i+d or i-d if arr[i] > arr[j] and 0 <= j < arr.length. Return the maximum number of indices you can visit starting from any index.

Constraints:
- 1 <= arr.length <= 1000
- 1 <= arr[i] <= 10^5
- 1 <= d <= arr.length

Example:
Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
"""
def maxJumps(arr, d):
    n = len(arr)
    dp = [0]*n
    def dfs(i):
        if dp[i]:
            return dp[i]
        res = 1
        for di in range(1, d+1):
            for j in [i-di, i+di]:
                if 0<=j<n and arr[j]<arr[i]:
                    if all(arr[k]<arr[i] for k in range(min(i,j)+1, max(i,j))):
                        res = max(res, 1+dfs(j))
        dp[i] = res
        return res
    return max(dfs(i) for i in range(n))

# Example usage:
arr = [6,4,14,6,8,13,9,7,10,6,12]
d = 2
print(maxJumps(arr, d))  # Output: 4
