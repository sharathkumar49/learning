"""
LeetCode 1562. Find Latest Group of Size M

Given an array arr and an integer m, return the latest step at which there exists a group of ones of length m.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= arr.length
- 1 <= m <= arr.length

Example:
Input: arr = [3,5,1,2,4], m = 1
Output: 4
"""
def findLatestStep(arr, m):
    n = len(arr)
    if m == n:
        return n
    length = [0] * (n + 2)
    count = [0] * (n + 1)
    res = -1
    for step, i in enumerate(arr):
        l = length[i - 1]
        r = length[i + 1]
        length[i - l] = length[i + r] = l + r + 1
        count[l] -= 1
        count[r] -= 1
        count[l + r + 1] += 1
        if count[m]:
            res = step + 1
    return res

# Example usage:
arr = [3,5,1,2,4]
m = 1
print(findLatestStep(arr, m))  # Output: 4
