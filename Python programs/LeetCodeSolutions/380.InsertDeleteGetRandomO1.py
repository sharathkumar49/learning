"""
380. Insert Delete GetRandom O(1)

Implement the RandomizedSet class:
- RandomizedSet() Initializes the RandomizedSet object.
- bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current set of elements. Each element must have the same probability of being returned.

Constraints:
- -2^31 <= val <= 2^31 - 1
- At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
"""
import random

class RandomizedSet:
    def __init__(self):
        self.vals = []
        self.idx = {}
    def insert(self, val: int) -> bool:
        if val in self.idx:
            return False
        self.idx[val] = len(self.vals)
        self.vals.append(val)
        return True
    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        last, i = self.vals[-1], self.idx[val]
        self.vals[i] = last
        self.idx[last] = i
        self.vals.pop()
        del self.idx[val]
        return True
    def getRandom(self) -> int:
        return random.choice(self.vals)

# Example usage:
rs = RandomizedSet()
print(rs.insert(1))  # Output: True
print(rs.remove(2))  # Output: False
print(rs.insert(2))  # Output: True
print(rs.getRandom()) # Output: 1 or 2
print(rs.remove(1))  # Output: True
print(rs.insert(2))  # Output: False
print(rs.getRandom()) # Output: 2
