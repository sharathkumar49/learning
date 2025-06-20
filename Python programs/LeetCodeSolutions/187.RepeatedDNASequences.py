"""
187. Repeated DNA Sequences
https://leetcode.com/problems/repeated-dna-sequences/

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either 'A', 'C', 'G', or 'T'.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
"""
def findRepeatedDnaSequences(s):
    seen = set()
    repeated = set()
    for i in range(len(s) - 9):
        seq = s[i:i+10]
        if seq in seen:
            repeated.add(seq)
        else:
            seen.add(seq)
    return list(repeated)

# Example usage:
if __name__ == "__main__":
    print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    # Output: ["AAAAACCCCC","CCCCCAAAAA"]
    print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))
    # Output: ["AAAAAAAAAA"]
