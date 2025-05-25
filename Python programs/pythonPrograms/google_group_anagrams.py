# Google: Group Anagrams
# Given an array of strings, group anagrams together.
from collections import defaultdict

def group_anagrams(strs):
    res = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        res[key].append(s)
    return list(res.values())

if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    # Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
