"""
781. Rabbits in Forest

There are n rabbits in a forest. Each rabbit tells you how many other rabbits have the same color as them. Given an integer array answers where answers[i] is the answer of the i-th rabbit, return the minimum number of rabbits that could be in the forest.

Example 1:
Input: answers = [1, 1, 2]
Output: 5

Example 2:
Input: answers = [10, 10, 10]
Output: 11

Constraints:
- 1 <= answers.length <= 1000
- 0 <= answers[i] < 1000
"""
from collections import Counter

def numRabbits(answers):
    count = Counter(answers)
    res = 0
    for k, v in count.items():
        groups = (v + k) // (k + 1)
        res += groups * (k + 1)
    return res

# Example usage:
print(numRabbits([1, 1, 2]))  # Output: 5
print(numRabbits([10, 10, 10]))  # Output: 11
