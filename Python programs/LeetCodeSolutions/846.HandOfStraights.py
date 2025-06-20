"""
846. Hand of Straights

Alice has a hand of cards, each represented by an integer. She wants to rearrange the cards into groups of size groupSize, where each group consists of groupSize consecutive cards. Return true if she can rearrange the cards, otherwise false.

Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true

Example 2:
Input: hand = [1,2,3,4,5], groupSize = 4
Output: false

Constraints:
- 1 <= hand.length <= 10^4
- 1 <= hand[i] <= 10^9
- 1 <= groupSize <= hand.length
"""
def isNStraightHand(hand, groupSize):
    from collections import Counter
    if len(hand) % groupSize != 0:
        return False
    count = Counter(hand)
    for x in sorted(count):
        if count[x] > 0:
            for i in range(groupSize):
                if count[x + i] < count[x]:
                    return False
                count[x + i] -= count[x]
    return True

# Example usage:
print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))  # Output: True
print(isNStraightHand([1,2,3,4,5], 4))           # Output: False
