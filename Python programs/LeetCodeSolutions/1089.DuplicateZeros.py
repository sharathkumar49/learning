"""
1089. Duplicate Zeros

Given a fixed-length array arr, duplicate each occurrence of zero, shifting the remaining elements to the right. Elements beyond the length of the array are not written. Modify the input array in-place.

Constraints:
- 1 <= arr.length <= 10^4
- 0 <= arr[i] <= 9

Example:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
"""
from typing import List

def duplicateZeros(arr: List[int]) -> None:
    n = len(arr)
    zeros = arr.count(0)
    for i in range(n-1, -1, -1):
        if i + zeros < n:
            arr[i + zeros] = arr[i]
        if arr[i] == 0:
            zeros -= 1
            if i + zeros < n:
                arr[i + zeros] = 0

# Example usage:
arr = [1,0,2,3,0,4,5,0]
duplicateZeros(arr)
print(arr)  # Output: [1, 0, 0, 2, 3, 0, 0, 4]
