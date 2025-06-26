# Facebook: Word Break
# Given a string s and a dictionary of words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

def word_break(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[n]

if __name__ == "__main__":
    s1 = "leetcode"
    word_dict1 = {"leet", "code"}
    print(word_break(s1, word_dict1))  # True
    s2 = "applepenapple"
    word_dict2 = {"apple", "pen"}
    print(word_break(s2, word_dict2))  # True
    s3 = "catsandog"
    word_dict3 = {"cats", "dog", "sand", "and", "cat"}
    print(word_break(s3, word_dict3))  # False
