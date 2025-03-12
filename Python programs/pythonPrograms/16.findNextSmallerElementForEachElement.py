


def find_next_smaller_elements(xs):
    ys=[-1 for x in xs]
    stack=[]
    for i,x in enumerate(xs):
        print("i:", i, "x:", x)
        while len(stack)>0 and x<xs[stack[-1]]:
           ys[stack.pop()]=x
           print("ys: ", ys)
        stack.append(i)
        print("stack:  ", stack)
    return ys

print(find_next_smaller_elements([4,2,1,5,3]))
print(find_next_smaller_elements([1,2,3,4,5]))
print(find_next_smaller_elements([5,4,3,2,1]))
print(find_next_smaller_elements([1,3,5,4,2]))
print(find_next_smaller_elements([6,4,2]))