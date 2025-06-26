# Microsoft: Find the intersection of two arrays
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    nums1 = list(map(int, input("First array: ").split()))
    nums2 = list(map(int, input("Second array: ").split()))
    print("Intersection:", intersection(nums1, nums2))
