class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        print("its coming here")
        self.value = value

# Usage
obj1 = Singleton(10)
obj2 = Singleton(20)

print(obj1.value)  # Output: 20
print(obj2.value)  # Output: 20

print(id(obj1))
print(id(obj2))

