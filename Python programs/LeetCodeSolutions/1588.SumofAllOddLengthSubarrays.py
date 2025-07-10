"""
LeetCode 1588. Sum of All Odd Length Subarrays

Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

Example 1:
Input: arr = [1,4,2,5,3]
Output: 58

Constraints:
- 1 <= arr.length <= 100
- 1 <= arr[i] <= 1000
"""

def sumOddLengthSubarrays(arr):
    n = len(arr)
    res = 0
    for i in range(n):
        for l in range(1, n+1, 2):
            if i + l <= n:
                res += sum(arr[i:i+l])
    return res

# Example usage:
# arr = [1,4,2,5,3]
# print(sumOddLengthSubarrays(arr))  # Output: 58
