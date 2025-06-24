"""
LeetCode 1426. Counting Elements

Given an integer array arr, count the number of elements x such that x + 1 is also in arr.

Constraints:
- 1 <= arr.length <= 1000
- 0 <= arr[i] <= 1000

Example:
Input: arr = [1,2,3]
Output: 2
"""
def countElements(arr):
    s = set(arr)
    return sum(1 for x in arr if x+1 in s)

# Example usage:
arr = [1,2,3]
print(countElements(arr))  # Output: 2
