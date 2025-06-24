"""
1218. Longest Arithmetic Subsequence of Given Difference

Given an integer array arr and an integer difference, return the length of the longest subsequence such that the difference between adjacent elements is equal to difference.

Constraints:
- 1 <= arr.length <= 10^5
- -10^4 <= arr[i], difference <= 10^4

Example:
Input: arr = [1,2,3,4], difference = 1
Output: 4

"""
def longestSubsequence(arr, difference):
    dp = {}
    res = 0
    for x in arr:
        dp[x] = dp.get(x - difference, 0) + 1
        res = max(res, dp[x])
    return res

# Example usage
if __name__ == "__main__":
    print(longestSubsequence([1,2,3,4], 1))  # Output: 4
