"""
LeetCode 1518. Water Bottles

Given numBottles full water bottles, you can exchange numExchange empty bottles for one full bottle. Return the total number of bottles you can drink.

Constraints:
- 1 <= numBottles <= 100
- 1 <= numExchange <= 100

Example:
Input: numBottles = 9, numExchange = 3
Output: 13
"""
def numWaterBottles(numBottles, numExchange):
    res = numBottles
    empty = numBottles
    while empty >= numExchange:
        new = empty // numExchange
        res += new
        empty = empty % numExchange + new
    return res

# Example usage:
numBottles = 9
numExchange = 3
print(numWaterBottles(numBottles, numExchange))  # Output: 13
