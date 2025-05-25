# Amazon: Find All Anagrams in a String
def find_anagrams(s, p):
    from collections import Counter
    res = []
    p_count = Counter(p)
    s_count = Counter(s[:len(p)-1])
    for i in range(len(p)-1, len(s)):
        s_count[s[i]] += 1
        if s_count == p_count:
            res.append(i - len(p) + 1)
        s_count[s[i - len(p) + 1]] -= 1
        if s_count[s[i - len(p) + 1]] == 0:
            del s_count[s[i - len(p) + 1]]
    return res

if __name__ == "__main__":
    s = input("Enter string: ")
    p = input("Enter pattern: ")
    print("Anagram indices:", find_anagrams(s, p))
