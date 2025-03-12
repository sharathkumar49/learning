
a = [1,2,3,4,5,6,7,8,9,10]


# Method 1
odd, even = [el for el in a if el % 2==1], [el for el in a if el % 2==0]
print(odd, even)


# Method 2
even, odd = [a.pop(index) for index, item in enumerate(a) if item % 2 == 0], a
print(even,odd)

