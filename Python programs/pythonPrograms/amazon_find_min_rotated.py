# Amazon: Find Minimum in Rotated Sorted Array
def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Minimum:", find_min(nums))
