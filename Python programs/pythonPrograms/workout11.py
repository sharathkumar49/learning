
class Singleton:
    _instance = None



    def __new__(cls, *args, **kwargs):
        print("_instance ", Singleton._instance)
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value


s1 = Singleton(10)
print(s1.value)  # Output: 10

s2 = Singleton(20)
print(s2.value)