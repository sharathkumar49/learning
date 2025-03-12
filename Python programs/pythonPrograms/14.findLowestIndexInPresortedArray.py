
## to find the lowest value index in the sorted array
## [1, 2, 3, 3, 4, 5], if we search for the value 3, it should give us index at position 2

def binary_search(arr, x):
    lo = 0
    hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2

        if a[mid] < x:
            lo = mid + 1
        elif a[mid] > x:
            hi = mid
        elif mid > 0 and a[mid-1] == x:
            hi = mid
        else:
            return mid

    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def findLowestIndex(arr, x):
    index = binary_search(arr, x)
    if index != -1:
        while index > 0:
            if arr[index] == arr[index -1]:
                index -= 1
            else:
                break
    return index


print(findLowestIndex([1,1,2,2,3,3,4,4,5,5,6], 2))

#binary-search in built:
print(binary_search([1,1,2,2,3,3,4,4,5,5,6], 2))
