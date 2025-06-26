def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

# Example usage
original_string = "hello"
print("Original string:", original_string)
print("Reversed string:", reverse_string(original_string))


