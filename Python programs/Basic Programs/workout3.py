
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


    # def __add__(a, b):
    #      return a.first + b.first

emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Jake', 'Bell')
print(emp_1)
print(emp_2)
print(emp_1 + emp_2)