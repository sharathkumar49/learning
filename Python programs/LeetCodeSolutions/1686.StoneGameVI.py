"""
LeetCode 1686. Stone Game VI

Alice and Bob take turns picking stones with values from two arrays. Return the score difference (Alice - Bob) if both play optimally.

Example 1:
Input: aliceValues = [1,3], bobValues = [2,1]
Output: 0

Constraints:
- 1 <= aliceValues.length, bobValues.length <= 10^5
- 1 <= aliceValues[i], bobValues[i] <= 100
"""

def stoneGameVI(aliceValues, bobValues):
    arr = sorted(zip(aliceValues, bobValues), key=lambda x: -(x[0]+x[1]))
    a = b = 0
    for i, (x, y) in enumerate(arr):
        if i % 2 == 0:
            a += x
        else:
            b += y
    return (a > b) - (a < b)

# Example usage:
# aliceValues = [1,3]
# bobValues = [2,1]
# print(stoneGameVI(aliceValues, bobValues))  # Output: 0
