"""
460. LFU Cache

Design and implement a data structure for a Least Frequently Used (LFU) cache.
Implement the LFUCache class:
- LFUCache(int capacity) Initializes the object with the capacity of the data structure.
- int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
- void put(int key, int value) Update the value of the key if present, or inserts the key if not present. When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item.

Constraints:
- 0 <= capacity <= 10^4
- 0 <= key <= 10^5
- 0 <= value <= 10^9
- At most 2 * 10^5 calls will be made to get and put.

Example:
Input: ["LFUCache","put","put","get","put","get","get","put","get","get","get"], [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
Output: [null,null,null,1,null,-1,3,null,-1,3,4]
"""

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2val = {}
        self.key2freq = {}
        self.freq2keys = defaultdict(OrderedDict)
        self.minfreq = 0

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        self._update(key)
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.key2val:
            self.key2val[key] = value
            self._update(key)
            return
        if len(self.key2val) == self.cap:
            k, _ = self.freq2keys[self.minfreq].popitem(last=False)
            del self.key2val[k]
            del self.key2freq[k]
        self.key2val[key] = value
        self.key2freq[key] = 1
        self.freq2keys[1][key] = None
        self.minfreq = 1

    def _update(self, key):
        freq = self.key2freq[key]
        del self.freq2keys[freq][key]
        if not self.freq2keys[freq]:
            del self.freq2keys[freq]
            if self.minfreq == freq:
                self.minfreq += 1
        self.key2freq[key] = freq + 1
        self.freq2keys[freq + 1][key] = None

# Example usage:
lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))  # Output: 1
lfu.put(3, 3)
print(lfu.get(2))  # Output: -1
print(lfu.get(3))  # Output: 3
lfu.put(4, 4)
print(lfu.get(1))  # Output: -1
print(lfu.get(3))  # Output: 3
print(lfu.get(4))  # Output: 4
