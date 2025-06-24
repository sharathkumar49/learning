"""
LeetCode 1333. Filter Restaurants by Vegan-Friendly, Price and Distance

Given a list of restaurants, filter and sort them by vegan-friendly, price, and distance. Return the ids of restaurants after filtering and sorting.

Constraints:
- 1 <= restaurants.length <= 10^4
- restaurants[i].length == 5
- 1 <= id, rating, price, distance <= 10^5
- veganFriendly is 0 or 1

Example:
Input: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10
Output: [3,1,5]
"""
def filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance):
    res = []
    for r in restaurants:
        if (not veganFriendly or r[2]) and r[3] <= maxPrice and r[4] <= maxDistance:
            res.append(r)
    res.sort(key=lambda x: (-x[1], -x[0]))
    return [x[0] for x in res]

# Example usage:
restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
veganFriendly = 1
maxPrice = 50
maxDistance = 10
print(filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))  # Output: [3,1,5]
