"""
841. Keys and Rooms

There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Each room has a list of keys to other rooms. Return true if you can visit all the rooms.

Example 1:
Input: rooms = [[1],[2],[3],[]]
Output: true

Example 2:
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false

Constraints:
- n == rooms.length
- 1 <= n <= 1000
- 0 <= rooms[i].length <= 1000
- 1 <= sum(rooms[i].length) <= 3000
- 0 <= rooms[i][j] < n
- All the values of rooms[i] are unique.
"""
def canVisitAllRooms(rooms):
    visited = set()
    def dfs(room):
        if room in visited:
            return
        visited.add(room)
        for key in rooms[room]:
            dfs(key)
    dfs(0)
    return len(visited) == len(rooms)

# Example usage:
print(canVisitAllRooms([[1],[2],[3],[]]))  # Output: True
print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))  # Output: False
