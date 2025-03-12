def reverse_string(input_string):
    reversed_list = [input_string[i] for i in range(len(input_string)-1, -1, -1)]
    return ''.join(reversed_list)

# Example usage
original_string = "hello"
print("Original string:", original_string)
print("Reversed string:", reverse_string(original_string))
