# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
#
# Example 2:
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
# Constraints:
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.

def groupAnagrams(strs):
    from collections import defaultdict
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

# Example usage
strs = ["eat","tea","tan","ate","nat","bat"]
print("Grouped anagrams:", groupAnagrams(strs))  # Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
