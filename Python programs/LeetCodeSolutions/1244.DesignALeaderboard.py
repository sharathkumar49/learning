"""
1244. Design A Leaderboard

Design a Leaderboard class to add scores, get the sum of top K scores, and reset a player's score.

Constraints:
- 1 <= playerId, K <= 10000
- 1 <= score <= 100
- At most 1000 calls will be made to each method.

Example:
Input: ["Leaderboard","addScore","addScore","addScore","top","reset","top"], [[],[1,73],[2,56],[3,39],[2],[1],[2]]
Output: [null,null,null,null,130,null,39]

"""
from collections import defaultdict
class Leaderboard:
    def __init__(self):
        self.scores = defaultdict(int)
    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score
    def top(self, K: int) -> int:
        return sum(sorted(self.scores.values(), reverse=True)[:K])
    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0

# Example usage
if __name__ == "__main__":
    lb = Leaderboard()
    lb.addScore(1, 73)
    lb.addScore(2, 56)
    lb.addScore(3, 39)
    print(lb.top(2))  # Output: 130
    lb.reset(1)
    print(lb.top(2))  # Output: 39
