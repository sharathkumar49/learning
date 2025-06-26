# Turing: Find Minimum in Rotated Sorted Array
# Find the minimum element in a rotated sorted array.

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
    print(find_min([3,4,5,1,2]))  # Output: 1
    print(find_min([4,5,6,7,0,1,2]))  # Output: 0
