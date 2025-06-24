"""
1153. String Transforms Into Another String

Given two strings str1 and str2 of the same length, return True if str1 can be transformed into str2 by repeatedly converting all occurrences of one character in str1 to any other lowercase English character. Each transformation must be applied to all occurrences of a character at once.

Constraints:
- 1 <= str1.length == str2.length <= 1000
- str1 and str2 consist of lowercase English letters.

Example:
Input: str1 = "aabcc", str2 = "ccdee"
Output: True

"""
def canConvert(str1, str2):
    if str1 == str2:
        return True
    mapping = {}
    for a, b in zip(str1, str2):
        if a in mapping and mapping[a] != b:
            return False
        mapping[a] = b
    return len(set(str2)) < 26

# Example usage
if __name__ == "__main__":
    print(canConvert("aabcc", "ccdee"))  # Output: True
