# Check if a string is a rotation of another string
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)

if __name__ == "__main__":
    s1 = input("First string: ")
    s2 = input("Second string: ")
    print("Is rotation:", is_rotation(s1, s2))
