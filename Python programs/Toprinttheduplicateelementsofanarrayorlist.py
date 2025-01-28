
#To print duplicate elements of an array or list:

arr = [int(x) for x in input("Enter the values: ").split()]
for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
        if(arr[i]==arr[j]):
            print(arr[j])