"""
1122. Relative Sort Array

Given two arrays arr1 and arr2, sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements not in arr2 should be placed at the end in ascending order.

Constraints:
- 1 <= arr1.length, arr2.length <= 1000
- 0 <= arr1[i], arr2[i] <= 1000
- All elements in arr2 are distinct.

Example:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
"""
from typing import List

def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    order = {x: i for i, x in enumerate(arr2)}
    return sorted(arr1, key=lambda x: order.get(x, x + 1000))

# Example usage:
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(relativeSortArray(arr1, arr2))  # Output: [2,2,2,1,4,3,3,9,6,7,19]
