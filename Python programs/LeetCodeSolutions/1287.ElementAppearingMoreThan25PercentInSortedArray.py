"""
LeetCode 1287. Element Appearing More Than 25% In Sorted Array

Given a sorted array arr, return the element that appears more than 25% of the time.

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 10^5

Example:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
"""
def findSpecialInteger(arr):
    n = len(arr)
    for i in [n//4, n//2, 3*n//4]:
        if arr.count(arr[i]) > n//4:
            return arr[i]
    return arr[0]

# Example usage:
arr = [1,2,2,6,6,6,6,7,10]
print(findSpecialInteger(arr))  # Output: 6
