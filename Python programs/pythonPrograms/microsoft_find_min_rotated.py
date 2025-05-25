# Microsoft: Find Minimum in Rotated Sorted Array
# Suppose an array sorted in ascending order is rotated at some pivot. Find the minimum element.

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
    arr1 = [3,4,5,1,2]
    print(find_min(arr1))  # Output: 1
    arr2 = [4,5,6,7,0,1,2]
    print(find_min(arr2))  # Output: 0
    arr3 = [11,13,15,17]
    print(find_min(arr3))  # Output: 11
