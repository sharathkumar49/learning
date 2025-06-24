"""
LeetCode 1402. Reducing Dishes

A chef has collected data on the satisfaction level of his n dishes. Return the maximum total Like-time coefficient that the chef can obtain after preparing the dishes optimally.

Constraints:
- n == satisfaction.length
- 1 <= n <= 500
- -1000 <= satisfaction[i] <= 1000

Example:
Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
"""
def maxSatisfaction(satisfaction):
    satisfaction.sort(reverse=True)
    res = total = 0
    for s in satisfaction:
        total += s
        if total > 0:
            res += total
        else:
            break
    return res

# Example usage:
satisfaction = [-1,-8,0,5,-9]
print(maxSatisfaction(satisfaction))  # Output: 14
