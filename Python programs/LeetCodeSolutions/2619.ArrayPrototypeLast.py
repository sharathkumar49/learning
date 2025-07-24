"""
LeetCode 2619. Array Prototype Last

Implement Array.prototype.last for a list.

Constraints:
- 0 <= arr.length <= 10^5
"""

def arrayLast(arr):
    return arr[-1] if arr else -1
# Example usage:
# print(arrayLast([1,2,3]))  # Output: 3
# print(arrayLast([]))       # Output: -1
