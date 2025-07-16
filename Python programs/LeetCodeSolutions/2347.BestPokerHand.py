"""
LeetCode 2347. Best Poker Hand

Given ranks and suits, return the best poker hand.

Example:
Input: ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]
Output: "Flush"

Constraints:
- ranks.length == suits.length == 5
"""

def bestHand(ranks, suits):
    if len(set(suits)) == 1:
        return "Flush"
    from collections import Counter
    c = Counter(ranks)
    if max(c.values()) >= 3:
        return "Three of a Kind"
    if max(c.values()) == 2:
        return "Pair"
    return "High Card"

# Example usage:
# print(bestHand([13,2,3,1,9], ["a","a","a","a","a"]))  # Output: "Flush"
