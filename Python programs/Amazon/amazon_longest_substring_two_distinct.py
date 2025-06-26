# Amazon: Find the Longest Substring with At Most Two Distinct Characters
# Given a string s, return the length of the longest substring that contains at most two distinct characters.

def length_of_longest_substring_two_distinct(s):
    left = 0
    count = {}
    max_len = 0
    for right, char in enumerate(s):
        count[char] = count.get(char, 0) + 1
        while len(count) > 2:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    print(length_of_longest_substring_two_distinct("eceba"))  # Output: 3
    print(length_of_longest_substring_two_distinct("ccaabbb"))  # Output: 5
