
nums = [12, 16, 18, 21, 26]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("No values divisible by 5 is found")





my_list = [2, 4, 6, 8, 10]
for lst in my_list:
    if lst % 2 != 0:
        print("the odd number found in this list is", lst)
        break
else:
    print("Since no odd values found, we're entering into else loop")




#else is also applied to while loop 
my_lst = [4, 8, 12, 16, 20]
i=0
while i<len(my_lst):
    if my_lst[i]%9 ==0:
        print("number found which is divisible by 9", my_lst[i])
        break
    i = i + 1
else:
    print("no value divisible by 9 is found")





def find_index(search, target):
    for i, value in enumerate(search):
        if value == target:
            break
    else:
        return -1
    return i 

mylst = ['steve', 'virat', 'kane']
index_location = find_index(mylst, 'kane')
print('Location of target is in the index: {}'.format(index_location))
    