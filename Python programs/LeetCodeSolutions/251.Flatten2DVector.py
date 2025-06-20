"""
251. Flatten 2D Vector
https://leetcode.com/problems/flatten-2d-vector/

Design and implement an iterator to flatten a 2d vector. It should support the next and hasNext operations.

Constraints:
- 0 <= vec.length <= 200
- 0 <= vec[i].length <= 500
- At most 10^4 calls will be made to next and hasNext.

Example:
Input
["Vector2D","next","next","hasNext","next","hasNext"]
[[[[1,2],[3],[4]]],[],[],[],[],[]]
Output
[null,1,2,true,3,true]
"""
class Vector2D:
    def __init__(self, vec):
        self.vec = vec
        self.row = 0
        self.col = 0
    def next(self):
        if not self.hasNext():
            raise Exception('No more elements')
        val = self.vec[self.row][self.col]
        self.col += 1
        return val
    def hasNext(self):
        while self.row < len(self.vec) and self.col == len(self.vec[self.row]):
            self.row += 1
            self.col = 0
        return self.row < len(self.vec)

# Example usage:
if __name__ == "__main__":
    v = Vector2D([[1,2],[3],[4]])
    print(v.next())    # Output: 1
    print(v.next())    # Output: 2
    print(v.hasNext()) # Output: True
    print(v.next())    # Output: 3
    print(v.hasNext()) # Output: True
    print(v.next())    # Output: 4
    print(v.hasNext()) # Output: False
