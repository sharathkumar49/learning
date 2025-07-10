"""
LeetCode 1953. Maximum Number of Weeks for Which You Can Work

Given an array milestones, return the maximum number of weeks you can work.

Example:
Input: milestones = [1,2,3]
Output: 6

Constraints:
- 1 <= milestones.length <= 10^5
- 1 <= milestones[i] <= 10^9
"""

def numberOfWeeks(milestones):
    s = sum(milestones)
    m = max(milestones)
    return min(s, 2*(s-m)+1)

# Example usage:
# print(numberOfWeeks([1,2,3]))  # Output: 6
