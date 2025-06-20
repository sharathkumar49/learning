"""
950. Reveal Cards In Increasing Order
https://leetcode.com/problems/reveal-cards-in-increasing-order/

You are given an integer array deck. Return an ordering of the deck that would reveal the cards in increasing order if you repeatedly reveal the top card and move the next card to the bottom of the deck.

Constraints:
- 1 <= deck.length <= 1000
- 1 <= deck[i] <= 10^6
- All the values of deck are unique.

Example:
Input: deck = [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
"""
from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [0] * len(deck)
        idxs = list(range(len(deck)))
        for card in deck:
            res[idxs.pop(0)] = card
            if idxs:
                idxs.append(idxs.pop(0))
        return res

# Example usage
if __name__ == "__main__":
    deck = [17,13,11,2,3,5,7]
    print(Solution().deckRevealedIncreasing(deck))  # Output: [2,13,3,11,5,17,7]
