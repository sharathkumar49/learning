"""
LeetCode 2299. Strong Password Checker II

Given password, return true if it is strong.

Example:
Input: password = "IloveLe3tcode!"
Output: True

Constraints:
- 1 <= password.length <= 100
"""

def strongPasswordCheckerII(password):
    import string
    if len(password) < 8:
        return False
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    for i in range(1, len(password)):
        if password[i] == password[i-1]:
            return False
    return has_lower and has_upper and has_digit and has_special

# Example usage:
# print(strongPasswordCheckerII("IloveLe3tcode!"))  # Output: True
