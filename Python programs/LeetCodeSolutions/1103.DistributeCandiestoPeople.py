"""
1103. Distribute Candies to People

We distribute some number of candies to a row of n people in a round robin way. Return an array representing the final distribution.

Constraints:
- 1 <= candies <= 10^9
- 1 <= num_people <= 1000

Example:
Input: candies = 7, num_people = 4
Output: [1,2,3,1]
"""
from typing import List

def distributeCandies(candies: int, num_people: int) -> List[int]:
    res = [0] * num_people
    i = 0
    give = 1
    while candies > 0:
        res[i % num_people] += min(give, candies)
        candies -= give
        give += 1
        i += 1
    return res

# Example usage:
candies = 7
num_people = 4
print(distributeCandies(candies, num_people))  # Output: [1, 2, 3, 1]
