"""
1166. Design File System

Design a file system that supports creating new paths and setting values, and getting the value for a path. Return True if a path is created successfully, else False.

Constraints:
- 1 <= path.length <= 500
- path consists of lowercase English letters and '/'.
- At most 300 calls will be made to create and get.

Example:
Input: ["FileSystem","createPath","get","createPath","get"], [[],["/a",1],["/a"],["/a/b",2],["/a/b"]]
Output: [null,true,1,true,2]

"""
class FileSystem:
    def __init__(self):
        self.paths = {'': -1}
    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths or not path or path == '/':
            return False
        parent = path[:path.rfind('/')]
        if parent not in self.paths:
            return False
        self.paths[path] = value
        return True
    def get(self, path: str) -> int:
        return self.paths.get(path, -1)

# Example usage
if __name__ == "__main__":
    fs = FileSystem()
    print(fs.createPath("/a", 1))  # Output: True
    print(fs.get("/a"))            # Output: 1
    print(fs.createPath("/a/b", 2)) # Output: True
    print(fs.get("/a/b"))          # Output: 2
