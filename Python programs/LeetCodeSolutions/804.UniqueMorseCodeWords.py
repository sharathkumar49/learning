"""
804. Unique Morse Code Words

Given a list of words, return the number of different Morse code representations.

Example 1:
Input: words = ["gin","zen","gig","msg"]
Output: 2

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 12
- words[i] consists of lowercase English letters.
"""
def uniqueMorseRepresentations(words):
    morse = [".---","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    seen = set()
    for word in words:
        seen.add(''.join(morse[ord(c)-ord('a')] for c in word))
    return len(seen)

# Example usage:
print(uniqueMorseRepresentations(["gin","zen","gig","msg"]))  # Output: 2
