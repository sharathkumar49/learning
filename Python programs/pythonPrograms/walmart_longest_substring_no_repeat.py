# Walmart: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))  # Output: 3
    print(length_of_longest_substring("bbbbb"))    # Output: 1
