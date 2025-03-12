
# By indexing
# Before going into the program, understand the range function deeply

def reverse_string(input_string):
    reversed_string = ""
    for i in range(len(input_string) - 1, -1, -1):
        print(i)
        reversed_string += input_string[i]
    return reversed_string

# Example usage
original_string = "hello"
print("Original string:", original_string)
print("Reversed string:", reverse_string(original_string))
