

def first_non_repeated_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in s:
        if char_count[char] == 1:
            return char
    return None

# Example usage:
input_string = "swiss"
result = first_non_repeated_char(input_string)
if result:
    print("The first non-repeated character is:", result)
else:
    print("No non-repeated character found.")
