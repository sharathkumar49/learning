"""
249. Group Shifted Strings
https://leetcode.com/problems/group-shifted-strings/

We can shift a string by shifting each of its letters to its successive letter. For example, "abc" -> "bcd". We can keep shifting the string to form a sequence.
Given a string array strings, group all strings that belong to the same shifting sequence. You may return the answer in any order.

Constraints:
- 1 <= strings.length <= 200
- 1 <= strings[i].length <= 50
- strings[i] consists of lowercase English letters.

Example 1:
Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

Example 2:
Input: strings = ["a"]
Output: [["a"]]
"""
def groupStrings(strings):
    from collections import defaultdict
    groups = defaultdict(list)
    for s in strings:
        key = tuple((ord(c) - ord(s[0])) % 26 for c in s)
        groups[key].append(s)
    return list(groups.values())

# Example usage:
if __name__ == "__main__":
    print(groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))
    # Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
    print(groupStrings(["a"]))
    # Output: [["a"]]
