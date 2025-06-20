"""
789. Escape The Ghosts

You are playing a simplified Pacman game. You start at the origin and there are ghosts at various positions. Each turn, you and the ghosts can move one unit in any direction. If any ghost reaches you (or the target) at the same time or before you, you lose. Return true if you can reach the target before any ghost, otherwise false.

Example 1:
Input: ghosts = [[1,0],[0,3]], target = [0,1]
Output: true

Example 2:
Input: ghosts = [[1,0]], target = [2,0]
Output: false

Constraints:
- 1 <= ghosts.length <= 100
- ghosts[i].length == 2
- target.length == 2
- -10^4 <= ghosts[i][j], target[j] <= 10^4
"""
def escapeGhosts(ghosts, target):
    player_dist = abs(target[0]) + abs(target[1])
    for g in ghosts:
        if abs(g[0] - target[0]) + abs(g[1] - target[1]) <= player_dist:
            return False
    return True

# Example usage:
print(escapeGhosts([[1,0],[0,3]], [0,1]))  # Output: True
print(escapeGhosts([[1,0]], [2,0]))        # Output: False
