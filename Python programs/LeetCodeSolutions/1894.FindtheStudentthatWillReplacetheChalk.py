"""
LeetCode 1894. Find the Student that Will Replace the Chalk

Given an integer array chalk and an integer k, return the index of the student that will replace the chalk.

Example:
Input: chalk = [5,1,5], k = 22
Output: 0

Constraints:
- 1 <= chalk.length <= 10^5
- 1 <= chalk[i] <= 10^5
- 1 <= k <= 10^9
"""

def chalkReplacer(chalk, k):
    total = sum(chalk)
    k %= total
    for i, c in enumerate(chalk):
        if k < c:
            return i
        k -= c

# Example usage:
# print(chalkReplacer([5,1,5], 22))  # Output: 0
