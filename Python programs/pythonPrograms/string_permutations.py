# Find all permutations of a string
def permute(s):
    if len(s) <= 1:
        return [s]
    perms = []
    for i, c in enumerate(s):
        for perm in permute(s[:i] + s[i+1:]):
            perms.append(c + perm)
    return perms

if __name__ == "__main__":
    s = input("Enter string: ")
    print("Permutations:", permute(s))
