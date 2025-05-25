# Find all pairs in a list that sum to a specific value
def find_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        if target - num in seen:
            pairs.add(tuple(sorted((num, target - num))))
        seen.add(num)
    return pairs

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Target sum: "))
    print("Pairs:", find_pairs(nums, target))
