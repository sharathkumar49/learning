"""
LeetCode 1487. Making File Names Unique

Given an array of strings names, return an array of strings where each name is made unique by appending the smallest integer (k >= 1) such that the name is not used.

Constraints:
- 1 <= names.length <= 5 * 10^4
- 1 <= names[i].length <= 20
- names[i] consists of lowercase English letters, digits, and/or parentheses.

Example:
Input: names = ["pes","fifa","gta","pes","gta"]
Output: ["pes","fifa","gta","pes(1)","gta(1)"]
"""
def getFolderNames(names):
    used = {}
    res = []
    for name in names:
        if name not in used:
            used[name] = 1
            res.append(name)
        else:
            k = used[name]
            while f"{name}({k})" in used:
                k += 1
            new_name = f"{name}({k})"
            used[name] = k + 1
            used[new_name] = 1
            res.append(new_name)
    return res

# Example usage:
names = ["pes","fifa","gta","pes","gta"]
print(getFolderNames(names))  # Output: ['pes', 'fifa', 'gta', 'pes(1)', 'gta(1)']
