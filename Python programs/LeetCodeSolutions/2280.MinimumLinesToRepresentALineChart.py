"""
LeetCode 2280. Minimum Lines to Represent a Line Chart

Given stockPrices, return the minimum number of lines to represent the chart.

Example:
Input: stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,3]]
Output: 1

Constraints:
- 1 <= stockPrices.length <= 10^5
"""

def minimumLines(stockPrices):
    stockPrices.sort()
    n = len(stockPrices)
    if n <= 1:
        return 0
    res = 1
    for i in range(2, n):
        x1, y1 = stockPrices[i-2]
        x2, y2 = stockPrices[i-1]
        x3, y3 = stockPrices[i]
        if (y2-y1)*(x3-x2) != (y3-y2)*(x2-x1):
            res += 1
    return res

# Example usage:
# print(minimumLines([[1,7],[2,6],[3,5],[4,4],[5,3]]))  # Output: 1
