"""
LeetCode 705. Design HashSet

Design a HashSet without using any built-in hash table libraries.

Implement the MyHashSet class:
- MyHashSet() Initializes the object.
- void add(key) Inserts the value key into the HashSet.
- void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
- bool contains(key) Returns true if this set contains the specified key.

Example 1:
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Constraints:
- 0 <= key <= 10^6
- At most 10^4 calls will be made to add, remove, and contains.
"""
class MyHashSet:
    def __init__(self):
        self.size = 10007
        self.buckets = [[] for _ in range(self.size)]
    def add(self, key: int) -> None:
        idx = key % self.size
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)
    def remove(self, key: int) -> None:
        idx = key % self.size
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)
    def contains(self, key: int) -> bool:
        idx = key % self.size
        return key in self.buckets[idx]

# Example usage
if __name__ == "__main__":
    myset = MyHashSet()
    myset.add(1)
    myset.add(2)
    print(myset.contains(1))  # Output: True
    print(myset.contains(3))  # Output: False
    myset.add(2)
    print(myset.contains(2))  # Output: True
    myset.remove(2)
    print(myset.contains(2))  # Output: False
