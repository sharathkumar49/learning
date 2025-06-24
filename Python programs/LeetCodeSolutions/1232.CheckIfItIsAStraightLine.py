"""
1232. Check If It Is a Straight Line

Given n coordinates, return True if they all lie on a straight line.

Constraints:
- 2 <= coordinates.length <= 1000
- coordinates[i].length == 2
- -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4

Example:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: True

"""
def checkStraightLine(coordinates):
    (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
    for x, y in coordinates:
        if (x1 - x0) * (y - y0) != (y1 - y0) * (x - x0):
            return False
    return True

# Example usage
if __name__ == "__main__":
    print(checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))  # Output: True
