"""
LeetCode 1846. Maximum Element After Decreasing and Rearranging

Given an array of positive integers arr, perform the following operations:
- Rearrange the elements in any order.
- Decrease the value of any element to a smaller positive integer.
Return the maximum possible value of the largest element after performing the operations such that the array satisfies arr[0] = 1 and abs(arr[i] - arr[i-1]) <= 1 for each i > 0.

Example 1:
Input: arr = [2,2,1,2,1]
Output: 2

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^9
"""

def maximumElementAfterDecrementingAndRearranging(arr):
    arr.sort()
    arr[0] = 1
    for i in range(1, len(arr)):
        arr[i] = min(arr[i], arr[i-1]+1)
    return arr[-1]

# Example usage:
# arr = [2,2,1,2,1]
# print(maximumElementAfterDecrementingAndRearranging(arr))  # Output: 2
