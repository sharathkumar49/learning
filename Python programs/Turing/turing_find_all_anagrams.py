# Turing: Find All Anagrams in a String
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
from collections import Counter

def find_anagrams(s, p):
    res = []
    p_count = Counter(p)
    s_count = Counter()
    for i in range(len(s)):
        s_count[s[i]] += 1
        if i >= len(p):
            if s_count[s[i-len(p)]] == 1:
                del s_count[s[i-len(p)]]
            else:
                s_count[s[i-len(p)]] -= 1
        if s_count == p_count:
            res.append(i-len(p)+1)
    return res

if __name__ == "__main__":
    print(find_anagrams("cbaebabacd", "abc"))  # Output: [0, 6]
    print(find_anagrams("abab", "ab"))         # Output: [0, 1, 2]
