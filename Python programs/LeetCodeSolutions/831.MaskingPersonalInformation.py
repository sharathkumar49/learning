"""
831. Masking Personal Information

Given a personal information string S, mask it. If it is an email, mask the name. If it is a phone number, mask the digits except the last four.

Example 1:
Input: S = "LeetCode@LeetCode.com"
Output: "l*****e@leetcode.com"

Example 2:
Input: S = "86-(10)12345678"
Output: "***-***-5678"

Constraints:
- S is a valid email or phone number.
"""
def maskPII(S):
    S = S.lower()
    if '@' in S:
        name, domain = S.split('@')
        return f"{name[0]}*****{name[-1]}@{domain}"
    digits = [c for c in S if c.isdigit()]
    local = '***-***-' + ''.join(digits[-4:])
    if len(digits) == 10:
        return local
    return '+' + '*' * (len(digits) - 10) + '-' + local

# Example usage:
print(maskPII("LeetCode@LeetCode.com"))  # Output: "l*****e@leetcode.com"
print(maskPII("86-(10)12345678"))        # Output: "+**-***-***-5678"
