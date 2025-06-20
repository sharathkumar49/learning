"""
588. Design In-Memory File System
Difficulty: Hard

Design an in-memory file system to simulate the following functions:
- ls: List the files and directories in a given path.
- mkdir: Create a directory at the given path.
- addContentToFile: Add content to a file.
- readContentFromFile: Read content from a file.

Example:
Input:
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
Output:
[null,[],null,null,["a"],"hello"]

Constraints:
1 <= command.length <= 200
1 <= path.length, content.length <= 50
The input is valid.
"""

class FileSystem:
    def __init__(self):
        self.fs = {'/': {}}
    def ls(self, path: str):
        node = self.fs['/']
        if path != '/':
            parts = path.strip('/').split('/')
            for p in parts:
                node = node[p]
            if isinstance(node, str):
                return [parts[-1]]
        return sorted(node.keys())
    def mkdir(self, path: str):
        node = self.fs['/']
        for p in path.strip('/').split('/'):
            if p:
                node = node.setdefault(p, {})
    def addContentToFile(self, filePath: str, content: str):
        node = self.fs['/']
        parts = filePath.strip('/').split('/')
        for p in parts[:-1]:
            node = node.setdefault(p, {})
        node[parts[-1]] = node.get(parts[-1], '') + content
    def readContentFromFile(self, filePath: str) -> str:
        node = self.fs['/']
        parts = filePath.strip('/').split('/')
        for p in parts[:-1]:
            node = node[p]
        return node[parts[-1]]

# Example usage
# fs = FileSystem()
# fs.mkdir("/a/b/c")
# fs.addContentToFile("/a/b/c/d", "hello")
# print(fs.ls("/"))  # Output: ['a']
# print(fs.readContentFromFile("/a/b/c/d"))  # Output: 'hello'
