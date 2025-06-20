"""
822. Card Flipping Game

On a table are n cards, each with a number on the front and back. Return the minimum number on the back of a card that is not on the front of any card. If no such number exists, return 0.

Example 1:
Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2

Example 2:
Input: fronts = [1], backs = [1]
Output: 0

Constraints:
- 1 <= fronts.length == backs.length <= 1000
- 1 <= fronts[i], backs[i] <= 2000
"""
def flipgame(fronts, backs):
    same = {x for x, y in zip(fronts, backs) if x == y}
    candidates = set(fronts + backs) - same
    return min(candidates) if candidates else 0

# Example usage:
print(flipgame([1,2,4,4,7], [1,3,4,1,3]))  # Output: 2
print(flipgame([1], [1]))  # Output: 0
