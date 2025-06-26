# Microsoft: Find the Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

def length_of_longest_substring(s):
    char_index = {}
    left = max_len = 0
    for right, c in enumerate(s):
        if c in char_index and char_index[c] >= left:
            left = char_index[c] + 1
        char_index[c] = right
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    s1 = "abcabcbb"
    print(length_of_longest_substring(s1))  # Output: 3
    s2 = "bbbbb"
    print(length_of_longest_substring(s2))  # Output: 1
    s3 = "pwwkew"
    print(length_of_longest_substring(s3))  # Output: 3
