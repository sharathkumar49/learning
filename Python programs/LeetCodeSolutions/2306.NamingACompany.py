"""
LeetCode 2306. Naming a Company

Given ideas, return the number of distinct company names.

Example:
Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6

Constraints:
- 2 <= ideas.length <= 5 * 10^4
"""

def distinctNames(ideas):
    from collections import defaultdict
    groups = defaultdict(set)
    for idea in ideas:
        groups[idea[0]].add(idea[1:])
    res = 0
    for a in groups:
        for b in groups:
            if a == b:
                continue
            res += len(groups[a] - groups[b]) * len(groups[b] - groups[a])
    return res

# Example usage:
# print(distinctNames(["coffee","donuts","time","toffee"]))  # Output: 6
