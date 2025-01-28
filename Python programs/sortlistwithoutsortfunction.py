n = int(input("Enter the number of values: "))
lst =[]
for i in range(n):
    k = int(input("Enter the number"))
    lst.append(k)


for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]<lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
print(lst)


'''
workflow:
Say we have 5 values in a list, [7, 8, 2, 1, 9]

The basic workflow is, it takes every value starting from the beginning and it checks with every 
other value and swap if its larger
So, by this way it will start adding the largest numbers from the beginning of the list
number is beginning

Take 7 the initial value, the i loop starts at lst[0], the j loop starts from lst[1] in this case
compared value = 7 comparing value = 8
comparing value is greater than compared value, so do swap 
now first place is 8 and second place is 7, lst[0] = 8  lst[1] = 7
so the compared value now becomes 8, compared = 8

Now, again compared value = 8, comparing value = 2
condition not satisfied
incrementing j

compared value = 8, comparing value = 1  (Note: lst[0]= 8)
condition not satisfied
incrementing j

compared value = 8, comparing value = 9
Here the comparing value is greater than compared value, so do swap 8 and 9
Now the lst[0] = 9 and lst[4] = 8

Now the list looks like [9, 7, 2, 1, 8]
As you can see, the largest of the list is at the beginning 

Now, the external loop increments the i value, so, the pointer is at 1st position lst[1] = 7
and the j pointer is at i+1 == 1+1 == 2 so lst[2] =2

compared value = 7 and comparing value = 2
condition not satisfied
incrementing j

compared value = 7 and comparing value = 1
conditon not satisfied
incrementing j

compared value = 7 and comparing value = 8
Here the comparing value is greater than compared value
So let's do the swap
lst[1]=8 and lst[4]= 7
and end of the list we can't increment j further

Now the list looks like [9, 8, 2, 1, 7]

this is how it goes for the rest of the values

'''