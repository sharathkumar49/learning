def add(a, b):
    return a + b



def sub(a, b):
    if a > b:
        return a - b

    else :
        return b - a


        
def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def floordiv(a, b):
    return a // b

def si(p, r, t):
    return (p * r * t)/ 100
def ci(p, r, t):
    return p * pow((1 + r/100), t)


def sqrt(a):
    return a ** 0.5


4 = 2
9 = 3

print("addition", add(5, 3),"\nsub: ", sub(5,3),"\nmul: ",  mul(5,3),"\ndiv: ", div(5,3),"\nfloordiv: ", floordiv(5, 3),"\nsimple interest: ", si(5, 4, 3),"\ncompound interest:", ci(9, 8, 7),"\nsquare root: ", sqrt(64) )