"""
LeetCode 1773. Count Items Matching a Rule

Given a list of items, each item is a list of [type, color, name], and a ruleKey and ruleValue, return the number of items that match the rule.

Example 1:
Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1

Constraints:
- 1 <= items.length <= 10^4
- 1 <= items[i].length == 3
- 1 <= items[i][j].length <= 10
- ruleKey is "type", "color", or "name"
"""

def countMatches(items, ruleKey, ruleValue):
    idx = {"type": 0, "color": 1, "name": 2}[ruleKey]
    return sum(item[idx] == ruleValue for item in items)

# Example usage:
# items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
# ruleKey = "color"
# ruleValue = "silver"
# print(countMatches(items, ruleKey, ruleValue))  # Output: 1
