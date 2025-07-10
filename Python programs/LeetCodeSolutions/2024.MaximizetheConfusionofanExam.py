"""
LeetCode 2024. Maximize the Confusion of an Exam

Given a string answerKey and an integer k, return the maximum number of consecutive 'T's or 'F's in the answerKey after changing at most k answers.

Example:
Input: answerKey = "TTFF", k = 2
Output: 4

Constraints:
- 1 <= answerKey.length <= 5 * 10^4
- answerKey[i] is either 'T' or 'F'.
- 1 <= k <= answerKey.length
"""

def maxConsecutiveAnswers(answerKey, k):
    def maxConsec(ch):
        left = 0
        count = 0
        res = 0
        for right in range(len(answerKey)):
            if answerKey[right] != ch:
                count += 1
            while count > k:
                if answerKey[left] != ch:
                    count -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
    return max(maxConsec('T'), maxConsec('F'))

# Example usage:
# print(maxConsecutiveAnswers("TTFF", 2))  # Output: 4
