"""
852. Peak Index in a Mountain Array

An array arr is a mountain if arr[0] < arr[1] < ... < arr[i] > arr[i+1] > ... > arr[arr.length - 1]. Return the index i of the peak.

Example 1:
Input: arr = [0,1,0]
Output: 1

Example 2:
Input: arr = [0,2,1,0]
Output: 1

Constraints:
- 3 <= arr.length <= 10^4
- 0 <= arr[i] <= 10^6
- arr is a mountain array.
"""
def peakIndexInMountainArray(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] < arr[m+1]:
            l = m + 1
        else:
            r = m
    return l

# Example usage:
print(peakIndexInMountainArray([0,1,0]))  # Output: 1
print(peakIndexInMountainArray([0,2,1,0]))  # Output: 1
