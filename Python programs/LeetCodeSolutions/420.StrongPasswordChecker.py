"""
420. Strong Password Checker

A password is considered strong if the following conditions are all met:
- It has at least 6 characters and at most 20 characters.
- It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
- It does not contain three repeating characters in a row ("...aaa...").

Given a string password, return the minimum number of steps required to make the password strong.

Constraints:
- 1 <= password.length <= 50
- password consists of letters, digits, and symbols.
"""
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing_type = 3 - int(any(c.islower() for c in password)) - int(any(c.isupper() for c in password)) - int(any(c.isdigit() for c in password))
        change = 0
        one = two = 0
        i = 2
        arr = list(password)
        while i < n:
            if arr[i] == arr[i-1] == arr[i-2]:
                l = 2
                while i < n and arr[i] == arr[i-1]:
                    l += 1
                    i += 1
                change += l // 3
                if l % 3 == 0:
                    one += 1
                elif l % 3 == 1:
                    two += 1
            else:
                i += 1
        if n < 6:
            return max(missing_type, 6 - n)
        elif n <= 20:
            return max(missing_type, change)
        else:
            delete = n - 20
            change -= min(delete, one)
            change -= min(max(delete - one, 0), two) // 2
            change -= max(delete - one - 2 * two, 0) // 3
            return delete + max(missing_type, change)

# Example usage:
password = "aA1aaa"
print(Solution().strongPasswordChecker(password))  # Output: 2
