"""
LeetCode 686. Repeated String Match

Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b to be a substring in this way, return -1.

Example 1:
Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: "abcd" repeated 3 times is "abcdabcdabcd", which contains "cdabcdab" as a substring.

Example 2:
Input: a = "a", b = "aa"
Output: 2

Constraints:
- 1 <= a.length, b.length <= 10^4
- a and b consist of lowercase English letters.
"""
def repeatedStringMatch(a: str, b: str) -> int:
    q = -(-len(b) // len(a))  # Ceiling division
    for i in range(q, q+2):
        if b in a * i:
            return i
    return -1

# Example usage
if __name__ == "__main__":
    print(repeatedStringMatch("abcd", "cdabcdab"))  # Output: 3
    print(repeatedStringMatch("a", "aa"))           # Output: 2
