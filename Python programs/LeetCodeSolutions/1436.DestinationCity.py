"""
LeetCode 1436. Destination City

You are given the array paths, where paths[i] = [cityA, cityB] means there exists a direct path going from cityA to cityB. Return the destination city, that is, the city without any path outgoing to another city.

Constraints:
- 1 <= paths.length <= 100
- paths[i].length == 2
- 1 <= cityA.length, cityB.length <= 10
- cityA != cityB

Example:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
"""
def destCity(paths):
    starts = set(a for a, b in paths)
    for a, b in paths:
        if b not in starts:
            return b

# Example usage:
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(destCity(paths))  # Output: "Sao Paulo"
