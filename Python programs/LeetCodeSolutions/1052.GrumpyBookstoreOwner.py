"""
1052. Grumpy Bookstore Owner

Given an array customers and an array grumpy, where customers[i] is the number of customers at minute i, and grumpy[i] is 1 if the owner is grumpy and 0 otherwise. The owner can keep themselves not grumpy for X minutes. Return the maximum number of satisfied customers.

Constraints:
- 1 <= customers.length == grumpy.length <= 20000
- 0 <= customers[i] <= 1000
- 0 <= X <= customers.length

Example:
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
"""
from typing import List

def maxSatisfied(customers: List[int], grumpy: List[int], X: int) -> int:
    baseline = sum(c for c, g in zip(customers, grumpy) if not g)
    extra = max(sum(c for c, g in zip(customers[:X], grumpy[:X]) if g), 0)
    curr = extra
    for i in range(X, len(customers)):
        if grumpy[i]:
            curr += customers[i]
        if grumpy[i-X]:
            curr -= customers[i-X]
        extra = max(extra, curr)
    return baseline + extra

# Example usage:
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
print(maxSatisfied(customers, grumpy, X))  # Output: 16
