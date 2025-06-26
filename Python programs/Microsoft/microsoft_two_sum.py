# Microsoft: Two Sum (hashmap)
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i
    return []

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    target = int(input("Target: "))
    print("Indices:", two_sum(nums, target))
