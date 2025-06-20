"""
851. Loud and Rich

There are n people with different amounts of money and a list richer[i] = [a, b] meaning a is richer than b. Also, quiet[i] is the quietness of the i-th person. Return the answer array where answer[x] = y means y is the least quiet person among all people who are at least as rich as x.

Example 1:
Input: richer = [[1,0],[2,1]], quiet = [0,1,2]
Output: [0,1,2]

Constraints:
- 1 <= n <= 500
- 0 <= quiet[i] < n
- All the values of quiet are unique.
- 0 <= richer.length <= n * (n - 1) / 2
- 0 <= a, b < n
- a != b
"""
def loudAndRich(richer, quiet):
    n = len(quiet)
    from collections import defaultdict
    graph = defaultdict(list)
    for a, b in richer:
        graph[b].append(a)
    ans = [-1] * n
    def dfs(x):
        if ans[x] != -1:
            return ans[x]
        ans[x] = x
        for y in graph[x]:
            if quiet[dfs(y)] < quiet[ans[x]]:
                ans[x] = dfs(y)
        return ans[x]
    for i in range(n):
        dfs(i)
    return ans

# Example usage:
print(loudAndRich([[1,0],[2,1]], [0,1,2]))  # Output: [0,1,2]
