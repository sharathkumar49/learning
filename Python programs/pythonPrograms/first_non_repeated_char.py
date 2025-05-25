# Find the first non-repeated character in a string
def first_non_repeated(s):
    counts = {}
    for c in s:
        counts[c] = counts.get(c, 0) + 1
    for c in s:
        if counts[c] == 1:
            return c
    return None

if __name__ == "__main__":
    s = input("Enter a string: ")
    print("First non-repeated character:", first_non_repeated(s))
