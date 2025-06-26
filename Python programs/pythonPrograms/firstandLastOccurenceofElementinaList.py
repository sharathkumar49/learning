
def solution(array, key):
    start_index = -1
    ending_index = -1
    if key not in array:
        return [start_index ,ending_index]
    else:
        for i in range(len(array)):
            print("going for i", i)
            if array[i] == key:
                print("hitting if loop array[i] == key")
                if start_index == -1:
                    print("hitting inner if loop start_index == -1")
                    start_index = i
                    ending_index = i
                else:
                    ending_index = i

        return [start_index ,ending_index]

print(solution([3, 5, 8, 9, 3, 4, 5], 5))