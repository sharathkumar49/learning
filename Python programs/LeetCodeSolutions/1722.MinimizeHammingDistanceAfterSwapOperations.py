"""
LeetCode 1722. Minimize Hamming Distance After Swap Operations

Given two arrays source and target and a list of allowed swap pairs, return the minimum Hamming distance after any number of swaps.

Example 1:
Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
Output: 1

Constraints:
- 1 <= source.length == target.length <= 10^5
- 0 <= source[i], target[i] <= 10^5
- 0 <= allowedSwaps.length <= 10^5
"""

def minimumHammingDistance(source, target, allowedSwaps):
    from collections import defaultdict, Counter
    n = len(source)
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in allowedSwaps:
        parent[find(a)] = find(b)
    groups = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    res = 0
    for idxs in groups.values():
        sc = Counter(source[i] for i in idxs)
        tc = Counter(target[i] for i in idxs)
        res += sum((sc - tc).values())
    return res

# Example usage:
# source = [1,2,3,4]
# target = [2,1,4,5]
# allowedSwaps = [[0,1],[2,3]]
# print(minimumHammingDistance(source, target, allowedSwaps))  # Output: 1
