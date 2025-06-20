# 17. Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# Return the answer in any order.
#
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
# Example 2:
# Input: digits = ""
# Output: []
#
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]
#
# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

def letterCombinations(digits):
    if not digits:
        return []
    phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    res = ['']
    for d in digits:
        res = [prefix + c for prefix in res for c in phone[d]]
    return res

# Example usage
digits = "23"
print("Letter combinations:", letterCombinations(digits))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
