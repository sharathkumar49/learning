"""
LeetCode 1514. Path with Maximum Probability

Given an undirected weighted graph, return the maximum probability of reaching from start to end.

Constraints:
- 2 <= n <= 10^4
- 0 <= edges.length <= 2 * 10^4
- 0 <= a, b < n
- 0 <= succProb.length == edges.length
- 0 <= succProb[i] <= 1
- start != end

Example:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25
"""
def maxProbability(n, edges, succProb, start, end):
    from collections import defaultdict
    import heapq
    graph = defaultdict(list)
    for (a, b), p in zip(edges, succProb):
        graph[a].append((b, p))
        graph[b].append((a, p))
    prob = [0.0] * n
    prob[start] = 1.0
    heap = [(-1.0, start)]
    while heap:
        p, node = heapq.heappop(heap)
        p = -p
        if node == end:
            return p
        for nei, w in graph[node]:
            if prob[nei] < p * w:
                prob[nei] = p * w
                heapq.heappush(heap, (-prob[nei], nei))
    return 0.0

# Example usage:
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
print(maxProbability(n, edges, succProb, start, end))  # Output: 0.25
