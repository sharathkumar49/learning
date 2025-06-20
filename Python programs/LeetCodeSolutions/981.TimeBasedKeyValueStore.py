"""
981. Time Based Key-Value Store
https://leetcode.com/problems/time-based-key-value-store/

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.
Implement the TimeMap class:
- TimeMap() Initializes the object.
- void set(String key, String value, int timestamp) Stores the key and value, along with the given timestamp.
- String get(String key, int timestamp) Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the one with the largest timestamp_prev. If there are no values, it returns "".

Constraints:
- 1 <= key.length, value.length <= 100
- key and value consist of lowercase English letters and digits.
- 1 <= timestamp <= 10^7
- All the timestamps set are strictly increasing.
- At most 2 * 10^5 calls will be made to set and get.

Example:
Input: ["TimeMap","set","get","get","set","get","get"], [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output: [null,null,"bar","bar",null,"bar2","bar2"]
"""
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        i = bisect_right(arr, (timestamp, chr(127)))
        return arr[i-1][1] if i else ""

# Example usage
if __name__ == "__main__":
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    print(tm.get("foo", 1))  # Output: "bar"
    print(tm.get("foo", 3))  # Output: "bar"
    tm.set("foo", "bar2", 4)
    print(tm.get("foo", 4))  # Output: "bar2"
    print(tm.get("foo", 5))  # Output: "bar2"
