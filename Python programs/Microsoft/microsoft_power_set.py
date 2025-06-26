# Microsoft: Find All Subsets (power set)
def power_set(arr):
    result = [[]]
    for num in arr:
        result += [curr + [num] for curr in result]
    return result

if __name__ == "__main__":
    arr = input("Elements: ").split()
    print("Power set:", power_set(arr))
