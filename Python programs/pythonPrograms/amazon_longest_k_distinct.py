# Amazon: Longest Substring with At Most K Distinct Characters
def length_of_longest_substring_k_distinct(s, k):
    left = 0
    max_len = 0
    char_map = {}
    for right, c in enumerate(s):
        char_map[c] = char_map.get(c, 0) + 1
        while len(char_map) > k:
            char_map[s[left]] -= 1
            if char_map[s[left]] == 0:
                del char_map[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    s = input("Enter string: ")
    k = int(input("Enter k: "))
    print("Length:", length_of_longest_substring_k_distinct(s, k))
