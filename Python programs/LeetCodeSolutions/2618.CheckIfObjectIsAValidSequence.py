"""
LeetCode 2618. Check if Object is a Valid Sequence

Given arr and sequence, return True if sequence is a valid subsequence of arr.

Constraints:
- 1 <= arr.length, sequence.length <= 10^5
"""

def isValidSequence(arr, sequence):
    it = iter(arr)
    return all(x in it for x in sequence)
# Example usage:
# print(isValidSequence([1,2,3,4], [2,4]))  # Output: True
