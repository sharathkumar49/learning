





def square(x):
    return x * x

def map_fun(fun, iterables):
    finallst =[]
    for i in iterables:
        finallst.append(fun(i))
    return fun

@map_fun
def func2(fun, iterablesstr):
    return (fun(iterablesstr))


print(map_fun(square, [1,2,3,4,5,6]))
print(func2(square,['a','b','c']))





