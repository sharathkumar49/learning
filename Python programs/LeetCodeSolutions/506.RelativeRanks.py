"""
506. Relative Ranks

Given scores of N athletes, return their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Constraints:
- n == score.length
- 1 <= n <= 10^4
- 0 <= score[i] <= 10^6
- All the scores are unique.

Example:
Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
"""

class Solution:
    def findRelativeRanks(self, score: list) -> list:
        rank = {s: str(i+1) for i, s in enumerate(sorted(score, reverse=True))}
        for i, s in enumerate(sorted(score, reverse=True)[:3]):
            rank[s] = ["Gold Medal", "Silver Medal", "Bronze Medal"][i]
        return [rank[s] for s in score]

# Example usage:
sol = Solution()
print(sol.findRelativeRanks([5,4,3,2,1]))  # Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
