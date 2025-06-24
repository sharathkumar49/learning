"""
LeetCode 1298. Maximum Candies You Can Get from Boxes

You have n boxes. Each box has candies, keys to other boxes, and other boxes inside. Some boxes are open, some are closed. You can only open a box if you have a key or it is already open. Return the maximum number of candies you can collect.

Constraints:
- 1 <= status.length <= 1000
- status[i] is 0 or 1
- 1 <= candies.length, keys.length, containedBoxes.length <= status.length
- 0 <= keys[i].length, containedBoxes[i].length <= status.length
- 0 <= status[i], candies[i] <= 2000
- 0 <= keys[i][j], containedBoxes[i][j] < status.length
- 1 <= initialBoxes.length <= status.length

Example:
Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
Output: 16
"""
def maxCandies(status, candies, keys, containedBoxes, initialBoxes):
    from collections import deque
    n = len(status)
    queue = deque(initialBoxes)
    opened = set()
    have = set(initialBoxes)
    res = 0
    while queue:
        box = queue.popleft()
        if status[box] == 1:
            res += candies[box]
            opened.add(box)
            for k in keys[box]:
                status[k] = 1
                if k in have and k not in opened:
                    queue.append(k)
            for b in containedBoxes[box]:
                have.add(b)
                if status[b] == 1 and b not in opened:
                    queue.append(b)
        else:
            queue.append(box)
            if all(status[b] == 0 or b in opened for b in queue):
                break
    return res

# Example usage:
status = [1,0,1,0]
candies = [7,5,4,100]
keys = [[],[],[1],[]]
containedBoxes = [[1,2],[3],[],[]]
initialBoxes = [0]
print(maxCandies(status, candies, keys, containedBoxes, initialBoxes))  # Output: 16
