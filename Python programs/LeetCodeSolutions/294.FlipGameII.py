"""
294. Flip Game II
https://leetcode.com/problems/flip-game-ii/

You are playing a Flip Game with a string s consisting of only '+' and '-'. You can flip two consecutive "++" into "--". Return true if the starting player can guarantee a win, otherwise return false.

Constraints:
- 1 <= s.length <= 60
- s[i] is either '+' or '-'.

Example 1:
Input: s = "++++"
Output: true

Example 2:
Input: s = "+"
Output: false
"""
def canWin(s):
    memo = {}
    def dfs(s):
        if s in memo:
            return memo[s]
        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                if not dfs(s[:i] + '--' + s[i+2:]):
                    memo[s] = True
                    return True
        memo[s] = False
        return False
    return dfs(s)

# Example usage:
if __name__ == "__main__":
    print(canWin("++++"))  # Output: True
    print(canWin("+"))     # Output: False
