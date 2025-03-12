# Using Two-Pointer Technique:

def reverse_string(input_string):
    input_list = list(input_string)
    left, right = 0, len(input_list) - 1

    while left < right:
        input_list[left], input_list[right] = input_list[right], input_list[left]
        left += 1
        right -= 1

    return ''.join(input_list)

# Example usage
original_string = "hello"
print("Original string:", original_string)
print("Reversed string:", reverse_string(original_string))
