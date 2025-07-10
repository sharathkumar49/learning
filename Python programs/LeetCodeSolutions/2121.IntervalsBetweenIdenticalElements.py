"""
LeetCode 2121. Intervals Between Identical Elements

Given an array arr, return an array intervals where intervals[i] is the sum of the distances between arr[i] and all other identical elements.

Example:
Input: arr = [2,1,3,1,2,3,3]
Output: [4,2,7,2,4,4,5]

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^5
"""

def getDistances(arr):
    from collections import defaultdict
    pos = defaultdict(list)
    for i, x in enumerate(arr):
        pos[x].append(i)
    res = [0]*len(arr)
    for idxs in pos.values():
        pre = [0]
        for i in idxs:
            pre.append(pre[-1]+i)
        n = len(idxs)
        for j, i in enumerate(idxs):
            left = i*j - pre[j]
            right = pre[n]-pre[j+1] - i*(n-j-1)
            res[i] = left + right
    return res

# Example usage:
# print(getDistances([2,1,3,1,2,3,3]))  # Output: [4,2,7,2,4,4,5]
