# Turing: Word Break
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

def word_break(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    return dp[-1]

if __name__ == "__main__":
    print(word_break("leetcode", ["leet", "code"]))  # Output: True
    print(word_break("applepenapple", ["apple", "pen"]))  # Output: True
    print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # Output: False
