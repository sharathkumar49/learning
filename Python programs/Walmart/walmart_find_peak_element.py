# Walmart: Find Peak Element
# A peak element is an element that is strictly greater than its neighbors. Return the index of any one of the peak elements.

def find_peak_element(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

if __name__ == "__main__":
    print(find_peak_element([1,2,3,1]))  # Output: 2
    print(find_peak_element([1,2,1,3,5,6,4]))  # Output: 5 or 1
