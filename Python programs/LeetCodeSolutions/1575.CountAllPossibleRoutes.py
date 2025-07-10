"""
LeetCode 1575. Count All Possible Routes

Given locations, start, finish, and fuel, return the count of all possible routes from start to finish with at most fuel units.

Constraints:
- 2 <= locations.length <= 100
- 1 <= locations[i] <= 10^9
- 0 <= start, finish < locations.length
- 1 <= fuel <= 200

Example:
Input: locations = [2,3,6,6,7], start = 1, finish = 2, fuel = 5
Output: 4
"""
def countRoutes(locations, start, finish, fuel):
    from functools import lru_cache
    n = len(locations)
    mod = 10**9 + 7
    @lru_cache(None)
    def dp(i, f):
        if f < 0:
            return 0
        res = 1 if i == finish else 0
        for j in range(n):
            if i != j:
                res = (res + dp(j, f - abs(locations[i] - locations[j]))) % mod
        return res
    return dp(start, fuel)

# Example usage:
locations = [2,3,6,6,7]
start = 1
finish = 2
fuel = 5
print(countRoutes(locations, start, finish, fuel))  # Output: 4
