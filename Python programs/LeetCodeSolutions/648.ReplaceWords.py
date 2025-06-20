"""
648. Replace Words
Difficulty: Medium

In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. Given a dictionary consisting of many roots and a sentence, replace all the successors in the sentence with the root forming it. If a successor has many roots that can form it, replace it with the shortest root.

Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Constraints:
1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
1 <= sentence.length <= 10^6
sentence consists of English letters and spaces.
"""

def replaceWords(dictionary, sentence):
    roots = set(dictionary)
    def replace(word):
        for i in range(1, len(word)+1):
            if word[:i] in roots:
                return word[:i]
        return word
    return ' '.join(replace(word) for word in sentence.split())

# Example usage
if __name__ == "__main__":
    print(replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))  # Output: "the cat was rat by the bat"
