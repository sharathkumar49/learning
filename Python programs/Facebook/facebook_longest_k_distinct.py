# Facebook: Longest Substring with At Most K Distinct Characters
# Given a string, find the length of the longest substring that contains at most k distinct characters.

def length_of_longest_substring_k_distinct(s, k):
    if k == 0 or not s:
        return 0
    left = 0
    count = {}
    max_len = 0
    for right, char in enumerate(s):
        count[char] = count.get(char, 0) + 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    s1 = "eceba"
    print(length_of_longest_substring_k_distinct(s1, 2))  # Output: 3
    s2 = "aa"
    print(length_of_longest_substring_k_distinct(s2, 1))  # Output: 2
