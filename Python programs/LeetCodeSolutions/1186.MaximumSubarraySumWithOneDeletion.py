"""
1186. Maximum Subarray Sum with One Deletion

Given an array arr, return the maximum sum of a non-empty subarray with at most one deletion.

Constraints:
- 1 <= arr.length <= 10^5
- -10^4 <= arr[i] <= 10^4

Example:
Input: arr = [1,-2,0,3]
Output: 4

"""
def maximumSum(arr):
    n = len(arr)
    dp0 = arr[0]
    dp1 = float('-inf')
    res = arr[0]
    for i in range(1, n):
        dp1 = max(dp0, dp1 + arr[i])
        dp0 = max(arr[i], dp0 + arr[i])
        res = max(res, dp0, dp1)
    return res

# Example usage
if __name__ == "__main__":
    print(maximumSum([1,-2,0,3]))  # Output: 4
