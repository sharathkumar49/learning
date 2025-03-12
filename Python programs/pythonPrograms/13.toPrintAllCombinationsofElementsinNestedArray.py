def print_combinations(arrays, prefix=""):
    # print("arrays: ", arrays, "prefix: ", prefix)
    if not arrays:
        print("prefix: ",prefix)
        return

    for item in arrays[0]:
        # print("item: ", item )
        print_combinations(arrays[1:], prefix + str(item))


# Example usage
arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_combinations(arrays)

# arrays = [[7, 8, 9]]
# print(arrays[1:])
