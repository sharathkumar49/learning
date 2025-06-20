"""
850. Rectangle Area II

You are given a list of rectangles. Return the total area covered by the rectangles.

Example 1:
Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6

Constraints:
- 1 <= rectangles.length <= 200
- rects[i].length == 4
- 0 <= rectangles[i][j] <= 10^9
- The total area is guaranteed to fit in a 32-bit integer.
"""
def rectangleArea(rectangles):
    MOD = 10**9 + 7
    events = []
    for x1, y1, x2, y2 in rectangles:
        events.append((x1, y1, y2, 1))
        events.append((x2, y1, y2, -1))
    events.sort()
    import bisect
    ylist = sorted(set([y for _, y1, y2, _ in events for y in (y1, y2)]))
    y_i = {y: i for i, y in enumerate(ylist)}
    count = [0] * (len(ylist) - 1)
    prev_x = area = 0
    for x, y1, y2, sig in events:
        area += sum((ylist[i+1] - ylist[i]) for i, c in enumerate(count) if c) * (x - prev_x)
        for i in range(y_i[y1], y_i[y2]):
            count[i] += sig
        prev_x = x
    return area % MOD

# Example usage:
print(rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))  # Output: 6
