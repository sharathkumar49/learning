"""
LeetCode 761. Special Binary String

Special binary strings are binary strings with the following two properties:
- The number of 0's is equal to the number of 1's.
- Every prefix of the binary string has at least as many 1's as 0's.

Given a special string S, a move consists of choosing two consecutive, non-empty special substrings of S, and swapping them. The goal is to make S lexicographically largest.
Return the lexicographically largest string possible after any number of moves.

Example 1:
Input: S = "11011000"
Output: "11100100"

Constraints:
- 1 <= S.length <= 50
- S consists of '0' and '1'.
- S is a special binary string as defined above.
"""
def makeLargestSpecial(S: str) -> str:
    count = i = 0
    res = []
    for j, c in enumerate(S):
        count += 1 if c == '1' else -1
        if count == 0:
            res.append('1' + makeLargestSpecial(S[i+1:j]) + '0')
            i = j + 1
    return ''.join(sorted(res, reverse=True))

# Example usage
if __name__ == "__main__":
    print(makeLargestSpecial("11011000"))  # Output: "11100100"
