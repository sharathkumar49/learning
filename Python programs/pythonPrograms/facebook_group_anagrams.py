# Facebook: Group Anagrams
# Given an array of strings, group anagrams together.
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())

if __name__ == "__main__":
    arr1 = ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams(arr1))
    arr2 = [""]
    print(group_anagrams(arr2))
    arr3 = ["a"]
    print(group_anagrams(arr3))
