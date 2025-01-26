

#Source : https://stackabuse.com/map-filter-and-reduce-in-python-with-examples/
#difference between map() and filter(): https://medium.com/@ankur.ghogle100/difference-between-map-and-filter-in-python-8c5bca11afe8

def starts_with_A(s):
    return s[0]=="A"

fruits = ["Apple", "Banana", "Strawberry", "Pear", "Apricot"]

#map
map_object = map(starts_with_A, fruits)
print(list(map_object))
map_object_lambda = map(lambda s: s[0]=="A", fruits)
print(list(map_object_lambda))

#filter
filter_object = filter(starts_with_A, fruits)
print(list(filter_object))
filter_object_lambda = filter(lambda s: s[0]=="A", fruits)
print(list(filter_object_lambda))

#reduce
from functools import reduce
lis = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x+y, lis, 10))


#map
mapobject = map(lambda s: s%2 == 0, range(1, 11))
print(list(mapobject))

#filter
filterobject = filter(lambda k : k%2 == 0, range(1, 11))
print(list(filterobject))
