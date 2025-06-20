#  554. Brick Wall
#  Difficulty: Medium
# 
#  There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number of bricks each of the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.
# 
#  The line should go through the edge between two bricks (if possible) and not through the middle of a brick.
# 
#  Return the minimum number of crossed bricks after drawing such a line.
# 
#  Example 1:
#  Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
#  Output: 2
# 
#  Example 2:
#  Input: wall = [[1],[1],[1]]
#  Output: 3
# 
#  Constraints:
#  1 <= wall.length <= 10^4
#  1 <= wall[i].length <= 10^4
#  1 <= sum(wall[i]) <= 2 * 10^4
#  sum(wall[i]) is the same for each row.

def leastBricks(wall):
    from collections import defaultdict
    edge_count = defaultdict(int)
    for row in wall:
        pos = 0
        for brick in row[:-1]:
            pos += brick
            edge_count[pos] += 1
    return len(wall) - max(edge_count.values(), default=0)

# Example usage
if __name__ == "__main__":
    wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
    print(leastBricks(wall))  # Output: 2
    print(leastBricks([[1],[1],[1]]))  # Output: 3
