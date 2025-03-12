class Base:
    def __new__(cls):
        print("Base __new__ called")
        print("cls in Base:", cls)
        return super(Base, cls).__new__(cls)

class Derived(Base):
    def __new__(cls):
        print("Derived __new__ called")
        print("cls in Derived:", cls)
        return super(Derived, cls).__new__(cls)


d = Derived()
print("end of d\n\n\n")
k = Derived()