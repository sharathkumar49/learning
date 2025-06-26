# Adobe: Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        tmp = expand_around_center(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        tmp = expand_around_center(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res

def expand_around_center(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l+1:r]

if __name__ == "__main__":
    print(longest_palindrome("babad"))  # Output: "bab" or "aba"
    print(longest_palindrome("cbbd"))   # Output: "bb"
