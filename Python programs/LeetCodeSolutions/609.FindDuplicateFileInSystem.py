"""
609. Find Duplicate File in System
Difficulty: Medium

Given a list of directory info including the directory path and all the files with contents in this directory, return all the groups of duplicate files in the file system in terms of their paths.
A group of duplicate files consists of at least two files that have the same content.

Example 1:
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Constraints:
1 <= paths.length <= 10^4
1 <= paths[i].length <= 3000
1 <= sum(paths[i].length) <= 5 * 10^5

"""

def findDuplicate(paths):
    from collections import defaultdict
    content_map = defaultdict(list)
    for path in paths:
        parts = path.split()
        root = parts[0]
        for file in parts[1:]:
            name, content = file.split('(')
            content = content[:-1]
            content_map[content].append(f"{root}/{name}")
    return [group for group in content_map.values() if len(group) > 1]

# Example usage
if __name__ == "__main__":
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    print(findDuplicate(paths))
    # Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
