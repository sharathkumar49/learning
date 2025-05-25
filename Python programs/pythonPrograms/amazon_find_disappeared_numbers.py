# Amazon: Find All Numbers Disappeared in an Array
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements of [1, n] inclusive that do not appear in this array.

def find_disappeared_numbers(nums):
    for n in nums:
        idx = abs(n) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
    return [i + 1 for i, n in enumerate(nums) if n > 0]

if __name__ == "__main__":
    print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))  # Output: [5,6]
