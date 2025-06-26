
class Parent:
    def __int__(self, x):
        self.x = x


class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

