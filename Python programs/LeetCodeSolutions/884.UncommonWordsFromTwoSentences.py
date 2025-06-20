"""
884. Uncommon Words from Two Sentences

Given two sentences A and B, return all the words that are uncommon in both sentences.

Example 1:
Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:
Input: A = "apple apple", B = "banana"
Output: ["banana"]

Constraints:
- 1 <= A.length, B.length <= 200
- A and B consist of lowercase English letters and spaces.
"""
def uncommonFromSentences(A, B):
    from collections import Counter
    count = Counter(A.split()) + Counter(B.split())
    return [word for word in count if count[word] == 1]

# Example usage:
print(uncommonFromSentences("this apple is sweet", "this apple is sour"))  # Output: ["sweet","sour"]
print(uncommonFromSentences("apple apple", "banana"))  # Output: ["banana"]
