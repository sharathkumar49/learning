"""
839. Similar String Groups

Two strings are similar if you can swap two letters (in different positions) to make them equal. Return the number of groups of similar strings.

Example 1:
Input: strs = ["tars","rats","arts","star"]
Output: 2

Example 2:
Input: strs = ["omv","ovm"]
Output: 1

Constraints:
- 1 <= strs.length <= 300
- 1 <= strs[i].length <= 300
- All strings have the same length.
- All strings consist of lowercase letters only.
"""
def numSimilarGroups(strs):
    def is_similar(a, b):
        diff = [(x, y) for x, y in zip(a, b) if x != y]
        return len(diff) == 2 and diff[0] == diff[1][::-1] or len(diff) == 0
    n = len(strs)
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i in range(n):
        for j in range(i+1, n):
            if is_similar(strs[i], strs[j]):
                pi, pj = find(i), find(j)
                if pi != pj:
                    parent[pi] = pj
    return sum(i == find(i) for i in range(n))

# Example usage:
print(numSimilarGroups(["tars","rats","arts","star"]))  # Output: 2
print(numSimilarGroups(["omv","ovm"]))  # Output: 1
