"""
LeetCode 1356. Sort Integers by The Number of 1 Bits

Given an array arr, sort it by the number of 1 bits in their binary representation. If two numbers have the same number of 1 bits, sort them by value.

Constraints:
- 1 <= arr.length <= 500
- 0 <= arr[i] <= 10^4

Example:
Input: arr = [0,1,2,3,4,5,6,7,8]
Output: [0,1,2,4,8,3,5,6,7]
"""
def sortByBits(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# Example usage:
arr = [0,1,2,3,4,5,6,7,8]
print(sortByBits(arr))  # Output: [0,1,2,4,8,3,5,6,7]
