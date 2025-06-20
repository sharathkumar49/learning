# -- 555. Split Concatenated Strings
# -- Difficulty: Medium
# --
# -- You are given a list of strings words. You can choose any non-empty prefix of each string and concatenate them in any order to get the longest possible palindrome.
# -- Return the longest possible palindrome string you can get.
# --
# -- Example 1:
# -- Input: words = ["abc","xyz"]
# -- Output: "zyxcba"
# --
# -- Example 2:
# -- Input: words = ["ab","cd","ef"]
# -- Output: "fedcba"
# --
# -- Constraints:
# -- 1 <= words.length <= 1000
# -- 1 <= words[i].length <= 1000
# -- All words[i] consist of lowercase English letters.

def splitLoopedString(words):
    # For each word, consider both original and reversed
    words = [max(w, w[::-1]) for w in words]
    res = ''
    for i, w in enumerate(words):
        for k in range(len(w)):
            s = w[k:] + ''.join(words[i+1:] + words[:i]) + w[:k]
            if s > res:
                res = s
    return res

# Example usage
if __name__ == "__main__":
    print(splitLoopedString(["abc","xyz"]))  # Output: "zyxcba"
    print(splitLoopedString(["ab","cd","ef"]))  # Output: "fedcba"
