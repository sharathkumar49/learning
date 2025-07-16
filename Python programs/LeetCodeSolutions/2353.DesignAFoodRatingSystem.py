"""
LeetCode 2353. Design a Food Rating System

Design a food rating system with changeRating and highestRated operations.

Example:
Input: ["FoodRatings","changeRating","highestRated"], [["food1","cuisine1",5],["food1",3],["cuisine1"]]
Output: [null,null,"food1"]

Constraints:
- 1 <= operations.length <= 10^5
"""

class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.foods = {f:(c,r) for f,c,r in zip(foods,cuisines,ratings)}
        self.cuisine_map = {}
        for f,c,r in zip(foods,cuisines,ratings):
            if c not in self.cuisine_map:
                self.cuisine_map[c] = []
            self.cuisine_map[c].append((r,f))
    def changeRating(self, food, newRating):
        c, _ = self.foods[food]
        self.foods[food] = (c, newRating)
        self.cuisine_map[c] = [(self.foods[f][1], f) for _,f in self.cuisine_map[c]]
    def highestRated(self, cuisine):
        return max(self.cuisine_map[cuisine])[1]

# Example usage:
# fr = FoodRatings(["food1"],["cuisine1"],[5])
# fr.changeRating("food1", 3)
# print(fr.highestRated("cuisine1"))  # Output: "food1"
