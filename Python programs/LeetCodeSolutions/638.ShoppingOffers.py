"""
638. Shopping Offers
Difficulty: Medium

You are given an integer array price where price[i] is the price of the i-th item, and a 2D array special where special[i] is a list of special offers, and an integer array needs where needs[i] is the number of items you need. Return the minimum cost to satisfy the needs.

Example 1:
Input: price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
Output: 14

Constraints:
1 <= price.length <= 6
0 <= price[i] <= 10
0 <= special.length, needs.length <= 100
0 <= special[i][j] <= 50
0 <= needs[i] <= 6
"""

def shoppingOffers(price, special, needs):
    memo = {}
    def dfs(cur):
        if tuple(cur) in memo:
            return memo[tuple(cur)]
        res = sum(cur[i]*price[i] for i in range(len(price)))
        for sp in special:
            nxt = [cur[i] - sp[i] for i in range(len(price))]
            if min(nxt) >= 0:
                res = min(res, dfs(nxt) + sp[-1])
        memo[tuple(cur)] = res
        return res
    return dfs(needs)

# Example usage
if __name__ == "__main__":
    print(shoppingOffers([2,5], [[3,0,5],[1,2,10]], [3,2]))  # Output: 14
