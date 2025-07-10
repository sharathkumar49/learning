"""
LeetCode 2092. Find All People With Secret

Given n people, meetings, and the initial people with the secret, return all people who will know the secret after all meetings.

Example:
Input: n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
Output: [0,1,2,3,5]

Constraints:
- 2 <= n <= 10^5
- 1 <= meetings.length <= 10^5
"""

def findAllPeople(n, meetings, firstPerson):
    from collections import defaultdict, deque
    meetings.sort(key=lambda x: x[2])
    know = set([0, firstPerson])
    i = 0
    while i < len(meetings):
        t = meetings[i][2]
        group = set()
        edges = defaultdict(list)
        while i < len(meetings) and meetings[i][2] == t:
            a, b, _ = meetings[i]
            group.add(a)
            group.add(b)
            edges[a].append(b)
            edges[b].append(a)
            i += 1
        q = deque([x for x in group if x in know])
        seen = set(q)
        while q:
            u = q.popleft()
            for v in edges[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        know |= seen
    return list(know)

# Example usage:
# print(findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]], 1))  # Output: [0,1,2,3,5]
