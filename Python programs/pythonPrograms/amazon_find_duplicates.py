# Amazon: Find All Duplicates in an Array
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for n in nums:
        if n in seen:
            duplicates.add(n)
        else:
            seen.add(n)
    return list(duplicates)

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Duplicates:", find_duplicates(nums))
