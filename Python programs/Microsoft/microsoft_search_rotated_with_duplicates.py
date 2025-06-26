# Microsoft: Search in Rotated Sorted Array with Duplicates
# Given an array that may contain duplicates and is rotated, determine if a target exists in the array.
# Return True if found, else False.

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        # If we can't be sure which part is sorted due to duplicates
        if nums[left] == nums[mid] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False

if __name__ == "__main__":
    arr1 = [2,5,6,0,0,1,2]
    print(search(arr1, 0))  # True
    print(search(arr1, 3))  # False
    arr2 = [1,0,1,1,1]
    print(search(arr2, 0))  # True
    arr3 = [1,1,3,1]
    print(search(arr3, 3))  # True
