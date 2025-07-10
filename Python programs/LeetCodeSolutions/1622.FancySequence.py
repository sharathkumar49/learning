"""
LeetCode 1622. Fancy Sequence

Design a Fancy class to support the following operations:
- append(val): Appends an integer to the sequence.
- addAll(inc): Increments all elements by inc.
- multAll(m): Multiplies all elements by m.
- getIndex(idx): Returns the current value at index idx modulo 10^9+7, or -1 if idx is invalid.

Example 1:
Input: ["Fancy","append","addAll","append","multAll","getIndex","addAll","append","getIndex"], [[],[2],[3],[7],[2],[0],[3],[10],[0]]
Output: [null,null,null,null,null,10,null,null,26]

Constraints:
- 1 <= val, inc, m <= 100
- At most 10^5 calls will be made to append, addAll, multAll, and getIndex.
"""

class Fancy:
    def __init__(self):
        self.seq = []
        self.add = 0
        self.mul = 1
        self.mod = 10**9+7
        self.inv = [1]
    def append(self, val):
        self.seq.append(((val - self.add) * pow(self.mul, -1, self.mod)) % self.mod)
    def addAll(self, inc):
        self.add = (self.add + inc) % self.mod
    def multAll(self, m):
        self.add = (self.add * m) % self.mod
        self.mul = (self.mul * m) % self.mod
    def getIndex(self, idx):
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.mod

# Example usage:
# f = Fancy()
# f.append(2)
# f.addAll(3)
# f.append(7)
# f.multAll(2)
# print(f.getIndex(0))  # Output: 10
# f.addAll(3)
# f.append(10)
# print(f.getIndex(0))  # Output: 26
