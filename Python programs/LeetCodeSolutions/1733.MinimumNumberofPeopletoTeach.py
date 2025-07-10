"""
LeetCode 1733. Minimum Number of People to Teach

Given a friendship graph and languages known by each person, return the minimum number of people to teach a language so everyone can communicate.

Example 1:
Input: n = 2, languages = [[1],[2]], friendships = [[1,2]]
Output: 2

Constraints:
- 2 <= n <= 500
- 1 <= languages[i].length <= 10
- 1 <= languages[i][j] <= 10^4
- 1 <= friendships.length <= n*(n-1)/2
"""

def minimumTeachings(n, languages, friendships):
    know = [set(l) for l in languages]
    need = set()
    for u, v in friendships:
        if know[u-1] & know[v-1]:
            continue
        need.add(u-1)
        need.add(v-1)
    cnt = [0] * (n+1)
    for i in need:
        for l in languages[i]:
            cnt[l] += 1
    return len(need) - max(cnt)

# Example usage:
# n = 2
# languages = [[1],[2]]
# friendships = [[1,2]]
# print(minimumTeachings(n, languages, friendships))  # Output: 2
