# Password Strength Checker
import re

def check_password(password):
    length = len(password) >= 8
    digit = re.search(r"\d", password)
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    if all([length, digit, upper, lower, special]):
        return "Strong"
    elif length and (upper or lower) and digit:
        return "Moderate"
    else:
        return "Weak"

if __name__ == "__main__":
    pwd = input("Enter password: ")
    print("Strength:", check_password(pwd))
