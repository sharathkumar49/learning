"""
LeetCode 1282. Group the People Given the Group Size They Belong To

Given an array groupSizes, group the people so that each group has the same size as specified. Return a list of groups.

Constraints:
- groupSizes.length == n
- 1 <= n <= 500
- 1 <= groupSizes[i] <= n

Example:
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
"""
def groupThePeople(groupSizes):
    from collections import defaultdict
    res = []
    groups = defaultdict(list)
    for i, size in enumerate(groupSizes):
        groups[size].append(i)
        if len(groups[size]) == size:
            res.append(groups[size][:])
            groups[size] = []
    return res

# Example usage:
groupSizes = [3,3,3,3,3,1,3]
print(groupThePeople(groupSizes))  # Output: [[0,1,2],[3,4,6],[5]]
