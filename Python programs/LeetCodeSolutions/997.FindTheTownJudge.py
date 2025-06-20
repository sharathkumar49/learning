"""
997. Find the Town Judge
https://leetcode.com/problems/find-the-town-judge/

In a town, there are n people labeled from 1 to n. There may be a town judge among them. The town judge trusts nobody, and everybody (except for the town judge) trusts the town judge. Return the label of the town judge if they exist, otherwise return -1.

Constraints:
- 1 <= n <= 1000
- 0 <= trust.length <= 10^4
- trust[i].length == 2
- All trust[i] are different
- trust[i][0] != trust[i][1]

Example:
Input: n = 2, trust = [[1,2]]
Output: 2
"""
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_score = [0] * (n+1)
        for a, b in trust:
            trust_score[a] -= 1
            trust_score[b] += 1
        for i in range(1, n+1):
            if trust_score[i] == n-1:
                return i
        return -1

# Example usage
if __name__ == "__main__":
    n = 2
    trust = [[1,2]]
    print(Solution().findJudge(n, trust))  # Output: 2
