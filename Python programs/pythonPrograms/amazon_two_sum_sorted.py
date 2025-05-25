# Amazon: Two Sum (sorted array, two pointers)
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []

if __name__ == "__main__":
    nums = list(map(int, input("Enter sorted numbers: ").split()))
    target = int(input("Target: "))
    print("Indices:", two_sum_sorted(nums, target))
