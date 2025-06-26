# Microsoft: Word Break II
# Given a string s and a dictionary of words, return all possible sentences where s can be segmented into a space-separated sequence of one or more dictionary words.

def word_break_ii(s, word_dict):
    memo = {}
    def dfs(start):
        if start in memo:
            return memo[start]
        res = []
        if start == len(s):
            res.append("")
        for end in range(start+1, len(s)+1):
            word = s[start:end]
            if word in word_dict:
                for sub in dfs(end):
                    res.append(word + (" " + sub if sub else ""))
        memo[start] = res
        return res
    return dfs(0)

if __name__ == "__main__":
    s1 = "catsanddog"
    word_dict1 = {"cat", "cats", "and", "sand", "dog"}
    print(word_break_ii(s1, word_dict1))  # Output: ["cats and dog", "cat sand dog"]
    s2 = "pineapplepenapple"
    word_dict2 = {"apple", "pen", "applepen", "pine", "pineapple"}
    print(word_break_ii(s2, word_dict2))
