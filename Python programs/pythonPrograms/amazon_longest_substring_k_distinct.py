# Amazon: Longest Substring with At Most K Distinct Characters
# Given a string s and an integer k, return the length of the longest substring with at most k distinct characters.

def length_of_longest_substring_k_distinct(s, k):
    from collections import defaultdict
    left = 0
    max_len = 0
    count = defaultdict(int)
    for right, char in enumerate(s):
        count[char] += 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

if __name__ == "__main__":
    print(length_of_longest_substring_k_distinct("eceba", 2))  # Output: 3
    print(length_of_longest_substring_k_distinct("aa", 1))    # Output: 2
