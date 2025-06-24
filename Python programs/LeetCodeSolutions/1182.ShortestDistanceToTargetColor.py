"""
1182. Shortest Distance to Target Color

You are given a list colors, where colors[i] is the color of the ith house, and a list queries where each query is [i, c]. For each query, return the shortest distance from house i to a house with color c. If no such house exists, return -1.

Constraints:
- 1 <= colors.length <= 5 * 10^4
- 1 <= colors[i] <= 3
- 1 <= queries.length <= 5 * 10^4

Example:
Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
Output: [3,0,3]

"""
def shortestDistanceColor(colors, queries):
    n = len(colors)
    pos = {1: [], 2: [], 3: []}
    for i, c in enumerate(colors):
        pos[c].append(i)
    from bisect import bisect_left
    res = []
    for i, c in queries:
        idxs = pos[c]
        if not idxs:
            res.append(-1)
            continue
        idx = bisect_left(idxs, i)
        ans = float('inf')
        if idx < len(idxs):
            ans = min(ans, abs(idxs[idx] - i))
        if idx > 0:
            ans = min(ans, abs(idxs[idx-1] - i))
        res.append(ans)
    return res

# Example usage
if __name__ == "__main__":
    colors = [1,1,2,1,3,2,2,3,3]
    queries = [[1,3],[2,2],[6,1]]
    print(shortestDistanceColor(colors, queries))  # Output: [3,0,3]
