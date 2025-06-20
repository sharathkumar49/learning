# 30. Substring with Concatenation of All Words
# You are given a string s and an array of strings words. All the strings of words are of the same length.
# Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, without any intervening characters.
#
# Example 1:
# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
#
# Example 2:
# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
#
# Constraints:
# 1 <= s.length <= 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.

def findSubstring(s, words):
    if not s or not words:
        return []
    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    res = []
    for i in range(len(s) - total_len + 1):
        seen = {}
        for j in range(0, total_len, word_len):
            word = s[i+j:i+j+word_len]
            if word in word_count:
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > word_count[word]:
                    break
            else:
                break
        else:
            res.append(i)
    return res

# Example usage
s = "barfoothefoobarman"
words = ["foo","bar"]
print("Substring with concatenation of all words:", findSubstring(s, words))  # Output: [0,9]
