# Microsoft: Maximum Subarray Product
def max_product(nums):
    res = max(nums)
    cur_min = cur_max = 1
    for n in nums:
        if n == 0:
            cur_min = cur_max = 1
            continue
        tmp = cur_max * n
        cur_max = max(n, cur_max * n, cur_min * n)
        cur_min = min(n, tmp, cur_min * n)
        res = max(res, cur_max)
    return res

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Max product:", max_product(nums))
