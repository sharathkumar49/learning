def longest_unique_substring(s):
    char_index = {}
    start = 0
    max_length = 0
    longest_substring = ""

    for i, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1

        char_index[char] = i
        current_length = i - start + 1

        if current_length > max_length:
            max_length = current_length
            longest_substring = s[start:i+1]

    return max_length, longest_substring


# Example usage
input_string = "abcabcbb"
#input_string = "xxyyxyzzzzyxk"
length, substring = longest_unique_substring(input_string)
print(f"Length: {length}, Substring: \"{substring}\"")
