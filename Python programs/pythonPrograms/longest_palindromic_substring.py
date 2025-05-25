# Longest palindromic substring
def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if sub == sub[::-1] and len(sub) > len(res):
                res = sub
    return res

if __name__ == "__main__":
    s = input("String: ")
    print("Longest palindrome:", longest_palindrome(s))
