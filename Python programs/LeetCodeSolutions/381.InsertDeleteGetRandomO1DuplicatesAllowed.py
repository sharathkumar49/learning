"""
381. Insert Delete GetRandom O(1) - Duplicates allowed

Implement the RandomizedCollection class:
- RandomizedCollection() Initializes the RandomizedCollection object.
- bool insert(int val) Inserts an item val into the collection. Returns true if the item was not present, false otherwise.
- bool remove(int val) Removes an item val from the collection if present. Returns true if the item was present, false otherwise.
- int getRandom() Returns a random element from the current collection of elements. The probability of each element being returned is linearly related to the number of same values the collection contains.

Constraints:
- -2^31 <= val <= 2^31 - 1
- At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
"""
import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.vals = []
        self.idx = defaultdict(set)
    def insert(self, val: int) -> bool:
        self.vals.append(val)
        self.idx[val].add(len(self.vals) - 1)
        return len(self.idx[val]) == 1
    def remove(self, val: int) -> bool:
        if not self.idx[val]:
            return False
        remove_idx = self.idx[val].pop()
        last = self.vals[-1]
        self.vals[remove_idx] = last
        self.idx[last].add(remove_idx)
        self.idx[last].discard(len(self.vals) - 1)
        self.vals.pop()
        return True
    def getRandom(self) -> int:
        return random.choice(self.vals)

# Example usage:
rc = RandomizedCollection()
print(rc.insert(1))  # Output: True
print(rc.insert(1))  # Output: False
print(rc.insert(2))  # Output: True
print(rc.getRandom()) # Output: 1 or 2
print(rc.remove(1))  # Output: True
print(rc.getRandom()) # Output: 1 or 2
