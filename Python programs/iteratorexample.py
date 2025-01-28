



it = [1, 2, 3, 4, 5]
for ele in it:
    print(ele)



my_iter = iter(it)
while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break
