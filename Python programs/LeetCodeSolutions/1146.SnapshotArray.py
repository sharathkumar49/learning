"""
1146. Snapshot Array

Implement a SnapshotArray that supports set, snap, and get operations efficiently.

Constraints:
- 1 <= length <= 5 * 10^4
- 0 <= index < length
- 0 <= val <= 10^9
- At most 5 * 10^4 calls will be made to set, snap, and get.

Example:
Input: ["SnapshotArray","set","snap","set","get"]
       [[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]

"""
class SnapshotArray:
    def __init__(self, length: int):
        self.data = [{} for _ in range(length)]
        self.snap_id = 0
    def set(self, index: int, val: int) -> None:
        self.data[index][self.snap_id] = val
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
    def get(self, index: int, snap_id: int) -> int:
        d = self.data[index]
        while snap_id not in d and snap_id >= 0:
            snap_id -= 1
        return d.get(snap_id, 0)

# Example usage
if __name__ == "__main__":
    obj = SnapshotArray(3)
    obj.set(0,5)
    print(obj.snap())  # Output: 0
    obj.set(0,6)
    print(obj.get(0,0))  # Output: 5
