"""
LeetCode 2359. Find Closest Node to Given Two Nodes

Given edges, node1, node2, return the closest node to both.

Example:
Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2

Constraints:
- 1 <= edges.length <= 10^5
"""

def closestMeetingNode(edges, node1, node2):
    def dist(start):
        d = [-1]*len(edges)
        curr = start
        step = 0
        while curr != -1 and d[curr] == -1:
            d[curr] = step
            curr = edges[curr]
            step += 1
        return d
    d1 = dist(node1)
    d2 = dist(node2)
    res = -1
    min_dist = float('inf')
    for i in range(len(edges)):
        if d1[i] != -1 and d2[i] != -1:
            if max(d1[i], d2[i]) < min_dist:
                min_dist = max(d1[i], d2[i])
                res = i
    return res

# Example usage:
# print(closestMeetingNode([2,2,3,-1], 0, 1))  # Output: 2
