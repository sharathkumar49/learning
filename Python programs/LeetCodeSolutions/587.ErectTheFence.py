"""
587. Erect the Fence
Difficulty: Hard

You are given an array trees where trees[i] = [x_i, y_i] represents the location of a tree in the garden. You are asked to fence the entire garden using the minimum length of rope as it is a convex hull problem. Return the coordinates of trees that are exactly located on the fence perimeter.

Example 1:
Input: trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]

Constraints:
1 <= trees.length <= 3000
All the trees are unique.
"""

def outerTrees(trees):
    trees = sorted(map(tuple, trees))
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
    hull = []
    for p in trees + trees[::-1]:
        while len(hull) >= 2 and cross(hull[-2], hull[-1], p) < 0:
            hull.pop()
        if not hull or hull[-1] != p:
            hull.append(p)
    return list(map(list, set(hull)))

# Example usage
if __name__ == "__main__":
    print(outerTrees([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]))  # Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
