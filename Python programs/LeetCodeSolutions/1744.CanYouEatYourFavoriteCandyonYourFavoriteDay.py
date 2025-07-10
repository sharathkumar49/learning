"""
LeetCode 1744. Can You Eat Your Favorite Candy on Your Favorite Day?

Given an array candiesCount and queries, for each query [favoriteType, favoriteDay, dailyCap], return true if you can eat a candy of favoriteType on favoriteDay.

Example 1:
Input: candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
Output: [true,false,true]

Constraints:
- 1 <= candiesCount.length <= 10^5
- 1 <= queries.length <= 10^5
- 1 <= candiesCount[i] <= 10^5
- 0 <= favoriteType < candiesCount.length
- 0 <= favoriteDay < 10^9
- 1 <= dailyCap <= 10^9
"""

def canEat(candiesCount, queries):
    prefix = [0]
    for c in candiesCount:
        prefix.append(prefix[-1] + c)
    res = []
    for t, d, cap in queries:
        min_candies = d + 1
        max_candies = (d + 1) * cap
        res.append(min_candies <= prefix[t+1] and max_candies > prefix[t])
    return res

# Example usage:
# candiesCount = [7,4,5,3,8]
# queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
# print(canEat(candiesCount, queries))  # Output: [True, False, True]
