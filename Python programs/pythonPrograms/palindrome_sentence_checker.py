# Palindrome Sentence Checker (ignoring spaces and punctuation)
import string

def is_palindrome(s):
    s = ''.join([c.lower() for c in s if c.isalnum()])
    return s == s[::-1]

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    if is_palindrome(text):
        print("Palindrome!")
    else:
        print("Not a palindrome.")
