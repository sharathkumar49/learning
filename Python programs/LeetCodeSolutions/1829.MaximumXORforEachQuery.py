"""
LeetCode 1829. Maximum XOR for Each Query

Given an array arr and an integer maximumBit, return the answer to each query as described in the problem.

Example 1:
Input: arr = [0,1,1,3], maximumBit = 2
Output: [0,3,2,3]

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= maximumBit <= 20
"""

def getMaximumXor(arr, maximumBit):
    res = []
    x = 0
    for a in arr:
        x ^= a
    for i in range(len(arr)-1, -1, -1):
        res.append(x ^ ((1<<maximumBit)-1))
        x ^= arr[i]
    return res

# Example usage:
# arr = [0,1,1,3]
# maximumBit = 2
# print(getMaximumXor(arr, maximumBit))  # Output: [0,3,2,3]
