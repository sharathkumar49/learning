"""
LeetCode 1797. Design Authentication Manager

Design an authentication manager with timeToLive. Implement generate, renew, and countUnexpiredTokens.

Example 1:
Input: ["AuthenticationManager","generate","renew","countUnexpiredTokens"], [[5],["aaa",1],["aaa",2],[6]]
Output: [null,null,null,1]

Constraints:
- 1 <= timeToLive <= 10^8
- 1 <= calls.length <= 2000
- 1 <= tokenId.length <= 5
- 1 <= currentTime <= 10^8
"""
class AuthenticationManager:
    def __init__(self, timeToLive):
        self.timeToLive = timeToLive
        self.tokens = {}
    def generate(self, tokenId, currentTime):
        self.tokens[tokenId] = currentTime + self.timeToLive
    def renew(self, tokenId, currentTime):
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive
    def countUnexpiredTokens(self, currentTime):
        return sum(exp > currentTime for exp in self.tokens.values())

# Example usage:
# am = AuthenticationManager(5)
# am.generate("aaa", 1)
# am.renew("aaa", 2)
# print(am.countUnexpiredTokens(6))  # Output: 1
