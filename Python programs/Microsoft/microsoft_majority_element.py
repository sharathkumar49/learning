# Microsoft: Find the majority element in an array (appears more than n/2 times)
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate if nums.count(candidate) > len(nums)//2 else None

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers: ").split()))
    print("Majority element:", majority_element(nums))
