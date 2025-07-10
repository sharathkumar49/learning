"""
LeetCode 1713. Minimum Operations to Make a Subsequence

Given two integer arrays target and arr, return the minimum number of operations to make target a subsequence of arr. In one operation, you can insert any integer at any position in arr.

Example 1:
Input: target = [5,1,3], arr = [9,4,2,3,4]
Output: 2

Constraints:
- 1 <= target.length, arr.length <= 10^5
- 1 <= target[i], arr[i] <= 10^9
"""

def minOperations(target, arr):
    pos = {x: i for i, x in enumerate(target)}
    seq = [pos[x] for x in arr if x in pos]
    import bisect
    lis = []
    for x in seq:
        idx = bisect.bisect_left(lis, x)
        if idx == len(lis):
            lis.append(x)
        else:
            lis[idx] = x
    return len(target) - len(lis)

# Example usage:
# target = [5,1,3]
# arr = [9,4,2,3,4]
# print(minOperations(target, arr))  # Output: 2
