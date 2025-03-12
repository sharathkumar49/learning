

str = "viji"

str1 = str.join("a")

print(str)
print(str1)

lst = [1, 2, 3, 4, 5]

lst1 = lst.remove(5)

print(lst)
print(lst1)


# shallow copy deep copy

import copy

a = [[1, 2, 3], [4, 5, 6]]

b = copy.deepcopy(a)
# c = copy.deepcopy(a)
b[0][1] =99
# c[0][0] = 91
print(b)
print(a)
# print(a)