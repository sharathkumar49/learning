"""
1202. Smallest String With Swaps

Given a string s and a list of pairs of indices, you can swap the characters at any pair of indices any number of times. Return the lexicographically smallest string possible.

Constraints:
- 1 <= s.length <= 10^5
- 0 <= pairs.length <= 10^5
- 0 <= pairs[i][0], pairs[i][1] < s.length

Example:
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"

"""
def smallestStringWithSwaps(s, pairs):
    from collections import defaultdict
    parent = list(range(len(s)))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in pairs:
        pa, pb = find(a), find(b)
        if pa != pb:
            parent[pa] = pb
    groups = defaultdict(list)
    for i in range(len(s)):
        groups[find(i)].append(i)
    res = list(s)
    for idxs in groups.values():
        chars = sorted(res[i] for i in idxs)
        for i, c in zip(sorted(idxs), chars):
            res[i] = c
    return ''.join(res)

# Example usage
if __name__ == "__main__":
    print(smallestStringWithSwaps("dcab", [[0,3],[1,2]]))  # Output: "bacd"
