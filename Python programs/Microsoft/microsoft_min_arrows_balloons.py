# Microsoft: Find the Minimum Number of Arrows to Burst Balloons
# Given a list of intervals representing balloons, return the minimum number of arrows required to burst all balloons.

def find_min_arrow_shots(points):
    if not points:
        return 0
    points.sort(key=lambda x: x[1])
    arrows = 1
    end = points[0][1]
    for x, y in points[1:]:
        if x > end:
            arrows += 1
            end = y
    return arrows

if __name__ == "__main__":
    points1 = [[10,16],[2,8],[1,6],[7,12]]
    print(find_min_arrow_shots(points1))  # Output: 2
    points2 = [[1,2],[3,4],[5,6],[7,8]]
    print(find_min_arrow_shots(points2))  # Output: 4
