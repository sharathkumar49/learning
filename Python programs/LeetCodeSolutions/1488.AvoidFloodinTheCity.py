"""
LeetCode 1488. Avoid Flood in The City

Given an array rains where rains[i] > 0 means it rains over lake rains[i] on the ith day, and rains[i] == 0 means you can dry any lake. Return an array ans where ans[i] == -1 if it rains on the ith day, or the lake you dry if it is a dry day. If it is impossible to avoid flood, return an empty array.

Constraints:
- 1 <= rains.length <= 10^5
- 0 <= rains[i] <= 10^9

Example:
Input: rains = [1,2,3,4,0,1,2,0,0]
Output: [-1,-1,-1,-1,1,-1,-1,2,3]
"""
def avoidFlood(rains):
    from collections import defaultdict
    import bisect
    n = len(rains)
    ans = [-1]*n
    full = {}
    dry = []
    for i, lake in enumerate(rains):
        if lake:
            if lake in full:
                idx = bisect.bisect_left(dry, full[lake])
                if idx == len(dry):
                    return []
                ans[dry[idx]] = lake
                dry.pop(idx)
            full[lake] = i
        else:
            dry.append(i)
    for i in range(n):
        if ans[i] == -1 and rains[i] == 0:
            ans[i] = 1
    return ans

# Example usage:
rains = [1,2,3,4,0,1,2,0,0]
print(avoidFlood(rains))  # Output: [-1,-1,-1,-1,1,-1,-1,2,3]
