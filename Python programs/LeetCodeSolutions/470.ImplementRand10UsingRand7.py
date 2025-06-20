"""
470. Implement Rand10() Using Rand7()

Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 that generates a uniform random integer in the range 1 to 10.

Note: The rand7 API is not implemented here. In a real interview, you would be provided with rand7().

Constraints:
- 1 <= rand7() <= 7

Example:
Output: [7,1,10,8,6]
"""

import random

def rand7():
    return random.randint(1, 7)

class Solution:
    def rand10(self) -> int:
        while True:
            num = (rand7() - 1) * 7 + rand7()
            if num <= 40:
                return 1 + (num - 1) % 10

# Example usage:
sol = Solution()
print([sol.rand10() for _ in range(5)])  # Output: e.g. [7, 1, 10, 8, 6]
