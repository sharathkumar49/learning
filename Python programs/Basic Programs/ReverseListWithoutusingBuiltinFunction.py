#Program 1:
num = [ 3, 5, 6, 7, 8, 9, 10]
length = len(num)



for i in range(length//2):
    n = num[i]
    num[i]= num[length - i -1]
    num[length - i -1] = n

print(num)
    


#Program 2:
def Reverse(lst):
    if(len(lst) == 1):
        return lst
    return Reverse(lst[1:]) + lst[0:1]

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(Reverse(mylist))


#Program 3:
def reverse(lst):
    return lst[::-1]

mylst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reverse(mylst))

'''
The proper syntax is:
[start:end:step] and each of the parameters may be omitted. Negative numbers mean counting backwards.

So:
[start::] will return the list starting from 'start' until the last element
[:end:] will return all from the first element until the one preceding 'end'
[0:-3] will return elements starting from the first one until (but not including) the third to last
[::2] will return every second element of the list
[::-3] will return every third element counting backwards
'''


#Program 4:
def reverse_fun(data_list):
    length = len(data_list)
    s = length

    new_list = [None] * length

    for item in data_list:
        s = s - 1
        new_list[s] = item
    return new_list


list1 = [1, 2, 3, 4, 5]
print(reverse_fun(list1))
