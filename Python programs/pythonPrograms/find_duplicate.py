# Find duplicate in array
def find_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return n
        seen.add(n)
    return None

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Duplicate:", find_duplicate(nums))
