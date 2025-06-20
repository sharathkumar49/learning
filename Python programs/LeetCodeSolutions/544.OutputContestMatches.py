"""
544. Output Contest Matches

Given n teams, return their contest matches in the form of a string as described in the problem.

Constraints:
- n == 2^k where k is in the range [1, 12].

Example:
Input: n = 4
Output: "((1,4),(2,3))"
"""

class Solution:
    def findContestMatch(self, n: int) -> str:
        teams = [str(i+1) for i in range(n)]
        while n > 1:
            teams = [f"({teams[i]},{teams[n-1-i]})" for i in range(n//2)]
            n //= 2
        return teams[0]

# Example usage:
sol = Solution()
print(sol.findContestMatch(4))  # Output: "((1,4),(2,3))"
