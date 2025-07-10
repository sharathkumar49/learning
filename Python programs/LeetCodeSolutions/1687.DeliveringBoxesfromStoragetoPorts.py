"""
LeetCode 1687. Delivering Boxes from Storage to Ports

Given n boxes, each box has a port, weight, and you can carry up to maxBoxes and maxWeight. Return the minimum number of trips to deliver all boxes in order.

Example 1:
Input: boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3
Output: 4

Constraints:
- 1 <= boxes.length <= 10^5
- 1 <= portsCount, maxBoxes, maxWeight <= 10^5
- 1 <= boxes[i][0] <= portsCount
- 1 <= boxes[i][1] <= maxWeight
"""

def boxDelivering(boxes, portsCount, maxBoxes, maxWeight):
    n = len(boxes)
    dp = [0] + [float('inf')]*n
    j = k = w = 0
    for i in range(1, n+1):
        w += boxes[i-1][1]
        if i == 1 or boxes[i-1][0] != boxes[i-2][0]:
            k += 1
        while w > maxWeight or i-j > maxBoxes:
            w -= boxes[j][1]
            if boxes[j][0] != boxes[j-1][0]:
                k -= 1
            j += 1
        dp[i] = min(dp[i], dp[j] + k + 1)
    return dp[n]

# Example usage:
# boxes = [[1,1],[2,1],[1,1]]
# portsCount = 2
# maxBoxes = 3
# maxWeight = 3
# print(boxDelivering(boxes, portsCount, maxBoxes, maxWeight))  # Output: 4
