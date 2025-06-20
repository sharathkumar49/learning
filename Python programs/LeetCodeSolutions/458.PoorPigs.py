"""
458. Poor Pigs

There are buckets of liquid, one of which is poisonous. You have pigs to test the buckets. Each pig can drink from any number of buckets and will die within a certain time after drinking the poison. Find the minimum number of pigs needed to figure out which bucket is poisonous within a given time.

Constraints:
- 1 <= buckets <= 1000
- 1 <= minutesToDie <= minutesToTest <= 100

Example:
Input: buckets = 1000, minutesToDie = 15, minutesToTest = 60
Output: 5
"""

import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests = minutesToTest // minutesToDie
        return math.ceil(math.log(buckets, tests + 1))

# Example usage:
sol = Solution()
print(sol.poorPigs(1000, 15, 60))  # Output: 5
