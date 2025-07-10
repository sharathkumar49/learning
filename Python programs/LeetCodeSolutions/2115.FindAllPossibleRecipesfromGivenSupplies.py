"""
LeetCode 2115. Find All Possible Recipes from Given Supplies

Given recipes, ingredients, and supplies, return all recipes that can be made.

Example:
Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour"]
Output: ["bread"]

Constraints:
- 1 <= recipes.length, ingredients.length, supplies.length <= 100
- 1 <= ingredients[i].length <= 100
"""

def findAllRecipes(recipes, ingredients, supplies):
    from collections import defaultdict, deque
    indegree = defaultdict(int)
    graph = defaultdict(list)
    items = set(supplies)
    for r, ing in zip(recipes, ingredients):
        for i in ing:
            graph[i].append(r)
            indegree[r] += 1
    q = deque([x for x in recipes if indegree[x] == 0])
    res = []
    while q:
        x = q.popleft()
        if x in items:
            continue
        res.append(x)
        items.add(x)
        for nei in graph[x]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return res

# Example usage:
# print(findAllRecipes(["bread"], [["yeast","flour"]], ["yeast","flour"]))  # Output: ["bread"]
