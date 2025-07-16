"""
LeetCode 2374. Node With Highest Edge Score

Given edges, return the node with the highest edge score.

Constraints:
- 1 <= edges.length <= 10^5
"""

def edgeScore(edges):
    n = len(edges)
    score = [0]*n
    for i, e in enumerate(edges):
        score[e] += i
    return score.index(max(score))

# Example usage:
# print(edgeScore([1,0,0,0,0,7,7,5]))  # Output: 7
