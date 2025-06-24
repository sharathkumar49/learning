"""
1213. Intersection of Three Sorted Arrays

Given three integer arrays arr1, arr2, and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Constraints:
- 1 <= arr1.length, arr2.length, arr3.length <= 1000
- 1 <= arr1[i], arr2[i], arr3[i] <= 2000

Example:
Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]

"""
def arraysIntersection(arr1, arr2, arr3):
    i = j = k = 0
    res = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            res.append(arr1[i])
            i += 1; j += 1; k += 1
        else:
            m = min(arr1[i], arr2[j], arr3[k])
            if arr1[i] == m: i += 1
            if arr2[j] == m: j += 1
            if arr3[k] == m: k += 1
    return res

# Example usage
if __name__ == "__main__":
    arr1 = [1,2,3,4,5]
    arr2 = [1,2,5,7,9]
    arr3 = [1,3,4,5,8]
    print(arraysIntersection(arr1, arr2, arr3))  # Output: [1,5]
