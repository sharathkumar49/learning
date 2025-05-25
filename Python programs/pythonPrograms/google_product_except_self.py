# Google: Product of Array Except Self
def product_except_self(nums):
    n = len(nums)
    res = [1]*n
    left = right = 1
    for i in range(n):
        res[i] *= left
        left *= nums[i]
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Product except self:", product_except_self(nums))
