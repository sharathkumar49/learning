# Regex: email and phone validation
import re

def is_valid_email(email):
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))

def is_valid_phone(phone):
    return bool(re.match(r"^\d{10}$", phone))

if __name__ == "__main__":
    email = input("Email: ")
    phone = input("Phone: ")
    print("Valid email:" if is_valid_email(email) else "Invalid email.")
    print("Valid phone:" if is_valid_phone(phone) else "Invalid phone.")
