"""
990. Satisfiability of Equality Equations
https://leetcode.com/problems/satisfiability-of-equality-equations/

You are given an array of strings equations that represent relationships between variables. Each string equations[i] is of the form "a==b" or "a!=b", where a and b are lowercase letters. Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

Constraints:
- 1 <= equations.length <= 500
- equations[i].length == 4
- equations[i][0] and equations[i][3] are lowercase English letters
- equations[i][1] is either '=' or '!'
- equations[i][2] is '='

Example:
Input: equations = ["a==b","b!=a"]
Output: false
"""
from typing import List

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z')+1)}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for eq in equations:
            if eq[1:3] == '==':
                parent[find(eq[0])] = find(eq[3])
        for eq in equations:
            if eq[1:3] == '!=' and find(eq[0]) == find(eq[3]):
                return False
        return True

# Example usage
if __name__ == "__main__":
    equations = ["a==b","b!=a"]
    print(Solution().equationsPossible(equations))  # Output: False
