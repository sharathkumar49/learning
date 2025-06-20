"""
299. Bulls and Cows

You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint with the following info:
- The number of "bulls", which are digits in the guess that are in the correct position.
- The number of "cows", which are digits in the guess that are in your secret number but in the wrong position.

Given the secret number and your friend's guess, return the hint as a string "xAyB" where x is the number of bulls and y is the number of cows.

Constraints:
- 1 <= secret.length, guess.length <= 1000
- secret.length == guess.length
- secret and guess consist of digits only.
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        s_count = {}
        g_count = {}
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s_count[s] = s_count.get(s, 0) + 1
                g_count[g] = g_count.get(g, 0) + 1
        for k in g_count:
            if k in s_count:
                cows += min(s_count[k], g_count[k])
        return f"{bulls}A{cows}B"

# Example usage:
# secret = "1807"
# guess = "7810"
# print(Solution().getHint(secret, guess))  # Output: "1A3B"
