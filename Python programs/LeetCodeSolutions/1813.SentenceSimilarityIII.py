"""
LeetCode 1813. Sentence Similarity III

Given two sentences, return true if they are similar as described in the problem.

Example 1:
Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
Output: true

Constraints:
- 1 <= sentence1.length, sentence2.length <= 100
- sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces
"""

def areSentencesSimilar(sentence1, sentence2):
    s1 = sentence1.split()
    s2 = sentence2.split()
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    l = 0
    while l < len(s2) and s1[l] == s2[l]:
        l += 1
    r = 0
    while r < len(s2) - l and s1[-1-r] == s2[-1-r]:
        r += 1
    return l + r == len(s2)

# Example usage:
# sentence1 = "My name is Haley"
# sentence2 = "My Haley"
# print(areSentencesSimilar(sentence1, sentence2))  # Output: True
