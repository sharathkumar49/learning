"""
LeetCode 2410. Maximum Matching of Players With Trainers

Given players and trainers, return the maximum number of matchings.

Constraints:
- 1 <= players.length, trainers.length <= 10^5
"""

def matchPlayersAndTrainers(players, trainers):
    players.sort()
    trainers.sort()
    i = j = res = 0
    while i < len(players) and j < len(trainers):
        if players[i] <= trainers[j]:
            res += 1
            i += 1
        j += 1
    return res

# Example usage:
# print(matchPlayersAndTrainers([4,7,9],[8,2,5,8]))  # Output: 2
