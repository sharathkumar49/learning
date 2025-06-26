# Amazon: Search in Rotated Sorted Array
# Given a rotated sorted array, search for a target value and return its index. If not found, return -1.

def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

if __name__ == "__main__":
    print(search([4,5,6,7,0,1,2], 0))  # Output: 4
    print(search([4,5,6,7,0,1,2], 3))  # Output: -1
