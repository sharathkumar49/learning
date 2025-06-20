"""
657. Robot Return to Origin
Difficulty: Easy

There is a robot starting at (0, 0) on a plane. Given a sequence of its moves ("U", "D", "L", "R"), return true if the robot returns to the origin after all moves, or false otherwise.

Example 1:
Input: moves = "UD"
Output: true

Example 2:
Input: moves = "LL"
Output: false

Constraints:
1 <= moves.length <= 10^4
moves only contains 'U', 'D', 'L', 'R'.
"""

def judgeCircle(moves):
    return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

# Example usage
if __name__ == "__main__":
    print(judgeCircle("UD"))  # Output: True
    print(judgeCircle("LL"))  # Output: False
