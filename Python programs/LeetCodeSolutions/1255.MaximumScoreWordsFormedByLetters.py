"""
1255. Maximum Score Words Formed by Letters

Given a list of words, letters, and score for each letter, return the maximum score of any valid set of words formed.

Constraints:
- 1 <= words.length <= 14
- 1 <= words[i].length <= 15
- 1 <= letters.length <= 100
- score.length == 26

Example:
Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23

"""
def maxScoreWords(words, letters, score):
    from collections import Counter
    letter_count = Counter(letters)
    def dfs(i, count):
        if i == len(words):
            return 0
        res = dfs(i+1, count)
        word_count = Counter(words[i])
        if all(count[c] >= word_count[c] for c in word_count):
            for c in word_count:
                count[c] -= word_count[c]
            res = max(res, sum(score[ord(c)-97]*word_count[c] for c in word_count) + dfs(i+1, count))
            for c in word_count:
                count[c] += word_count[c]
        return res
    return dfs(0, letter_count)

# Example usage
if __name__ == "__main__":
    words = ["dog","cat","dad","good"]
    letters = ["a","a","c","d","d","g","o","o"]
    score = [1,0,9,5,0,0,3,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
    print(maxScoreWords(words, letters, score))  # Output: 23
