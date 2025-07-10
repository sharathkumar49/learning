"""
LeetCode 1619. Mean of Array After Removing Some Elements

Given an integer array arr, return the mean of the remaining elements after removing the smallest 5% and the largest 5% of the elements. Answers within 10^-5 of the actual answer will be accepted.

Example 1:
Input: arr = [6,2,7,5,1,2,0,10,3,2,5,5,5,5,5,5,5,5,5,5]
Output: 4.00000

Constraints:
- 20 <= arr.length <= 1000
- arr.length is a multiple of 20.
- 0 <= arr[i] <= 10^5
"""

def trimMean(arr):
    arr.sort()
    n = len(arr)
    k = n // 20
    return sum(arr[k:-k]) / (n - 2*k)

# Example usage:
# arr = [6,2,7,5,1,2,0,10,3,2,5,5,5,5,5,5,5,5,5,5]
# print(trimMean(arr))  # Output: 4.0
