# Google: Longest Substring Without Repeating Characters
def length_of_longest_substring(s):
    char_map = {}
    left = max_len = 0
    for right, c in enumerate(s):
        if c in char_map and char_map[c] >= left:
            left = char_map[c] + 1
        char_map[c] = right
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    s = input("Enter string: ")
    print("Length:", length_of_longest_substring(s))
