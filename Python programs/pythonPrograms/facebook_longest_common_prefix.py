# Facebook: Find the Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

if __name__ == "__main__":
    arr1 = ["flower","flow","flight"]
    print(longest_common_prefix(arr1))  # Output: "fl"
    arr2 = ["dog","racecar","car"]
    print(longest_common_prefix(arr2))  # Output: ""
