"""
LeetCode 1648. Sell Diminishing-Valued Colored Balls

Given an array of integers inventory and an integer orders, return the maximum profit you can achieve by selling balls. Each time you sell a ball, the value decreases by 1.

Example 1:
Input: inventory = [2,5], orders = 4
Output: 14

Constraints:
- 1 <= inventory.length <= 10^5
- 1 <= inventory[i] <= 10^9
- 1 <= orders <= min(sum(inventory), 10^9)
"""

def maxProfit(inventory, orders):
    mod = 10**9+7
    inventory.sort(reverse=True)
    inventory.append(0)
    res = 0
    k = 1
    for i in range(len(inventory)-1):
        if inventory[i] > inventory[i+1]:
            sell = min(orders, k*(inventory[i]-inventory[i+1]))
            whole, rem = divmod(sell, k)
            res += k*(inventory[i]+inventory[i]-whole+1)*whole//2
            res += rem*(inventory[i]-whole)
            res %= mod
            orders -= sell
            if orders == 0:
                break
        k += 1
    return res

# Example usage:
# inventory = [2,5]
# orders = 4
# print(maxProfit(inventory, orders))  # Output: 14
