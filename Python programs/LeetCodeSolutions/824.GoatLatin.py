"""
824. Goat Latin

A sentence S is given, composed of words separated by spaces. Each word is transformed as follows:
- If the word starts with a vowel, append "ma" to the end.
- If the word starts with a consonant, move the first letter to the end and then append "ma".
- Add one letter 'a' to the end of each word per its word index in the sentence.
Return the final sentence after transformation.

Example 1:
Input: sentence = "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Constraints:
- 1 <= sentence.length <= 150
- sentence consists of English letters and spaces.
- All the words in sentence are separated by a single space.
"""
def toGoatLatin(sentence):
    vowels = set('aeiouAEIOU')
    words = sentence.split()
    res = []
    for i, word in enumerate(words):
        if word[0] in vowels:
            new_word = word + 'ma'
        else:
            new_word = word[1:] + word[0] + 'ma'
        new_word += 'a' * (i + 1)
        res.append(new_word)
    return ' '.join(res)

# Example usage:
print(toGoatLatin("I speak Goat Latin"))  # Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
