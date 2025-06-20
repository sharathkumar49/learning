"""
843. Guess the Word

This is an interactive problem. You are given a secret word and a list of words. You can guess up to 10 times. Each guess returns the number of matching letters in the correct position. Implement the function to find the secret word.

Example 1:
Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
Output: You guessed the secret word within 10 tries.

Constraints:
- 1 <= wordlist.length <= 100
- wordlist[i].length == 6
- All words are lowercase letters.

Note: The Master API is not implemented here. This is a template for the solution.
"""
# The Master API is not implemented in this code. This is a template for the solution.
def findSecretWord(wordlist, master):
    import random
    for _ in range(10):
        guess = random.choice(wordlist)
        matches = master.guess(guess)  # This API is not implemented here
        wordlist = [w for w in wordlist if sum(a==b for a,b in zip(w,guess))==matches]

# Example usage:
# Not executable without the Master API.
