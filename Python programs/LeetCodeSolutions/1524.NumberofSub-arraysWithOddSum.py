"""
LeetCode 1524. Number of Sub-arrays With Odd Sum

Given an array of integers arr, return the number of sub-arrays with odd sum. Since the answer may be too large, return it modulo 10^9 + 7.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 100

Example:
Input: arr = [1,3,5]
Output: 4
"""
def numOfSubarrays(arr):
    mod = 10**9 + 7
    odd = even = res = 0
    for a in arr:
        if a % 2:
            odd, even = even + 1, odd
        else:
            odd, even = odd, even + 1
        res = (res + odd) % mod
    return res

# Example usage:
arr = [1,3,5]
print(numOfSubarrays(arr))  # Output: 4
