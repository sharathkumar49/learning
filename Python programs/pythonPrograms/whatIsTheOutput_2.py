
#copying will point to the same list in the memory
a = [1, 2, 3]
b = a
a[1] = 3
print(b)
print(a)
print(id(a))
print(id(b))


# concatenating creates a new list, and b still refers to the original list
a = [1, 2, 3]
b = a
a = a + [4, 5]
print(b)
print(a)
print(id(a))
print(id(b))
