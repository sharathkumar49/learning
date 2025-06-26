# Google: Find Peak Element
def find_peak(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid
    return left

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Peak index:", find_peak(nums))
