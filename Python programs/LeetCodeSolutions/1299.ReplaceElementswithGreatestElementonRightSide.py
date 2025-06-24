"""
LeetCode 1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element with the greatest element among the elements to its right, and replace the last element with -1.

Constraints:
- 1 <= arr.length <= 10^4
- 1 <= arr[i] <= 10^5

Example:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""
def replaceElements(arr):
    n = len(arr)
    max_right = -1
    for i in range(n-1, -1, -1):
        arr[i], max_right = max_right, max(max_right, arr[i])
    return arr

# Example usage:
arr = [17,18,5,4,6,1]
print(replaceElements(arr))  # Output: [18,6,6,6,1,-1]
