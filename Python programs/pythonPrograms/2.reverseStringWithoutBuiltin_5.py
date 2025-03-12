# Using Stack:

def reverse_string(input_string):
    stack = list(input_string)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
    return reversed_string

# Example usage
original_string = "hello"
print("Original string:", original_string)
print("Reversed string:", reverse_string(original_string))
