# Amazon: Rotate Array
def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    k = int(input("Rotate by: "))
    print("Rotated:", rotate(nums, k))
