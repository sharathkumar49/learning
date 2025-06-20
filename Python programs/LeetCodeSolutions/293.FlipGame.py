"""
293. Flip Game
https://leetcode.com/problems/flip-game/

You are playing a Flip Game with a string s consisting of only '+' and '-'. You can flip two consecutive "++" into "--". Return all possible states of the string after one valid move.

Constraints:
- 1 <= s.length <= 500
- s[i] is either '+' or '-'.

Example 1:
Input: s = "++++"
Output: ["--++","+--+","++--"]

Example 2:
Input: s = "+"
Output: []
"""
def generatePossibleNextMoves(s):
    res = []
    for i in range(len(s)-1):
        if s[i:i+2] == '++':
            res.append(s[:i] + '--' + s[i+2:])
    return res

# Example usage:
if __name__ == "__main__":
    print(generatePossibleNextMoves("++++"))  # Output: ['--++', '+--+', '++--']
    print(generatePossibleNextMoves("+"))     # Output: []
