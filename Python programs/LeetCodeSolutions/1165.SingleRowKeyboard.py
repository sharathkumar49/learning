"""
1165. Single-Row Keyboard

Given a string keyboard of length 26 indicating the layout of the keyboard, and a string word, return the total time to type the word using one finger starting at index 0. Time to move from index i to j is |i - j|.

Constraints:
- keyboard.length == 26
- word consists of lowercase English letters.

Example:
Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
Output: 4

"""
def calculateTime(keyboard, word):
    pos = {c: i for i, c in enumerate(keyboard)}
    time = 0
    prev = 0
    for ch in word:
        time += abs(pos[ch] - prev)
        prev = pos[ch]
    return time

# Example usage
if __name__ == "__main__":
    print(calculateTime("abcdefghijklmnopqrstuvwxyz", "cba"))  # Output: 4
