# Facebook: Find the Duplicate Number
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), find the duplicate number.

def find_duplicate(nums):
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow2 = 0
    while slow != slow2:
        slow = nums[slow]
        slow2 = nums[slow2]
    return slow

if __name__ == "__main__":
    arr1 = [1,3,4,2,2]
    print(find_duplicate(arr1))  # Output: 2
    arr2 = [3,1,3,4,2]
    print(find_duplicate(arr2))  # Output: 3
