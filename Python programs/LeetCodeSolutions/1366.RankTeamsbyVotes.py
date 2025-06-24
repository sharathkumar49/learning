"""
LeetCode 1366. Rank Teams by Votes

Given an array of strings votes, each string is a ranking of teams. Return the ranking of teams based on votes.

Constraints:
- 1 <= votes.length <= 1000
- 1 <= votes[i].length <= 26
- votes[i] consists of uppercase English letters only.

Example:
Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
Output: "ACB"
"""
def rankTeams(votes):
    from collections import defaultdict
    n = len(votes[0])
    rank = {c: [0]*n for c in votes[0]}
    for v in votes:
        for i, c in enumerate(v):
            rank[c][i] -= 1
    return ''.join(sorted(votes[0], key=lambda c: (rank[c], c)))

# Example usage:
votes = ["ABC","ACB","ABC","ACB","ACB"]
print(rankTeams(votes))  # Output: "ACB"
