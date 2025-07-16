"""
LeetCode 2212. Maximum Points in an Archery Competition

Given Alice's and Bob's scores, return the maximum points Bob can earn.

Example:
Input: numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
Output: 8

Constraints:
- 1 <= numArrows <= 10^5
- aliceArrows.length == 12
- 0 <= aliceArrows[i] <= numArrows
"""

def maximumBobPoints(numArrows, aliceArrows):
    maxPoints = 0
    best = [0]*12
    for mask in range(1<<12):
        arrows = 0
        points = 0
        curr = [0]*12
        for i in range(12):
            if mask & (1<<i):
                arrows += aliceArrows[i]+1
                points += i
                curr[i] = aliceArrows[i]+1
        if arrows <= numArrows and points > maxPoints:
            maxPoints = points
            best = curr[:]
    # Distribute remaining arrows
    left = numArrows - sum(best)
    for i in range(12):
        if left > 0 and best[i] == 0:
            best[i] += left
            break
    return maxPoints

# Example usage:
# print(maximumBobPoints(9, [1,1,0,1,0,0,2,1,0,1,2,0]))  # Output: 8
