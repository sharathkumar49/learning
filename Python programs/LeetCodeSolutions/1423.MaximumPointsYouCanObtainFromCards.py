"""
LeetCode 1423. Maximum Points You Can Obtain from Cards

Given an integer array cardPoints and an integer k, return the maximum score you can obtain by picking k cards from either end of the array.

Constraints:
- 1 <= cardPoints.length <= 10^5
- 1 <= cardPoints[i] <= 10^4
- 1 <= k <= cardPoints.length

Example:
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
"""
def maxScore(cardPoints, k):
    n = len(cardPoints)
    total = sum(cardPoints[:k])
    res = total
    for i in range(1, k+1):
        total = total - cardPoints[k-i] + cardPoints[-i]
        res = max(res, total)
    return res

# Example usage:
cardPoints = [1,2,3,4,5,6,1]
k = 3
print(maxScore(cardPoints, k))  # Output: 12
