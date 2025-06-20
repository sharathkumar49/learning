"""
LeetCode 706. Design HashMap

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:
- MyHashMap() initializes the object.
- void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists, update the value.
- int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
- void remove(int key) removes the mapping for the specified key if this map contains a mapping for the key.

Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1,1], [2,2], [1], [3], [2,1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Constraints:
- 0 <= key, value <= 10^6
- At most 10^4 calls will be made to put, get, and remove.
"""
class MyHashMap:
    def __init__(self):
        self.size = 10007
        self.buckets = [[] for _ in range(self.size)]
    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                return
        self.buckets[idx].append((key, value))
    def get(self, key: int) -> int:
        idx = key % self.size
        for k, v in self.buckets[idx]:
            if k == key:
                return v
        return -1
    def remove(self, key: int) -> None:
        idx = key % self.size
        self.buckets[idx] = [(k, v) for k, v in self.buckets[idx] if k != key]

# Example usage
if __name__ == "__main__":
    hashmap = MyHashMap()
    hashmap.put(1, 1)
    hashmap.put(2, 2)
    print(hashmap.get(1))  # Output: 1
    print(hashmap.get(3))  # Output: -1
    hashmap.put(2, 1)
    print(hashmap.get(2))  # Output: 1
    hashmap.remove(2)
    print(hashmap.get(2))  # Output: -1
