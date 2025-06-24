"""
LeetCode 1394. Find Lucky Integer in an Array

Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value. Return the largest lucky integer in the array. If there is no lucky integer, return -1.

Constraints:
- 1 <= arr.length <= 500
- 1 <= arr[i] <= 500

Example:
Input: arr = [2,2,3,4]
Output: 2
"""
def findLucky(arr):
    from collections import Counter
    count = Counter(arr)
    res = -1
    for k, v in count.items():
        if k == v:
            res = max(res, k)
    return res

# Example usage:
arr = [2,2,3,4]
print(findLucky(arr))  # Output: 2
