"""
LeetCode 2678. Number of Senior Citizens

Given details, return the number of senior citizens (age >= 60).

Constraints:
- 1 <= details.length <= 100
"""

def countSeniors(details):
    return sum(int(x[11:13]) > 60 for x in details)
# Example usage:
# print(countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))  # Output: 1
