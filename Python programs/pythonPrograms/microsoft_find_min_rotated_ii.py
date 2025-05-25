# Microsoft: Find Minimum in Rotated Sorted Array II
# Suppose an array sorted in ascending order is rotated at some pivot and may contain duplicates. Find the minimum element.

def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right -= 1
    return nums[left]

if __name__ == "__main__":
    arr1 = [2,2,2,0,1]
    print(find_min(arr1))  # Output: 0
    arr2 = [1,3,5]
    print(find_min(arr2))  # Output: 1
