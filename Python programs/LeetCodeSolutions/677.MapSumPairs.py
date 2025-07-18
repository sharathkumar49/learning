"""
LeetCode 677. Map Sum Pairs

Design a map that allows you to do the following:
- Maps a string key to a given value.
- Returns the sum of the values that have a key with a prefix equal to a given string.

Implement the MapSum class:
- MapSum() Initializes the MapSum object.
- void insert(String key, int val) Inserts the key-val pair into the map. If the key already existed, the original key-value pair will be overridden to the new one.
- int sum(string prefix) Returns the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple",3], ["ap"], ["app",2], ["ap"]]
Output
[null, null, 3, null, 5]

Constraints:
- 1 <= key.length, prefix.length <= 50
- key and prefix consist of only lowercase English letters.
- 1 <= val <= 1000
- At most 50 calls will be made to insert and sum.
"""
class MapSum:
    def __init__(self):
        self.map = {}
    def insert(self, key: str, val: int) -> None:
        self.map[key] = val
    def sum(self, prefix: str) -> int:
        return sum(v for k, v in self.map.items() if k.startswith(prefix))

# Example usage
if __name__ == "__main__":
    mapsum = MapSum()
    mapsum.insert("apple", 3)
    print(mapsum.sum("ap"))  # Output: 3
    mapsum.insert("app", 2)
    print(mapsum.sum("ap"))  # Output: 5
