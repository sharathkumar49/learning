"""
LeetCode 1801. Number of Orders in the Backlog

Given a list of buy and sell orders, return the total number of orders in the backlog after processing all orders.

Example 1:
Input: orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
Output: 6

Constraints:
- 1 <= orders.length <= 10^5
- orders[i].length == 3
- 1 <= pricei, amounti <= 10^9
- orderTypei is 0 (buy) or 1 (sell)
"""

def getNumberOfBacklogOrders(orders):
    import heapq
    buy, sell = [], []
    MOD = 10**9+7
    for price, amount, orderType in orders:
        if orderType == 0:
            while amount and sell and sell[0][0] <= price:
                sp, sa = heapq.heappop(sell)
                if sa > amount:
                    heapq.heappush(sell, (sp, sa-amount))
                    amount = 0
                else:
                    amount -= sa
            if amount:
                heapq.heappush(buy, (-price, amount))
        else:
            while amount and buy and -buy[0][0] >= price:
                bp, ba = heapq.heappop(buy)
                if ba > amount:
                    heapq.heappush(buy, (bp, ba-amount))
                    amount = 0
                else:
                    amount -= ba
            if amount:
                heapq.heappush(sell, (price, amount))
    return (sum(a for _, a in buy) + sum(a for _, a in sell)) % MOD

# Example usage:
# orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
# print(getNumberOfBacklogOrders(orders))  # Output: 6
