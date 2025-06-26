# Twitter: Minimum number of platforms required for trains
def min_platforms(arr, dep):
    arr.sort(); dep.sort()
    n = len(arr)
    plat = result = 0
    i = j = 0
    while i < n and j < n:
        if arr[i] <= dep[j]:
            plat += 1
            i += 1
            result = max(result, plat)
        else:
            plat -= 1
            j += 1
    return result

if __name__ == "__main__":
    arr = list(map(int, input("Arrival times: ").split()))
    dep = list(map(int, input("Departure times: ").split()))
    print("Minimum platforms:", min_platforms(arr, dep))
