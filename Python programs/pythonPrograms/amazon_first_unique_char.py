# Amazon: Find the first unique character in a string
def first_unique_char(s):
    from collections import Counter
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1

if __name__ == "__main__":
    s = input("Enter string: ")
    idx = first_unique_char(s)
    print("First unique character index:", idx)
