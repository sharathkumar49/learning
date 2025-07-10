"""
LeetCode 1554. Strings Differ by One Character

Given a list of strings dict, return true if there are two strings that differ by exactly one character in the same position.

Constraints:
- 2 <= dict.length <= 10^5
- 1 <= dict[i].length <= 100

Example:
Input: dict = ["abcd","acbd","aacd"]
Output: True
"""
def differByOne(dict):
    seen = set()
    for word in dict:
        for i in range(len(word)):
            mask = word[:i] + '*' + word[i+1:]
            if mask in seen:
                return True
            seen.add(mask)
    return False

# Example usage:
dict = ["abcd","acbd","aacd"]
print(differByOne(dict))  # Output: True
