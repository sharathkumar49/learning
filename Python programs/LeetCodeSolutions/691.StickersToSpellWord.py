"""
LeetCode 691. Stickers to Spell Word

We are given n different types of stickers. Each sticker has a lowercase English word on it.
You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them as many times as necessary.
Return the minimum number of stickers that you need to spell out the target. If the task is impossible, return -1.

Example 1:
Input: stickers = ["with","example","science"], target = "thehat"
Output: 3

Example 2:
Input: stickers = ["notice","possible"], target = "basicbasic"
Output: -1

Constraints:
- n == stickers.length
- 1 <= n <= 50
- 1 <= stickers[i].length <= 10
- 1 <= target.length <= 15
- stickers[i] and target consist of lowercase English letters.
"""
from typing import List
from collections import Counter

def minStickers(stickers: List[str], target: str) -> int:
    m = len(stickers)
    sticker_counts = [Counter(s) for s in stickers]
    memo = {}
    def dp(remain):
        if remain == '':
            return 0
        if remain in memo:
            return memo[remain]
        res = float('inf')
        target_count = Counter(remain)
        for sc in sticker_counts:
            if remain[0] not in sc:
                continue
            new_remain = ''
            for c in target_count:
                if target_count[c] > sc.get(c, 0):
                    new_remain += c * (target_count[c] - sc.get(c, 0))
            tmp = dp(new_remain)
            if tmp != -1:
                res = min(res, 1 + tmp)
        memo[remain] = -1 if res == float('inf') else res
        return memo[remain]
    ans = dp(target)
    return ans

# Example usage
if __name__ == "__main__":
    print(minStickers(["with","example","science"], "thehat"))  # Output: 3
    print(minStickers(["notice","possible"], "basicbasic"))      # Output: -1
