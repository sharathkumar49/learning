# Singleton class in Python
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

if __name__ == "__main__":
    a = Singleton()
    b = Singleton()
    print(a is b)  # True
