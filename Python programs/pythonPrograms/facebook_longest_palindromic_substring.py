# Facebook: Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        tmp = expand(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        tmp = expand(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res

def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

if __name__ == "__main__":
    s1 = "babad"
    print(longest_palindrome(s1))  # Output: "bab" or "aba"
    s2 = "cbbd"
    print(longest_palindrome(s2))  # Output: "bb"
