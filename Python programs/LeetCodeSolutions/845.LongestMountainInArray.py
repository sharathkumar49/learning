"""
845. Longest Mountain in Array

Given an array arr, return the length of the longest mountain. A mountain is defined as a sequence that increases and then decreases, with at least 3 elements.

Example 1:
Input: arr = [2,1,4,7,3,2,5]
Output: 5

Example 2:
Input: arr = [2,2,2]
Output: 0

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 10^6
"""
def longestMountain(arr):
    n = len(arr)
    ans = 0
    i = 1
    while i < n-1:
        if arr[i-1] < arr[i] > arr[i+1]:
            l, r = i, i
            while l > 0 and arr[l-1] < arr[l]:
                l -= 1
            while r < n-1 and arr[r] > arr[r+1]:
                r += 1
            ans = max(ans, r-l+1)
            i = r
        i += 1
    return ans

# Example usage:
print(longestMountain([2,1,4,7,3,2,5]))  # Output: 5
print(longestMountain([2,2,2]))          # Output: 0
