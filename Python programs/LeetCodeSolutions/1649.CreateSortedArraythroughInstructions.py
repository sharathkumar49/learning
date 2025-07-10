"""
LeetCode 1649. Create Sorted Array through Instructions

Given an array of instructions, return the cost to create a sorted array. The cost is the minimum of the number of elements less than and greater than the current element. Return the answer modulo 10^9+7.

Example 1:
Input: instructions = [1,5,6,2]
Output: 1

Constraints:
- 1 <= instructions.length <= 10^5
- 1 <= instructions[i] <= 10^5
"""

def createSortedArray(instructions):
    import bisect
    arr = []
    res = 0
    mod = 10**9+7
    for x in instructions:
        l = bisect.bisect_left(arr, x)
        r = bisect.bisect_right(arr, x)
        res = (res + min(l, len(arr)-r)) % mod
        arr.insert(r, x)
    return res

# Example usage:
# instructions = [1,5,6,2]
# print(createSortedArray(instructions))  # Output: 1
