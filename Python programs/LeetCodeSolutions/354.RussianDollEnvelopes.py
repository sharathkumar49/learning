"""
354. Russian Doll Envelopes

You are given a 2D array of envelopes where envelopes[i] = [wi, hi] representing the width and the height of an envelope. One envelope can fit into another if and only if both the width and height of one envelope is greater than the other envelope.

Return the maximum number of envelopes you can Russian doll (put one inside the other).

Constraints:
- 1 <= envelopes.length <= 10^5
- envelopes[i].length == 2
- 1 <= wi, hi <= 10^5
"""
from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [h for w, h in envelopes]
        dp = []
        for h in heights:
            i = bisect.bisect_left(dp, h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h
        return len(dp)

# Example usage:
envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(Solution().maxEnvelopes(envelopes))  # Output: 3
