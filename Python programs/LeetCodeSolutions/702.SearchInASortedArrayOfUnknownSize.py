"""
LeetCode 702. Search in a Sorted Array of Unknown Size

Given an integer array sorted in ascending order, unknown size, and an interface ArrayReader, return the index of target if it exists, otherwise return -1.

The ArrayReader interface has the following functions:
- int get(int index): returns the value at index, or 2^31-1 if index is out of bounds.

Example 1:
Input: array = [-1,0,3,5,9,12], target = 9
Output: 4

Constraints:
- 1 <= array.length <= 10^4
- -10^4 <= array[i], target <= 10^4
- array is sorted in ascending order.
- array.length is unknown to you.
"""
# The ArrayReader API is not implemented here. This is a template for LeetCode.
class ArrayReader:
    def get(self, index: int) -> int:
        pass

def search(reader: 'ArrayReader', target: int) -> int:
    left, right = 0, 1
    while reader.get(right) < target:
        left = right
        right <<= 1
    while left <= right:
        mid = (left + right) // 2
        val = reader.get(mid)
        if val == target:
            return mid
        elif val > target or val == 2**31-1:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# Example usage (not executable without ArrayReader implementation)
# reader = ArrayReader([-1,0,3,5,9,12])
# print(search(reader, 9))  # Output: 4
