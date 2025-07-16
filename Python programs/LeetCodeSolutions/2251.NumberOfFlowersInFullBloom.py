"""
LeetCode 2251. Number of Flowers in Full Bloom

Given flowers and people, return the number of flowers in bloom for each person.

Example:
Input: flowers = [[1,4],[2,3],[4,6]], people = [2,3,4,5]
Output: [2,2,2,1]

Constraints:
- 1 <= flowers.length <= 5 * 10^4
- 1 <= people.length <= 5 * 10^4
"""

def fullBloomFlowers(flowers, people):
    starts = sorted(f[0] for f in flowers)
    ends = sorted(f[1] for f in flowers)
    import bisect
    res = []
    for p in people:
        res.append(bisect.bisect_right(starts, p) - bisect.bisect_left(ends, p))
    return res

# Example usage:
# print(fullBloomFlowers([[1,4],[2,3],[4,6]], [2,3,4,5]))  # Output: [2,2,2,1]
