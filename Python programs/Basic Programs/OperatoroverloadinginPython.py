#Operator Overloading in Python

class Operatoroverloading:
    def __init__(self, a = 0, b= 0):
        self.a = a
        self.b = b

    def __str__(self):
        return "({0},{1})".format(self.a, self.b)

    def __add__(self, other):
        i = self.a + other.a
        j = self.b + other.b
        c = Operatoroverloading(i, j)
        return c

    def __sub__(self, other):
        g = self.a + other.a
        h = self.b + other.b
        d = g - h
        return d

a = Operatoroverloading(5, 6)
b = Operatoroverloading(8, 5)
addition = a + b
subtraction = a - b
print(addition)
print(subtraction)