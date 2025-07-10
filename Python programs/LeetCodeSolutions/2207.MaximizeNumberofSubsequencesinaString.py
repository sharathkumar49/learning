"""
LeetCode 2207. Maximize Number of Subsequences in a String

Given a string text and a string pattern, return the maximum number of non-overlapping pattern subsequences in text after inserting one character anywhere in text.

Example:
Input: text = "abdcdbc", pattern = "ac"
Output: 4

Constraints:
- 1 <= text.length <= 10^5
- 1 <= pattern.length <= 2
- text and pattern consist of lowercase English letters.
"""

def maximumSubsequenceCount(text: str, pattern: str) -> int:
    if pattern[0] == pattern[1]:
        count = text.count(pattern[0])
        return (count + 1) * count // 2
    
    count1, count2 = 0, 0
    result = 0
    
    # Add pattern[0] at start
    result1 = 0
    count = 0
    for c in text:
        if c == pattern[1]:
            result1 += count
        if c == pattern[0]:
            count += 1

    # Add pattern[1] at end
    result2 = 0
    count = 0
    for c in text:
        if c == pattern[0]:
            count += 1
        if c == pattern[1]:
            result2 += count

    return max(result1 + count, result2) + 1

# Example usage:
# print(maximumSubsequenceCount("abdcdbc", "ac"))  # Output: 4
