"""
LeetCode 1574. Shortest Subarray to be Removed to Make Array Sorted

Given an array arr, return the length of the shortest subarray to remove to make arr sorted in non-decreasing order.

Constraints:
- 1 <= arr.length <= 10^5
- 0 <= arr[i] <= 10^9

Example:
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
"""
def findLengthOfShortestSubarray(arr):
    n = len(arr)
    left = 0
    while left+1 < n and arr[left] <= arr[left+1]:
        left += 1
    if left == n-1:
        return 0
    right = n-1
    while right > 0 and arr[right-1] <= arr[right]:
        right -= 1
    res = min(n-left-1, right)
    i, j = 0, right
    while i <= left and j < n:
        if arr[i] <= arr[j]:
            res = min(res, j-i-1)
            i += 1
        else:
            j += 1
    return res

# Example usage:
arr = [1,2,3,10,4,2,3,5]
print(findLengthOfShortestSubarray(arr))  # Output: 3
