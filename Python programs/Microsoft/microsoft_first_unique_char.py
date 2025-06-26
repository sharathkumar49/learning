# Microsoft: Find First Unique Character in a String
# Given a string, find the first non-repeating character and return its index. If it doesn't exist, return -1.
from collections import Counter

def first_uniq_char(s):
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1

if __name__ == "__main__":
    s1 = "leetcode"
    print(first_uniq_char(s1))  # Output: 0
    s2 = "loveleetcode"
    print(first_uniq_char(s2))  # Output: 2
    s3 = "aabb"
    print(first_uniq_char(s3))  # Output: -1
