"""
LeetCode 2225. Find Players With Zero or One Losses

Given matches, return players with zero or one losses.

Example:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]

Constraints:
- 1 <= matches.length <= 10^5
- 1 <= matches[i][j] <= 10^5
"""

def findWinners(matches):
    from collections import defaultdict
    losses = defaultdict(int)
    players = set()
    for w, l in matches:
        losses[l] += 1
        players.add(w)
        players.add(l)
    zero = [p for p in players if losses[p] == 0]
    one = [p for p in players if losses[p] == 1]
    return [sorted(zero), sorted(one)]

# Example usage:
# print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))  # Output: [[1,2,10],[4,5,7,8]]
