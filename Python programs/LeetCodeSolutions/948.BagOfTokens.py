"""
948. Bag of Tokens
https://leetcode.com/problems/bag-of-tokens/

You have an initial power of P and a bag of tokens. Each token can be used at most once. If you have at least the value of a token, you may play it face up, losing that token's value and gaining 1 point. If you have at least 1 point, you may play a token face down, gaining that token's value and losing 1 point. Return the largest number of points you can have after playing any number of tokens.

Constraints:
- 0 <= tokens.length <= 1000
- 0 <= tokens[i], P < 10000

Example:
Input: tokens = [100,200,300,400], P = 200
Output: 2
"""
from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        i, j = 0, len(tokens) - 1
        score = res = 0
        while i <= j:
            if P >= tokens[i]:
                P -= tokens[i]
                score += 1
                i += 1
                res = max(res, score)
            elif score > 0:
                P += tokens[j]
                score -= 1
                j -= 1
            else:
                break
        return res

# Example usage
if __name__ == "__main__":
    tokens = [100,200,300,400]
    P = 200
    print(Solution().bagOfTokensScore(tokens, P))  # Output: 2
