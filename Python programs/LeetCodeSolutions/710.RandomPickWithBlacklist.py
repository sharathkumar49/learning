"""
LeetCode 710. Random Pick with Blacklist

Given a blacklist B containing unique integers from [0, n), implement the function pick() to return a random integer from [0, n) that is not in B. Each integer should have equal probability.

Implement the Solution class:
- Solution(int n, int[] blacklist) Initializes the object with the integer n and the blacklisted integers blacklist.
- int pick() Returns a random integer from [0, n) that is not in blacklist. Each integer should have equal probability.

Example 1:
Input
["Solution", "pick", "pick", "pick", "pick"]
[[7, [2, 3, 5]], [], [], [], []]
Output
[null, 0, 4, 1, 6]

Constraints:
- 1 <= n <= 10^9
- 0 <= blacklist.length < min(10^5, n)
- 0 <= blacklist[i] < n
- All the values of blacklist are unique.
- At most 2 * 10^4 calls will be made to pick.
"""
import random
from typing import List

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.bound = n - len(blacklist)
        self.mapping = {}
        black = set(b for b in blacklist if b >= self.bound)
        w = self.bound
        for b in blacklist:
            if b < self.bound:
                while w in black:
                    w += 1
                self.mapping[b] = w
                w += 1
    def pick(self) -> int:
        x = random.randint(0, self.bound - 1)
        return self.mapping.get(x, x)

# Example usage
if __name__ == "__main__":
    sol = Solution(7, [2, 3, 5])
    print([sol.pick() for _ in range(10)])  # Output: random numbers from [0,1,4,6]
