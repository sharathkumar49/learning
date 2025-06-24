"""
1233. Remove Sub-Folders from the Filesystem

Given a list of folder paths, return the list after removing all sub-folders. A folder is a sub-folder if it is inside another folder.

Constraints:
- 1 <= folder.length <= 4 * 10^4
- 2 <= folder[i].length <= 100
- folder[i] contains only lowercase English letters, '/' and is a valid path.

Example:
Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]

"""
def removeSubfolders(folder):
    folder.sort()
    res = []
    for f in folder:
        if not res or not f.startswith(res[-1] + '/'):
            res.append(f)
    return res

# Example usage
if __name__ == "__main__":
    print(removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))  # Output: ['/a','/c/d','/c/f']
