# Microsoft: Rotate Array
# Rotate an array to the right by k steps.

def rotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]
    return nums

if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6,7]
    print(rotate(arr1, 3))  # Output: [5,6,7,1,2,3,4]
    arr2 = [-1,-100,3,99]
    print(rotate(arr2, 2))  # Output: [3,99,-1,-100]
