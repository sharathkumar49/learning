"""
823. Binary Trees With Factors

Given an array of unique integers arr, return the number of binary trees we can make where each non-leaf node's value is the product of its children's values. The answer may be too large, so return it modulo 10^9 + 7.

Example 1:
Input: arr = [2,4]
Output: 3

Example 2:
Input: arr = [2,4,5,10]
Output: 7

Constraints:
- 1 <= arr.length <= 1000
- 2 <= arr[i] <= 10^9
- All the values of arr are unique.
"""
def numFactoredBinaryTrees(arr):
    arr.sort()
    dp = {}
    index = {x: i for i, x in enumerate(arr)}
    for i, x in enumerate(arr):
        dp[x] = 1
        for j in range(i):
            if x % arr[j] == 0 and x // arr[j] in dp:
                dp[x] += dp[arr[j]] * dp[x // arr[j]]
    return sum(dp.values()) % (10**9 + 7)

# Example usage:
print(numFactoredBinaryTrees([2,4]))  # Output: 3
print(numFactoredBinaryTrees([2,4,5,10]))  # Output: 7
