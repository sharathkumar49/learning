# 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
#
# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
#
# Constraints:
# 1 <= haystack.length, needle.length <= 10^4
# haystack and needle consist of only lowercase English characters.

def strStr(haystack, needle):
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

# Example usage
haystack = "sadbutsad"
needle = "sad"
print("Index of first occurrence:", strStr(haystack, needle))  # Output: 0
