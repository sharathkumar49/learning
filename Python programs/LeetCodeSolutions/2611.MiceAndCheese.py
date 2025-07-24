"""
LeetCode 2611. Mice and Cheese

Given reward1, reward2, and k, return the maximum reward by choosing k indices for the first mouse.

Constraints:
- 1 <= reward1.length == reward2.length <= 10^5
"""

def miceAndCheese(reward1, reward2, k):
    diff = sorted([a-b for a,b in zip(reward1, reward2)], reverse=True)
    return sum(reward2) + sum(diff[:k])
# Example usage:
# print(miceAndCheese([1,1,3,4],[4,4,1,1],2))  # Output: 15
