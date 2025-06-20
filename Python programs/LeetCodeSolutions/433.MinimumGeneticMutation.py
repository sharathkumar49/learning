"""
433. Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', 'T'.
A mutation is defined as a single character change in the gene string.
Given a start gene string, an end gene string, and a bank of valid gene mutations, return the minimum number of mutations needed to mutate from start to end. If there is no such mutation sequence, return -1.

Constraints:
- start.length == end.length == 8
- 0 <= bank.length <= 10^4
- start, end, and bank[i] consist of only characters ['A', 'C', 'G', 'T']

Example:
Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
"""

from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: list) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        queue = deque([(start, 0)])
        while queue:
            curr, steps = queue.popleft()
            if curr == end:
                return steps
            for i in range(8):
                for c in 'ACGT':
                    if c != curr[i]:
                        nxt = curr[:i] + c + curr[i+1:]
                        if nxt in bank:
                            bank.remove(nxt)
                            queue.append((nxt, steps+1))
        return -1

# Example usage:
sol = Solution()
print(sol.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # Output: 1
