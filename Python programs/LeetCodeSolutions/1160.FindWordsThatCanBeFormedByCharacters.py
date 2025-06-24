"""
1160. Find Words That Can Be Formed by Characters

Given an array of strings words and a string chars, return the sum of lengths of all good strings. A string is good if it can be formed by characters from chars (each character can only be used once).

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length, chars.length <= 100
- words[i] and chars consist of lowercase English letters.

Example:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6

"""
def countCharacters(words, chars):
    from collections import Counter
    chars_count = Counter(chars)
    total = 0
    for word in words:
        word_count = Counter(word)
        if all(word_count[c] <= chars_count.get(c, 0) for c in word_count):
            total += len(word)
    return total

# Example usage
if __name__ == "__main__":
    print(countCharacters(["cat","bt","hat","tree"], "atach"))  # Output: 6
