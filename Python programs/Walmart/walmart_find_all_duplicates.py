# Walmart: Find All Duplicates in an Array
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others once. Find all elements that appear twice.

def find_duplicates(nums):
    res = []
    for n in nums:
        idx = abs(n) - 1
        if nums[idx] < 0:
            res.append(abs(n))
        else:
            nums[idx] *= -1
    return res

if __name__ == "__main__":
    print(find_duplicates([4,3,2,7,8,2,3,1]))  # Output: [2,3]
    print(find_duplicates([1,1,2]))            # Output: [1]
