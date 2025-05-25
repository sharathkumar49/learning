# LinkedIn: Longest substring with at most two distinct characters
def length_of_longest_substring_two_distinct(s):
    left = 0
    max_len = 0
    char_map = {}
    for right, c in enumerate(s):
        char_map[c] = right
        if len(char_map) > 2:
            del_idx = min(char_map.values())
            del char_map[s[del_idx]]
            left = del_idx + 1
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    s = input("Enter string: ")
    print("Longest substring with at most two distinct:", length_of_longest_substring_two_distinct(s))
