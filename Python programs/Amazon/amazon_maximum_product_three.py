# Amazon: Find the Maximum Product of Three Numbers
# Given an integer array, find three numbers whose product is maximum and return the maximum product.

def maximum_product(nums):
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

if __name__ == "__main__":
    print(maximum_product([1,2,3]))  # Output: 6
    print(maximum_product([1,2,3,4]))  # Output: 24
    print(maximum_product([-4,-3,-2,-1,60]))  # Output: 720
