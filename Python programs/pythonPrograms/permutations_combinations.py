# Permutations and Combinations
from itertools import permutations, combinations

if __name__ == "__main__":
    arr = input("Elements (space separated): ").split()
    r = int(input("Length: "))
    print("Permutations:")
    for p in permutations(arr, r):
        print(p)
    print("Combinations:")
    for c in combinations(arr, r):
        print(c)
