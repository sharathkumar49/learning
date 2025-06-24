"""
LeetCode 1418. Display Table of Food Orders in a Restaurant

Given the array orders, which represents the food orders in a restaurant, return the display table of food orders in the restaurant. The table should be sorted by table number and food name.

Constraints:
- 1 <= orders.length <= 500
- orders[i].length == 3
- 1 <= customerName.length, foodItem.length <= 20
- 1 <= tableNumber <= 500

Example:
Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]
"""
def displayTable(orders):
    from collections import defaultdict
    food_set = set()
    table_orders = defaultdict(lambda: defaultdict(int))
    for _, table, food in orders:
        food_set.add(food)
        table_orders[table][food] += 1
    foods = sorted(food_set)
    tables = sorted(table_orders.keys(), key=lambda x: int(x))
    res = [["Table"] + foods]
    for table in tables:
        row = [table] + [str(table_orders[table][food]) for food in foods]
        res.append(row)
    return res

# Example usage:
orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
print(displayTable(orders))
# Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]
